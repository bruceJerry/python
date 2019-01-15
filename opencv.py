import numpy as np


dt = np.dtype([('age', np.int8)])
print(dt)
print(type(dt))

dd = np.dtype([('size', np.int16)])  # name and type
print(dd)
print(type(dd))

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=dd)
print(a['size'])

student_type = np.dtype([('name', 'S40'), ('age', np.int8), ('marks', np.float32)])
print(student_type)

student = np.array([[('bruce', 21, 89.4), ('linda', 32, 99.5)], [('bruce', 21, 89.4), ('linda', 32, 99.5)]], dtype=student_type)
print(student)

test = np.array([12, 34, 56])

print("秩 = {0}".format(test.ndim))
print("秩 = {0}".format(student.ndim))
print("维度={}".format(test.shape))
print("维度={}".format(student.shape))
print("大小={}".format(test.size))
print("类型={}".format(test.dtype))
print("item size={}".format(test.itemsize))

x = np.empty([3, 2])
print(x)

y = np.zeros([3, 2])
print(y)

z = np.ones([3, 2])
print(z)

# 创建 randn(size) 服从 X~N(0,1) 的正态分布随机数组
xx = np.random.randn(2, 3)
print(xx)

yy = np.random.randint(100, 300, (3, 3))
print(yy)

xxx = [[1, 2, 3], [4, 4]]
yyy = np.asarray(xxx)
print(yyy.shape)

frombuffer_val = b'hello world'
res = np.frombuffer(frombuffer_val, dtype='S1')
print(res)

list = range(5)
print(list)
it = iter(list)
res = np.fromiter(it, dtype=float)
print(res)

x = np.arange(10, 20, 2)
print("last item = {0}".format(x[-1]))

a = np.linspace(10, 20,  5, endpoint = True)
print(a)

a = np.arange(0, 60, 5).reshape(3,4)
print(a.T)
b = a.T
for x in np.nditer(a, order='F'):
    print(x, end=", ")
print("\n")