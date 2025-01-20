class PersonalInformation:
    """
    私有属性和私有方法：__ + 变量名/方法名
    私有属性和私有方法只能在类中的函数调用，不能在类外被调用
    """

    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.__ID = ID

    def __private_method(self):
        print("这是一个私有方法")

    def call_private_method(self):
        self.__private_method()
        print(f"ID是{self.__ID}")


class Person(PersonalInformation):
    def get_ID(self):
        print(self.__ID)  # 继承父类，但是无法使用父类的私有属性和私有方法


if __name__ == '__main__':
    pi = PersonalInformation("zhangsan", 19, "88888888")
    print(pi.name)
    print(pi.age)
    # print(pi.__ID)  # 打印私有变量会报错
    # print(pi.__private_method)  # 打印私有方法同样会报错
    pi.call_private_method()
    print("-" * 100)
    p = Person("lisi", 22, "99999999")
    # p.get_ID()  # 会报错
