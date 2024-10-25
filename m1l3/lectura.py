#Lectura de archivos 
#f = open("texto.txt", "r", encoding="utf=8")
#text = f.read()
#print(text)
#f.close()

#Sobre escribir archivo de texto
#f = open("texto.txt", "w", encoding="utf=8")
#text = "Cambio de texto"
#f.write(text)
#f.close()

#abreviacion
with open("texto.txt", "r", encoding="utf=8") as f:
    print(f.read())


# abrir imagenes 
i = open("images/block.png", "rb")

#Alternativa para la ruta
#C:/Users/JJNO/Documents/Kodland/3713/m1l3/texto.txt