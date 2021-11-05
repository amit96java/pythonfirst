f=open("_amit_photo.JPG","rb")
f1=open("amit_python.JPG","wb")

for i in f:
    f1.write(i)