# 类的常用四个内置方法 __init__  __del__  __str__  __new__
class Cat:
    # def __new__(cls, *args, **kwargs):
    #     """
    #     对象创建时执行的函数，一般默认使用系统内置的，如果要实现“单例模式”等一些特殊模式，则需要重写__new__
    #     :param args:
    #     :param kwargs:
    #     """

    def __init__(self, name):
        """
        对象初始化时执行的函数
        :param name:
        """
        print("这是一个初始化方法")
        self.name = name

    def __del__(self):
        """
        对象被销毁时执行的内置函数
        :return:
        """
        print(f"{self.name} 对象被销毁")

    def __str__(self):
        """
        对象描述信息，通过print(对象)可得到该函数返回值
        :return:
        """
        return f"对象 {self.name}"

    def eat(self):
        print(f"{self.name}吃鱼")

    def drink(self):
        print(f"{self.name}喝水")


if __name__ == '__main__':
    kitty = Cat("kitty")
    print("-" * 100)
    kitty.eat()
    print("-" * 100)
    kitty.drink()
    print("-" * 100)
    print(kitty)
    print("-" * 100)
    # kitty.name = "hello kitty" # 不规范的编程，不可在类外给对象修改属性
