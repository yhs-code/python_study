def demo1():
    num = int(input("输入整数："))
    print("I am demo1")
    return num


def demo2():
    num2 = demo1()
    print("I am demo2")
    return num2


try:
    print(demo2())  # 发生错误后，从发生错误的那一条语句开始回传，不会执行接下来的语句
except Exception as e:
    print(f"未知错误:{e}")
