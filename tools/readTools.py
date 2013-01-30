'''
Created on Jan 25, 2013

@author: parce
'''
def createBaseSpaceToColorSpaceDictionary():
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

def createColorSpaceToBaseSpaceDictionary():
	dict = {}
	dict['T0'] = 'T'
	dict['T1'] = 'G'
	dict['T2'] = 'C'
	dict['T3'] = 'A'
	dict['G0'] = 'G'
	dict['G1'] = 'T'
	dict['G2'] = 'A'
	dict['G3'] = 'C'
	dict['C0'] = 'C'
	dict['C1'] = 'A'
	dict['C2'] = 'T'
	dict['C3'] = 'G'
	dict['A0'] = 'A'
	dict['A1'] = 'C'
	dict['A2'] = 'G'
	dict['A3'] = 'T'
	return dict

def baseSpaceReadToColorSpace(inputRead, adapter):
    traduccion = createBaseSpaceToColorSpaceDictionary()
    outputRead = adapter
    caracterAnterior = adapter
    for caracter in inputRead:
        nuevoCaracter = caracter
        color = traduccion[caracterAnterior + nuevoCaracter]
        outputRead = outputRead + color
        caracterAnterior = nuevoCaracter
    return outputRead

def colorSpaceReadToBaseSpace(inputRead):
    traduccion = createColorSpaceToBaseSpaceDictionary()
    oldBase = inputRead[0]
    for color in inputRead[1:]
        nuevoCaracter = color
        newBase = traduccion[oldBase + nuevoCaracter]
        outputRead = outputRead + newBase
        caracterAnterior = nuevoCaracter
    return outputRead


