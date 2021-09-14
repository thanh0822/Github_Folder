traudung =0
traunam =0
traugia =0
for traudung in range(1,100):
 for traunam in range(1,100):
  for traugia in range(1,100):
    if ((traudung+traunam+traugia==100) and (traudung*5+traunam*3+traugia/3==100)):
      print("Vay so con trau dung la",traudung, "Vay so con trau nam la ",traunam, "Vay so con trau gia la",traugia, )