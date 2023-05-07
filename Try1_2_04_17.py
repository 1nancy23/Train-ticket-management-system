import math
import random
import tkinter
from copy import deepcopy
class Station():###按对应车站初始化
    def __init__(self,name,dict_information):
        self.name=name
        self.arrived=dict_information###经停该站的列车的车次:时间
    pass
class Person():
    def __init__(self,ALL,name,ID,phone_number,password,is_buy):
        self.System=ALL###系统
        self.name=name###名字
        self.id_number=ID###身份证
        self.number=phone_number
        self.password=password###登录密码
        self.is_buy=is_buy###是否买票
        self.buy_train={}###购买车次列车:[当前列车名,出发站，目的站，n站时间，座位位置，票价)
        self.HouBu=[]###保存购票信息,与Buy_Tickt函数同构
    def Make_Houbu(self,Person_Name,Train_Name,Station_begin,Station_end,list_time,list_site):
        def Get_True():
            self.Buy_Tickt(Person_Name,Train_Name,Station_begin,Station_end,list_time,list_site,1)
        Get_True()
        tkinter.messagebox.showinfo('候补', '候补成功！')
    ####实现候补
    def Buy_Tickt(self,Person_Name,Train_Name,Station_begin,Station_end,list_time,list_site,remain):
        if remain<=0:
            ###进行候补订票
            print('进行候补')
            # self.Make_Houbu(Person_Name,Train_Name,Station_begin,Station_end,list_time,list_site)
            self.HouBu.append([Person_Name,Train_Name,Station_begin,Station_end,list_time,list_site])
            return 0
        ###tuple_time=[begin_time,end_time]
        else:
            self.is_buy=True
            Train_now=self.System.Trains[Train_Name]
            Time_Begin=list_time[0]
            Time_End=list_time[1]
            self.buy_train[Person_Name+Train_Name]=[Train_now.name,Station_begin,Station_end,list_time,list_site,0]
            print(self.buy_train)
            try:
                Train_now.remian[str(list_time)]-=1
                Train_now.remian[str(list_time)][list_site[0]][list_site[1]]=1
                ###中途没有停靠站
            except:
                List_Last=[]
                Flag=False
                for k in Train_now.remian.keys():
                    temp=k[1:-1].replace("'","").replace(" ","")
                    temp=temp.split(",")
                    ###格式规范统一
                    # print(temp[0])
                    # print(Time_Begin)
                    if Time_Begin==temp[0]:Flag=True
                    if Time_End==temp[1]:
                        List_Last.append(k)
                        break
                    if Flag:
                        List_Last.append(k)

                # print(123,List_Last)
                ###有停靠站
                for x in List_Last:
                    # print()
                    Train_now.site[x][list_site[0]][list_site[1]]=1###占坐
                    Train_now.remian[x]-=1###位置减1
                    self.buy_train[Person_Name+Train_Name][5]+=Train_now.price[x]###加上该区间票价
                        # print(id(j))
                    # print(Train_now.site[x])
                ###list_time代表乘车时间段，list_site代表该位置以被坐下
                print(1)
    def Back_Tickt(self,Person_Name,Train_Name):
        self.is_buy=False
        Train_now=self.System.Trains[Train_Name]
        list_time,list_site=self.buy_train[Person_Name+Train_Name][3],self.buy_train[Person_Name+Train_Name][4]
        del self.buy_train[Person_Name+Train_Name]
        Time_Begin=list_time[0]
        Time_Begin_2=Time_Begin.replace(':','').replace('.','')
        Time_End=list_time[1]
        Time_End_2 = Time_End.replace(':', '').replace('.', '')
        try:
            Train_now.remian[str(list_time)]+=1
            Train_now.remian[str(list_time)][list_site[0]][list_site[1]]=0
            ###中途没有停靠站
        except:
            List_Last=[]
            Flag=False
            for k in Train_now.remian.keys():
                temp=k[1:-1].replace("'","").replace(" ","")
                temp=temp.split(",")
                ###格式规范统一
                # print(temp[0])
                # print(Time_Begin)
                if Time_Begin==temp[0]:Flag=True
                if Time_End==temp[1]:
                    List_Last.append(k)
                    break
                if Flag:
                    List_Last.append(k)

            # print(123,List_Last)
            ###有停靠站
            for x in List_Last:
                # print()
                Train_now.site[x][list_site[0]][list_site[1]]=0
                Train_now.remian[x]-=1
                    # print(id(j))
                # print(Train_now.site[x])
            ###list_time代表乘车时间段，list_site代表该位置以被坐下
        ###与Buy_Tickt反向操作

        ###下面查询候补订单
        HouBu_Information=[]
        HouBu=self.System.Persons
        print('Persons',HouBu)
        for name,Person1 in HouBu.items():
            print(Person1)
            HouBu_Information.append((Person1,Person1.HouBu))
        print(HouBu_Information)
        ###下面查询是拥有与退票匹配的路线,按车次和时间判断
        Ans=[]
        ###买票信息如图
        #[Person_Name, Train_Name, Station_begin, Station_end, list_time, list_site]
        for Person_HouBu in HouBu_Information:
            for HouBu_DingDan in Person_HouBu[1]:
                if Train_Name==HouBu_DingDan[1]:###车次相同
                    Time_Begin_Temp=(HouBu_DingDan[4][0].replace(':','').replace('.',''))
                    Time_End_Temp=(HouBu_DingDan[4][1].replace(':','').replace('.',''))
                    if int(Time_Begin_Temp)>=int(Time_Begin_2) and int(Time_End_Temp)<=int(Time_End_2):
                        Ans.append((int(Time_End_Temp)-int(Time_Begin_Temp),HouBu_DingDan))
                        Person_HouBu[0].HouBu.pop(Person_HouBu[0].HouBu.index(HouBu_DingDan))
        print("Ans",Ans)
        ###下面依照距离（等效于时间差从大到小排序）
        Ans.sort(key=lambda x:x[0])
        try:
            Information=Ans[0][1]
            self.Make_Houbu(Information[0],Information[1],Information[2],Information[3],Information[4],Information[5])
        except:pass
    def Return_tickts(self,Person_Name):
        ###返回找到的Day当天的车票信息构成的列表
        Results=[]###用来保存购买的当天车票的所有车票
        if self.buy_train:
            for k,v in self.buy_train.items():
                if Person_Name in k:###按出发时间算
                    Results.append(v)
            return Results
        return 0
    def Lamda_Sort_Day(self,List_Search):
        ###区间座位所有子区间最少数量作为区间座位数
        Time_Begin=List_Search[3][0]
        Time_End=List_Search[3][1]
        Train_Name=List_Search[0]
        Dict_Time=self.System.Trains[Train_Name].By_Time
        print(Dict_Time,Time_Begin,Time_End)
        List_Need_Time=[]
        Flag=False
        for i in Dict_Time.keys():
            if Flag:
                List_Need_Time.append(i)
            if Time_Begin==i:
                List_Need_Time.append(i)
                Flag=True
                pass
            if Time_End==i:
                break
        Ans=1000000
        print("Need_time",List_Need_Time)
        for i in range(len(List_Need_Time)-1):
            print(self.System.Trains[Train_Name].remian[str([List_Need_Time[i],List_Need_Time[i+1]])])
            Ans=min(Ans,self.System.Trains[Train_Name].remian[str([List_Need_Time[i],List_Need_Time[i+1]])])
        List_Search.append(Ans)
        return Ans
    def Search_by_DAY(self,Day,Station_Begin_Name,Station_End_Name):
        Station_Begin=self.System.Stations[Station_Begin_Name]
        Station_end=self.System.Stations[Station_End_Name]
        ###找到车站对象
        List_Train1=[]
        for k,v in Station_Begin.arrived.items():
            if Day in v:
                List_Train1.append(k)###按车次k,Day当天经过出发站的车次
        List_Trains=[]
        def Compute_Piaojia(Train_Name,Time_Begin,Time_End):
            Train_now=self.System.Trains[Train_Name]
            ans=0
            try:
                List_Last = []
                Flag = False
                for k in Train_now.remian.keys():
                    temp = k[1:-1].replace("'", "").replace(" ", "")
                    temp = temp.split(",")
                    ###格式规范统一
                    # print(temp[0])
                    # print(Time_Begin)
                    if Time_Begin == temp[0]: Flag = True
                    if Time_End == temp[1]:
                        List_Last.append(k)
                        break
                    if Flag:
                        List_Last.append(k)
                for x in List_Last:
                    ans += Train_now.price[x]
                ###中途有停靠站
            except:pass
            return ans
        for k in List_Train1:
            try:
                # if Day in Station_end.arrived[k]:
                    Time1,Time2=Station_Begin.arrived[k],Station_end.arrived[k]
                    if int(Time1.replace(':','').replace('.',''))<int(Time2.replace(':','').replace('.','')):
                        List_Trains.append([k,Station_Begin.name,Station_end.name
                    ,[Station_Begin.arrived[k],Station_end.arrived[k]],Compute_Piaojia(k,Station_Begin.arrived[k],Station_end.arrived[k])])###与购票函数参数同构,此时缺少位置信息
            except:pass
        print("246",List_Trains)
        ####下面查询中转站
        ###出发站:{到达站：{列车名：[出发时间，到达时间]}}
        Ans=[]
        Visited={}
        def Search_Mid_Dfs(next_station,list_way_mid,list_time,To_station):
            if next_station==To_station:
                print("找到对应路线",list_way_mid)
                Ans.append(deepcopy(list_way_mid))
                return
            if len(list_time)==0 or next_station==None:
                return
            try:
                if Visited[next_station] == True:
                    return
            except:pass

            print("查询出发站",next_station)
            A=[]
            try:
                A=self.System.Ways[next_station]
            except:
                print('没有此站')
            Visited[next_station]=True
            print(A)
            list_temp = []
            for Station_name,V_Station in A.items():
                for k,v in V_Station.items():
                    print("查询2",Station_name,v)
                    time_begin = int(v[0].replace(':', '').replace('.', ''))
                    time_end = int(v[1].replace(':', '').replace('.', ''))
                    if time_begin>=min(list_time):

                        list_way_mid.append([k,next_station,V_Station,v])
                        list_temp.append(time_end)###到达改的该站点所有路线的时间
                Search_Mid_Dfs(Station_name,list_way_mid,list_temp,To_station)
                for k, v in V_Station.items():
                    time_begin = int(v[0].replace(':', '').replace('.', ''))
                    time_end = int(v[1].replace(':', '').replace('.', ''))
                    if time_begin >= min(list_time):
                        list_way_mid.pop(list_way_mid.index([k,next_station,V_Station,v]))

        Search_Mid_Dfs(Station_Begin.name,[],[0],Station_End_Name)

        if len(List_Trains)!=0:
            List_Trains.sort(key=self.Lamda_Sort_Day,reverse=True)###按剩余票降序排
        print("123",Ans)
        return List_Trains###返回满足要求的车次及其对应的信息
        ###返回所有
        pass
    def Lamda_Sort_Station(self,List_Search):
        Time=List_Search[3][0][-5:].replace(":","")
        ans=0
        try:
            ans=float(Time)
        except:
            print(List_Search)
        return ans
    def Search_by_Station(self,Day,Station_name):
        ###返回值与购票函数同构
        Station1=self.System.Stations[Station_name]###找到该车站对象
        List_Trains=[]###找到满足对应条件的所有车次及其对应信息
        for k,v in Station1.arrived.items():
            if Day in v:
                List_Trains.append([k,Station_name,0,[v,0]])
        pass
        if len(List_Trains)!=0:
            List_Trains.sort(key=self.Lamda_Sort_Station,reverse=False)###按降序排列
        return List_Trains
    def Change_Tickt(self,Old_Information,New_Infromation):
        Information_Back=Old_Information
        Information_Need=New_Infromation
        self.Back_Tickt(Old_Information[0],Old_Information[1])
        self.Buy_Tickt(Information_Need[0],Information_Need[1],Information_Need[2],Information_Need[3],Information_Need[4])
