############### SLEEP_IN

# El parametro weekday es True si es un dia de semana
# y el parametro vacaciones es True si estamos de vacaciones.
# Devolver True si podemos dormir hasta tarde (sleep in)

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

    

############### monkey_trouble

# Tenemos 2 monos, a y b, y los parametros a_smile y b_smile
# que indican si cada uno sonrie. Estamos en problemas si ambos
# o ninguno sonrie. Devuelve si estamos en problemas

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not  a_smile and not b_smile:
    return True
  else:
    return False



############### sum_double 

# Dados dos valores enteros devuelve su suma. A no ser que estos
#  sean iguales, en tal caso devolver el doble de su suma.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
  if  a == b:
    return (2*a) + (2*b)
  else:
    return a+b
  


############### diff21

# Dado un valor entero, devuelve la diferencia absoluta
# entre n y 21, a exepcion de que n sea mayor a 21 en tal caso 
# devolver el doble de su diferencia.

# diff21(19) → 2
# diff21(50) → 58
# diff21(21) → 0

def diff21(n):
  if  n > 21:
    return(n - 21) * 2
  else:
    return 21 - n
      


############### parrot_trouble 

# Tenemos un loro que habla muy fuerte. El parametro "hora"
# es la hora actual en el rango 0..23. Estamos en problemas si
# el loro esta hablando y la hora es antes de las 7 o despues
# de las 20. Devuelve True si estamos en problemas.

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def parrot_trouble(habla, hora):
  if habla == True and hora < 7:
    return True
  elif habla == True and hora > 20:
    return True
  else:
    return False
    


############### makes10 

# Dados 2 enteros, a y b, devolver True si uno de ellos es
# 10 o si la suma de ambos es 10.

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  if a == 10 or b == 10 or (a+b) == 10:
    return True
  else:
    return False
      


############### near_hundred 

# Dado un entero n, devuelve True si esta a 10 de 100 o 200.
# //Nota: abs(num) calcula el valor absoluto de un numero.

# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
  if (90 <= n and n <= 110) or (n <= 110 and n>=90) or (n >= 190 and n<=210):
    return True
  else:
    return False
    
def near_hundred_abs(n):
   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    


############### pos_neg 

# Dados 2 valores enteros, devolver True si uno de ellos es
# negativo y el otro positivo. Si el parametro "negativo" es True, 
# entones devuelve True solo si ambos son negativos.

# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def pos_neg(a, b, negativo):
  if  negativo == True:
    return (a < 0 and b < 0)
  else:
    return (a >=0 and b<=0) or (b>=0 and a<=0)
      


############### not_string  

# Dada una cadena, devuelve una nueva donde NOT sea agreguegado al
# comienzo. De todas maneras, si la cadena ya empieza con "NOT", 
# devuelve la cadena sin cambios.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
  if str.startswith('not'):
    return str
  else:
    return 'not '+str
      


############### missing_char   

# Dada una cadena no vacia y un entero n, devuelve una nueva cadena
# donde el caracter del indice n sea removido. El valor de n sera un 
# indice valido de un caracter en la cadena original.

# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  if  n == 0:  
    return str[1:]
    
  elif n == len(str)-1:
    return str[:n]
    
  else :
    return str[:n]+str[n+1:]
      


############### front_back 

# Dada una cadena devuelve una nueva cadena donde el primer y ultimo
# caracter fueron intercambiados

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  largo=len(str)-1
  if len(str) <= 1:
    return str
  else:
    primer = str[:1]
    ultimo = str[-1:]
    medio = str[1:largo]
  
    return ultimo+medio+primer
      


############### front3

# Dada una cadena, vamos a decir que el comienzo son los primeros
# 3 caracteres de la cadena. Si el largo de la cadena is menor a 3
# el comienzo sigue siendo lo que sea que este ahi. Devuelve una nueva
# cadena que triplique el comienzo.

# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

def front3(str):
  return 3*str[:3]
