'''
Created on Jan 25, 2013

@author: parce
'''
import readTools

def pruebaTransformaReads():
    readNormal = 'TTTAGAGACATGGAAGAGGGACAGACTGTCATTCAAAA'
    readInsercion = 'TTTAGAGACATGGAAGTAGGGACAGACTGTCATTCAAA'
    readDeleccion = 'TTTAGAGACATGGAAGAGGGACAGCTGTCATTCAAAAT'
    readSustitucion = 'TTTAGAGACATGGAAGACGGACAGACTGTCATTCAAAA'
    readDobleDeleccion = 'TTTAGAGACATGGAAGAGGGACAGTGTCATTCAAAATG'
    ejemploReal = 'GAGGCATATTTATAAGAACTTGGCTGAAATGTCAAATT'
	
    
    print 'Read Normal:'
    print readNormal + ' - ' + readTools.convierteReadAColorSpace(readNormal, 'T')
    print ''
    print 'Read adaptador \'A\':'
    print readNormal + ' - ' + readTools.convierteReadAColorSpace(readNormal, 'A')
    print ''
    print 'Read Insercion:'
    print readInsercion + ' - ' + readTools.convierteReadAColorSpace(readInsercion, 'T')
    print ''
    print 'Read Deleccion:'
    print readDeleccion + ' - ' + readTools.convierteReadAColorSpace(readDeleccion, 'T')
    print ''
    print 'Read Sustitucion:'
    print readSustitucion + ' - ' + readTools.convierteReadAColorSpace(readSustitucion, 'T')
    print ''
    print 'Read Doble Deleccion:'
    print readDobleDeleccion + ' - ' + readTools.convierteReadAColorSpace(readDobleDeleccion, 'T')

    print ''
    print 'Ejemplo real Para variar:' 
    print ejemploReal + ' - ' + readTools.convierteReadAColorSpace(ejemploReal, 'T')
    print 'Deberia ser:                             T12203133300333022012010321200311210030'

pruebaTransformaReads()