class Train():###按车次初始化
    def __init__(self,name,site_x,site_y,dict_information):
        self.name = name  ###车次名
        self.remian = {}  ###剩余座位,list: site_x * site_y
        self.site = {}  ###此处应做出修改，因为list对象无法哈希,list: [[0] * site_x] * site_y
        self.price={}###list:price
        ###座位剩余,每行x个座位,list=[上一次达到时间，下一次到站时间]即两站之间的时间
        self.List_Time=[x for x in dict_information.keys()]
        self.List_Station=[x for x in dict_information.values()]
        self.By_Time = {}  ###到达时间：站台
        self.By_Station = {}  ###站台:达到时间
        ###得到时间段
        print("读取",self.List_Station)
        for i in range(len(self.List_Station)-1):
            self.remian[str([self.List_Time[i],self.List_Time[i+1]])]=self.List_Station[i][2]
            self.site[str([self.List_Time[i],self.List_Time[i+1]])]=[[0] * site_y  for _ in range(site_x)]
            self.price[str([self.List_Time[i],self.List_Time[i+1]])]=float(self.List_Station[i][1])
            self.By_Time[self.List_Time[i]]=self.List_Station[i][0]
            self.By_Station[self.List_Station[i][0]]=self.List_Time[i]
            # self.price[str([self.List_Time[i],self.List_Time[i+1]])]=
        self.By_Time[self.List_Time[-1]]=self.List_Station[-1][0]
        self.By_Station[self.List_Station[-1][0]]=self.List_Time[-1]
        # print("A",self.remian)
        # for i in range(len(dict_information)-1):
        #     pass
        self.Begin=str
        self.End=str

    def Is_Site_Empty(self,list_time,list_site):
        ###查看整列车有没有空位
        if self.remian==0:return 0
        ###查看对应位置有没有空位
    pass
