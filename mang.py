a=[]
n=int(input(' Nhap vao so phan tu cua mang n = '))
for i in range(n):
    print(' Nhap a[',i,'] = ', end=' ')
    a.append(int(input()))
print(' Mang ban vua nhap la : ')
print(a)
#in ra phan tu lon nhat trong mang cach 1
print(" Gia tri phan tu lon nhat trong mang la ",max(a))
#in ra phan tu lon nhat trong mang cach 2 tu viet
max=a[0]
for i in range(n):
    if a[i]>max:
        max=a[i]
print(" Gia tri phan tu lon nhat trong mang la theo cach 2 la : ",max)    

# Sx mang tang dan
# cach 1 dung ham
print(' Mang tang dan theo cach dung ham la:')
a.sort()
print(a)
# Cach 2 tu viet ham sx mang tang dan
for i in range(n):
    for j in range (i):
        if a[j]>a[i]:
            tam=a[i]
            a[i]=a[j]
            a[j]=tam
print(" Mang sau khi sap xep tang dan la")
print(a)