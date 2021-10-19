# from GrammerUtils import turpleMem

class Assign:
    def __init__(s,var,expression,memory):
        # memory = turpleMem(memory)
        s.memory = memory
        s.var = [v for v in var]
        s.expression = expression

        if var == '':
            s.type = 'nullExp'
            s.run = lambda:expression.evaluate()

        elif not (var == 'return' or var == 'yield'):

            s.type = 'assign'


            if len(var) == 1:
                s.v = s.var[0]
                s.run = lambda: None#'#memory[1].overwrite(s.v, s.expression.evaluate())
            elif expression.type == 'star':

                s.vars = s.var[::2] # You're supposed to split with ` not that

                s.range_ = range(len(s.vars))
                s.run = lambda: s.multiVarAssign(memory,s.expression.evaluate(),s.range_)
            else:

                s.vars = s.var[::2]  # You're supposed to split with ` not that
                s.run = lambda: s.multiAssign(memory, s.expression.evaluate())


        else:
            s.type = 'return'
            s.run = lambda:expression.evaluate()

    def multiAssign(s,memory,result):
        for v in s.vars:
            memory.overwrite(v,result)
    def multiVarAssign(s,memory,result,range_):
        for x in range_:
            memory.overwrite(s.vars[x],result[x])