from collections import defaultdict
class AllTrain():
    def __init__(self):
        self.Stations={}###所有站台
        self.Trains={}###列车名：列车对象
        self.Persons={}###人名：人对象
        self.Ways=defaultdict(dict)###出发站:{到达站：{列车名：[出发时间，到达时间]}}
    def Add_Train(self,Train1):
        self.Trains[Train1.name]=Train1
        list_Time,list_station=[k for k in Train1.By_Time.keys()],[v for v in Train1.By_Time.values()]
        print("list_time",list_Time)
        print("list_station",list_station)
        for i in range(len(list_station)):
            for j in range(i+1,len(list_station)):
                try:
                    self.Ways[list_station[i]][list_station[j]][Train1.name]=[list_Time[i],list_Time[j]]
                except:
                    try:
                        self.Ways[list_station[i]][list_station[j]]={Train1.name:[list_Time[i],list_Time[j]]}
                    except:
                        self.Ways[list_station[i]]={list_station[j]:{Train1.name:[list_Time[i],list_Time[j]]}}
    def Delate_Train(self,Train1):
        del self.Trains[Train1.name]
    def Return_Train(self):
        List_All=[]
        for k,v in self.Trains.items():
            List_All.append([k,v.By_Time])
        return List_All
    def Fix_Train_timelist(self,Train2,dict_new):
        dict_origin=Train2.By_Time
        Train2.By_Time=dict_new###改为新的时间表dict_new
    def Fix_Train_Remain_site(self,name,list_time,list_site):
        self.Trains[name].remian[list_time]-=1
        self.Trains[name].remian[list_time][list_site[1]][list_site[0]]=1
        ###将name次列车list_time时间段,list_site时间段即为已被购买
        pass
    def Add_Station(self,Station1):
        self.Stations[Station1.name]=Station1
        pass
    def Delate_Station(self,Station1):
        del self.Stations[Station1.name]
        pass
    def Return_Station(self):
        List_All=[]
        for k,v in self.Stations.items():
            List_All.append([k,v.arrived])
            pass
    def Fix_Station(self,Station1,Station2):
        self.Stations[Station1.name]=Station2
        pass
    def Add_Person(self,Person1):
        try:
            if self.Persons[Person1.id_number]!=None:
                print("Be Saved")
                return 0
        except:pass
        self.Persons[Person1.id_number]=Person1
        pass
    def Delate_Person(self,Person1):
        del  self.Persons[Person1.id_number]
        pass
    def Return_Person(self):
        List_All=[]
        for k,v in self.Persons.items():
            List_All.append([k,v.name])
        return List_All

    def Fix_Person(self, Person1):
        self.Persons[Person1.id_number] = Person1
        pass


    # def Person_Buy(self,Person1,):
    #     ###提取买票火车对象
    #     pass
