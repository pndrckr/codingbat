############### hello_name 

# Dada una cadena nombre, ej "Bob", devuelve un 
# saludo de la siguiente forma: "Hola Bob!"

# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
  return "Hola "+name+"!"

  
  
############### hello_name 

# Dadas dos cadenas, a y b, devuelve el resultado de ponerlas
# juntas en el orden abba ej:"Hi"y"Bye" devuelve "HiByeByeHi"

# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
  return a+b+b+a
  
  
  
############### make_tags 

# Crea taags HTML a partir de dos cadenas
# tags y palabras

# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>''

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"
  
  
  
############### make_out_word 

# Dada una cadena "out" de 4 caracteres de longitud, y
# y otra cadena con una palabra, devuelve la palabra en
# medio de la cadena "out"

# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out, word):
  return out[0:2]+word+out[2:4]



############### extra_end

# Dada una cadena haz una cadena nueva a partir de los
# ultimos 2 caracteres repetidos 3 veces
# La Cadena debe tener al menos 2.

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
  if len(str) >= 2:
    return str[-2:]*3
    
    

############### extra_end

# Dada una cadena devuelve una cadena nueva a partir
# de los primeros 2 caracteres. Si la cadena es menor a
# 2 o vacia devuelvela como esta.

# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'

def first_two(str):
  return str [0:2]
  
  
  
############### first_half

# Dada una cadena de numeros pares, devuelve la primer
# mitad de la cadena.

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
  largo = len(str)
  if largo%2 == 0:
    return str[:largo/2]
    
    
    
############### without_end 

# Dada una cadena devuelve una version sin el primer ni 
# el ultimo caracter

# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
  return str[1:-1]



############### combo_string  

# Dadas 2 cadenas, a y b, devuelve una cadena de la 
# siguiente forma corta+larga+corta. Las cadenas no seran
# del mismo largo pero si pueden estar vacias

# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
  l_a = len(a)
  l_b = len(b)
  if  l_a > l_b:
    return b+a+b
  else:
    return a+b+a
    
    
  
############### non_start   

# Dadas 2 cadenas, devuelve una cadena que concatene las mismas
# pero sin su primer caracter.  Las cadenas seran de al menos 1
# de largo.

# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def non_start(a, b):
  return a[1:]+b[1:]



############### left2   

# Dada una cadena, devuelve una version de la misma donde los
# primeros 2 caracteres esten al final. La cadena sera de al menos 2
# de largo.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
  return str[2:]+str[:2]
