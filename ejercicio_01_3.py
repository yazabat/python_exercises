def posibles_sospechosos(equipos, calificaciones):
    sospechosos = ""
    # Codigo para Pregunta 3 comienza aqui
    e=[i.strip() for i in equipos.split(", ")]
    c=[i.strip() for i in calificaciones.split(", ")]
    j={}
    for key in e:
        for val in c:
            j[key] = val
            c.remove(val)
            break

    rev_dict = {}
    for key, value in j.items():
        rev_dict.setdefault(value, set()).add(key)
      
    result = [key for key, values in rev_dict.items() if len(values) > 1]
    print(result)
    print(j)
    sospechosos = [k for k,v in j.items() if v in result]

            
    # Codigo para Pregunta 3 acaba aqui
    return sospechosos

equipos = " Alfalfa , Rabano , Choclito , Zanahoria , Frijolito , Arroz "
calificaciones = "56 , 14 , 56 , 60 , 56 , 75"
print(posibles_sospechosos(equipos, calificaciones))