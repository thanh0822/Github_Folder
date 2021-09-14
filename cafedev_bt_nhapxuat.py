# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------


#bai 1

import time

x = time.localtime()
print (x[0])

def Xuat_tuoi(Namsinh):
	x=time.localtime()
 	a=x[0] - Namsinh
 	if a==0:
      print ("Tuoi cua ban la :",a+1)
 	elif (a<0):
      print ("Tuoi nay chua ton tai")
 	else:
      print ("Tuoi cua ban la :",a)

Namsinh = int(input("Nhap nam sinh : "))
Xuat_tuoi(Namsinh)

#bai 2

import math

def Tinh(R):
   if R<0:
       print("Ban kinh khong nho hon 0")
       print("Ban nhap khong hop le")
   else:
       CV=2*R*math.pi
       DT=R*R*math.pi
       print "Chu vi la :",CV
       print "Dien tich la :",DT
 
print("-------Tinh Chu Vi, Dien Tich Hinh Tron---------")  
r=float(input("Nhap ban kinh hinh tron: "))
Tinh(r)

# bai 3

import math
def Bai_3(R,h):
   S_DAY=R**2*math.pi
   S_XQ=2*R*h*math.pi
   V=S_DAY*h
   if (R<0)or(h<0):
       print "Ban nhap khong hop le"
   else:
       print "Dien tich day la :",S_DAY
       print "Dien tich xung quanh la :",S_XQ
       print "The tich la :",V
print"-----Tinh Dien Tich,The Tich Hinh Tru Tron-------"
if __name__=="__main__":
   r=float(raw_input("Nhap ban kinh :"))
   h=float(raw_input("Nhap chieu cao :"))
   Bai_3(r,h)

 #bai 4

import math
def Bai_4(x):
   y1=4*(x*x+10*math.pow(x, 1.5)+3*x+1)
   y2=(math.sin(math.pi*x*x)+math.sqrt(x*x+1))/(math.exp(2*x)+math.cos((math.pi/4)*x))
   print "Y1 = ",y1
   print "Y2 = ",y2
print "------Tinh gia tri bieu thuc-------------  "
x=float(raw_input("Nhap so thuc X : "))     
Bai_4(x)

# bai 5

def tinh_so_to_tien(tien):

	loai_tien = [50000,20000,10000,5000,2000,1000]

	for i in loai_tien:
	so_to = tien/i
	print "co %d to %d nghin dong" %(so_to, i)
	tien = tien%i

print " Nhap so tien:"
n = int(raw_input(">"))
tinh_so_to_tien(n)

# bai 6

x=int(input("Nhập số cần tính giai thừa:"))

def tong(x):
  a=0
  s=0
  if x/10 >= 1:
     s=x%10
     a=int(x/10)
     print("tổng là:" , a+s)
  else:
     print("tổng các phần tử là: ", x)
  return

tong(x)

