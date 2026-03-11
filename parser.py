import ply.yacc as yacc
from lexer import tokens

commands = []

def p_create_list(p):
    '''statement : CREATE LIST FROM NUMBER TO NUMBER'''
    commands.append(("create_list", p[4], p[6]))

def p_filter_even(p):
    '''statement : FILTER EVEN'''
    commands.append(("filter_even",))

def p_filter_odd(p):
    '''statement : FILTER ODD'''
    commands.append(("filter_odd",))

def p_calculate_sum(p):
    '''statement : CALCULATE SUM'''
    commands.append(("sum",))

def p_print_result(p):
    '''statement : PRINT RESULT'''
    commands.append(("print",))

# ---- NEW COMMANDS ----

def p_print_list(p):
    '''statement : PRINT LIST'''
    commands.append(("print_list",))

def p_calculate_average(p):
    '''statement : CALCULATE AVERAGE'''
    commands.append(("average",))

def p_filter_greater(p):
    '''statement : FILTER GREATER NUMBER'''
    commands.append(("filter_greater", p[3]))

# ---- ERROR HANDLING ----

def p_error(p):
    if p:
        print("Ignored unknown command:", p.value)
    else:
        print("Syntax error")

parser = yacc.yacc()