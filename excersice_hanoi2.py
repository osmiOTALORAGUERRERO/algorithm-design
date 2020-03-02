from programs.files import files
from programs.Hanoi import HanoiTowerAgain


def parserTower(array):
    tower = ''
    while len(array) > 0:
        row = ''
        for list in array:
            row += str(list.pop(0)) + '\t \t'

        empty = len(array[-1]) == 0
        while len(array) > 0 and empty:
            if len(array[-1]) == 0:
                array.remove(array[-1])
            if len(array) > 0:
                empty = len(array[-1]) == 0
            else:
                empty = False
        tower = row + '\n' + tower
    return tower

needles = int(input('Ingresa un Numero: '))
respuesta = HanoiTowerAgain.hanoiPower(needles)

view = 'La respuesta es: {} \n'.format(respuesta[0])
view += '--------------------------------\n'
view += parserTower(respuesta[1])
view += '--------------------------------'

files.writeFile(view, "\\files\\hanoi2", "answer.txt")
