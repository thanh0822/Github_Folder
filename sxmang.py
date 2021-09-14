lst = []
n = int( input(" Nhap n = "))

for i in range(n):
    lst.append(int(input(" Nhap Lst[" + str(i) +"] = ")))

for i in range(len(lst)):
    for j in range(i):
        if lst[i] < lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
print(lst)

lst.sort()
print(lst)