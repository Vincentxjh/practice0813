#第八个练习 - 打印没有销售明细
class Monthly_sales:
    # 月份的销售明细表（暂时只有1、2、3月份）
    commodity1 = (('T0001', '笔记本电脑'), ('T0002', '华为荣耀6X'), ('T0003', 'iPad'))
    commodity2 = (('T0001', '笔记本电脑'), ('T0002', '华为荣耀6X'), ('T0003', 'iPad'), ('T0004', '华为荣耀V9'))
    commodity3 = (('T0001', '笔记本电脑'), ('T0002', '华为荣耀6X'), ('T0003', 'iPad'), ('T0004', '华为荣耀V9'), ('T0005', 'MacBock'))
    # 初始化方法 传递月份 参数判断销售数据
    def __init__(self, monthly):
       #  判断该月份销售情况
       if monthly=='1':
           print('1月份的商品销售明细如下：')
           for i in range(len(Monthly_sales.commodity1)):
              print('{}{}  {}{}'.format('商品编号：',Monthly_sales.commodity1[i][0],'商品名称：',Monthly_sales.commodity1[i][1]))
           mothlys = input('\n请输入要查询的月份（比如1、2、3等）：')
           mothly_sales = Monthly_sales(mothlys)
       if monthly == '2':
           print('2月份的商品销售明细如下：')
           for i in range(len(Monthly_sales.commodity2)):
               print('{}{}  {}{}'.format('商品编号：', Monthly_sales.commodity2[i][0], '商品名称：',Monthly_sales.commodity2[i][1]))
           mothlys = input('\n请输入要查询的月份（比如1、2、3等）：')
           mothly_sales = Monthly_sales(mothlys)
       if monthly=='3':
           print('3月份的商品销售明细如下：')
           for i in range(len(Monthly_sales.commodity3)):
              print('{}{}  {}{}'.format('商品编号：',Monthly_sales.commodity3[i][0],'商品名称：',Monthly_sales.commodity3[i][1]))
           mothlys = input('\n请输入要查询的月份（比如1、2、3等）：')
           mothly_sales = Monthly_sales(mothlys)
       else:
        #    其它月份销售情况
        print('\n该月份没有销售数据或者输入月份有误！\n')
        mothlys = input('请输入要查询的月份（比如1、2、3等）：')
        mothly_sales = Monthly_sales(mothlys)

print('——————————销售明细——————————')
mothlys =input('请输入要查询的月份（比如1、2、3等）：')
mothly_sales=Monthly_sales(mothlys)
