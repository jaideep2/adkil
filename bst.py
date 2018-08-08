import pytest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class bst:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data, currentNode=None):
        #If current node is None return head (base condition)
        if not currentNode:
            currentNode=self.root
        #If data is less than current node value then go left
        if data < currentNode.data: #<=?
            if currentNode.left:
                self.insert(data,currentNode.left)
            else:
                currentNode.left = Node(data)
        #Else go right
        else:
            if currentNode.right:
                self.insert(data,currentNode.right)
            else:
                currentNode.right = Node(data)

    def search(self, data, current=None, parent=None):
        #Same as insert instead of printing return data
        if not parent:
            current = self.root
        if data<current.data:
            #Go left
            if current.left:
                return self.search(data,current.left,current)
            else:
                return None, None
        elif data>current.data:
            #Go right
            if current.right:
                return self.search(data,current.right,current)
            else:
                return None, None
        else:
            return current,parent



    def delete(self, data):
        #lookup first
        node, parent = self.search(data)
        if node:
            #Count children
            numChildren = 0
            if node.left: numChildren+=1
            if node.right:numChildren+=1
            #Case 1: 0 children
            if numChildren==0:
                pass
            #Case 2: 1 children
            if numChildren==1:
                pass
            #Case 3: 2 children
            else:
                pass
        else:
            print('cannot find node with data ',data)

    def findMin(self, root):
        pass

    def findMax(self, root):
        pass

    def findHeight(self, node):
        if node is None:
            return -1
        return max(self.findHeight(node.left),self.findHeight(node.right))+1

    def printLevelOrder(self):
        #Find height/Max Depth
        h = self.findHeight(self.root)
        #Iterate through all levels
        for level in range(h+1):
            self.printCurrentLevel(self.root,level)

    def printCurrentLevel(self, node, level):
        if node is None:
            return
        if level==0:
            print(node.data)
        elif level>0:
            self.printCurrentLevel(node.left,level-1)
            self.printCurrentLevel(node.right,level-1)

    def bfs(self):
        #TODO ask arjun aboot this
        out = []
        if not self.root:
            return out
        else:
            current_level = [self.root]
            while current_level:
                out.append([n.data for n in current_level])
                next_level = list()
                for current in current_level:
                    if current.left:
                        next_level.append(current.left)
                    if current.right:
                        next_level.append(current.right)
                    print('>>',' '.join(str(n) for n in current_level),'|',' '.join(str(n) for n in next_level))
                    current_level = next_level
            return out

    def isLeaf(self, node):
        if node:
            if not node.left and not node.right:
                return True
        return False

    def printLeaves(self, node=None):
        if node is None: node = self.root
        if node.left: self.printLeaves(node.left)
        if node.right:self.printLeaves(node.right)
        if self.isLeaf(node):
            print(node.data)

    def dfs(self, node=None): #postorder
        if node is None: node = self.root
        if node.left: self.dfs(node.left)
        if node.right:self.dfs(node.right)
        print(node.data)

    def isBST(self):
        pass

    def getSuccessor(self, node):
        pass


def test():
    b = bst(5)
    b.insert(2)
    b.insert(7)
    b.insert(1)
    b.insert(3)
    b.insert(6)
    b.insert(8)
    b.printLeaves()
    #b.printLevelOrder()

if __name__ == '__main__':
    test()