import os
import shutil

from_dir=r"C:/Users/malak/Downloads"
to_dir=r"C:/Users/malak/Downloads"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    ruta_extención=os.path.splitext(file_name)
    if(ruta_extención[1] == ""):
        continue
    if(ruta_extención[1] in [".mp4"]):
        ruta1=from_dir+"/"+file_name
        ruta2=to_dir+"/"+"videos"
        ruta3=to_dir+"/"+"videos"+"/"+file_name
        if(os.path.exists(ruta2)):
            print("moviendo"+file_name)
            shutil.move(ruta1,ruta3)
        else:
            os.makedirs(ruta2)
            print("moviendo"+file_name)
            shutil.move(ruta1,ruta3)
