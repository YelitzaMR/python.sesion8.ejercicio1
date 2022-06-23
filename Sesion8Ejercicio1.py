f = open ('miMensaje.txt', 'x')

def escribir (miMensaje):
        f = open (miMensaje, 'w')
    
        f.write('Gracias por todo, OpenBootcamp')
    
        f.close()
    
escribir ('miMensaje.txt')
