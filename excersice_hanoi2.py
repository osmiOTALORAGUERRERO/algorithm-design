from programs.files import files
from programs.Hanoi import HanoiTowerAgain


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
