class FalseException_:
    pass

class Print:
    def __init__(self,Exp):
        self.exp = Exp
        self.type = 'print_st'
        pass

    def run(self):
        x = self.exp.evaluate()
        if isinstance(x,list):
             for v in x:
                 if type(v) == str and v[0] == '\'':

                     v = v[1:len(v)-1]

                 print(str(v)+' ',end='')
             print('\n')
        else:print(x)