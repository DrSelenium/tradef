import requests
import json

# Test data
test_data = [
    {
        "name": "test1",
        "formula": "Fee = \\text{TradeAmount} \\times \\text{BrokerageRate} + \\text{FixedCharge}",
        "variables": {
            "TradeAmount": 10000.0,
            "BrokerageRate": 0.0025,
            "FixedCharge": 10.0
        },
        "type": "compute"
    },
    {
        "name": "test2",
        "formula": "Fee = \\max(\\text{TradeAmount} \\times \\text{BrokerageRate}, \\text{MinimumFee})",
        "variables": {
            "TradeAmount": 1000.0,
            "BrokerageRate": 0.003,
            "MinimumFee": 15.0
        },
        "type": "compute"
    },
    {
        "name": "test3",
        "formula": "Fee = \\frac{\\text{TradeAmount} - \\text{Discount}}{\\text{ConversionRate}}",
        "variables": {
            "TradeAmount": 11300.0,
            "Discount": 500.0,
            "ConversionRate": 1.2
        },
        "type": "compute"
    }
]

response = requests.post('http://127.0.0.1:4000/trading-formula', json=test_data)
print("Status:", response.status_code)
print("Response:", response.json())
