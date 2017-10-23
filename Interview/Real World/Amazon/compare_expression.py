# -(a+b+c) = -c-a-b
# (a-b)-c = -c + a - b
from collections import defaultdict


def compare_expression(expr1, expr2):
    expr_1_map = {}
    expr_2_map = {}
    expr_1_map = construct_exporession_map(expr1)
    expr_2_map = construct_exporession_map(expr2)
    print  expr_2_map, expr_1_map
    for key in expr_1_map.keys():
        if key in expr_2_map and expr_2_map[key] >= 0:
            expr_2_map[key] -= 1
        else:
            return False
    return True

def construct_exporession_map(expr):
    expression_map = defaultdict(int)
    for i in xrange(0,len(expr),2):
        if expr[i].isalpha():
            key = '+' + expr[i]
        else:
            key = expr[i] + expr[i + 1]

        if key in expression_map:
            expression_map[key] += 1
        else:
            expression_map[key] = 1
    #print expression_map
    return expression_map

print compare_expression('-a+b+c', '-a+b+c-a')
