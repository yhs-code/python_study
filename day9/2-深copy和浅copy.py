import copy


def use_list_copy():
    """
    使用列表自身的copy
    """
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 10
    print(a)
    print(b)


def use_copy():
    """
    使用copy包中的copy，浅拷贝，开辟新空间，但是内部元素直接进行赋值
    """
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 10
    print(c)
    print(d)
    print(id(c))
    print(id(d))


def use_copy2():
    """
    copy是浅拷贝，只做第一层copy
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    a[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)


def use_deepcopy():
    """
    递归去copy，不管有多少层，都会开辟新空间去复制数据
    """
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    a[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)


class Student:
    def __init__(self, name, age, score: list = []):
        self.name = name
        self.age = age
        self.score = score


def use_copy_own_object():
    """
    实际对于自定义对象的拷贝
    :return:
    """
    zhangsan = Student("zhangsan", 19, [77, 88, 99])
    zhangsan2 = copy.copy(zhangsan)
    zhangsan3 = copy.deepcopy(zhangsan)
    zhangsan.score[0] = 66
    print(zhangsan.score)
    print(zhangsan2.score)
    print("-" * 100)
    print(zhangsan3.score)


if __name__ == '__main__':
    # use_list_copy()
    # print("-"*100)
    # use_copy()
    # print("-"*100)
    # use_copy2()
    # print("-"*100)
    # use_deepcopy()
    # print("-" * 100)
    use_copy_own_object()
