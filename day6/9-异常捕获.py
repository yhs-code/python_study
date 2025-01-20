def use_exception1():
    try:
        num = int(input("请输入一个整数："))
        print(num)
    except:
        print("输入的必须是整数")


def use_exception2():
    """
    掌握不同的异常类型，可以跳转到不同的分支上
    :return: 
    """
    try:
        num = int(input("请输入一个整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入一个整数")
    except ZeroDivisionError:
        print("除 0 错误")


def use_exception3():
    """
    掌握不同的异常类型，可以跳转到不同的分支上
    :return:
    """
    try:
        num = int(input("请输入一个整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入一个整数")
    except Exception as e:
        print(e)


def use_exception4():
    """
    学习else 和 finally
    :return:
    """
    try:
        num = int(input("请输入一个整数："))
        result = 8 / num
        print(result)
        return
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as e:
        print(e)
    else:
        print("正常执行")  # 如果正常执行时有return，则不会执行else
    finally:
        print("执行完成，但是不保证正确")  # 不受到return的影响


def test():
    num = 1 / 0


def use_exception5():
    """
    如何捕获异常发生的文件（模块）和具体行数
    :return:
    """
    try:
        test()
    except Exception as e:
        print(e)
        print("异常发生的文件（模块）：", e.__traceback__.tb_frame.f_globals["__file__"])
        print("异常发生的行数：", e.__traceback__.tb_lineno)


def use_exception6():
    try:
        test()
    except Exception as e:
        import traceback
        # 打印异常信息
        print("异常信息：", e)

        # 获取完整的回溯信息
        tb = e.__traceback__
        while tb.tb_next:  # 循环到异常发生的最后一层，即 test 函数内部
            tb = tb.tb_next

        # 输出异常发生的文件、行号和代码内容
        filename = tb.tb_frame.f_code.co_filename
        lineno = tb.tb_lineno
        func_name = tb.tb_frame.f_code.co_name

        print(f"异常发生的文件：{filename}")
        print(f"异常发生的函数：{func_name}")
        print(f"异常发生的行数：{lineno}")

        # 如果需要打印具体行内容，可以用 open 读取
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(f"发生异常的代码：{lines[lineno - 1].strip()}")


if __name__ == '__main__':
    # use_exception1()
    # use_exception2()
    # use_exception3()
    # use_exception4()
    # use_exception5()
    use_exception6()
