import os
import shutil
 
from_dir= 'C:/Users/hongh/OneDrive/Escritorio/miprimerpython/Pro_C112_ActividaddelaMaestra/PRO112/images'
to_dir='C:/Users/hongh/OneDrive/Escritorio/miprimerpython/Pro_C112_ActividaddelaMaestra/assets'

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,ext=os.path.splitext(file)
    print(name)
    print(ext)

    if ext==' ':
      continue
    if ext in ['.jpeg','.jpg','.png']:
       path1=from_dir+'/'+ file
       path2=to_dir

       if os.path.exists(path2):
            print("Moviendo archivos")

            shutil.move(path1,path2)
       else:
         os.makedirs(path2)
         shutil.move(path1,path2)