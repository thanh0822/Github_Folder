# Viet CT kiem tra mot so nhap vao co phai la so nguye to ko?
# HD bạn có thể dùng vòng lặp để đếm số ước của n, nếu số ước của n là 2 thì return True, ngược lại return False.
# Viet 1 ham de kiem tra cho thuan tien
def LaSoNT(n):
	dem = 0
	for i in range (1,n+1):
		if n%i==0 :
			dem=dem+1
	if dem ==2 :
		return True
	else :
		return False

n=int(input(" Ban nhap vao so can kiem tra xem co phai la so nguyen to ko n = "))
print(LaSoNT(n))
print('\n')
# In dien giai cu the hon la
if LaSoNT(n):
	print(n," La so nguyen to \n" )
else :
	print(n," Khong la so nguyen to \n" )

