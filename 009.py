#第九个练习 - 模拟电影院的自动售票机选票页面

class Tvm:
    def __init__(self):
        print("欢迎使用自动售票机~~~")
    def chooseMovie(self):
        self.movies = {'1': '《环太平洋：雷霆再起》', '2': '《头号玩家》', '3': '《红海行动》'}
        print("请选择正在上映的电影：", end="")
        for key, value in self.movies.items():
            print(key + "、" + value, end=" ")
        print()
        self.chooseNum1 = input("")
        print("已选电影：", self.movies[self.chooseNum1])
    def chooseTime(self):
        self.times = {'1': '9:30', '2': '10:40', '3': '12:00'}
        print("请选择电影播放场次：", end="")
        for key, value in self.times.items():
            print(key + "、" + value, end=" ")
        print()
        self.chooseNum2 = input("")
        print("已选场次：", self.times[self.chooseNum2])
    def chooseSeat(self):
        self.seats = ["10-01", "10-02", "10-03", "10-04"]
        print("请选择座位剩余座位：")
        for i in self.seats:
            print(i, end=" ")
        print()
        self.chooseNum3 = input("")
        print("已选座位：", self.chooseNum3)
    def ticketPrint(self):
        print("\n正在出票......\n")
        print("电影：",self.movies[self.chooseNum1])
        print("播出时间：2019.04.08", self.times[self.chooseNum2])
        print("座位：", self.chooseNum3)
        print("\n出票完成，请别忘记取票")
tvm = Tvm()
tvm.chooseMovie()
tvm.chooseTime()
tvm.chooseSeat()
tvm.ticketPrint()


#参考答案
'''
class Ticketing_machine:
    Films_name=''
    seat=''
    Movie_field=''
    # 初始化方法
    def __init__(self):
        print('\n欢迎使用自动售票机~~')
        pass
    # 选择电影
    def Films(self,Films_name):
        Ticketing_machine.Films_name = Films_name
        print('已选电影：'+Films_name)
        pass
    # 选择电影场次
    def Movie_fields(self,Movie_field):
        Ticketing_machine.Movie_field="2018.4.12 "+Movie_field
        print('电影场次：' + Movie_field)
    # 选择座位
    def seats(self,seat):
        Ticketing_machine.seat = seat
        print('选择座位：' + seat)
        pass
    # 打印电影票
    def Cinema_ticket(self):
        print("电影："+Ticketing_machine.Films_name)
        print("播出时间：" + Ticketing_machine.Movie_field)
        print("座位：" + Ticketing_machine.seat)
        pass
# 初始化售票机对象
ticketing = Ticketing_machine()
# 提示正在上映电影
print('\n请选择正在上映的电影：1、《环太平洋：雷霆再起》  2、《头号玩家》  3、《红海行动》')
# 选择的电影
ticketing.Films('《头号玩家》')
# 提示选择场次
print('\n请选择电影播放场次：1、9:30  2、10:40  3、12:00')
# 选择的场次
ticketing.Movie_fields('10:40')
# 提示选择座位
print('\n请选择座位剩余座位：10-01,10-02,10-03,10-04')
# 选择的座位
ticketing.seats('10-3')
print('\n正在出票。。。\n')
# 电影票信息
ticketing.Cinema_ticket()
print('\n出票完成，请别忘记取票')
'''
