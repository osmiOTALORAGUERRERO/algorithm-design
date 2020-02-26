import math

def hanoiPower(numberOfNeedles):
  if numberOfNeedles > 0 and numberOfNeedles < 1000:
    hanoi = []
    for i in range(numberOfNeedles):
      hanoi.append([])

    perfectSquare = True
    count = 0
    greater = count;
    while perfectSquare:
      currentNeedle = 1
      count += 1
      for needle in hanoi:
        if len(needle) == 0:
          needle.append(count)
          greater = count
          break
        elif round(math.sqrt(needle[-1]+count))*round(math.sqrt(needle[-1]+count)) == needle[-1]+count:
          needle.append(count)
          greater = count
          break
        else:
          if (currentNeedle == len(hanoi)):
            perfectSquare = False
            break
          else:
            currentNeedle += 1

    return greater, hanoi

def parserTower(array):
    tower = ''
    while len(array) > 0:
        row = ''
        for list in array:
            row += str(list.pop(0)) + '\t'
            if len(list) == 0:
                array.remove(list)
        tower = row + '\n' + tower
    return tower

needles = int(input('Ingresa un Numero: '))
respuesta = hanoiPower(needles)
print('La respuesta es: {}'.format(respuesta[0]))
print('--------------------------------')
print(parserTower(respuesta[1]))
print('--------------------------------')
