n = int(input(" Ban hay nhap vao gia tri n = "))
i = 0
s = 0
print()
# Tinh tong tu 1 den n
while i<=n :
	s=s+i # giong lenh s+=i
	i=i+1
print ("Tong tu 1 den",n," la : ",s)
# Tinhtong cac so le
print()
i = 0
s1 =0
s2= 0
while i<= n :
	if (i%2 == 0):
		s2=s2+i # Tinh tong cac so chan
		i = i+1
	else :
	    s1=s1+i # Tinh tong cac so le
	    i=i+1

print(" Tong cac so le tu 1 den ",n, "la : ",s1)
print(" Tong cac so chan tu 1 den ",n, "la : ",s2)


   