from PIL import Image
import pygame
import numpy as np
image = Image.open("pixil-frame-0.png")


mode = image.mode
size = image.size
data = image.tobytes()

x = np.array(image)
#py_image = pygame.image.fromstring(data, size, mode)
def detectSame(a,b):
    for i in range(len(a)):
        if (a[i]!=b[i]):
            return False
    return True

    map = " "
    for i in x:
        for y in i:
            #print(y)
           if(detectSame(y,[[0,0,0,255]]) or detectSame(y,[[255,255,255,255]])):
               pass
               #map+='1'
           else:
               print(y)
               #map+='0'

    #map+= '\n'

#print(map)




#for i in x:
    #for y in i:
        #print(y)

'''temp = []
map = " "
for i in x:
    for y in i:
       if(detectSame(y,[162,170,159])):
           map+='1'
       else:
           map+='0'
    temp.append(map)
    map = ''

#for i in temp:
    #print(i)



print('hola mundo')'''