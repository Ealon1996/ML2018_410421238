import numpy as np

from PIL import Image



ep = Image.open("Eprime.png")

print("\nloading images...\n")

print("load Eprime.png--")

print(ep.format, ep.size ,ep.mode)

k1 = Image.open("key1.png")

print("\nload key1.png--")

print(k1.format, k1.size ,k1.mode)

k2 = Image.open("key2.png")

print("\nload key2.png--")

print(k2.format, k2.size ,k2.mode)

img = Image.open("I.png")

print("\nload I.png--")

print(img.format, img.size ,img.mode)

e = Image.open("E.png")

print("\nload E.png--")

print(e.format, e.size ,e.mode)

print("\nstart decryption...")

epoch=1

eparray=np.array(ep)

k1array=np.array(k1)
print(k1array.shape,k1array)
k2array=np.array(k2)
print(k2array.shape,k2array)
Iarray=np.array(img)
print(Iarray.shape,Iarray)
Earray=np.array(e)
print(Earray.shape,Earray)


w=np.array([1,1,1])
print(w.shape,w)

eptest = np.random.randn(300,400)

for epoch in range(100):
    for k in range(300):
        for p in range(400):
            x=np.array([k1array[k,p],k2array[k,p],Iarray[k,p]])
            xt=np.transpose(x)
            a=np.dot(w,xt)
            etemp=Earray[k,p]-a
            w=w+0.0000001*etemp*x


w = np.transpose(w)


<<<<<<< HEAD
#宣告eptest用來測試並載入每個像素的值
eptest = np.random.randn(300,400)
#套用公式還原每個pixel的值
=======

>>>>>>> parent of 94ef1b7... discribe
for k in range(300):

    for p in range(400):

        eptest[k,p] = (eparray[k,p] - w[0]*k1array[k,p] - w[1]*k2array[k,p])/w[2]

        if eptest[k,p] >255:

            eptest[k,p] = 255

        elif eptest[k,p] <0:

            eptest[k,p] = 0





eptest = np.array(eptest,dtype=np.uint8)

ans = Image.fromarray(eptest)

<<<<<<< HEAD
ans.save("Iprime1.png")
=======
etest.save("Iprime.png")
>>>>>>> parent of 94ef1b7... discribe
