#第六个练习 - 修改手机的默认语言
class Cellphone:
    def __init__(self):
        print("智能手机的默认语言为英文")
    def resetLanguage(self,newLanguage):
        print("将智能手机的默认语言设置为" + newLanguage)
Cellphone().resetLanguage("中文")