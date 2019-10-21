"""Biblioteca interfaz

ya irá creciendo.... de momento real pedido 

"""





def realPedido (mini,maxi,msg):
    """float, float, str -->float
    OBJ: pide real a usuario, entre min y max, mostrando msg    """

    pedir = True
    while  pedir or not (mini<=n<=maxi):
        try:
            n = float(input(msg))
            pedir = False
        except:print('debe ser un real. ', end='')
            
    return n

'''
#PROBADOR
print(realPedido(min,max,'real entre '+str(min)+' y '+str(max)+': '))
'''
