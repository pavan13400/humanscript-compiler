import ply.lex as lex

tokens = (
    'CREATE','LIST','FROM','TO',
    'FILTER','EVEN','ODD','GREATER',
    'CALCULATE','SUM','AVERAGE',
    'PRINT','RESULT','NUMBER'
)

t_CREATE = r'Create'
t_LIST = r'list'
t_FROM = r'from'
t_TO = r'to'
t_FILTER = r'Filter'
t_EVEN = r'even'
t_ODD = r'odd'
t_GREATER = r'greater'
t_CALCULATE = r'Calculate'
t_SUM = r'sum'
t_AVERAGE = r'average'
t_PRINT = r'Print'
t_RESULT = r'result'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()