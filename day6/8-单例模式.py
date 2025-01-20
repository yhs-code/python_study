class MusicPlayer:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    player1 = MusicPlayer("QQ音乐")
    print(id(player1))
    print(player1.name)
    print("-" * 100)
    player2 = MusicPlayer("网易云")
    print(id(player1))
    print(player1.name)
    print(id(player2))
    print(player2.name)
