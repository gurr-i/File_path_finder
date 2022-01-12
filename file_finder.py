import os

##Function for finding file root directory by name
def find_files(filename, search_path):
   LIST = []
   
   for root, dir, files in os.walk(search_path):
      if filename in files:
         LIST.append(os.path.join(root, filename))
   print(*LIST, sep = ', ')      
   return ("")


print(find_files("Space_char.txt","D:"))