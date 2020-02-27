from programs.files import files
from programs.sort_and_search import sort, search
import random
import time

#crear archivo con numeros
PATH = '\\files\\sort_and_search'
newText = ''
for number in range(1000):
    newText += str(random.randrange(1000))+','
writed = files.writeFile(str(newText.strip(',')), PATH, 'inputNumber.txt')

if writed > 0:
    #obtener arachivo
    numbers = files.readFile('\\files\\sort_and_search\\inputNumber.txt').split(',')
    numbers = list(int(numbers[i]) for i in range(len(numbers)))

    #Algoritmos de ordenamiento
    bubbleSort = sort.bubble_sort(numbers[:])
    insertionSort = sort.insertion(numbers[:])
    selectionSort = sort.select_sort(numbers[:])
    start_time = time.time()
    quikSort = sort.Quick_Sort(numbers[:])
    elapsed_time = time.time() - start_time
    print("Elapsed time: %0.10f seconds of function Quick_Sort()." % elapsed_time)

    #Resultados ordenados en un archivo
    files.writeFile(','.join(str(num) for num in bubbleSort), PATH, 'bubble_sort.txt')
    files.writeFile(','.join(str(num) for num in insertionSort), PATH, 'insertion_sort.txt')
    files.writeFile(','.join(str(num) for num in selectionSort), PATH, 'selection_sort.txt')
    files.writeFile(','.join(str(num) for num in quikSort), PATH, 'quik_sort.txt')

    #Algoritmos de busqueda
    searchTarget = random.randrange(1000)
    print('Numero a buscar: {}'.format(searchTarget))
    linearSearch = search.linearsearch(quikSort, searchTarget)
    binarySearch = search.BinarySearch(quikSort, searchTarget)
    start_time = time.time()
    binarySearchRecursive = search.BinarySearch_Recursive(quikSort, searchTarget, 0, len(quikSort))
    elapsed_time = time.time() - start_time
    print("Elapsed time: %0.10f seconds of function bsRecursive()." % elapsed_time)

    #resultado
    answerSearch = 'Numero buscado: {}\n'.format(searchTarget)
    answerSearch += 'Busqueda lineal posicion en x = {}\nBusqueda binaria posicion en x = {}\n'.format(linearSearch, binarySearch)
    answerSearch += 'Busqueda binaria recursica en x = {}'.format(binarySearchRecursive)
    files.writeFile(answerSearch, PATH, 'search_algorithm.txt')
