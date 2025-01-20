class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}在吃东西")

    def drink(self):
        print(f"{self.name}在喝水")

    def run(self):
        print(f"{self.name}在跑")

    def sleep(self):
        print(f"{self.name}在睡觉")


class Dog(Animal):  # 通过在类名后加上(父类)，代表继承父类
    def __init__(self, name, gender):
        super(Dog, self).__init__(name)
        self.gender = gender

    def bark(self):
        print(f"{self.name}在汪汪叫")

    def run(self):
        super(Dog, self).run()
        print(f"{self.name}不断在加速")


class RoaringDog(Dog):
    def __init__(self, name, gender, age):
        super(RoaringDog, self).__init__(name, gender)
        self.age = age

    def fly(self):
        print(f"{self.name}会飞")


if __name__ == '__main__':
    wangcai = Dog("旺财", "雄性")
    wangcai.bark()
    wangcai.run()
    print("-" * 100)
    xiaotianquan = RoaringDog("哮天犬", "雄性", 100)
    xiaotianquan.eat()
    xiaotianquan.bark()
    xiaotianquan.run()
    xiaotianquan.fly()
