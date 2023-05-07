import os
import random


def Read_Train_Test(path_file):
    file1=open(path_file,encoding='utf-8')
    Dict_All={}
    for i in file1.readlines():
        List_1=list(map(str,i[:-1].split(" ")))
        print(List_1)
        Dict_Station={}
        j=3
        while j<len(List_1)-2:
            Remain_Tickt=1
            Dict_Station["2022.12.6."+List_1[j]]=[List_1[j+1],List_1[j+2],Remain_Tickt]
            j+=3
        Dict_Station['2022.12.6.'+List_1[-2]]=[List_1[-1],0,1]
        Dict_All[List_1[0]]=Dict_Station
    print(Dict_All)
    return Dict_All
    pass
def Read_Station(path_file1):
    file1=open(path_file1,encoding='utf-8')
    Dict_All={}
    for i in file1.readlines():
        List_1=list(map(str,i[:-1].split(" ")))
        # print(List_1)
        Dict_Time={}
        j=1
        while j<len(List_1)-1:
            Dict_Time[List_1[j+1]]="2022.12.6."+List_1[j]
            j+=2
        Dict_All[List_1[0]]=Dict_Time
    return Dict_All
def Read_Person_Test(path_file):
    pass

