from flask import Flask, request, jsonify
import re
import os
import math

app = Flask(__name__)

@app.route('/trading-formula', methods=['POST'])
def trading_formula():
    data = request.get_json()
    results = []
    for test in data:
        formula = test['formula']
        variables = test['variables']
        
        # Remove surrounding $$ if present
        formula = formula.strip('$$')
        
        # Split by = and take the right-hand side
        if '=' in formula:
            rhs = formula.split('=', 1)[1].strip()
        else:
            rhs = formula
        
        # Preprocess the LaTeX expression
        rhs = re.sub(r'\\text\{([^}]+)\}', r'\1', rhs)
        rhs = rhs.replace(r'\times', '*')
        rhs = rhs.replace(r'\cdot', '*')
        rhs = rhs.replace(r'\max', 'max')
        rhs = rhs.replace(r'\min', 'min')
        rhs = rhs.replace(r'\sum', 'sum')
        rhs = rhs.replace(r'\exp', 'math.exp')
        rhs = rhs.replace(r'\log', 'math.log')
        rhs = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1)/(\2)', rhs)
        # Handle e^{x}
        rhs = re.sub(r'e\^\{([^}]+)\}', r'math.exp(\1)', rhs)
        # Handle \ln
        rhs = rhs.replace(r'\ln', 'math.log')
        # Handle Greek letters
        rhs = rhs.replace(r'\beta', 'beta')
        rhs = rhs.replace(r'\alpha', 'alpha')
        rhs = rhs.replace(r'\sigma', 'sigma')
        # Handle brackets
        rhs = rhs.replace(r'\left(', '(')
        rhs = rhs.replace(r'\right)', ')')
        rhs = rhs.replace(r'\left[', '[')
        rhs = rhs.replace(r'\right]', ']')
        # Handle implicit multiplication
        rhs = re.sub(r'(\w)\s*\(', r'\1*(', rhs)
        rhs = re.sub(r'\)\s*(\w)', r')*\1', rhs)
        
        # Evaluate
        try:
            result = eval(rhs, {"max": max, "min": min, "math": math, "sum": sum}, variables)
            # Round to 4 decimal places
            rounded = round(float(result), 4)
        except Exception as e:
            # In case of error, perhaps return 0 or something, but for now
            rounded = 0.0
        
        results.append({"result": f"{rounded:.4f}"})
    
    return jsonify(results)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)