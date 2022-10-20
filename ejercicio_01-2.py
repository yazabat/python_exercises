def resolviendo_el_mensaje(mensaje_copiado , horas , mensaje_encriptado , R):
    mensaje_ordenado = ""
    es_copia = False
    
    if (horas>=10) | (horas<=21):
        horas = -1 * horas
        for i in mensaje_encriptado.lower():
            print(i)
            if (ord(i)>=97) & (ord(i)<=122):
                c = ord(i) + (horas)%(122-97+1)
                c = 97+(c-97)%(122-97+1)
            else:
                #d={ord('$'):ord('.'),ord('.'):ord('$'),ord('&'):ord(','),ord(','):ord('&'),ord('/'):ord(' '),ord(' '):ord('/')}
                desencriptar = {ord('$'):ord('.'),ord('&'):ord(','),ord('/'):ord(' ')}
                c = desencriptar.get(ord(i))      
            mensaje_ordenado = mensaje_ordenado + chr(c)

    words = mensaje_ordenado.split(' ')
    string =[]
    for word in words:
      string.insert(-R, word)
      mensaje_ordenado=" ".join(string)
    
    if mensaje_ordenado.upper()==mensaje_copiado.upper():
      es_copia=True
 
    return  mensaje_ordenado, mensaje_ordenado, es_copia
 
 
  #resultado_final = [mensaje_desencriptado, mensaje_ordenado, es_copia]
  
"""
  mensaje_copiado=a
  a=int(input("mensaje_copiado:"))
  b=int(input("horas:"))
  c=int(input("mensaje_a_desencriptar:"))
  d=int(input("R:"))
"""
print(resolviendo_el_mensaje(mensaje_copiado="Tienes que optimizar el codigo con division y conquista. Ten cuidado con el redondeo de valores .", horas=15,mensaje_encriptado="topl/op/nzxz/cpdzwgpcwz$/yz/epyrz/yt", R=4))