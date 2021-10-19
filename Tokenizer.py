from GrammerUtils import operators
# def print(*a):
#     pass

def tokenize(line:str):
    code = []
    l = ''
    in_quotes = False
    line = line+' '
    ignoreNext = False
    for x in range(len(line)):
        c: str = line[x]
        c1: str = line[min(x+1, len(line) - 1)]
        c_1: str = line[max(x-1, 0)]

        # --------------------------

        if in_quotes:
            c = c.replace('\\', '').replace('`', ' ')
        l += c

        if c == '\'' and not c_1 == '\\':
            in_quotes = not in_quotes

        # This allows and or xor instead of &&, ||

        vn = var_token(l)
        ln = l+''
        if vn != l and code[len(code) - 1]=='`':
            del code[len(code) - 1]
        #
        # if var_token(parr) == parr:
        #     continue


        if not in_quotes:
            if not (''.join(c + c1) in operators):
                if is_var(c1) != is_var(c):
                    if not (ignoreNext and ln=='`'):
                        code.append(var_token(l))
                    ignoreNext = False
                    l = ''
                elif not is_var(c):
                    if not (ignoreNext and ln=='`'):
                        code.append(var_token(l))
                    ignoreNext = False
                    l = ''

        ignoreNext = False
        if vn != ln:
            ignoreNext = True
        # ignoreNext = False

    code.append(var_token(l))
    # print(code,'final-code===')
    return code

def is_var(c1:str):
    return c1.isalnum() or c1 == '_' or c1 == '@' or c1 == '\'' or c1 == '\"'

def var_token(v):
    # print('{',v,'}vvv--v-vv-v')
    # print(v == 'and')
    if v == 'or': return '||'
    if v == 'and': return '&&'
    if v == 'xor': return '^'
    if v == 'in': return '@='
    return v