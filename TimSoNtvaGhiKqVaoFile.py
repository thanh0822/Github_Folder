print(" Tim so nguyen to tu 1 den N")
N=int(input(" Nhap N = "))
with open ("kqsont.txt", 'w') as f:
	f.write(" Ket qua so nguyen to trong khoang tu 1 den " + str(N) +'\n')
	for i in range (1,N):
		LaSoNt = True
		for j in range (2,i):
			if i%j==0 :
				LaSoNt = False
		if LaSoNt :
			f.write("     "+str(i))
f.close()
with open ("kqsont.txt",'a+') as f1:
	f1.write(" \n Mo file  bang mode a+ de ghi them noi dung vao cuoi file \n")
	f1.write(" Writen by Nguyen Xuan Thanh ")
f1.close()



