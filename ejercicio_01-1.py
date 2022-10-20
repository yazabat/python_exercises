def desencriptando_mensajes(horas, mensaje_desencriptado):
    message_f = ""
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
            message_f = message_f + chr(c)
    return message_f

a=int(input("horas:"))
b=str(input("mensaje_encriptado:"))
print(desencriptando_mensajes(a, b))


