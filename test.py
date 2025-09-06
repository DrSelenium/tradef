import re
from sympy.parsing.latex import parse_latex
import sympy

formula = r'TradeAmount * BrokerageRate + FixedCharge'
print("Original:", formula)

expr = parse_latex(formula)
print("Parsed expr:", expr)

# Substitute
subs = {sympy.Symbol('TradeAmount'): 10000, sympy.Symbol('BrokerageRate'): 0.0025, sympy.Symbol('FixedCharge'): 10}
result = expr.subs(subs)
print("Substituted:", result)
print("Evaluated:", float(result.evalf())) sympy.parsing.latex import parse_latex
import sympy

formula = r'a \times b + c'
print("Original:", formula)

expr = parse_latex(formula)
print("Parsed expr:", expr)

# Substitute
subs = {sympy.Symbol('a'): 10000, sympy.Symbol('b'): 0.0025, sympy.Symbol('c'): 10}
result = expr.subs(subs)
print("Substituted:", result)
print("Evaluated:", float(result.evalf()))
