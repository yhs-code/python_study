import os


def seek_start():
    """
    相对于开头（文件起始位置）进行偏移
    :return:
    """
    file = open("file1", mode="r+", encoding='utf-8')
    file.seek(2, os.SEEK_SET)  # 相对于开头偏移两个字节
    text = file.read()
    print(text)
    file.close()


def seek_end():
    """
    相对于文件尾部进行偏移
    :return:
    """
    file = open("file1", mode="r+", encoding='utf-8')
    file.seek(0, os.SEEK_END)  # 采用非字节流方式打开文件，如果是按尾部偏移，则偏移量只能写0
    text = file.read()
    print(text)  # 读不到字符串，因为光标在文件结尾
    file.close()


def seek_cur():
    """
    相当于当前位置进行偏移
    :return:
    """
    file = open('file1', mode='r+', encoding='utf8')
    file.seek(0, os.SEEK_CUR)  # 采用非字节流方式打开文件，如果是按当前位置偏移，则偏移量只能写0
    text = file.read(5)
    print(text)  # 读不到内容，是空字符串
    file.close()


def seek_b_cur_end():
    """
    在b模式（字节流模式）下打开，常用与读取图片，音视频
    采用字节流模式进行偏移没有特殊限制
    :return:
    """
    file = open("file1", mode='rb+')
    file.seek(5, os.SEEK_CUR)
    file.seek(-3, os.SEEK_END)
    bits = file.read()
    print(bits)
    file.close()


if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_cur()
    seek_b_cur_end()
