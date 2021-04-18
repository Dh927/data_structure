# -*- coding: utf-8 -*-
#create by Hao Ding 2021/4/17
#vresion python 3.7
#用于实现顺序表的相关操作
#部分思路灵感借鉴于张光河先生的《数据结构————python语言描述》


class SequenceList(object):
    
    #初始化空的顺序表
    def __init__(self,max_size=20):
        """
        maxsize表示顺序表最大容量，默认20
        Seqlist存储顺序表数据
        num表示顺序表当前个数
        """
        self.Seqlist=[]
        self.num=0
        self.maxsize=max_size
        
    #创建顺序表
    def CreateSequenceList(self):
        """
        (1调用input()方法接受用户的输入
        (2若用户的输入部位'#'，则调用append()方法将其添加指线性表中并转(3)
        (3)重复(1)
        (4)若输入为'#'，则结束当前输入并完成线性表的创建
        若超过最大容量，则结束，且提示
        """
        self.Seqlist=[]
        self.num=0
        print('***************')
        print('*请输入数据后按回车键确认，若想要结束请输入"#"*')
        print('***************')
        Element=input('请输入元素:')
        while Element!='#' and self.num<self.maxsize:
            self.num+=1
            self.Seqlist.append(Element)
            Element=input("请输入元素")
        else :
            if Element=='#':
                print('*输入完毕*')
            else :
                print('超过最大容量')
        
    #销毁顺序表
    def DestorySequenceList(self):
        """
        将顺序表初始化
        """
        self.__init__()
    
    #判断顺序表是否为空
    def IsEmpty(self):
        if self.num == 0:
            return True
        else:
            return False
    
    #获取表中指定位置的元素值
    def GetElement(self,index):
        if not isinstance(index,int):
            raise TypeError
        if index<=self.num and index>0:
            element=self.Seqlist[index-1]
        else:
            return '超出顺序表范围'
        return element
    
    #在表中查找某一指定元素
    def FindElement(self,ele_value):
        for i in range(self.num):
            if self.Seqlist[i] == ele_value:
                return i+1
        else:
            return -1
    
    #快速查找，基于上一函数改造
    def FindElement1(self,ele_value):
        if ele_value in self.Seqlist:
            return self.Seqlist.index(ele_value)+1
        else:
            return -1
    
    #获取表中的最大值,常规
    def maxElement(self):
        max_value=self.Seqlist[0]
        for i in self.Seqlist:
            if i>max_value:
                max_value=i
        return max_value
    
    #改进1
    def maxElement1(self):
        return max(self.Seqlist)
    
    #获取表中的最小值,常规
    def minElement(self):
        min_value=self.Seqlist[0]
        for i in self.Seqlist:
            if i<min_value:
                min_value=i
        return min_value
    
    #改进1
    def minElement1(self):
        return min(self.Seqlist)
    
    #在指定位置插入元素
    def InsertElement(self,index,value):
        if not isinstance(index,int):
            raise TypeError
        if self.num+1>self.maxsize:
            raise TypeError
        if index<1 or index >self.num+1:
            raise TypeError
        self.Seqlist.append(value)
        for j in range(self.num,index-1,-1):
            self.Seqlist[j]=self.Seqlist[j-1]
        self.Seqlist[index-1]=value
        self.num+=1
    
    #在表末尾插入元素
    def Appendlement(self,value):
        if self.num+1>self.maxsize:
            raise TypeError
        self.Seqlist.append(value)
    
    #修改线性表种某一位置的元素
    def Setitem(self,index,value):
        if not isinstance(index,int):
            raise TypeError
        if index<1 or index>self.num:
            raise IndexError
        self.date[index-1] = value
        
    #删除表中某一位置元素
    def DeleteElement(self,index):
        if not isinstance(index,int):
            raise TypeError
        if index<1 or index>self.num:
            raise IndexError
        for i in range(index-1,self.num-1):
            self.Seqlist[i]=self.Seqlist[i+1]
        self.num-=1
    
    #快速操作，随上一函数改进
    def DeleteElement1(self,index):
        if not isinstance(index,int):
            raise TypeError
        if index<1 or index>self.num:
            raise IndexError
        self.Seqlist.pop(index)
        self.num-=1

a=SequenceList(max_size=5)
a.Seqlist
a.num
a.CreateSequenceList()
a.IsEmpty()
a.GetElement(1)
a.FindElement('1')
a.FindElement1(1)
a.maxElement()
a.minElement()
a.InsertElement(5,5)
a.AppendElement(5)
a.Setitem(1,2)
a.DeleteElement(2)
a.DeleteElement1(2)
a.DestorySequenceList()
