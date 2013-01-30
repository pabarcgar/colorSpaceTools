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
    
    print 'Read Normal:'
    print readNormal + ' - ' + readTools.convierteReadAColorSpace(readNormal)
    print ''
    print 'Read Insercion:'
    print readInsercion + ' - ' + readTools.convierteReadAColorSpace(readInsercion)
    print ''
    print 'Read Deleccion:'
    print readDeleccion + ' - ' + readTools.convierteReadAColorSpace(readDeleccion)
    print ''
    print 'Read Sustitucion:'
    print readSustitucion + ' - ' + readTools.convierteReadAColorSpace(readSustitucion)
    print ''
    print 'Read Doble Deleccion:'
    print readDobleDeleccion + ' - ' + readTools.convierteReadAColorSpace(readDobleDeleccion)

pruebaTransformaReads()
