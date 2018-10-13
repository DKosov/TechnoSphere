
from collections import deque

class TreeNode:
    
    def __init__(self,value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None
    
    def __next__(self):
        if len(self.deq) == 0:
            raise StopIteration
        currentNode = self.deq.popleft()
        if currentNode.leftChild:
            self.deq.append(currentNode.leftChild)
        if currentNode.rightChild:
            self.deq.append(currentNode.rightChild)
        return currentNode.value
    
    def __iter__(self):
        self.deq = deque()
        self.deq.append(self)
        return self


class BinarySearchTree:
    
    def __init__(self, value=None):
        if value:
            self.node = TreeNode(value)
        else:
            self.node = None

def _search(self, value, currentNode):
    if currentNode:
        if value == currentNode.value:
            return True
            elif value < currentNode.value:
                return self._search(value, currentNode.leftChild)
        else:
            return self._search(value, currentNode.rightChild)
        else:
            return False

                
                def _put(self, value, currentNode):
                    if value < currentNode.value:
if currentNode.leftChild:
    self._put(value, currentNode.leftChild)
        else:
            currentNode.leftChild = TreeNode(value=value)
        else:
            if currentNode.rightChild:
                self._put(value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(value=value)

def append(self, value):
    if self.node:
        if value not in self:
            self._put(value, self.node)
        else:
            self.node = TreeNode(value)
                
                def __contains__(self, value):
                    if self._search(value, self.node):
                        return True
                            else:
                                return False
                                    
                                    def __next__(self):
                                        raise StopIteration()
                                            
                                            
                                            def __iter__(self):
                                                if self.node:
                                                    return self.node.__iter__()
                                                        else:
                                                            return self
