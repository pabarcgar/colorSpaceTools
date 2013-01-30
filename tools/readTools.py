'''
Created on Jan 25, 2013

@author: parce
'''
def createColorSpaceDictionary():
    dict = {}
    dict['AT'] = '3'
    dict['CG'] = '3'
    dict['GC'] = '3'
    dict['TA'] = '3'
    dict['AC'] = '1'
    dict['CA'] = '1'
    dict['GT'] = '1'
    dict['TG'] = '1'   
    dict['AA'] = '0'
    dict['CC'] = '0'
    dict['GG'] = '0'
    dict['TT'] = '0'
    dict['GA'] = '2'
    dict['TC'] = '2'
    dict['AG'] = '2'
    dict['CT'] = '2'
    return dict

#def createColorSpaceToBaseSpaceDictionary():
#	dict = {}
#	dict['T0'] = 'A'
#	dict['T1'] = 'G'
#	dict['T2'] = 'T'
#	dict['T3'] = 'C'
	#dict[''] = ''



def convierteReadAColorSpace(inputRead, adapter):
    traduccion = createColorSpaceDictionary()
    outputRead = adapter
    caracterAnterior = adapter
    for caracter in inputRead:
        nuevoCaracter = caracter
        color = traduccion[caracterAnterior + nuevoCaracter]
        outputRead = outputRead + color
        caracterAnterior = nuevoCaracter
    return outputRead

#def convierteColorSpaceReadABaseSpace(inputRead):
#    traduccion = createColorSpaceDictionary()
#    outputRead = adapter
#    caracterAnterior = adapter
#    for caracter in inputRead:
#        nuevoCaracter = caracter
#        color = traduccion[caracterAnterior + nuevoCaracter]
#        outputRead = outputRead + color
#        caracterAnterior = nuevoCaracter
#    return outputRead

