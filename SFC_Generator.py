# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:22:34 2020

@author: 16321
"""

import random as rd
#import math

if __name__ == "__main__":
    EdgeNum=10
    #先生成各个类型的VNF集合，每个VNF的属性包括：需求的计算资源，数据包大小的改变率，带宽需求（与前一个VNF之间的），时延需求（与前一个VNF之间的）
    #考虑两种类型的VNF，第一种是数据量大(初始数据包更大，带宽需求更高)的，第二种是时延敏感的，第三种是无需求的的
    RI_Nums,DS_Nums,NR_Nums=10,10,20
    for ep in range(50):
        RI_VNFs,DS_VNFs,NR_VNFs=[None]*RI_Nums,[None]*DS_Nums,[None]*NR_Nums
        #生成各个VNF的数据：
        for i in range(RI_Nums):
            RI_VNFs[i]=[]
            #先生成计算资源
            RI_VNFs[i].append(rd.choice([0.5,1,2,4]))
            #生成数据包大小改变率
            RI_VNFs[i].append(rd.choice([0.8,0.9,1,1.1,1.2]))
            #生成带宽需求
            RI_VNFs[i].append(rd.randrange(7,11)*100)
            #生成时延需求
            #RI_VNFs[i].append(180*rd.uniform(0.8,1.2))
        for i in range(DS_Nums):
            DS_VNFs[i]=[]
            #先生成计算资源
            DS_VNFs[i].append(rd.choice([0.5,1,2,4]))
            #生成数据包大小改变率
            DS_VNFs[i].append(rd.choice([0.8,0.9,1,1.1,1.2]))
            #生成带宽需求
            DS_VNFs[i].append(rd.randrange(2,6)*100)
            #生成时延需求
            #DS_VNFs[i].append(50*rd.uniform(0.8,1.2))
        for i in range(NR_Nums):
            NR_VNFs[i]=[]
            #先生成计算资源
            NR_VNFs[i].append(rd.choice([0.5,1,2,4]))
            #生成数据包大小改变率
            NR_VNFs[i].append(rd.choice([0.8,0.9,1,1.1,1.2]))
            #生成带宽需求
            NR_VNFs[i].append(rd.randrange(2,6)*100)
            #生成时延需求
            #NR_VNFs[i].append(180*rd.uniform(0.8,1.2))
        SFC_Num = 20
        fsfc = open("SFC-small/SFC"+str(ep)+".txt",'w')
        fsfc.write(str(SFC_Num)+"\n")
        for s in range(SFC_Num):
            #生成VNF个数
            rdn = rd.random()
            if(rdn < 0.15):
                VNF_Num = 2
            elif(rdn < 0.40):
                VNF_Num = 3
            elif(rdn < 0.65):
                VNF_Num = 4
            elif(rdn < 0.85):
                VNF_Num = 5
            else:
                VNF_Num = 6
            #随机生成服务链在网络中的起点
            Source = rd.randrange(0,EdgeNum)
            #生成服务链的类型
            #1/2的服务链为时延敏感的，1/2为数据量大的
            rdn = rd.random()
            if(VNF_Num < 4):
                if(rdn < 0.3):
                    ReqType=[0]*VNF_Num
                else:
                    ReqType=[1]*VNF_Num
            elif(VNF_Num > 4):
                if(rdn < 0.55):
                    ReqType=[0]*VNF_Num
                else:
                    ReqType=[1]*VNF_Num
            else:
                if(rdn < 0.7):
                    ReqType=[0]*VNF_Num
                else:
                    ReqType=[1]*VNF_Num
            # rdn,ll,hl = rd.random(),0.20,0.80
            # if(VNF_Num >= 4):
            #     ll,hl = 0.1,0.9
            # if(rdn < ll):
            #     ReqType1 = 1
            # elif(rdn > hl):
            #     ReqType1 = 2
            # else:
            #     ReqType1 = 0
            # #20%的服务链的全部VNF需要部署在边缘服务器上
            # if(ReqType1 == 1):
            #     ReqType = [1]*VNF_Num
            # #20%的服务链的全部VNF需要部署在云服务器上
            # elif(ReqType1 == 2):
            #     ReqType = [2]*VNF_Num
            # #对于剩余的服务链，20%的VNF需要部署在边缘服务器上，20%的VNF需要部署在边缘服务器上
            # else:
            #     #mnum,cnum分别代表需求类型为1和2的VNF的数目
            #     mnum,cnum=0,0
            #     if(VNF_Num == 2):
            #         if(rd.random() < 0.2):
            #             mnum = 1;
            #         if(rd.random() < 0.2):
            #             cnum = 1;
            #     elif(VNF_Num == 3):
            #         if(rd.random() < 0.6):
            #             mnum = 1;
            #         if(rd.random() < 0.6):
            #             cnum = 1;
            #     elif(VNF_Num == 4):
            #         rdm,rdc=rd.random(),rd.random();
            #         if(rdm < 0.4):
            #             mnum = 1
            #         elif(rdm < 0.6):
            #             mnum = 2
            #         if(rdc < 0.4):
            #             cnum = 1
            #         elif(rdc < 0.6):
            #             cnum = 2
            #     elif(VNF_Num == 5):
            #         rdm,rdc=rd.random(),rd.random();
            #         if(rdm < 0.4):
            #             mnum = 1
            #         elif(rdm < 0.7):
            #             mnum = 2
            #         if(rdc < 0.4):
            #             cnum = 1
            #         elif(rdc < 0.7):
            #             cnum = 2
            #     ReqType = [1]*mnum+[0]*(VNF_Num-mnum-cnum)+[2]*cnum
            
            #每个VNF需求的计算资源
            ReqCPU = [0]*VNF_Num
            #服务链的时延需求,时延敏感的服务要求更低的时延
            #
            if(ReqType[0] == 1): 
                ReqDelay = 100*VNF_Num
            else:
                ReqDelay = 200*VNF_Num
            #代表数据包大小，PackageSize[i]代表第i个VNF接收到的数据包大小，PackageSize[i+1]代表经过第i个VNF处理后的数据包大小
            #特别的，PackageSize[0]代表初始的数据包大小
            #数据量大的服务链请求初始数据包更大
            PackageSize = [0]*VNF_Num
            if(ReqType[0] == 0):
                PackageSize[0] = rd.randrange(5,8)
            else:
                PackageSize[0] = rd.randrange(2,5)
            #每条虚拟链路需求的带宽资源
            ReqBand = [0]*VNF_Num
            #生成服务链各个VNF的参数
            for i in range(VNF_Num):
                #根据VNF的类型设置参数
                if(ReqType[i] == 0):
                    #随机从对应的VNF集合中获取一个VNF，使用其的参数
                    index = rd.randrange(0,RI_Nums)
                    # ReqCPU[i],ReqBand[i],ReqDelay[i]=RI_VNFs[index][0],RI_VNFs[index][2],RI_VNFs[index][3]
                    ReqCPU[i],ReqBand[i]=RI_VNFs[index][0],RI_VNFs[index][2]
                    if(i < VNF_Num-1):
                        PackageSize[i+1] = PackageSize[i]*RI_VNFs[index][1]
                elif(ReqType[i] == 1):
                    #随机从对应的VNF集合中获取一个VNF，使用其的参数
                    index = rd.randrange(0,DS_Nums)
                    # ReqCPU[i],ReqBand[i],ReqDelay[i]=DS_VNFs[index][0],DS_VNFs[index][2],DS_VNFs[index][3]
                    ReqCPU[i],ReqBand[i]=DS_VNFs[index][0],DS_VNFs[index][2]
                    if(i < VNF_Num-1):
                        PackageSize[i+1] = PackageSize[i]*DS_VNFs[index][1]
                else:
                    #随机从对应的VNF集合中获取一个VNF，使用其的参数
                    index = rd.randrange(0,NR_Nums)
                    # ReqCPU[i],ReqBand[i],ReqDelay[i]=NR_VNFs[index][0],NR_VNFs[index][2],NR_VNFs[index][3]
                    ReqCPU[i],ReqBand[i]=NR_VNFs[index][0],NR_VNFs[index][2]
                    if(i < VNF_Num-1):
                        PackageSize[i+1] = PackageSize[i]*NR_VNFs[index][1]          
            #生命周期，以时隙数为单位；
            LifeTime = VNF_Num * 5 + rd.randrange(-3,4)
            print(LifeTime)
             
            #将生成的服务链写入文件
            fsfc.write(str(VNF_Num)+" "+str(Source)+" "+str(LifeTime)+" "+str(ReqDelay)+" ")
            for i in range(VNF_Num):
                fsfc.write(str(ReqType[i])+" ")
            # for i in range(VNF_Num):
            #     fsfc.write(str(ReqDelay[i])+" ")
            for i in range(VNF_Num):
                fsfc.write(str(ReqBand[i])+" ")
            for i in range(VNF_Num):
                fsfc.write(str(ReqCPU[i])+" ")
            for i in range(VNF_Num):
                fsfc.write(str(PackageSize[i])+" ")
            fsfc.write("\n")
        fsfc.close()
        print("生成完毕")