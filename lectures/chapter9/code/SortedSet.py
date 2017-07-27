class SortedSet(list):
           
    def __init__(self, initial=None):
        list.__init__(self) 

        if initial: 
            self.extend(initial)
    
    def insert(self, value):
        if value not in self:
            list.append(self, value)
            list.sort(self)
            
    def append(self, value):
        self.insert(value)
        
    def extend(self, other):
        for element in other:
            self.insert(element)

    def __add__(self, other):
        result = SortedSet(self)
        result.extend(other)
        
        return result
        
    def sort(self):
        pass
        
    def reverse(self):
        raise RuntimeError('SortedSet cannot be reversed')

    def __setitem__(self, index, object):
        raise RuntimeError('This syntax not supported by SortedSet')
