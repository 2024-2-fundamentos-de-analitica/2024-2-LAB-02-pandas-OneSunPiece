"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    tb0 = 'files/input/tbl0.tsv'
    df1 = pd.read_csv(tb0, sep='\t')

    # Tabla 2
    tb2 = 'files/input/tbl2.tsv'
    df2 = pd.read_csv(tb2, sep='\t')

    # Se unen
    df = pd.merge(df1, df2, on='c0', how='inner')

    # Se hace un group by y se suman las de la columna c5b
    agrupados = df.groupby('c1')['c5b'].sum()
    
    return agrupados