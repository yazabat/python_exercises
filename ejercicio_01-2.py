def resolviendo_el_mensaje(mensaje_copiado , horas , mensaje_encriptado , R):
  mensaje_desencriptado = ""
  mensaje_ordenado = ""
  es_copia = False

  def rotar(x,horas):
    horas=-1*horas
    if (x>=97) & (x<=122):
      c=x+(horas)%(122-97+1)
      c=97+(c-97)%(122-97+1)
    else:
      #desencriptar={ord('$'):ord('.'),ord('.'):ord('$'),ord('&'):ord(','),ord(','):ord('&'),ord('/'):ord(' '),ord(' '):ord('/')}
      desencriptar={ord('$'):ord('.'),ord('&'):ord(','),ord('/'):ord(' ')}
      c=desencriptar.get(x,x)      
    return chr(c)
  

  def resultado_final(horas,mensaje_encriptado, R):
    mensaje_desencriptado = ''.join([rotar(ord(i),horas) for i in list(mensaje_encriptado.lower())])

    words = mensaje_desencriptado.split(' ')
    string =[]
    for word in words:
      string.insert(-R, word)
      mensaje_ordenado=" ".join(string)
    
    if mensaje_ordenado.upper()==mensaje_desencriptado.upper():
      es_copia=True
 
  return  mensaje_desencriptado, mensaje_ordenado, es_copia
 
 
  #resultado_final = [mensaje_desencriptado, mensaje_ordenado, es_copia]
  
"""
  mensaje_copiado=a
  a=int(input("mensaje_copiado:"))
  b=int(input("horas:"))
  c=int(input("mensaje_a_desencriptar:"))
  d=int(input("R:"))
"""
return resultado_final(mensaje_desencriptado, mensaje_ordenado, es_copia)