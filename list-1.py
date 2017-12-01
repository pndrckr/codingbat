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
