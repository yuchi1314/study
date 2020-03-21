from collections import defaultdict 

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Graph:
    # Constructor 
    def __init__(self): 
        #建立附近的節點關係圖
        self.graph = defaultdict(list) 
        #
        self.val = None
        self.next = None
        self.head = None
        
    # 建立關係圖，u為節點，v為u附近的節點
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def insertNode(self,val):
        new = ListNode(val)
        new.val = val
        new.next = None

        if self.head == None:
            self.head = new
            return
        else:
            now = self.head
            while now != None:
                stop = now
                now = now.next
            if stop.next == None:
                stop.next = new
            return
        return

    def searchNode(self,val):
        if self.head == None:
            return False
        else:
            now = self.head
            while now != None:
                if now.val == val:
                    return True
                else:
                    now = now.next
            return False
        return

    def DFS(self, s):
        order = [] #存放走訪順序
        if order == [] and self.head == None:
            order.append(s)
            if self.graph[s] != None:
                for g in self.graph[s]:
                    self.insertNode(g)
        #如果有暫存點
        while self.head != None:
            #暫存不只一個
            if self.head.next != None:
                now = self.head
                while now.next != None:
                    stop = now
                    now = now.next
                if stop != None:
                    temp = now.val
                    stop.next = None
            #暫存只一個
            else:
                temp = self.head.val
                self.head = None
            order.append(temp)
            for g in self.graph[temp]:
                o = 0 #order裡的順序
                while o < len(order):
                    tempo = o
                    if g != order[o]:
                        o = o+1
                    else:
                        break
                if g != order[tempo]:
                    if self.searchNode(g) == False:
                        self.insertNode(g)
        return order

      
"""
執行區


g = Graph()

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)

print(g.DFS(0))

## 參考資料   
https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html#code
https://docs.python.org/3.5/library/collections.html#collections.defaultdict
https://codertw.com/程式語言/365414/
http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
http://alrightchiu.github.io/SecondRound/graph-li-yong-dfshe-bfsxun-zhao-connected-component.html
"""