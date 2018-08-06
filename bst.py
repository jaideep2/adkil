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

    def findHeight(self, root):
        pass

    def bfs(self):
        #TODO ask arjun aboot this
        if not self.root:
            print('None')
        else:
            current_level = [self.root]
            while current_level:
                print(' '.join(str(n) for n in current_level))
                next_level = list()
                for current in current_level:
                    if current.left:
                        next_level.append(current.left)
                    if current.right:
                        next_level.append(current.right)
                    #print('>>',' '.join(str(n) for n in current_level),'|',' '.join(str(n) for n in next_level))
                    current_level = next_level

    def dfs(self, root):
        pass

    def isBST(self, root):
        pass

    def getSuccessor(self, root):
        pass


def test():
    b = bst(10)
    b.insert(5)
    b.insert(15)
    b.insert(2)
    b.insert(8)
    b.insert(11)
    b.insert(30)
    b.bfs()

if __name__ == '__main__':
    test()