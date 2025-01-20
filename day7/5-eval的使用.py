def read_conf():
    """
    读取配置
    :return:
    """
    file = open("file4", mode="r+", encoding='utf-8')
    text = file.read()
    print(text)
    my_dict = eval(text)
    print(type(my_dict))
    print(my_dict)
    file.close()


if __name__ == '__main__':
    read_conf()
