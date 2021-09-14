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


# Độ khó mức 3 - Các bài tập liên quan tới tính toán, nhap xuat, vòng lặp, string, class, hàm, biến

#Bài 1

import re
value = []
items=[x for x in input("Nhập mật khẩu: ").split(',')]

for p in items:
	if len(p)<6 or len(p)>12:
		continue
	else:
		pass
	if not re.search("[a-z]",p):
		continue
	elif not re.search("[0-9]",p):
		continue
	elif not re.search("[A-Z]",p):
		continue
	elif not re.search("[$#@]",p):
		continue
	elif re.search("\s",p):
		continue
	else:
		pass
value.append(p)
print (",".join(value))

#Bài 2

from operator import itemgetter, attrgetter

l = []
while True:
	s = input()
	if not s:
		break
	l.append(tuple(s.split(",")))
print (sorted(l, key=itemgetter(0,1,2)))

#Bài 3
def putNumbers(n):
	i = 0
	while i<n:
		j=i
		i=i+1
		if j%7==0:
			yield j

	for i in putNumbers (100):
		print (i)

#Bài 4

import math
pos = [0,0]
while True:
 s = input()
 if not s:
 	break
 movement = s.split(" ")
 direction = movement[0]
 steps = int(movement[1])
 if direction=="UP":
 	pos[0]+=steps
 elif direction=="DOWN":
 	pos[0]-=steps
 elif direction=="LEFT":
 	pos[1]-=steps
 elif direction=="RIGHT":
 	pos[1]+=steps
 else:
 	pass

print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))

#Bài 5

freq = {} # frequency of words in text
line = input()
for word in line.split():
	freq[word] = freq.get(word,0)+1

words = sorted(freq.keys())
for w in words:
	print ("%s:%d" % (w,freq[w]))

