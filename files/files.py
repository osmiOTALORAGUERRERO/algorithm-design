import random
import time

fw = open('ejemplo.txt','w')
newText = ''
for number in range(1000):
    newText += str(random.randrange(1000))+','
fw.write(newText.strip(','))

fw.close()

fr = open('ejemplo.txt','r')
mensaje = fr.read()
mensaje = mensaje.split(',')

second = time.time()
suma = 0
for num in mensaje:
  suma += int(num)
print(time.time() - second)


fw = open('ejemplo1.txt','w')
fw.write(str(suma))

fr.close()
fw.close()
