############### string_times 

# Dada una cadena y un entero positivo n, devuelve una cadena mas larga
# que copie n veces la cadena original

# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  return str*n

    

############### front_times 

# Dada una cadena y un entero positivo n, decimos que el comienzo 
# de la cadena son los primeros 3 caracteres, o lo que sea que este.
# Devuelve n copias del comienzo de la cadena.

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
  return str[0:3]*n
    


############### string_bits  

# Dada una cadena, devuelve una nueva hecha a raiz de los carateres 
# impares de la misma asi, "hola" seria "Hl".

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(str):
  largo = len(str)
  palabra = ""
  for n in range(largo):
    if n % 2 == 0:
      palabra = palabra +str [n]
  return  palabra  
    


############### string_splosion   

# Dada una cadena no vacia como "Code" devuelve otra cadena 
# como "CCoCodCode"

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  largo = len(str)
  palabra = ""
  for n in range(largo):
    if n <= largo:
        palabra = palabra + str[:n+1]
  return palabra
    


############### array_count9  

# Dada un array de numeros enteros, devuelve la cantidad de
# "9" que aparecen en la cadena

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  cn = 0
  for nu in nums:
    if nu == 9:
      cn +=1
  return cn
    


############### array_front9 

# Dada un array de numeros enteros, devuelve True si en los primeros
# cuatro elementos hay un "9". El largo de la cadena puede ser menor a 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  array_4 = nums[:4]
  if 9 in array_4:
    return True
  else:
    return False

  

############### array123 

# Dada un array de numeros enteros, devuelve True si existe la 
# secuencia 1, 2, 3.

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  largo_para_range = len(nums)-2
  for n in range(largo_para_range):
    if nums[n]==1 and nums[n+1]==2 and nums[n+2]==3:
      return True
  return False
