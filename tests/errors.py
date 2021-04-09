

def fahr_to_celsius(temperature_f):
    temperature_c = ((temperature_f - 32) * (5/9))
    assert(temperature_c >= -273.15)
    return temperature_c
    
def celsius_to_kelvin(temperature_c):
    temperature_k = temperature_c + 273.15
    assert (temperature_k >= 0.0)
    return temperature_k

def test_functions():
    print('freezing point of water:', fahr_to_celsius(32), 'C')
    print('boiling point of water:', fahr_to_celsius(212), 'C')
    print('very cold:',celsius_to_kelvin(fahr_to_celsius(-300)), 'K')

    assert(fahr_to_celsius(32) == 0.0)
    assert(fahr_to_celsius(212) == 100.0)
    assert(celsius_to_kelvin(fahr_to_celsius(-300)) > 0.0)

test_functions()