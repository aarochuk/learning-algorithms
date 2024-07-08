class Tree:
    def __init__(self, val):
        self.val = val
        self.r = None
        self.l = None
    
    def print(self):
        print(self.val)

def bfs(node: Tree):
    
