def posibles_sospechosos(equipos, calificaciones):        
  sospechosos = ""
  # Codigo para Pregunta 3 comienza aqui
  e=equipos.split(" ")
  c=calificaciones.split(" ")
  j={}
  for x in c:
      if x not in c:
          j[x]=1
      else:
          j[x]+=1
  for x in range(len(c)):
      if j[c[x]] > 2:
        sospechosos.appened(e[x])
      else:

  # Codigo para Pregunta 3 acaba aqui
  return sospechosos

