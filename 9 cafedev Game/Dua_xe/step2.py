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


import pygame		#1
import time		#4

pygame.init()		#2

display_width = 800     #8
display_height = 600
black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))	#3
pygame.display.set_caption("Racing car")    #3

clock = pygame.time.Clock() 	#4
crashed = False #5
carImg = pygame.image.load('racecar1.png')   #9

def car(x,y):   #10
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45) #11
y = (display_height * 0.8)

while not crashed:	#6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    gameDisplay.fill(white) #12
    car(x,y)    #13
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()		#7
quit()
