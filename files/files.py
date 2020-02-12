import random
import time

def readFile(path):
    fr = open(path,'r')
    output = fr.read()
    fr.close()
    return output

def writeFile(input, path='newFile.txt'):
    fw = open(path,'w')
    print(fw.write(str(input)))
    fw.close()

def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper(arr):
        # Start counting.
        start_time = time.time()
        # Take the original function's return value.
        ret = f(arr)
        # Calculate the elapsed time.
        elapsed_time = time.time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret

    return wrapper

@count_elapsed_time
def sum(nums):
    answer = 0
    for num in nums:
        answer += int(num)
    return answer


newText = ''
for number in range(100):
    newText += str(random.randrange(1000))+','

writeFile(newText.strip(','), 'numbersFile.txt')

numbers = readFile('numbersFile.txt').split(',')

sumNumber = sum(numbers)
print(sumNumber)
