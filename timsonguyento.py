print(" Thanh viet chuong trinh tim so nguyen to tu 1 den so ban nhap vao")
n=int(input(" Nhap vao so n = "))
for i in range(1,n):
	songuyento=True
	for j in range (2,i):
		if i%j==0:
			songuyento=False
			break
	if songuyento:
		print('%d' %i, end='  ')

for chu in 'quantrimang':
    print('Chữ cái hiện tại:', chu)