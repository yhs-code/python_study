def sym_judge():
    try:
        num = int(input("请输入一个整数"))
        s = str(num)
        i = 0
        while i < len(s) / 2:
            if s[i] != s[len(s) - i - 1]:
                print("非对称")
                return
            i += 1
        print("对称")
    except ValueError:
        print("您输入的不是一个整数")


if __name__ == '__main__':
    sym_judge()
