class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"[{self.name}] 占地面积 {self.area} 平方"


class House:
    def __init__(self, house_type, area):
        """
        房子初始化方法
        :param house_type: 房子的类型（字符串）
        :param area: 房子的占地面积
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.items_list = []

    def __str__(self):
        return f"户型：{self.house_type}\n" \
               f"总面积：{self.area}\n" \
               f"剩余面积：{self.free_area}\n" \
               f"家居：{self.items_list}"

    def add_item(self, item: HouseItem):  # “变量名:类名”的格式是暗示变量是某个特定类
        if self.free_area < item.area:
            print("房间已经没有空位置了")
            return
        self.free_area -= item.area
        self.items_list.append(item.name)


if __name__ == '__main__':
    bed = HouseItem("席梦思", 6)
    sofa = HouseItem("沙发", 6)
    table = HouseItem("桌子", 4)

    print(bed)
    print(sofa)
    print(table)
    print("-" * 100)
    house = House("一室一厅", 20)
    house.add_item(bed)
    print(house)
    print("-" * 100)
    house.add_item(sofa)
    print(house)
    print("-" * 100)
    house.add_item(table)
    print(house)
    print("-" * 100)
    wardrode = HouseItem("衣柜", 10)
    house.add_item(wardrode)
