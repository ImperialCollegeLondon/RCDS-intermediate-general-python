from types import FunctionType

# Import wet_bulb_stull
try:
    from wet_bulb import wet_bulb_stull
except ModuleNotFoundError:
    assert False, "wet_bulb_checker.py tried to import from the file wet_bulb.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "wet_bulb_checker.py tried to import the function 'wet_bulb_stull' from the file wet_bulb.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check wet_bulb_stull is a function
assert type(wet_bulb_stull) == FunctionType, "wet_bulb_stull is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def check_web_bulb_stull(dry_temperature, relative_humidity, reference_wet_temperature):
    try:
        wet_temperature = wet_bulb_stull(dry_temperature, relative_humidity)
    except:
        print("When called with a temperature {}C and a relative humidity of {}%, wet_bulb_stull raised the following exception. You may have modified he function - try re-downloading the file if this problem persists.".format(dry_temperature, relative_humidity))
        raise

    assert type(wet_temperature) == float, "When called with a temperature {}C and a relative humidity of {}%, wet_bulb_stull returned a value which was of the type {} instead of a float. You may have modified he function - try re-downloading the file if this problem persists.".format(dry_temperature, relative_humidity, type(wet_temperature))

    assert abs(wet_temperature - reference_wet_temperature) < 0.1, "When called with a temperature {}C and a relative humidity of {}%, wet_bulb_stull returned {}C as a wet bulb temperature, instead of te correct value of {}C. You may have modified he function - try re-downloading the file if this problem persists.".format(dry_temperature, relative_humidity, wet_temperature, reference_wet_temperature)

check_web_bulb_stull(10, 50, 5.101)
check_web_bulb_stull(35, 99, 34.96)
check_web_bulb_stull(35, 5, 13.307)

# Import habitability_analyser
try:
    from wet_bulb import habitability_analyser
except ModuleNotFoundError:
    assert False, "wet_bulb_checker.py tried to import from the file wet_bulb.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "wet_bulb_checker.py tried to import the function 'habitability_analyser' from the file wet_bulb.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check habitability_analyser is a function
assert type(habitability_analyser) == FunctionType, "habitability_analyser is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def habitability_analyser_checker(dry_temperatures, relative_humidities, reference_result):
    try:
        student_result = habitability_analyser(dry_temperatures, relative_humidities)
    except:
        print("When habitability_analyser was called with the dry temperatures of {} and relative humidities of {} the following exception was raised. Check the logic of your code.".format(dry_temperatures, relative_humidities))
        raise

    assert type(student_result) == bool, "When habitability_analyser was called with the dry temperatures {} and relative humidities {} the returned result had a type of {} instead of bool. Check the logic of your code.".format(dry_temperatures, relative_humidities, type(student_result))

    assert student_result == reference_result, "When habitability_analyser was called with the dry temperatures  {} and relative humidities {} the returned result a value of {} instead of the correct result of {}. Check the logic of your code.".format(dry_temperatures, relative_humidities, student_result, reference_result)

# Check habitability_analyser returns the correct values
habitability_analyser_checker((), (), True)
habitability_analyser_checker((10,), (50,), True)
habitability_analyser_checker((40,), (99,), False)
habitability_analyser_checker((40, 10), (99, 50), False)
habitability_analyser_checker((10, 40), (50, 99), False)
habitability_analyser_checker((40, 50), (99, 90), False)
habitability_analyser_checker((10, 35), (50, 50), True)
habitability_analyser_checker((10, 40, 40), (50, 99, 10), False)

print("Congratulations - your function 'habitability_analyser' passed all the tests")

# Import find_hot_indexes
try:
    from wet_bulb import find_hot_indexes
except ModuleNotFoundError:
    assert False, "wet_bulb_checker.py tried to import from the file wet_bulb.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "wet_bulb_checker.py tried to import the function 'find_hot_indexes' from the file wet_bulb.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

# Check find_hot_indexes is a function
assert type(find_hot_indexes) == FunctionType, "find_hot_indexes is not a function. Make sure you're using def to define it as a function and have not redefined it later in your script."

def find_hot_indexes_checker(dry_temperatures, relative_humidities, reference_result):
    try:
        student_result = find_hot_indexes(dry_temperatures, relative_humidities)
    except:
        print("When find_hot_indexes was called with the dry temperatures of {} and relative humidities of {} the following exception was raised. Check the logic of your code.".format(dry_temperatures, relative_humidities))
        raise

    assert type(student_result) == list, "When find_hot_indexes was called with the dry temperatures {} and relative humidities {} the returned result had a type of {} instead of list. Check the logic of your code.".format(dry_temperatures, relative_humidities, type(student_result))

    assert student_result == reference_result, "When find_hot_indexes was called with the dry temperatures  {} and relative humidities {} the returned result a value of {} instead of the correct result of {}. Check the logic of your code.".format(dry_temperatures, relative_humidities, student_result, reference_result)

# Check find_hot_indexes_checker returns the correct values
find_hot_indexes_checker((), (), [])
find_hot_indexes_checker((10,), (50,), [])
find_hot_indexes_checker((40,), (99,), [0])
find_hot_indexes_checker((40, 10), (99, 50), [0])
find_hot_indexes_checker((10, 40), (50, 99), [1])
find_hot_indexes_checker((40, 50), (99, 90), [0,1])
find_hot_indexes_checker((10, 35), (50, 50), [])
find_hot_indexes_checker((10, 40, 40), (50, 99, 10), [1])

print("Congratulations: both functions passed all the tests!")