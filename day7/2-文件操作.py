def open_r():
    """
    读取文件
    文件如果不存在 ，则会报错
    :return:
    """
    file = open('file1', mode='r', encoding='utf-8')
    text = file.read()  # read没有参数默认读到最后
    print(text)
    file.close()


def open_rw():
    """
    读写方式打开文件
    文件如果不存在，则会报错
    :return:
    """
    file = open("file2.txt", mode="r+", encoding="utf-8")
    text = file.read()
    print(text)
    file.write("hello garbage")
    file.close()


def open_w():
    """
    写模式打开文件，文件存在则清空文件，文件不存在则创建文件
    :return:
    """
    file = open("file3", mode="w", encoding="utf-8")
    file.write("快跑，千万别学编程！")
    file.close()


def open_a():
    """
    追加模式打开，如果文件存在，打开后光标会自动落在文件末尾，
    如果文件不存在也会创建文件
    :return:
    """
    file = open("file4", mode="a", encoding="utf-8")
    file.write("快跑！！！！")
    file.close()


def use_readline():
    file = open("file2.txt", encoding="utf-8")
    while True:
        text = file.readline()
        if not text:
            break

        print(text, end="")
    file.close()


if __name__ == '__main__':
    # open_r()
    # open_rw()
    # open_w()
    # open_a()
    use_readline()
