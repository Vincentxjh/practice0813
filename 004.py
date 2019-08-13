#第四个练习 - 创建水果类及其派生类
class Fruit:
    color = "绿色"
    def harvest(self, color):
        print("水果是：" + color + "的！")
        print("水果已经收获......")
        print("水果原来是：" + Fruit.color + "的！")
class Apple(Fruit):
    color = "红色"
    def __init__(self):
        print("我是苹果")
class Orange(Fruit):
    color = "橙色"
    def __init__(self):
        print("\n我是橘子")
apple = Apple()
apple.harvest(apple.color)
orange = Orange()
orange.harvest(orange.color)