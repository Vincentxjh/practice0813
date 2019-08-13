#第w五个练习 - 在派生类中调用基类的__init__()方法定义类属性
class Fruit:
    def __init__(self, color = "绿色"):
        Fruit.color = color
    def harvest(self,color):
        print("水果是：" + color + "的！")
        print("水果已经收获......")
        print("水果原来是：" + Fruit.color + "的！")
class Apple(Fruit):
    color = "红色"
    def __init__(self):
        print("我是苹果")
        super().__init__()
class Sapodilla(Fruit):
    def __init__(self, color):
        print("\n我是人参果")
        super().__init__(color)
    def harvest(self, color):
        print("人参果是：" + color + "的！")
        print("人参果已经收获......")
        print("人参果原来是：" + Fruit.color + "的！")
apple = Apple()
apple.harvest(apple.color)
sapodilla = Sapodilla("白色")
sapodilla.harvest("金黄色带紫色条纹")


#如果不调用基类__init__()方法，还可以用以下代码代替
'''class Fruit:
    color = "绿色"
    def harvest(self, color):
        print("水果是：" + self.color + "的！")
        print("水果已经收获......")
        print("水果原来是：" + Fruit.color + "的！")
class Apple(Fruit):
    color = "红色"
    print("我是苹果")
class Sapodilla(Fruit):
    def __init__(self, color):
        Sapodilla.color = color
        print("\n我是人参果")
    def harvest(self, color):
        print("人参果是：" + color + "的！")
        print("人参果已经收获......")
        print("人参果原来是：" + Sapodilla.color + "的！")
apple = Apple()
apple.harvest(apple.color)
sapodilla = Sapodilla("白色")
sapodilla.harvest("金黄色带紫色条纹")
'''
