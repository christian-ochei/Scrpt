class CollectionExp:
    def __init__(self, arr):
        self.arr = arr


        if len(arr) == 1:
            self.arr = self.arr[0]
            self.solve = lambda:self.arr.solve()
        else:
            # print(self.arr)
            # print('.....')
            self.solve = lambda: [exp.solve() for exp in self.arr]


class ListCollectionExp(CollectionExp):
    pass



class ArgLiteral:

    def __init__(self,args):
        pass

class Void:

    def __init__(self):
        pass


class CodeLiteral:
    def __init__(s,code,compiler):
        code = code[:len(code)-1] # Remove Braces at the end


        s.type = 'CodeLiteral'
        # print(code,'c0--')
        # print(compiler)
        pass

    def run(self):
        pass