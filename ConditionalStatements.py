def immutableSequence(immutable):
   return tuple if immutable else list

seq = immutableSequence(immutable=True)
s = seq("Hellow")

print(type(s))


seq = immutableSequence(immutable=False)
seq("Hellow")

print(type(seq("Hellow")))