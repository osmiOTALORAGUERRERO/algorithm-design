fr = open('ejemplo.txt','r')
mensaje = fr.read().replace('\n','')
mensaje = mensaje.split(',')
fr.close()

fw = open('ejemplo.txt','w')
newText = ''
for number in mensaje:
    numberStr = str( int(number) + 1 )
    newText += numberStr+','
fw.write(newText.strip(','))
fw.close()
