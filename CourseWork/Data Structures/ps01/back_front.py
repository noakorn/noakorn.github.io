##################################################
# Problem 1. BackFront
##################################################

# Create a datastructure to support O(1) random access,
# and O(1) amortized inserts/deletes to the front and back end of the record

class BackFront():
    def __init__(self):
        self.ls = [None]
        self.start = 0
        self.end = 0

    def __repr__(self):
        return str([i for i in self.ls if i is not None])

    def __setitem__(self, key, value):
        '''
        Stores value at the index of key
        '''
        self.ls[self.start + key] = value

    def __getitem__(self, key):
        '''
        Returns value at the index of key
        '''
        return self.ls[self.start + key]

    def as_list(self):
        '''
        Should return all the elements in the record in order
        '''
        return [i for i in self.ls if i is not None]

    def append(self, value):
        '''
        Should add on value to the record at the end
        '''
        if self.ls[self.end] is not None:
            self.end += 1
        end = self.end
        if end == len(self.ls)-1:
            self.ls += [None for i in range(end+1)]
        self.ls[end] = value

    def delete_last(self):
        '''
        Should remove the last element in the record
        '''
        self.ls[self.end] = None
        self.end = max(self.start,self.end-1)
        if self.start == self.end and self.ls[self.start] is None:
             self.start,self.end,self.ls = 0,0,[None]

    def prepend(self, value):
        '''
        Should add on value to the beginning of the record
        '''
        if self.start == 0:
            factor = self.end if self.end != 0 else 1
            self.start += factor - 1
            if self.ls[self.end] is not None:
                self.end += factor
            self.ls = [None for i in range(factor)] + self.ls
        else:
            self.start -= 1
        start = self.start
        self.ls[start] = value

    def delete_first(self):
        '''
        Should remove the first element in the record
        '''
        self.ls[self.start] = None
        self.start = min(self.start + 1,self.end)
        if self.start == self.end and self.ls[self.start] is None:
            self.start,self.end,self.ls = 0,0,[None]
