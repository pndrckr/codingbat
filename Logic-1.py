############### cigar_party

# Cuando las ardillas se juntan en una fiesta, les gusta fumar
# cigarros. Una fiesta de ardillas es exitosa cuando la cantidad
# de cigarros esta entre 40 y 60. A no ser que sea fin de semana,
# en tal caso no hay un litmite maximo. Segun los valores dados,
# Devuelve True si la fiesta fue un exito o False si no.

# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
  if is_weekend==True:
    return cigars >= 40
  else:
    return 60>= cigars >=40



############### date_fashion

# Tu y tu cita estan buscando una mesa en un restaurante. El parametro
# "you" es el nivel de estilo del 0 al 10, y el parametro "date" el de 
# tu cita. El resultado de obtener una mesa esta codificado en valores:
# 0=no, 1=quizas, 2=si. Si tu cualquiera de los dos tiene 8 o mas el
# resultado es 2 (Si), a exepcion que alguno tenga 2 o menos, dando
# como resultado 0 (No). De otra forma el resultado es 1 (quizas).

# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you+date > 10 and  you > 8 or date > 8:
      return 2
  else:
    return 1



############### squirrel_play

# Las ardillas de Palo Alto se la pasan jugando la mayor parte del dia.
# Especialmente cuando la tempreatura marca entre 60 y 90 (inclusive). 
# A no ser en verano que el limite sube a 100. Dada la temperatura (temp)
# y un booleano (is_summer), devuelve True o False si las ardillas juegan o no.

# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
  if is_summer==True:
    return 60 <= temp <=100
  else:
    return  60 <= temp <= 90



############### caught_speeding

# Estas conduciendo un poco ligero, y la policia te detiene. Escribe el 
# codigo que compute el resultado de tu  multa: 0=No hay multa, 1=pequeña
# multa y 3=gran muta. Si la velocidad (speed) es 60 o menor el resultado es 0.
# Si la velocidad esta entre 61 y 80 inclusive, es 1. Si la velocidad supera 81
# el resultado es 2. A no ser que sea tu cumpleaños (is_birthday), en tal caso 
# la velocidad puede aumentar 5 en cada caso.

# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed <= 65:
      return 0
    elif 65 < speed <= 85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif 60 < speed <= 80:
      return 1
    else:
      return 2



############### sorta_sum

# Dados 2 enteros, a y b, devuelve su suma. Aunque si la suma da entre
# 10 a 19 inclusive, estan prohibidos, en ese caso devuelve 20.

# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):
  if 10 <= a+b < 20:
    return 20
  else:
    return a + b
    
    

############### alarm_clock

# Dado un dia de a semana encodificado (0=Dom, 1=Lun, ...6=Sab)
# y un booleano que indica si estamos de vacaciones (vacation),
# devuelve una cadena ("7:00") indicando la hora del despertador.
# Lunes a Vierenes "7:00" y fines de semana "10:00". A no ser de
# estar en vacaciones, en tal caso de Lunes a Viernes "10:00" y 
# fines de semana "off".

# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
  if vacation==True:
    if day == 0 or day == 6:
      return "off"
    return "10:00"
  else:
    if day == 0 or day == 6:
      return "10:00"
    return "7:00"



############### love6

# Dados 2 numeros enteros, a y b, devuelve True si alguno 
# es un 6 o si su suma o diferencia es 6.

# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True

def love6(a, b):
  return a+b==6 or abs(a-b)==6 or a==6 or b==6



############### in1to10

# Dado un numero n, devuelve True si n esta entre 1 y 10 (incl).
# A no ser que outside_mode es True, en tal caso devuelve True
# si n es menor o igual a 1 o mayor o igual a 10.

# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True

def in1to10(n, outside_mode):
  if outside_mode==True:
    return n not in range(2,10)
  return n in range(1,11)



############### near_ten 

# Dado un numero positivo "num", devuelve True si num esta a 2 de 
# un multiplo de 10.

# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True

def near_ten(num):
  return 0 <= (num % 10) <= 2 or 8 <= (num % 10) <= 10
