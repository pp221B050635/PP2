import os
filepath='C:\\Users\\pdash\\OneDrive\\Документы\\GitHub\\PP2\\Lab6\\D.txt'
if os.path.exists(filepath):
    os.remove(filepath)
else:
    print("Can not delete the file as it doesn't exists")