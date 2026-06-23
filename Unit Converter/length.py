length_units = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344
}

def convert_length(value, from_unit, to_unit):
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]