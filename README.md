# Search Bar Scrap
El siguiente código realiza webscrapping de forma masiva a la **primera página** de Google (título y url). Lo anterior, tomando como base un dataframe de Python. 

## Ejemplo de uso 📑
```
columnas = ['Persona','Auto']
busqueda_Google(df,columnas,exacta=True)
```

## Salida ⌛
<img align="center" src=https://github.com/Cuadernin/Search-Bar-Scrap/blob/main/Ejemplo_uso.png height="340" width="750"> 
<br/>

**NOTA:** Como se crea un driver con cada iteración puede ser ligeramente más lento que abrir un solo driver y actualizar la búsqueda. Ambos casos son detectados por
Google. Dependiendo de la página en cuestión, habrá ocasiones en las que no sea posible guardar todos las urls ni títulos. 
