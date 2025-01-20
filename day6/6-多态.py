class Dog(object):  # 默认就继承object类
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name}在快乐的玩耍")


class RoaringDog(Dog):
    def __init__(self, name, owner):
        super(RoaringDog, self).__init__(name)
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog: Dog):
        print(f"{self.name} 与狗狗 {dog.name} 一起快乐的玩耍")
        dog.game()


if __name__ == '__main__':
    wangcai = Dog("旺财")
    xiaotianquan = RoaringDog("哮天犬", "二郎神")
    zhangsan = Person("zhangsan")
    # 不同的类可被同一个函数调用
    zhangsan.game_with_dog(wangcai)
    zhangsan.game_with_dog(xiaotianquan)
