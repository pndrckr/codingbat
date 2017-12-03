############### first_last6  

# Dado un array de numeros enteros, devuelve True si
# el 6 es el primer o ultimo elemento.

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False
  
  
  
############### same_first_last   

# Dado un array de numeros enteros, devuelve True si
# el largo es 1 o mas y el primer y ultimo elemento son iguales.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

def same_first_last(nums):
  return len(nums) >=1 and nums[0] == nums[-1]



############### make_pi

# Devuelve un array de enteros de largo 3 que contengan los
# primeros 3 digitos de pi {3, 1, 4}

#make_pi() → [3, 1, 4]

def make_pi():
  pi = [3, 1, 4]
  return pi



############### common_end

# Dados 2 arrays de entero, a y b, devuelve True si
# coinciden el primer o ultimo elemento

# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]



############### sum3 

# Dado un array de numeros enteros de largo 3
# devuelve la suma de los elementos

# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(nums):
  return nums[0]+nums[1]+nums[2]



############### rotate_left3

# Dado un array de numeros enteros de largo 3
# devuelve un array donde el primer elemento este ultimo.

# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]




############### reverse3

# Dado un array de numeros enteros de largo 3  devuelve
# un array con los elementos ordenados a la inversa

# rotate_left3([1, 2, 3]) → [3, 2, 1]
# rotate_left3([5, 11, 9]) → [9, 11, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
  return [nums[2],nums[1],nums[0]]



############### max_end3

# Dado un array de numeros enteros de largo 3 descubre cual
# es mayor del primer o ultimo elemento y devuelve un array
# donde los otros elementos tomen ese valor.

# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
  if nums[0] > nums[2]:
    n = nums[0]
  else:
    n = nums[2]
  return [n,n,n]



############### sum2 

# Dado un array de enteros, devuelve la suma de los priemros
# dos elementos. Si el array es menor a 2 suma los elementos
# existentes, devolviendo 0 si el array esta vacio.

# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(nums):
  lg=len(nums)
  if  lg == 0:
    return 0
  elif lg == 1:
    return nums[0]
  else:
    return nums[0]+nums[1]



############### middle_way

# Dados 2 arrays de enteros, a y b de 3 elementos cada uno,
# devuelve un array de largo dos que contenga el elemento del
# medio de cada array(a y b).

# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
  return [a[1],b[1]]



############### make_ends

# Dadoo un array de enteros, devuelve un array de largo 2 que 
# contenga el primer y ultimo elemento del array original.
# El array original sera de largo 1 o mas.

# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
    return [nums[0],nums[-1]]



############### has23 

# Dadoo un array de enteros de largo 2, devuelve True si
# contiene un 2 o un 3.

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
  return 2 in nums or 3 in nums
