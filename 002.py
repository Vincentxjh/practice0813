#第二个练习 - 通过类属性统计类的实例个数
class Geese:
    '''大雁类'''
    neck = "脖子较长"
    wing = "振翅频率高"
    leg = "腿位于身体的中心支点，行走自如"
    num = 0
    def __init__(self):
        Geese.num += 1
        print("\n我是第" + str(Geese.num) + "只大雁，我是大雁类！我有以下特征：")
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)
list = []
for i in range(4):
    list.append(Geese())
print("\n总共有" + str(Geese.num) + "只大雁。")