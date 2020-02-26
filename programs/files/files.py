import random
import os

def readFile(path):
    newPath = os.getcwd()+path
    fr = open(newPath,'r')
    output = fr.read()
    fr.close()
    return output

def writeFile(input = '', path='', file='input.txt'):
    newPath = os.getcwd()

    if os.path.exists(os.getcwd()+path):
        print('true')
        newPath = os.getcwd()+path+'\\'+file
    else:
        print('false')
        os.mkdir(os.getcwd()+path)
        newPath = os.getcwd()+path+'\\'+file

    fw = open(newPath,'w')
    bytesWrited = -1
    if input == '':
        newText = ''
        for number in range(100):
            newText += str(random.randrange(1000))+','
            bytesWrited = fw.write(str(newText.strip(',')))
    else:
        bytesWrited = fw.write(str(input))
    fw.close()
    return bytesWrited
