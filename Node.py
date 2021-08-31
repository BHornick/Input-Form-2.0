'''
Created on Nov 19, 2018

@author: Brett
'''
class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        self.data.printOutput()
        if self.right:
            self.right.printTree()
            
    def writeToFile(self,file):
        if self.left:
            self.left.writeToFile(file)
        self.data.writeOutput(file)
        if self.right:
            self.right.writeToFile(file)
            