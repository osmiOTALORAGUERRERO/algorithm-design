from programs.files import files
from programs.basic_operations import operations

import os
print( os.getcwd())

if files.writeFile(path='\\files\\exercise_one', file='inputOperations.txt') > 0:
    numbers = files.readFile('\\files\\exercise_one\\inputOperations.txt').split(',')

    sumNumber = 'La suma de todos los numeros es igual a: {}'.format(operations.sumNums(numbers))
    files.writeFile(sumNumber, '\\files\\exercise_one', 'outputSum.txt')

    repeated = 'La cantidad de veces que se repiten los siguientes numeros \n{}'.format(operations.repeatedNumbers([34,3,2,57,100], numbers))
    files.writeFile(repeated, '\\files\\exercise_one\\', 'outputRepeated.txt')
