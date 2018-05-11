graph = {
    'group1': ['user1', 'user2', 'group2'],
    'group2': ['group3', 'group1'],
    'group3': ['user3']
}

'''
isUserInGroup(username, groupname)
isUserInGroup('user3', 'group2') = True

usersInGroup(groupname)
usersInGroup('group2') = ['user1', 'user2', 'user3']
'''