
print(" Giải Hệ PT Bậc Nhật Hai Ẩn \n")
a1=float(input(" Nhap he so pt1 a1 = "))
b1=float(input(" Nhap he so pt1 b1 = "))
c1=float(input(" Nhap c1 = "))
a2=float(input(" Nhap he so pt2 a2 = "))
b2=float(input(" Nhap he so pt2 b2 = "))
c2=float(input(" Nhap c2 = "))
D=Dx=Dy=x=y=0.000
D=a1*b2-a2*b1
Dx=c1*b2-c2*b1
Dy=a1*c2-a2*c1
if D != 0 :
	x=Dx/D
	y=Dy/D
	print("x = ",x)
	print("y= ",y)
elif ((Dx==0) and (Dy==0 )):
 	print(" He phuong trinh co vo so nghiem ")
else :
 	print(" He phuong trinh vo nghiem ")
