weight_units = {
    "milligram": 0.000001,
    "gram": 0.001,
    "kilogram": 1,
    "ounce": 0.0283495,
    "pound": 0.453592
}

def convert_weight(value, from_unit, to_unit):
    kg = value * weight_units[from_unit]
    return kg / weight_units[to_unit]