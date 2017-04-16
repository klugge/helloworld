""" howto generate hello number (note list inversion slicing)
p = 0
for x in 'Hello, world!'[::-1]:
  p = p*88 + (ord(x) -32)

pp = p
"""
p = 384468986177509059152608

while p > 0:
  print(chr(p%88 +32), end='')
  p //= 88
print('')

""" an example of howtodo execfile() in python3 
def execfile(fname):
  exec(open(fname).read())
"""






