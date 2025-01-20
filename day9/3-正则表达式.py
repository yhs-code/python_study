import re


def simple():
    """
    初识正则表达式
    re.rematch(正则表达式, 要匹配的字符串)
    :return:
    """
    result = re.match("www", "www.baidu.com")
    if result:
        print(result.group())


def single_char_match():
    """
    匹配单个字符
    :return:
    """
    ret = re.match(r".", "m")  # . 匹配任意字符
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"he.lo", "hello")
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"[hH]", "Hello")  # []匹配所列举的字符
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"[a-z]", "hello")  # []内可以标注一个范围:a-z
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"[a-z]ello", "hello world")
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"嫦娥\d号", "嫦娥6号")  # \d匹配数字
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"你\w", "你好啊")
    print(ret.group())


def multi_char_match():
    """
    匹配多个字符
    :return:
    """
    ret = re.match(r"[A-Z][a-z]*", "M")
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"[A-Z][a-z]*", "Aabcd")
    print(ret.group())
    print("-" * 100)

    # 匹配多字符的格式只与前一个单字符格式组合使用，此处*与[a-z]组合使用
    ret = re.match(r"[A-Z][a-z]*", "AbbbbAAAA")
    print(ret.group())
    print("-" * 100)

    code_name = ["name1", "_name", "123name", "__name__"]
    for name in code_name:
        ret = re.match(r"[a-zA-Z_]+\w", name)
        if ret:
            print(f"{ret.group()} 符合命名规则")
        else:
            print(f"{name} 不符合命名规则")
    print("-" * 100)

    ret = re.match(r"[0-9]?[0-9]", "6")  # 此时的6匹配的是后面的[0-9]
    # ret = re.match(r"\d?\d", "6") # [0-9]可以直接写成\d
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"[a-zA-Z_0-9]{6}", "123abc456def789")
    print(ret.group())
    print("-" * 100)

    # 至少出现6个匹配字符，最多出现20个匹配字符
    ret = re.match(r"[a-zA-Z_0-9]{6,20}", "123abc456def&&&&789")
    print(ret.group())
    print("-" * 100)


def begin_end_match():
    """
    匹配开头和结尾
    :return:
    """
    # 一般match函数无需设置开头^匹配，但是如果用的是search，则需要用到^
    ret = re.search("hello", "nihao hello")
    print(ret.group())
    print("-" * 100)

    ret = re.search("^hello", "nihao hello")
    if ret:
        print(ret.group())
    else:
        print("hello不在开头")
    print("-" * 100)

    web_name = ["http:zhangwei_shi_ge_hun_dan.com", "www.baidu.com", "https://www.bilibili.com/",
                "www.http.https.com"]
    for name in web_name:  # 找到https:开头的网址
        ret = re.search(r"^http:[^ ]+", name)  # ^ 和 http:连用，[^ ]和+连用-->[^ ]代表非空白
        if ret:
            print(f"http网址为{ret.group()}")
        else:
            print(f"{name}不是http网站")
    print("-" * 100)

    email_name = ["xiaoming@163.com", "88888888@qq.com", "James@163.commmmmmm", "111@1631com"]
    for name in email_name:
        # \w 和 + 连用， @163\.com和$连用, \.代表转义，因为.在正则表达式中代表任意字符
        ret = re.match(r"\w+@163\.com$", name)
        if ret:
            print(f"符合163格式的邮箱：{ret.group()}")
        else:
            print(f"不符合163格式的邮箱：{name}")
    print("-" * 100)


def group_match():
    """
    匹配分组
    :return:
    """
    # 匹配0到100
    # [1-9]?匹配0个或者1个1-9的字符，\d$代表必须以数字结尾，| 代表满足两边任意一个即可
    ret = re.match(r"[1-9]?\d$|100", "99")
    print(ret.group())
    print("-" * 100)
    # 如果\d后没有$，则出现 00，01,02,03...09时，\d会默认匹配到0
    # ret = re.match(r"[1-9]?\d", "08")
    # print(ret.group())
    # print("-" * 100)

    email_name = ["xiaoming@163.com", "88888888@qq.com", "James@163.commmmmmm", "111@1631com"]
    # 匹配出163邮箱和qq邮箱
    for name in email_name:
        ret = re.match(r"\w+@(163|qq)\.com$", name)  # 加了()代表里面匹配到的内容所属一个分组
        if ret:
            print(f"符合要求的邮箱：{ret.group()}")
        else:
            print(f"不符合要求的邮箱：{name}")
    print("-" * 100)

    dir_path = "D:\pythonProject\project1\current_project.py"
    # \在正则表达式用作转义字符，故用 \\ 来代表字符 \
    ret = re.match(r"([^\\]+)\\([^\\]+)\\([^\\]+)\\([^\\]+)", dir_path)
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))
    print(ret.group(3))
    print(ret.group(4))
    print("-" * 100)

    # 分组后还可以用 \num代表第几个分组，如\1代表第一个分组
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")  # \1 匹配的就是 ([a-zA-Z]*)
    print(ret.group())
    print("-" * 100)

    ret = re.match(r"<(\w+)><(\w+)>.+</\2></\1>", "<html><w1>www.baidu.com</w1></html>")
    print(ret.group())
    print("-" * 100)

    # 由于\1 \2等写法易读性较差，所以可以通过(?P<name>)起名字，并通过(?P=name)格式引用
    ret = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>.+</(?P=name2)></(?P=name1)>",
                   "<html><w1>www.bilibili.com</w1></html>")
    print(ret.group())


