import os
from pickle import LIST
from difflib import SequenceMatcher

##Function for finding common directory of two diffrent files
def find_files_Dir(filename1,filename2, search_path):
   LIST_1 = []
   # for file no. 1
   for root, dir, files in os.walk(search_path):
      if filename1 in files:
         LIST_1.append(os.path.join(root, filename1))
   print(*LIST_1, sep = ', ')     

   #for file no. 2
   LIST_2 = []  
   for root, dir, files in os.walk(search_path):
      if filename2 in files:
         LIST_2.append(os.path.join(root, filename2))
   print(*LIST_2, sep = ', ')     
   # print(LIST_2) 
   
   S1 = LIST_1[0]
   S2 = LIST_2[0]
   
   Len = len(S1)
   LIST2 = []
   for i in range(Len):
       if(S1[i] == S2[i]):
         #   print("pass")
         # Passing
           LIST2.append(S1[i])
       else:
           break
   # print(LIST2)
   print(*LIST2, sep = '')     
   
   return LIST,LIST_2
    
find_files_Dir("A.txt","b.txt","D:")
    
        


