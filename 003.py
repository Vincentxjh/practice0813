#第三个练习 - 在模拟电影点播功能时应用属性
class TVshow:
    list_film = ["战狼2", "红海行动", "西游记女儿国", "熊出没", "变形记"]
    def __init__(self, show):
        self.__show = show
    @property
    def show(self):
        return self.__show
    @show.setter
    def show(self, value):
        if value in TVshow.list_film:
            self.__show = "您选择了《" + value + "》，稍后为您播放"
        else:
            self.__show = "您点播的电影不存在"
tvshow = TVshow("战狼2")
print("正在播放：《" + tvshow.show + "》")
print("您可以从", (tvshow.list_film), "中选择要点播的电影")
tvshow.show = "红海行动"
print(tvshow.show)

