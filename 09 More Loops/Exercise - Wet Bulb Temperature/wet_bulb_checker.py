from types import FunctionType

# Import wet_bulb_stull
try:
    from wet_bulb import wet_bulb_stull
except ModuleNotFoundError:
    assert False, "wet_bulb_checker.py tried to import from the file wet_bulb.py but the file didn't exist. Check it is present and the name is spelt correctly."
except ImportError:
    assert False, "wet_bulb_checker.py tried to import the function 'wet_bulb_stull' from the file wet_bulb.py. The file existed, but the function didn't. Check the function is in that file and that the name is spelt correctly."

def check_web_bulb_stull(dry_temperature, relative_humidity, reference_wet_temperature):
    try:
        wet_temperature = wet_bulb_stull(dry_temperature, relative_humidity)
    except:
        print("When called with a temperature {}C and arelative humidity of {}%, wet_bulb_stull raised the followin exception. You may have modified he function - try re-downloading the file if this problem persists.".format(dry_temperature, relative_humidity))
        raise

    assert type(wet_temperature) == float, "When called with a temperature {}C and arelative humidity of {}%, wet_bulb_stull returned a vlaue which was of the type {} instead of a float. You may have modified he function - try re-downloading the file if this problem persists.".format(dry_temperature, relative_humidity, type(wet_temperature))

    assert abs(wet_temperature - reference_wet_temperature) < 0.1, "When called with a temperature {}C and arelative humidity of {}%, wet_bulb_stull returned {}C as a wet bulb temperature, insead of te crrect value of {}C. You may have modified he function - try re-downloading the file if this problem persists.".format(dry_temperature, relative_humidity, wet_temperature, reference_wet_temperature)

check_web_bulb_stull(10, 50, 5.101)
check_web_bulb_stull(35, 99, 34.96)
check_web_bulb_stull(35, 5, 13.307)