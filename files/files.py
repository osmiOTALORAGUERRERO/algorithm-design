import random
import time

def readFile(path):
    fr = open(path,'r')
    output = fr.read()
    fr.close()
    return output

def writeFile(input = '', path='newFile.txt'):
    fw = open(path,'w')
    bytesWrited = fw.write(str(input))
    fw.close()
    return bytesWrited

def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper(*args, **kwargs):
        # Start counting.
        start_time = time.time()
        # Take the original function's return value.
        ret = f(*args, **kwargs)
        # Calculate the elapsed time.
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: %0.10f seconds of function {f.__name__}()." % elapsed_time)
        return ret

    return wrapper


newText = ''
for number in range(1000):
    newText += str(random.randrange(1000))+','

writeFile(newText.strip(','), 'numbersFile.txt')

numbers = readFile('numbersFile.txt').split(',')

sumNumber = sum(numbers)
repeated = repeatedNumbers([34,3,2,57,100], numbers)

print(sumNumber)
print(repeated)
