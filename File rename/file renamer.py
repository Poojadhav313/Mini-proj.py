import os

folder = "." 

for counter, file in enumerate(os.listdir(folder)):

  if file.endswith(".jpg"): 
    dst = (f"cat {counter}.jpg")
    src = os.path.join(folder, file)
    dst = os.path.join(folder, dst)

    os.rename(src, dst)

