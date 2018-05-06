import numpy as np  #宣告Numpy套件

from PIL import Image #宣告Python Image Library 套件

#開檔動作

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

epoch=1 #初始epoch
#將圖片讀入np.array
eparray=np.array(ep)
k1array=np.array(k1)
k2array=np.array(k2)
Iarray=np.array(img)
Earray=np.array(e)

#初始權重w
w=np.array([1,1,1])

#利用gradient descent 解碼 每個pixel檢測一次 做十次
for epoch in range(10):
    for k in range(300):
        for p in range(400):
            x=np.array([k1array[k,p],k2array[k,p],Iarray[k,p]])
            xt=np.transpose(x)  #轉置以便相乘
            a=np.dot(w,xt) #w*xt
            etemp=Earray[k,p]-a #loss function
            w=w+0.00001*etemp*x  #修改權重

#轉置w
w = np.transpose(w)


#宣告eptest用來測試並載入每個像素的值
eptest = np.random.randn(300,400)
#套用公式還原每個pixel的值
for k in range(300):

    for p in range(400):

        eptest[k,p] = (eparray[k,p] - w[0]*k1array[k,p] - w[1]*k2array[k,p])/w[2]

        if eptest[k,p] >255:

            eptest[k,p] = 255

        elif eptest[k,p] <0:

            eptest[k,p] = 0

#印出權重
print(w[0],"\n",w[1],"\n",w[2])

eptest = np.array(eptest,dtype=np.uint8)

ans = Image.fromarray(eptest)

ans.save("Iprime1.png")