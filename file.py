import zipfile 
with zipfile.ZipFile("Vaibhav.zip", "w") as zipf :
    zipf.write("pratice.txt")
    zipf.write("pratice1.txt")