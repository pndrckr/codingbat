############### make_bricks

# Queremos hacer una fila de ladrillos que es "goal" de largo.
# Tenemos un numero de ladrillos de 1 (small) y otros de 5 (big)
# Devuelve True si es posible hacer la fila o False si no.

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  if goal%5 > small:
    return False
  elif goal > (small+big*5):
    return False
  else:
    return True



############### lone_sum

# Dados 3 valores enteros, a b c, devuelve su suma. A no ser que
# alguno de los valores se repita, no seran contados en la suma.

# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
  cnt = 0
  for n in (a, b, c):
    if n == a and n not in(b, c):
      cnt = cnt+n
    if n == b and n not in(a, c):
      cnt =cnt+n
    if n == c and n not in(a, b):
      cnt=cnt+n
  return cnt



############### lucky_sum

# Dados 3 valores enteros, a b c, devuelve su suma. A no ser que
# alguno de los valores sea 13, en tal caso no sera sumado y
# tampoco los valores a su derecha,

# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  for n in (a, b, c):
    if n == 13:
      if n == a:
        return 0
      if n == b:
        return a
      if n ==c:
        return a+b
  return a+b+c



############### no_teen_sum

# Dados 3 valores enteros, a b c, devuelve su suma. A no ser que
# alguno de los valores sea "teen" en el rango 13..19 inclusive,
# su valor cuenta como 0, exepto 15 y 16 que no cuentan. Escribe
# una definicion de ayuda "def fix_teen(n):" que tome un valor y
# devuelve el valor correspondiente. De esta forma se evita repetir
# el codigo. 

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
  teen=(range(13,15)+range(17,20))
  if n in teen:
    return 0
  else:
    return n
def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
