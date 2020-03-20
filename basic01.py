from math import *
from PIL import Image
im=Image.open("s.jpg")
m=im.size[0]
n=im.size[1]
new=Image.new('RGB',(m,n),(0,0,0))
def f1(x):
    return int(255*sqrt(x/255))
def f2(x):
    return int(255*(x/255)**2)
for i in range(m):
    for j in range(n):
        r,g,b=im.getpixel((i,j))
        R=f1(r)
        G=f1(g)
        B=f1(b)
        new.putpixel((i,j),(R,G,B))        
new.save("T1.jpg")
print("OK")
