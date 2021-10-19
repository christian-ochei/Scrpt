

operators = ['==', '/=', '!=', '*=', '@=', '&&', '||', '<<', '>>', '-=', '^=', '&=', '|=', '%%', '>=', '<=', '>', '<', '+', '-',
             '*', '/', '//', '%', '**', '^','.']

symbols = '!@#$%^&*()_+{":><?"}|\\'
symbols = [x for x in symbols]
from MemoryManagement import Memory
# def turpleMem(memory):
#     if isinstance(memory,(tuple,list)):
#         memory = turpleMem(memory[0]).using(turpleMem(memory[1]))
#     return memory

def print(*args):
    pass


def rindex(alist, value):
    return len(alist) - alist[::-1].index(value) -1

def split(arr, key):
    print(arr,":::")
    out = []
    o = []

    if key in arr:
        for val in arr:
            o.append(val)

            if val == key:
                out.append(o[:len(o) - 1])
                o = []
        out.append(o[:len(o)])
        return out
    print(arr, "::::------++")
    return [arr]



def is_compound(code):
    # print(code,"--=++") # @Be careful
    return code[len(code)-3] == '{'


def is_setter(code):
    return '=' in code and not '(' in code[code.index('=')]


def index(txt):
    v = 1
    for x,line in enumerate(txt):
        if '}' in line:
            v -= 1
            if v==1:
                return x


        if '{' in line:
            v+=1

    return len(txt)-1


def defaulter(line,val):
    if len(line)>1 and line[2:][0] == '':

        append = val
    else:
        append = line[2:] if line[1] == '`' else line[1:]

    return append

def anActualVariableName(x):
    return x.isalnum and not (x in operators or x in symbols)
