# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:45:47 2020

@author: 16321
"""
import random as rd
import math
if __name__ == "__main__":
    node_num,server_num,mec_num  = 25,20,5
    nodes = [None]*node_num
    # tranp用于计算节点关联链路的发射功率和接受功率之和
    tranp = [0]*node_num
    index = 0
    #记录服务器节点的序号对应的坐标，假设节点的排列为3*5
    xc,yc = [0]*15,[0]*15
    for i in range(30):
        xc[i],yc[i] = i%5,i/5
    #分别表示节点间的最小距离和最大距离
    mind,maxd = 1,6.403
    #开始生成节点信息
    #节点信息的顺序为节点的类型,计算资源,处理效率
    #生成边缘服务器
    for i in range(mec_num):
        nodetype = 0
        cpu = rd.choice([8,12,16])
        prot = rd.randrange(10,15)
        # prop = rd.randrange(4,9)*10
        # recp = 20
        # idlep = prop*rd.uniform(0.3,0.5)
        # opene,offe = 400,200
        # nodes[index] = [nodetype,cpu,prot,prop,recp,idlep,opene,offe]
        nodes[index] = [nodetype,cpu,prot]
        index += 1
        #fnet.write(str(nodetype)+" "+str(cpu)+" "+str(prot)+" "+str(prop)+" "+str(recp)+" "+str(idlep)+" "+str(opene)+" "+str(offe)+"\n")
        #print(cpu) 
    #生成云服务器
    for i in range(mec_num,server_num):
        nodetype = 1
        cpu = rd.choice([8,12,16])
        prot = rd.randrange(4,9)
        # prop = rd.randrange(8,13)*10
        # recp = 30
        # idlep = prop*rd.uniform(0.3,0.5)
        # opene,offe = 600,300
        # nodes[index] = [nodetype,cpu,prot,prop,recp,idlep,opene,offe]
        nodes[index] = [nodetype,cpu,prot]
        #fnet.write(str(nodetype)+" "+str(cpu)+" "+str(prot)+" "+str(prop)+" "+str(recp)+" "+str(idlep)+" "+str(opene)+" "+str(offe)+"\n")
        index += 1
    #生成交换机
    for i in range(server_num,node_num):
        nodetype = 2
        cpu = prot = 0
        # recp = 20
        # idlep = 0
        # opene,offe = 400,200
        # nodes[index] = [nodetype,cpu,prot,prop,recp,idlep,opene,offe]
        nodes[index] = [nodetype,cpu,prot]
        #fnet.write(str(nodetype)+" "+str(cpu)+" "+str(prot)+" "+str(prop)+" "+str(recp)+" "+str(idlep)+" "+str(opene)+" "+str(offe)+"\n")
        index += 1
    #开始构造节点之间的连接信息：
    havelink = [None] * node_num
    for i in range(node_num):
        havelink[i] = [False]*node_num
    #边信息的顺序为边的起点，边的终点，边的带宽资源，边的传播时延，边起点到边终点的发送能耗
    linkad = [None] * node_num
    link_num = 0
    for i in range(node_num):
        #采用字典存储边的消息
        linkad[i] = {}
    #生成边缘服务器的链接信息,边缘服务器只能与边缘服务器和交换机相连，不能与云服务器直接连接
    for i in range(mec_num):
        #工业物联网结构下，边缘服务器只与交换机相连
        #生成边缘服务器之间的边
        # for j in range(i,mec_num):
        #     if(i == j or havelink[j][i]):
        #         continue
        #     #以0.3的概率生成服务器之间的边
        #     if(rd.random() < 0.3):
        #         havelink[i][j] = havelink[j][i] = True
        #         linkad[i][j],linkad[j][i] = [0,0,0],[0,0,0]
        #         linkij,linkji = linkad[i][j],linkad[j][i]
        #         #随机生成链路的带宽、时延和发送功耗
        #         linkij[0] = linkji[0] = rd.randrange(50,76)*100
        #         #服务器节点间的时延与节点间的距离成正比
        #         #最小2，最大6
        #         linkij[1] = linkji[1] = (2 + (math.sqrt((xc[j]-xc[i])**2+(yc[j]-yc[i])**2) - mind) * 4 / (maxd-mind)) * rd.uniform(0.9,1.1)
        #         #发送能耗与节点间的距离成正比
        #         linkij[2] = linkji[2] = linkij[1] * rd.uniform(0.9,1.1) * 5
        #         #更新链路的两个端点的传输功率和信息
        #         tranp[i] += linkij[2]+nodes[i][4]
        #         tranp[j] += linkji[2]+nodes[j][4]
        #         link_num += 2
        #生成边缘服务器和交换机之间的边
        for j in range(server_num,int(0.5*server_num+0.5*node_num)):
            # if(i == j or havelink[j][i]):
            #     continue
            #以0.5的概率生成边
            if(rd.random() < 0.5):
                havelink[i][j] = True
                linkad[i][j] = [0,0]
                linkij = linkad[i][j]
                #带宽
                linkij[0] = rd.randrange(50,71)*100
                #传输时延，最小4，最大8
                linkij[1] = rd.randrange(4,9)
                #linkij[2] = linkij[1] * rd.uniform(0.9,1.1) * 5
                link_num += 1
    #生成云服务器的链接信息,云服务器只能与云服务器和交换机相连，不能与边缘服务器直接连接
    for i in range(mec_num,server_num):
        #生成云服务器之间的边
        for j in range(i,server_num):
            if(i == j or havelink[j][i]):
                continue
            #以0.35的概率生成云服务器之间的边
            if(rd.random() < 0.3):
                havelink[i][j] = havelink[j][i] = True
                linkad[i][j],linkad[j][i] = [0,0],[0,0]
                linkij,linkji = linkad[i][j],linkad[j][i]
                #带宽
                linkij[0] = linkji[0] = rd.randrange(80,101)*100
                #服务器节点间的传播时延与节点间的距离成正比
                #最小12，最大18
                linkij[1] = linkji[1] = (10 + (math.sqrt((xc[j-mec_num]-xc[i-mec_num])**2+(yc[j-mec_num]-yc[i-mec_num])**2) - mind) * 5 / (maxd-mind)) * rd.uniform(0.9,1.1)
                #linkij[2]=linkji[2] = linkij[1] * rd.uniform(0.9,1.1) * 5
                link_num += 2
        if(i < mec_num+10):
            #生成云服务器和交换机之间的边
            for j in range(int(0.5*server_num+0.5*node_num),node_num):
                if(i == j or havelink[j][i]):
                    continue
                #以0.35的概率生成边
                if(rd.random() < 0.5):
#                    print("生成云和交换机之间的边")
                    havelink[j][i] = True
                    linkad[j][i] = [0,0]
                    linkji = linkad[j][i]
                    #带宽
                    linkji[0] = rd.randrange(80,101)*100
                    #传播时延，最小10，最大15
                    linkji[1] = rd.randrange(10,16)
                    #linkji[2] = linkij[0] * rd.uniform(0.9,1.1) / 8
                    link_num += 1
    #生成交换机的链接信息,交换机与其他节点都可以相连
    for i in range(server_num,node_num):
        #生成交换机之间的边
        for j in range(i,node_num):
            if(i == j or havelink[j][i]):
                continue
            #以0.35的概率生成交换机之间的边
            if(rd.random() < 0.3):
                havelink[i][j] = havelink[j][i] = True
                linkad[i][j],linkad[j][i] = [0,0],[0,0]
                linkij,linkji = linkad[i][j],linkad[j][i]
                #带宽
                linkij[0] = linkji[0] = rd.randrange(110,131)*100
                #传播时延，最小18，最大36
                linkij[1] = linkji[1] = rd.randrange(18,31)
                #linkij[2] = linkji[2] = linkij[1] * rd.uniform(0.9,1.1) * 2
                #更新链路的两个端点的传输功率和信息
                link_num += 2
    fnet = open("network2.txt",'w')
    #写入节点的信息
    fnet.write(str(node_num)+" "+str(server_num)+" "+str(mec_num)+"\n")
    for i in range(node_num):
        nodeinfo = nodes[i]
        fnet.write(str(nodeinfo[0])+" "+str(nodeinfo[1])+" "+str(nodeinfo[2])+"\n")
    
    #写入边的信息
    fnet.write(str(link_num)+"\n")
    for i in range(node_num):
        for j in linkad[i]:
            linkinfo = linkad[i][j]
            fnet.write(str(i)+" "+str(j)+" "+str(linkinfo[0])+" "+str(linkinfo[1])+"\n")
    fnet.close()