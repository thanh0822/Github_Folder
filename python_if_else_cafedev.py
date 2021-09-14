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

#bài 1

a= int(input("nhập số 1: ")) b= int(input("nhập số 2: ")) c= int(input("nhập số 3: ")) if a<b and b<c:

  print(a,b,c)
elif a<c and c<b:

  print(a,c,b)
elif b<a and a<c:

  print(b,a,c)
elif b<c and b<a:

  print (b,c,a)
elif c<b and b<a:

  print(c,b,a)
else:

  print(c,a,b)

  #Bài 2

  def Max(a,b,c,d):
   max=a
   if b>max :
       max=b
   if c>max :
       max=c
   if d>max:
       max=d
   return max
def Min(a,b,c,d):
   min=a
   if b<min:
       min=b
   if c<min :
       min=c
   if d<min:
       min=d
   return min
def Trung_gian(a,b,c,d):
   max=Max(a,b,c,d)
   min=Min(a,b,c,d)
   if (max!=a)and(min!=a):
       print "So trung gian :",a
   if (max!=b)and(min!=b):
       print "So trung gian :",b
   if (max!=c)and(min!=c):
       print "So trung gian :",c
   if (max!=d)and(min!=d):
       print "So trung gian :",d
   
if __name__=="__main__":  
   a=int(raw_input("Nhap a :"))
   b=int(raw_input("Nhap b :"))
   c=int(raw_input("Nhap c :"))
   d=int(raw_input("Nhap d :"))
   print "So Lon Nhat :", Max(a,b,c,d)
   print "So Nho Nhat :", Min(a,b,c,d)             
   Trung_gian(a,b,c,d)

#Bài 3

def Bai3(a,b,c):

   if (a+b)>c and (a+c)>b and (b+c)>a and (a>0) and (b>0) and (c>0):
       if(a==b)and (b==c):
           return 0
       elif((a*b+b*b==c*c)and(a==b))or((a*a+c*c==b*b)and(a==c))or((c*c+b*b==a*a)and(c==b)):
           return 1
       elif(a==b)or(b==c)or(a==c):
           return 2
       elif((a*a==b*b+c*c)or(b*b==a*a+c*c)or(c*c==a*a+b*b)):
           return 3
       else:
           return 4
   else:
       return 5
       
       
if __name__=="__main__":

   a=int(raw_input("Nhap a :"))
   b=int(raw_input("Nhap b :"))
   c=int(raw_input("Nhap c :"))         
   r=['Tam giac deu','tam giac vuong can','tam giac can','tam giac vuong ','tam giac thuong','khong hop le']
   i=Bai3(a,b,c)
   print r[i]

# Bài 4

def Bai4(km):
   if km==1:
       print "So tien phai tra la : 5000d"
   else:
       if km<=5:
           print "So tien phai tra la :",((km-1)*4500+5000)
       else:
           if(km<120):
                print "So tien phai tra la :",((km-5)*3500+4500*4+5000)
           else:     
               print "So tien phai tra la :",((((km-5)*3500+4500*4+5000)*1/10))
if __name__=="__main__":  
   km=int(raw_input("Nhap so km da di :"))
   Bai4(km)   

# Bài 5

def Bai5(BD,KT):

   h=KT-BD # So gio truy cap
   T=1 #Thanh tien
   if((BD>=0)and(BD<=7)):
       if h>=7:
           T=(T*h*300*60)/0.15
       else:
           T=T*h*300
   if((BD>7)and (BD<=17)):
      if h>=6:
           T=(T*h*400*60)/0.1
      else:
           T=T*h*400
   if((BD>17)and (BD<=24)):
      if h>=4:
           T=(T*h*350*60)*0.12
      else:
           T=T*h*350                
   return T       
               
if __name__=="__main__":

   BD=int(raw_input("Nhap thoi gian bat dau :"))    
   KT=int(raw_input("Nhap thoi gian ket thuc :"))
   print "Thanh tien",Bai5(BD,KT)

#Bài 6

def Bai7(m):
   if(m<1)or(m>12):
       print "Nhap thang khong hop le"
   if(m>=1)and(m<=3):
       print "Mua xuan"
   if(m>=4)and(m<=6):    
       print "Mua ha"
   if(m>=6)and(m<=9):
       print "Mua thu"
   if(m>=10)and(m<=12):
       print "Mua dong"        
       
if __name__=="__main__":  
   M=int(raw_input("Nhap 1 thang trong nam :"))
   Bai7(M)