def add(x):
    result = x.group()
    return str(int(result) + 100)


def other_function():
    """
    re模块中的其他函数：search findall sub split
    :return:
    """
    ret = re.search(r"\d+", "阅读次数:9999，点赞次数：888")
    print(ret.group())
    print("-" * 100)

    ret = re.findall(r"\d+", "阅读次数:9999，点赞次数：888")  # 会返回一个list
    print(ret)
    print("-" * 100)

    # sub将匹配到的数据进行进行替换
    ret = re.sub(r"\d+", "1000", "int a = 997")
    print(ret)
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "int a = 1200")
    print(ret)
    ret = re.sub(r"\d+", add, "int a = 1300")
    print(ret)
    print("-" * 100)

    # sub可选择替换的数量
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    new_text = re.sub(pattern, replacement, text, count=3)
    print(new_text)
    print("-" * 100)


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


def use_finditer():
    """
    使用finditer
    :return:
    """
    # 示例用法
    text = "abc123def456ghi789"
    pattern = r"\d+"
    second_match = find_second_match(pattern, text)
    print(second_match)


def number_generator(start=0):
    while start <= 5:  # 无限循环，持续生成数字
        yield start  # 程序在这里暂停，start值被return回来，下次函数进来也从这开始
        start += 1
    return


def use_generator():
    """
    使用生成器，理解next
    :return:
    """
    # # 示例使用
    gen = number_generator()  # 创建生成器实例，从0开始
    print(type(gen))
    # print(next(gen))  # 输出 0
    # print(next(gen))  # 输出 1
    # print(next(gen))  # 输出 2
    for i in gen:
        print(i)


def use_findall():
    """
    findall函数的一些机制问题
    :return:
    """
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(ret_s)
    print("-" * 100)

    # findall函数有bug，如果pattern中有分组()则执行findall后会返回分组的内容，所以需要在分组中加上?:
    # findall 内部的设计机制，在分组前面加?:
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern.findall(ret_s)
    print(ret)
    print("-" * 100)

    pattern1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    # search 没问题
    ret1 = pattern1.search(ret_s)
    print(ret1.group())


def use_sub():
    long_text = """<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
    """
    # print(long_text)
    ret = re.sub(r'<[^>]*>|&nbsp;|\n|\s', '', long_text)
    print(ret)


def use_split():
    # 根据: | 空格对后续字符串进行切割
    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


def greedy_and_no_greedy():
    """
    python的正则表达式默认是贪婪的，会包含尽可能多的字符串，通过加?可以变为非贪婪
    :return:
    """
    s = "This is a number 234-235-22-423"
    # .+ 会一直读取到字符3，因为有\d所以4不能被.+读完
    ret = re.match(r".+(\d+-\d+-\d+-\d+)", s)
    print(ret.group(1))
    print("-" * 100)
    # 加了?后变为非贪婪
    ret = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(ret.group(1))
    print("-" * 100)
    print(re.match(r"aa(\d+)", "aa2343ddd").group(1))
    print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))
    print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))
    # 字符要匹配ddd，所以\d+?就算是非贪婪也必须读完2343
    print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))


# re.A 不让\w 匹配汉字
# re.I 是否区分大小写
# re.S 可以让.匹配上\n
def use_option():
    print(re.match(r'\w*', 'abc函', flags=re.A).group())
    print("-" * 100)
    print(re.match(r'a*', 'aA', flags=re.I).group())
    print("-" * 100)
    print(re.match(r'.*', 'abc\ndef', flags=re.S).group())


if __name__ == '__main__':
    # simple()
    # single_char_match()
    # multi_char_match()
    # begin_end_match()
    # group_match()
    # other_function()
    # print("-----------finditer的使用：-------------")
    # use_finditer()
    # print("-----------finditer的使用：-------------")
    # use_generator()
    # use_findall()
    # use_sub()
    # use_split()
    # greedy_and_no_greedy()
    use_option()
