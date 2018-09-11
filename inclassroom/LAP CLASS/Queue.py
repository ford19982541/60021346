from collections import deque
queue = deque([])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()

'''

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0,val)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0
    def print_q(self):
        
        for i in len(self.queue):
            return(self.queue[i])
        
q = Queue()
q.enqueue("Graham")
q.enqueue("Terry")

'''