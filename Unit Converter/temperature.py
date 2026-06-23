def convert_temperature(value, from_unit, to_unit):

    if from_unit == to_unit:
        return value

    if from_unit == "fahrenheit":
        value = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        value = value - 273.15

    if to_unit == "fahrenheit":
        return (value * 9 / 5) + 32
    elif to_unit == "kelvin":
        return value + 273.15

    return value