import math
print(math.pow(2,2))

def hanoiPower(numberOfNeedles):
  if numberOfNeedles > 0 and numberOfNeedles < 1000:
    hanoi = []
    for i in range(numberOfNeedles):
      hanoi.append([])
    
    perfectSquare = True
    count = 1

    while perfectSquare:
      currentNeedle = 1
      for needle in hanoi:
        if len(needle) == 0:
          needle.append(count)
          count += 1
          break
        elif math.sqrt(needle[-1]+count)*math.sqrt(needle[-1]+count) == needle[-1]+count:
          needle.append(count)
          count += 1
          break
        else:
          if (currentNeedle == len(hanoi)):
            perfectSquare = False
            break
          else:
            currentNeedle += 1
            
