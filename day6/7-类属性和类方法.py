class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    def func(self):
        print(f"{self.name}可以做很多事情")

    @classmethod
    def show_tool_count(cls):
        """
        classmethod不使用对象属性，只使用类属性和类方法
        :return:
        """
        print(cls.count)

    @staticmethod
    def help():
        """
        staticmethod不使用对象属性和方法，也不使用类属性和方法
        :return:
        """
        print("这是一个工具类")


if __name__ == '__main__':
    tool1 = Tool("充电器")
    print(tool1.count)
    tool2 = Tool("插头")
    print(tool2.count)
    print(Tool.count)
    print("-" * 100)
    Tool.show_tool_count()
    print("-" * 100)
    Tool.help()
