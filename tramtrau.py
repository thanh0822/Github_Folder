traudung =1
traunam =1
traugia =1
for traudung in range(1,20): # traudung nhận các giá trị từ 1 đến 20
  for traunam in range(1,33): # traunam nhận các giá trị từ 1 đến 33
     for traugia in range(1,100): # traugia nhận các giá trị từ 1 đến 100
       if ((traudung*5 + traunam*3 + traugia/3 == 100) and (( traudung+traunam+traugia==100))) : 
          print("Trau dung = ", traudung ,"Traunam = ",traunam, " Traugia = ",traugia)