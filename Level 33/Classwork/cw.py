def convert_temperature(value, scale):
    if scale.lower() == 'celsious':
        return (value * 9/5) + 32
    elif scale.lower() == 'fahrenheit':
        return (value - 32) * 5/9
    else:
        return "Enter Celsious or Fahrenheit"

# მაგალითები
print(convert_temperature(25, 'C'))   # 25 °C to °F
print(convert_temperature(77, 'F'))   # 77 °F to °C