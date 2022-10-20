#-horas = Numero de horas desde que empezó la competencia. 10 ≤ horas ≤ 21
#letras minusculas
# $ → .
# & → ,
# / → Espacio en blanco
# 36 → 46
# 38 → 44
# 47 → 32

def desencriptando_mensajes ( horas , mensaje_encriptado ) :

    traduccion = ''
    
    for i in mensaje_encriptado:
        if i.isalpha():
            num=ord(i)
            num+=horas        

            if i.isupper():
                if num>ord('Z'):
                    num-=21
                elif num<ord('A'):
                    num+=10
            elif i.isslower():
                if i>ord('z'):
                    i-=21
                elif i<ord('a'):
                    i+=10
        
            traduccion += chr(i)
        else:
                 # how to add condition 
            chars_to_check = ["$", ",", "/" ]
            for char in chars_to_check:
                if char in mensaje_encriptado:
                    ["$", ",", "/" ]==[".", "&", " " ]
                        
            traduccion += i

    return traduccion







"""

    key=-key #desencriptando
  #upper = collections.deque(string.ascii_uppercase)
    #lower = collections.deque(string.ascii_lowercase)

    #upper.rotate(horas)
    #lower.rotate(horas)

    #upper = ''.join(list(upper))
    #lower = .''.join(list(upper))

    #return mensaje_encriptado.translate(string_maketrans)
    """
