'''
Created on Jan 25, 2013

@author: parce
'''
def createColorSpaceDictionary():
    dict = {}
    dict['AT'] = '0'
    dict['CG'] = '0'
    dict['GC'] = '0'
    dict['TA'] = '0'
    dict['AC'] = '1'
    dict['CA'] = '1'
    dict['GT'] = '1'
    dict['TG'] = '1'   
    dict['AA'] = '2'
    dict['CC'] = '2'
    dict['GG'] = '2'
    dict['TT'] = '2'
    dict['GA'] = '3'
    dict['TC'] = '3'
    dict['AG'] = '3'
    dict['CT'] = '3'
    return dict

def convierteReadAColorSpace(inputRead):
    traduccion = createColorSpaceDictionary()
    outputRead = 'T'
    caracterAnterior = 'T'
    for caracter in inputRead:
        nuevoCaracter = caracter
        color = traduccion[caracterAnterior + nuevoCaracter]
        outputRead = outputRead + color
        caracterAnterior = nuevoCaracter
    return outputRead