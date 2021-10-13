# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:08:45 2021

@author: rokefeler@gmail.com
"""

#formato_tabla.py
class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr>',end='')
        for h in headers:
            print(f'<th>{h}</th>',end='')
        print('</tr>')

    def fila(self, data_fila):
        print('<td>',end='')
        for d in data_fila:
            print(f'<td>{d}</td>',end='')
        print('</td>')
        
def crear_formateador(nombre):
    ''' permite crear un objeto formateador dado un tipo de salida
    como txt, csv, o html
    '''
    formateador = None
    # Elige formato
    if nombre.lower() == 'txt':
       formateador = FormatoTablaTXT()
    elif nombre.lower() == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre.lower() == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador

def imprimir_tabla(camion, listaColumnas, formateador):
    '''  imprime una tabla mostrando, de una lista de objetos de tipo 
    arbitrario, una lista de atributos especificados
    '''
    formateador.encabezado(listaColumnas)
        
    for lote in camion:
        row = [str(getattr(lote,colname)) for colname in listaColumnas]
        formateador.fila(row)
    