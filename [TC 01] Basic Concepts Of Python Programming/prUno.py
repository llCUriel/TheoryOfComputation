Sigma = ["E", "S", "C", "O", "M", "/", "$", "X"]
miCadena = input("Introduce una cadena de texto: ")
cnt = 1
for caracter in miCadena:
    if (caracter  not in Sigma):
        cnt = 0
if (cnt == 0):
            print ("La cadena '" + miCadena + "' no se encuentra en el alfabeto")
else:
            print ("La cadena '" + miCadena + "' si se encuentra en el alfabeto")






        

    
       
       
       
       



    



