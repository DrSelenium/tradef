import re
import math

variables = {'R_f':0.02,'beta_i':1.2,'E_R_m':0.08}

formula = r'R_f + \beta_i (E[R_m] - R_f)'
print("Original:", formula)

# Preprocess
formula = re.sub(r'\\text\{([^}]+)\}', r'\1', formula)
formula = formula.replace(r'\times', '*')
formula = formula.replace(r'\cdot', '*')
formula = formula.replace(r'\max', 'max')
formula = formula.replace(r'\min', 'min')
formula = formula.replace(r'\exp', 'math.exp')
formula = formula.replace(r'\log', 'math.log')
formula = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1)/(\2)', formula)
# Handle Greek letters
formula = formula.replace(r'\beta', 'beta')
formula = formula.replace(r'\alpha', 'alpha')
formula = formula.replace(r'\sigma', 'sigma')
# Handle subscripts
formula = formula.replace('[', '_')
formula = formula.replace(']', '')
print("Preprocessed:", formula)

# Handle implicit multiplication
formula = re.sub(r'(\w)\s*\(', r'\1*(', formula)
formula = re.sub(r'\)\s*(\w)', r')*\1', formula)
print("After implicit:", formula)

# Evaluate
result = eval(formula, {"max": max, "min": min, "math": math}, variables)
print("Result:", result)
