import zipfile
# from pratice import *
# if choice1 == choice2 :
#     print("Same name ")


with zipfile.ZipFile("Vaibhav.zip","r") as zipf :
    zipf.extractall("extracted_files")