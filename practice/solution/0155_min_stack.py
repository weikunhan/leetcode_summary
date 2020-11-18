class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.value_stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        temp_value = self.getMin()
        
        if not self.value_stack or x < temp_value:
            temp_value = x
            
        self.value_stack.append((x, temp_value))

    def pop(self):
        """
        :rtype: None
        """
        
        self.value_stack.pop()
    
    def top(self):
        """
        :rtype: int
        """
        
        temp_value = None
        
        if self.value_stack:
            temp_value = self.value_stack[-1][0] 
            
        return temp_value

    def getMin(self):
        """
        :rtype: int
        """
        
        temp_value = None
        
        if self.value_stack:
            temp_value = self.value_stack[-1][1] 
            
        return temp_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()