def print_directory_contents(sPath):
    import os
    print sPath
    for sChild in os.listdir(sPath):
        newPath = os.path.join(sPath, sChild)
        if os.path.isdir(newPath):
            print_directory_contents(newPath)


print_directory_contents(r'C:\Users\212534368\Documents\PythonScripts\numlearn')
