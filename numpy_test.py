import numpy as np

a, b = 13, 17
print(bin(a), bin(b))

c = np.bitwise_and(a, b)
print(c)

c = np.bitwise_or(a, b)
print(c)

x = np.char.add(['hello', 'hi'], [' xyz', ' bruce'])
print(x)

print(np.char.multiply("hello ", 3))

print(np.char.center("hello", 20, "*"))

print(np.char.capitalize("hello"))

print(np.char.title("how are you"))

print(np.char.lower("HOW ARE YOU"))  # upper

print(np.char.splitlines('hello\nhow are you'))

print(np.char.strip("ahelloa", "oah"))






