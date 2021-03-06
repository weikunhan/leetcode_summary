"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        self.dummy_head = Node(-1)
        self.temp_res = self.dummy_head
        
        if not root:
            
            return self.dummy_head.right
        
        self.inorder(root)
        #self.temp_res.right = self.dummy_head.right
        #self.dummy_head.right.left = self.temp_res
        self.temp_res.right, self.dummy_head.right.left = self.dummy_head.right, self.temp_res

        return self.dummy_head.right
    
    def inorder(self, root):
        if not root:
            
            return 
        
        self.inorder(root.left)
        temp = self.temp_res
        self.temp_res.right = root
        self.temp_res = root
        root.left = temp
        #temp = root
        #root.left = self.temp_res
        #self.temp_res.right = temp
        #self.temp_res = temp
        self.inorder(root.right)