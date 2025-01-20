class A:
    def __init__(self):
        print("A类的init")

    def test(self):
        print("A的test")


class B:
    def __init__(self):
        print("B类的init")

    def test(self):
        print("B的test")

    def haha(self):
        print("B类的haha")


class C(A, B):
    def __init__(self):
        print("C类的init")
        super(C, self).__init__()

    def test1(self):
        print("C的test")


if __name__ == '__main__':
    c_object = C()
    c_object.test()
    c_object.test1()
    c_object.haha()
    # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
    # 输出结果A类在C类的后面，故C类的super()会先找A类，如果A类没有则会找B类
    print(C.__mro__)
