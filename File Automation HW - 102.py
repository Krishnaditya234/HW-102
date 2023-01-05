import os
import shutil
from_dir =  "C:/Users/krish/School CS Codes"
to_dir = "D:/Downloads"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path4 = from_dir + "/" + file_name
        path5 = to_dir + "/" + 'Document_Files'
        path6 = to_dir + "/" + 'Document_Files' + "/" + file_name
        if os.path.exists(path5):
            print("Moving "+file_name+"...")
            shutil.move(path4,path6)
        else:
            os.makedirs(path5)
            print("moving " + file_name + "...")
            shutil.move(path4,path6)
