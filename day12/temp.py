import numpy as np

four = np.array([[1, 2, 3], [4, 5, 6]])
print(four)
print("-" * 100)
# ndarray也是可变数据类型
four1 = four
print(id(four1))
print("-" * 100)
four.shape = (3, 2)  # 改变数组的形状
print(four)
print(id(four))
print(id(four1))  # 数组的id不变
print("-" * 100)

# 返回一个新数组，reshape后id和之前的不一样
four2 = four.reshape(2, 3)
print(id(four))
print(id(four2))
print(four2)
