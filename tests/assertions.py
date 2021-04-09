
absolute_zero_c = -273.15

def fahr_to_celsius(temperature):
    return((temperature -32) * (5/9))

def celsius_to_kelvin(temperature):
    # Pre-conditions:
    assert(temperature >= absolute_zero_c)
    return(temperature+273.15)

def fahr_to_kelvin(temperature_fahr):
    temperature_c = fahr_to_celsius(temperature_fahr)
    temperature_k = celsius_to_kelvin(temperature_c)
    assert(temperature_k >= 0.0)
    return temperature_k


print("freezing point:", fahr_to_celsius(32))
print("boiling point:", fahr_to_celsius(212))
print("cold point:", fahr_to_kelvin(-212))

# Post-conditions:
assert (fahr_to_celsius(32) == 0.0)
assert (fahr_to_celsius(212) == 100.0)

assert (celsius_to_kelvin(0.0) == 273.15)
assert (celsius_to_kelvin(100.0) == 373.15)

assert (fahr_to_kelvin(32) == 273.15)

# Invariants:
assert (absolute_zero_c == -273.15)
fahr_to_kelvin(32)
assert (absolute_zero_c == -273.15)