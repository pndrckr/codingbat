############### double_char

# Dada una cadena nombre, ej "Bob", devuelve  
# otra donde se duplique cada caracter.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  rs = ""
  for i in str:
   rs += i*2
  return rs


  
############### count_hi 

# Devuelve la cantidad de veces que la cadena
# "hi" aparece en la cadena dada.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  return len(str.split("hi"))-1
  
  
 
############### cat_dog 

# Devuelve True si la cadena contiene la misma
# cantidad de veces "cat" y "dog".

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  c = str.split("cat")
  d = str.split("dog")
  return len(c)==len(d)
