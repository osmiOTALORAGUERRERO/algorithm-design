import math
from ..efficiency.functionTime import count_elapsed_time

@count_elapsed_time
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
