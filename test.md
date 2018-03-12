---
layout: post
title:  "Ansible"
date:   2018-01-31 14:51:39 +0100
comments: true
categories: Ansible Linux
---

**[Follow Ansible2 Tutorial](https://serversforhackers.com/c/an-ansible2-tutorial)**

env:</br>
master    192.168.0.43</br>
node      192.168.0.45<br />

- [install Ansible on master](#install-ansible-on-master)
- [Test connection between master and node with Ansible](#test-connection-between-master-and-node-with-ansible)
- [Install nginx on node](#install-nginx-on-node)
- [Install nginx on node via playbook](#install-nginx-on-node-via-playbook)
- [Handlers](#handlers)
- [More tasks](#more-tasks)

# install Ansible on master
```
# Go to my user's home directory,
# make a directory to play with ansible
cd ~/
mkdir ansible-play
cd ansible-play

# Create a python virtual environment
virtualenv .venv
# Enable the virtual environment
source .venv/bin/activate

# Then anything we intall with pip will be
# inside that virtual environment
pip install ansible

# At any time, you can update ansible by running:
# Assumes the virtualenv is active - `source .venv/bin/activate`
# Assuming the virtualenv is active
pip install -U ansible

nano ~/ansible-play/hosts
[local]
127.0.0.1
[remote]
192.168.0.45
```

# Test connection between master and node with Ansible
```
# Run against localhost
$ ansible -i ./hosts --connection=local local -m ping

# Run against remote server
$ ansible -i ./hosts remote -m ping
127.0.0.1 | success >> {
    "changed": false,
    "ping": "pong"
}
```
Let's cover these commands:
* `-i ./hosts` - Set the inventory file, the one named hosts
* `remote, local, all` - Use the servers defined under this label in the hosts inventory file. "all" is a special keyword to run against every server defined in the file
* `-m ping` - Use the "ping" module, which simply runs the ping command and returns the results
* `-c local | --connection=local` - Run commands on the local server, not over SSH

# Install nginx on node
```
# Run against a remote server
ansible -i ./hosts remote -b --become-user=root \
    -m apt -a 'name=nginx state=installed update_cache=true'

127.0.0.1 | success >> {
    "changed": false
}
```
Going over the command:
* -i ./hosts - Set the inventory file, the one named hosts
* -b - "become", tell Ansible to become another user to run the command
* --become-user=root - Run the following commands as user "root" (e.g. use "sudo" with the command)
* local | remote - Run on local or remote defined hosts from the inventory file
* -m apt - Use the apt module
* -a 'name=nginx state=installed update_cache=true' - Provide the arguments for the apt module, including the package name, our desired end state and whether to update the package repository cache or not

# Install nginx on node via playbook
Create file nginx.yml:
```
---
# hosts could have been "remote" or "all" as well
- hosts: remote
  become: yes
  become_user: root
  tasks:
   - name: Install Nginx
     apt:
       name: nginx
       state: installed
       update_cache: true
```

```
$ ansible-playbook -i ./hosts nginx.yml

PLAY [remote] ******************************************************************

GATHERING FACTS ***************************************************************
ok: [192.168.0.43]

TASK: [Install Nginx] *********************************************************
ok: [192.168.0.43]

PLAY RECAP ********************************************************************
192.168.0.43                  : ok=2    changed=0    unreachable=0    failed=0
```

# Handlers
A Handler is exactly the same as a Task (it can do anything a Task can), but it will only run when called by another Task. You can think of it as part of an Event system; A Handler will take an action when called by an event it listens for.

This is useful for "secondary" actions that might be required after running a Task, such as starting a new service after installation or reloading a service after a configuration change.

```
---
# Example shows using the local machine still
# Remove 'connection' and set hosts to 'remote' for a remote connection
- hosts: local
  # connection: local
  become: yes
  become_user: root
  tasks:
   - name: Install Nginx
     apt:
       name: nginx
       state: installed
       update_cache: true
     notify:
      - Start Nginx

  handlers:
   - name: Start Nginx
     service:
       name: nginx
       state: started
```
Here we add a notify directive to the installation Task. This notifies any Handler named "Start Nginx" after the Task is run.

This particular Handler uses the Service module, which can start, stop, restart, reload (and so on) system services. In this case, we tell Ansible that we want Nginx to be started.

Note that Ansible has us define the state you wish the service to be in, rather than defining the change you want. Ansible will decide if a change is needed, we just tell it the desired result.


```
$ ansible-playbook -i ./hosts nginx.yml
```

# More tasks
```
---
# Example shows using the local machine still
# Remove 'connection' and set hosts to 'remote' for a remote connection
- hosts: remote
  # connection: local
  become: yes
  become_user: root
  vars:
   - docroot: /var/www/serversforhackers.com/public
  tasks:
   - name: Add Nginx Repository
     apt_repository:
       repo: ppa:nginx/stable
       state: present
     register: ppastable

   - name: Install Nginx
     apt:
       pkg: nginx
       state: installed
       update_cache: true
     when: ppastable|success
     notify:
      - Start Nginx

   - name: Create Web Root
     file:
      path: '{{ docroot }}'
      mode: 775
      state: directory
      owner: www-data
      group: www-data
     notify:
      - Reload Nginx

  handlers:
   - name: Start Nginx
     service:
       name: nginx
       state: started

    - name: Reload Nginx
      service:
        name: nginx
        state: reloaded
```
There are now three Tasks:
* Add Nginx Repository - Add the Nginx stable PPA to get the latest stable version of Nginx, using the apt_repository module.
* Install Nginx - Installs Nginx using the Apt module.
* Create Web Root - Finally, create a web root directory.
Also new here are the register and when directives. These tell Ansible to run a Task when something else happens.

The "Add Nginx Repository" Task registers "ppastable". Then we use that to inform the Install Nginx Task to only run when the registered "ppastable" Task is successful. This allows us to conditionally stop Ansible from running a Task.

This particular example of only installing Nginx when the ppa repository was added is superfluous, as if adding the repository fails, Ansible will stop and report the error. However it's good to know the functionality exists.

You can register the results of a modules action as well, and use the variable defined in register to conditionally perform actions when based on the registered variables values. For example, registering the result of the command run via the shell module can let you access the stdout of that command.

We also use a variable. The _docroot_ variable is defined in the var section. It's then used as the destination argument of the file module which creates the defined directory.

Note that the path configuration uses brackets {{ var-name }} - This is Jinja2 templating. In order for Ansible to parse the Jinja2 template variable within the brackets, the line must be in **single or double quotes** - e.g. path: '{{ docroot }}' instead of path: {{ docroot }}. Not using quotes will result in an error.

This playbook can be run with the usual command:
```
ansible-playbook -i ./hosts nginx.yml
```