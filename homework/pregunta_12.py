"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def list_to_dic(lista):
     dic = {}

     # Se itera sobre la lista de valores, acumulando las cadenas en un diccionario
     # según su clave
     for clave, c5a, c5b in lista:
          # Se convierte de in a str
          c5b = str(c5b)

          # Si no esta en el diccionario, se crea
          if clave not in dic:
               dic[clave] = [c5a+':'+c5b]
          else:
               dic[clave].append(c5a+':'+c5b)
     
     # Se ordenan las listas y se convierten en cadenas
     for clave in dic:
          dic[clave] = sorted(dic[clave])

          dic[clave] = ','.join(dic[clave])
     
     return dic
     

def pregunta_12():
     tb2 = 'files/input/tbl2.tsv'
     df = pd.read_csv(tb2, sep='\t')

     # Tomamos lo que necesitamos para operarlo aparte
     agrupado = df[['c0','c5a','c5b']].groupby('c0')

     # Lo convertimos a una lista
     resultado_lista = []
     for group in agrupado:
          resultado_lista.extend(group[1].values.tolist())

     # Se toman los datos manipulados
     datos = list_to_dic(resultado_lista).items()

     # Se crea el nuevo dataframe
     df_manipulado = pd.DataFrame(datos,columns=['c0','c5'])
     
     return df_manipulado