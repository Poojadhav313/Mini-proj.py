import os

path = "." 

files_in_folder = os.listdir(path)

index = 0

try:
  for file in files_in_folder:
    if file.endswith(".jpg"): 

        new_filename = f"cat {index}.jpg"
        
        old_path = os.path.join(path, file)
        new_path = os.path.join(path, new_filename)

        os.rename(old_path, new_path)
        index += 1
except:
   print("Can't rename the file with same names")
   print(Exception)
else:
  print("Rename successfull")
