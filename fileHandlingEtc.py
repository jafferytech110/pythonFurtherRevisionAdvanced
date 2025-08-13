import os

filePath = "test.txt"
if os.path.exists(filePath):
    print(f"The location of this file exist. {filePath}")
else:
    print("location doesn't exists.")