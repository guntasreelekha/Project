#import cv2
from matplotlib import pyplot as plt
import numpy as np
#import numpy as np
count,count1=0,0
arr=[]
brr=[]
img=cv2.imread("C:\\Users\\ASUS\\Desktop\\leaf_dataset\\test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.startWindowThread()
#cv2.namedWindow("leaf detection")
cv2.waitKey(0)
cv2.destroyAllWindows()
gray=cv2.resize(gray,(400,400))
#cv2.imshow("sathish",z)
rows,cols=gray.shape
for i in range(rows-1):
    for j in range(cols-1):
       if gray[i,j]!=0:
           count+=1
       else:
           count1+=1
if count!=0 and count1!=0:
 print("it is not a healthy leaf")
else:
 print("it is a healthy leaf")
plt.imshow(gray,cmap="gray",interpolation="bicubic")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#x,y=np.load("sathish.npy"),np.load("haritha.npy")
plt.show()
