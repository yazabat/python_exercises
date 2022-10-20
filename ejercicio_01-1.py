def desencriptando_mensajes(horas, mensaje_desencriptado):
  
  def rotar(x,horas):
    horas=-1*horas
    if (x>=97) & (x<=122):
      c=x+(horas)%(122-97+1)
      c=97+(c-97)%(122-97+1)
    else:
      #d={ord('$'):ord('.'),ord('.'):ord('$'),ord('&'):ord(','),ord(','):ord('&'),ord('/'):ord(' '),ord(' '):ord('/')}
      desencriptar={ord('$'):ord('.'),ord('&'):ord(','),ord('/'):ord(' ')}
      c=desencriptar.get(x,x)      
    return chr(c)

  def encriptar(horas,mensaje_desencriptado):
    return ''.join([rotar(ord(i),horas) for i in list(mensaje_desencriptado.lower())])
  
  a=int(input("horas:"))
  b=str(input("mensaje_encriptado:"))
  
  return encriptar(a, b)