from Read_data import Read_Train_Test,Read_Station

def Init():
    System=AllTrain()
    Dict_Train=Read_Train_Test('.\按车次记录.txt')###初始化火车
    for k,v in Dict_Train.items():
        temp=Dict_Train
        Train1=Train(k,300,5,v)
        Train1.Begin=k
        System.Add_Train(Train1)
        Train_test=System.Trains[k]
    Dict_Station=Read_Station(".\按车站.txt")
    for k,v in Dict_Station.items():
        Station1=Station(k,v)
        System.Add_Station(Station1)
    Person1 = Person(System,"nancy","12","15984612072","1", False)
    # Person2 = Person(System, "tom", "510724", "123456", False)
    System.Add_Person(Person1)
    # System.Add_Person(Person2)
    return System
System=Init()
def Test_Person():
    ###按区间买票退票已经实现
    Person1 = Person(System, "nancy", 510725, 123456789, False)
    Person2 = Person(System, "tom", 510724, 123456, False)
    A=Person1.Search_by_DAY("2022.12.6","宜昌东","达州")
    B=Person2.Search_by_Station("2022.12.6","杭州")
    # print(B)
    Train_Time=System.Trains["K1154"].By_Station

    # print()
    Person2.Buy_Tickt("K1154","重庆西","芜湖",list_time=[B[3][3][0],Train_Time["芜湖"]],list_site=[3,0])

    # Person2.Buy_Tickt(B[3][0], B[3][1], B[3][2], B[3][3], [3, 0])
    # print("买票后",Person2.Return_tickts("2022.12.6"))
    # print(Person2.Price)
    Person2.Back_Tickt("K1154")
    # print("退票后",Person2.Return_tickts("2022.12.6"))
    # print(B)
    Max_Ticks=A[0]
    Person1.Buy_Tickt(Max_Ticks[0],Max_Ticks[1],Max_Ticks[2],Max_Ticks[3],[1,3])
    # print(A)
# Test_Person()
# print(1)