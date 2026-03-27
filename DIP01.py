from PIL import Image
img = Image. open ("Image1.jpg")
w,h = img.size

filename = "Image1"
for i in range(10,76):
    per = i
    dec = 100-per
    newW = int(w*dec/100)
    newH =int(h*dec/100)
    print(per,w,h,newW,newH)
    img = img.resize((newW,newH))
    img.save(filename + str(i) + ".jpg")
    

