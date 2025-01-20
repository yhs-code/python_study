def input_password():
    pwd = input("请输入不少于八位的密码：")

    if len(pwd) >= 8:
        return pwd
    raise Exception("密码长度必须大于等于8位")


if __name__ == '__main__':
    try:
        print(input_password())
    except Exception as result:
        print(result)

    print("-" * 100)
    # 断言式 抛出异常写法
    try:
        assert 1 == 0, "你的程序出现了些许异常"
    except Exception as e:
        print(e)
