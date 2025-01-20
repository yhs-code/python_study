my_list = "This is a test string for testing Sort And sorted".split()
print(my_list)


def change_lower(para_str: str):
    return para_str.lower()


my_list.sort()
print(my_list)
print("-" * 100)
# key是传入的一个函数，相当于改变比较的规则
my_list.sort(key=change_lower)
print(my_list)

print('-' * 100)
student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]
# sort函数会直接改变原列表的元素顺序，sorted会返回一个新的排好序的列表
# lambda是一个匿名函数，lambda的语法：lambda 参数1, 参数2, ... : 返回值1, 返回值2, ...
# lambda用法举例：lambda a, b : a + b
print(sorted(student_tuples, key=lambda x: x[2]))
print("-" * 100)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        跟__str__一样都是通过print(对象)后执行的内置函数，但是比起__str__更加方便，可以返回非字符串类型
        如果同时有__str__和__repr__则通过print(对象)会优先执行__str__
        :return:
        """
        return repr((self.name, self.grade, self.age))


student = Student("zhangsan", 'A', 19)
print(student)
print("-" * 100)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda stu: stu.age))  # 此处的stu相当于列表中的元素
print("-" * 100)

from operator import itemgetter, attrgetter

print("使用operator系列")
# itemgetter：用于从 可迭代对象（如列表、元组、字典） 中提取元素。
# attrgetter：用于从 对象 中提取属性。
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_objects, key=attrgetter('age')))
print("使用operator系列进行多列排序")
print(sorted(student_tuples, key=itemgetter(0, 1)))
print(sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True))
print("-" * 100)
print("lambda进行多列排序")
print(sorted(student_tuples, key=lambda s: (s[1], s[2])))
print(sorted(student_tuples, key=lambda s: (s[1], -s[2])))  # 第一列升序，第二列降序
print("-" * 100)

print("查看排序稳定性")
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(0)))
mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}
print(sorted(mydict.items(), key=lambda x: x[1][1]))
print("-" * 100)

gameresult = [
    {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
    {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
    {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
    {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]

print(sorted(gameresult, key=lambda x: x['rating']))
print(sorted(gameresult, key=itemgetter("rating", "name")))
