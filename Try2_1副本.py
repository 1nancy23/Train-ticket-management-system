import random


class Station():###按对应车站初始化
    def __init__(self,name,dict_information):
        self.name=name
        self.arrived=dict_information###经停该站的列车的车次:时间
    pass
class Person():
    def __init__(self,ALL,name,ID,password,is_buy):
        self.System=ALL###系统
        self.name=str()###名字
        self.id_number=str()###身份证
        self.password=str()###登录密码
        self.is_buy=bool()###是否买票
        self.buy_train={str:list}###购买车次列车:[当前列车对象,出发站，目的站，n站时间，（n+1）站时间])
    def Buy_Tickt(self,name,Station_begin,Station_end,list_time,list_site):
        ###tuple_time=[begin_time,end_time]
        self.is_buy=True
        Train_now=self.System.Trains[name]
        self.buy_train={name:[Train_now,Station_begin,Station_end,list_time[0],list_time[1]]}

        Train_now.remian[str(list_time)]-=1
        ###list_time

        Train_now.site[list_time][list_site[0]][list_site[1]]=1
        ###list_time代表乘车时间段，list_site代表该位置以被坐下
    def Back_Tickt(self,name):
        self.is_buy=False
        Train_now=self.buy_train[name][0]
        list_time,list_site=self.buy_train[name][3],self.buy_train[name][4]
        Train_now.remian[list_time]+=1

        Train_now.site[list_time][list_site[0]][list_site[1]]=0
        ###与Buy_Tickt反向操作
    def Return_tickts(self,Day):
        ###返回找到的Day当天的车票信息构成的列表
        Results=[]###用来保存购买的当天车票的所有车票
        if self.buy_train:
            for k,v in self.buy_train.items():
                if Day in v[3]:###按出发时间算
                    Results.append(v)
            return Results
        return 0
    def Lamda_Sort_Day(self,List_Search):
        return self.System.Trains[List_Search[0]].remian
    def Search_by_DAY(self,Day,Station_Begin_Name,Station_End_Name):
        Station_Begin=self.System.Stations[Station_Begin_Name]
        Station_end=self.System.Stations[Station_End_Name]
        ###找到车站对象
        List_Train1=[]
        for k,v in Station_Begin.arrived.items():
            if Day in v:
                List_Train1.append(k)###按车次k
        List_Trains=[]
        for k in List_Train1:###经过出发站的车次
            try:
                if Day in Station_end.arrived[k]:List_Trains.append([k,Station_Begin.name,Station_end.name
                ,[Station_Begin.arrived[k],Station_end.arrived[k]]])###与购票函数参数同构,此时缺少位置信息
            except:pass
        if len(List_Trains)!=0:
            List_Trains.sort(key=self.Lamda_Sort_Day,reverse=True)###按剩余票价降序排
        return List_Trains###返回满足要求的车次及其对应的信息
        ###返回所有
        pass
    def Lamda_Sort_Station(self,List_Search):
        return int(List_Search[3][0])
    def Search_by_Station(self,Day,Station_name):
        ###返回值与购票函数同构
        Station1=self.System.Stations[Station_name]###找到该车站对象
        List_Trains=[]###找到满足对应条件的所有车次及其对应信息
        for k,v in Station1.arrived.items():
            if Day in v:
                List_Trains.append([k,Station_name,0,[v,0]])
        pass
        if len(List_Trains)!=0:
            List_Trains.sort(key=self.Lamda_Sort_Station,reverse=True)###按降序排列
        return List_Trains
class Train():###按车次初始化
    def __init__(self,name,site_x,site_y,dict_information):
        self.name = name  ###车次名
        self.remian = {list: site_x * site_y}  ###剩余座位
        self.site = {list: [[0] * site_x] * site_y}  ###此处应做出修改，因为list对象无法哈希
        ###座位剩余,每行x个座位,list=[上一次达到时间，下一次到站时间]即两站之间的时间

        self.List_Time=[x for x in dict_information.keys()]
        self.List_Station=[x for x in dict_information.values()]
        ###得到时间段
        for i in range(len(self.List_Station)-1):
            self.remian[str([self.List_Time[i],self.List_Time[i+1]])]=site_x * site_y
            self.site[str([self.List_Time[i],self.List_Time[i+1]])]=[[0] * site_x] * site_y
        print("A",self.remian)


        for i in range(len(dict_information)-1):

            pass
        self.Begin=str
        self.End=str
        self.By_Time = dict_information  ###到达时间：站台
        self.By_Station = {Station: str}  ###站台:达到时间
    def Is_Site_Empty(self,list_time,list_site):
        ###查看整列车有没有空位
        if self.remian==0:return 0
        ###查看对应位置有没有空位
    pass
class AllTrain():
    def __init__(self):
        self.Stations={str:object}###所有站台
        self.Trains={str:object}###列车名：列车对象
        self.Persons={str:object}
    def Add_Train(self,Train1):
        self.Trains[Train1.name]=Train1
    def Delate_Train(self,Train1):
        del self.Trains[Train1.name]
    def Fix_Train_timelist(self,Train2):
        dict_origin=Train2.By_Time
        dict_new=None
        Train2.By_Time=dict_new###改为新的时间表dict_new
    def Fix_Train_Remain_site(self,name,list_time,list_site):
        self.Trains[name].remian[list_time]-=1
        self.Trains[name].remian[list_time][list_site[0]][list_site[1]]=1
        ###将name次列车list_time时间段,list_site时间段即为已被购买
        pass
    def Add_Station(self,Station1):
        self.Stations[Station1.name]=Station1
    def Add_Person(self,Person1):
        try:
            if self.Persons[Person1.id_number]!=None:
                print("Be Saved")
                return 0
        except:pass
        self.Persons[Person1.id_number]=Person
        pass
    def Delate_Person(self,Person1):
        del  self.Persons[Person1.id_number]
        pass
    def Fix_Person(self,Person1):
        pass
    def Add_Station(self,Station1):
        self.Stations[Station1.name]=Station1

    # def Person_Buy(self,Person1,):
    #     ###提取买票火车对象
    #     pass
from Read_data import Read_Train_Test,Read_Station

def Init():
    System=AllTrain()
    Dict_Train=Read_Train_Test('D:\课程\ipynb_try\按车次记录.txt')###初始化火车
    for k,v in Dict_Train.items():
        Train1=Train(k,random.randint(1,300),5,v)
        Train1.Begin=k
        System.Add_Train(Train1)
        Train_test=System.Trains[k]
    Dict_Station=Read_Station("D:\课程\ipynb_try\按车站.txt")
    for k,v in Dict_Station.items():
        Station1=Station(k,v)
        System.Add_Station(Station1)
    return System
System=Init()
def Test_Person():

    Person1=Person(System,"nancy",26347826,123456789,False)
    System.Add_Person(Person1)
    A=Person1.Search_by_DAY("2022.12.6","宜昌东","达州")
    Max_Ticks=A[0]
    Person1.Buy_Tickt(Max_Ticks[0],Max_Ticks[1],Max_Ticks[2],Max_Ticks[3],[31,2])
    print(A)
Test_Person()
print(1)