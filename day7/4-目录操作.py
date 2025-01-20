import os


def use_rename():
    """
    理解相对路径，绝对路径
    :return:
    """
    os.rename("./dir1/file1", "./dir1/file2")
    os.remove('./dir1/file2')  # 移除文件


def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    print("-" * 100)
    os.mkdir('dir_temp')  # 创建一个目录
    print(os.getcwd())
    print("-" * 100)
    file_list = os.listdir('.')
    print(file_list)
    os.rmdir('dir_temp')  # 只能移除空目录


def change_dir():
    """
    改变当前路径
    :return:
    """
    print(os.getcwd())
    os.chdir('dir1')
    print(os.getcwd())


def scan_dir(current_path, width):
    """
    深度优先遍历
    :param current_path:
    :param width:
    :return:
    """
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' ' * width, file)  # 打印文件名，width代表多少个空格
        new_path = current_path + '/' + file
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


def use_stat(file_path):
    """
    获取文件相关属性
    :return:
    """
    file_info = os.stat(file_path)
    print(f'size:{file_info.st_size}, uid:{file_info.st_uid},'
          f' mode:{file_info.st_mode:x}, mtime:{file_info.st_mtime}')
    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    # scan_dir('.', 0)
    use_stat("file4")
