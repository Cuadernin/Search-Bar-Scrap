# Search Bar Scrap
El siguiente código realiza webscrapping de forma másica a la **primera página** de Google. Lo anterior, tomando como base un dataframe de Python. 

## Ejemplo de uso 📑
```
columnas = ['Persona','Auto']
busqueda_Google(df,columnas,exacta=True)
```

## Salida ⌛

**NOTA:** Como se crea un driver con cada iteración puede ser ligeramente más lento que abrir un solo drive y solo actualizar la búsqueda. Ambos casos son detectados por
Google. 
