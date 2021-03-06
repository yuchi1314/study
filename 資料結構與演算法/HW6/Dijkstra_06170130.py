from collections import defaultdict 
"""
import numpy as np
import pandas as pd
"""

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]  
        #是否已經走訪過 
        self.visit = [False] * vertices 
        #最短路徑
        self.SP = []
        """
        self.parent = [-1] * vertices
        self.MST = {}
        self.data = 0
        self.u = []
        self.v = []
        self.w = []
        """


    def adddict(self,a):
        index = []
        for i in range(self.V):
            index.append(str(i))
        data = dict(zip(index,a))
        return data
        
    #SP
    #s為起始點
    def Dijkstra(self, s):
        #從第一個點開始
        n = 0
        #一個很大的正數
        maxnum = (self.V*100)**(self.V*100)
        #暫時存放最短路徑
        minpoint = []
        #若是第一個點
        if self.SP == []:
            #目前的最佳路徑
            self.SP = self.graph[s]
            #表示已經走過
            self.visit[s] = True    
            #在尋找下一個最佳路徑時
            while n < len(self.SP):
                #某點已有走最短路徑
                if self.visit[n] == True:
                    minpoint.append(maxnum)
                    n = n+1
                #某點尚未有走最短路徑
                elif self.visit[n] == False:
                    #有到某得點
                    if self.SP[n] != 0:
                        minpoint.append(self.SP[n])
                        n = n+1
                    #沒有到某得點
                    else:
                        minpoint.append(maxnum)                            
                        n = n+1
            #找出最短路徑的點
            n = minpoint.index(min(minpoint))
            return self.Dijkstra(n)
        #非起始點
        else:
            #表示已經走過
            if self.visit[s] == False:
                self.visit[s] = True
                #在尋找下一個最佳路徑時
                while n < len(self.SP):
                    #若已經還沒走訪過
                    if self.visit[n] != True:
                        #目前距離
                        now = self.SP[s] + self.graph[s][n]
                        #如果可以到某個點
                        if self.graph[s][n] != 0:
                            #若SP中沒有此路徑
                            if self.SP[n] == 0:
                                self.SP[n] = now
                                minpoint.append(self.SP[n])
                                n = n+1
                            #若原本有路徑，但是now較小
                            elif self.SP[n] != 0 and now < self.SP[n]:
                                self.SP[n] = now
                                minpoint.append(self.SP[n])
                                n = n+1
                            #若原本有路徑，但是now較大
                            else:
                                minpoint.append(self.SP[n])
                                n = n+1
                        #若已經走訪過
                        else:
                            #無法到某個點
                            if self.SP[n] == 0:
                                minpoint.append(maxnum)
                                n = n+1
                            #目前路徑    
                            else:
                                minpoint.append(self.SP[n])
                                n = n+1
                    #已經走訪過
                    else:
                        minpoint.append(maxnum)
                        n = n+1
                n = minpoint.index(min(minpoint))
                return self.Dijkstra(n)
        return self.adddict(self.SP)
"""
    def weight(self,arr):
        return arr[2]

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
        if len(self.graph) >=2:
            self.graph = self.graph.sort(key = self.weight, reverse = True)
        return
        
    def k_adddict(self,u,v,w):
        path = []
        point = "%d-%d"%(u,v)
        path.append(point)
        self.MST[point] = w
        return

    #MST
    def Kruskal(self):
        #for i in range(0,len(self.graph)-1):

        return


       

執行程式碼

g = Graph(6)
g.graph = [[0,100,200,0,0,0],[100,0,50,200,100,0],[200,50,0,0,40,0],[0,200,0,0,150,100],[0,100,40,150,0,100],[0,0,0,100,100,0]]
print("Dijkstar",g.Dijkstra(0))


g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)

print("Kruskal",g.Kruskal())



參考資料
https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/     
https://pythonnote.wordpress.com/2014/04/03/python技巧漂亮又通順的程式碼/      
https://www.runoob.com/python/python-dictionary.html        
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/      
https://zh.wikipedia.org/wiki/戴克斯特拉算法     
http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html     
https://wiki.mbalib.com/zh-tw/Dijkstra算法      
https://zh.wikipedia.org/wiki/克鲁斯克尔演算法         
http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html     

"""