# TP lettre qui saute 
# Arnaud Cojez et Matthieu Caron

class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self, val, succ):
        super(LinkedList, self).__init__()
        self.val = val
        self.succ = succ

    def add(self, succ) :
        if self.succ == None :
            self.succ = succ
        else :
            self.succ.add(succ)
    
