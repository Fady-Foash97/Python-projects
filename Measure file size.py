# Import os module for file operations
import os
# Name the file you want to be found
file_size = "Area of triangle.py"
#Get file information or file size
try:
    file_size_bytes = os.path.getsize("d:\Programming Course\Python\Area of triangle.py")
    file_size_kb = file_size_bytes / 1024    
#Print the size of the file 
    print(f"\nThe size of Area of triangle.py is: {file_size_kb: .2f} ","Kilobytes")
except FileNotFoundError:
    print(f"\n The file {file_size} is not found")