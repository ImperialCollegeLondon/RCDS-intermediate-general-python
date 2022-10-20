from math import atan, sqrt

def wet_bulb_stull(dry_temperature, relative_humidity):
    # This function calculates the wet bulb temperature in Celsius according to the Stull formula
    # dry_temperature is the dry bulb temperature in Celsius (e.g. it might have the value 20)
    # relative humidity is the relative humidity in % (e.g. it might have the value 50)

    # Sometimes when calculating the result of a specific equation, it can be easier to split it into several smaller terms. This can increase readability and make finding errors easier, although it is slower to execute than using a single long expression
    term_1 = dry_temperature * atan(0.151977 * (sqrt(relative_humidity + 8.313659)))
    term_2 = atan(dry_temperature + relative_humidity)
    term_3 = - atan(relative_humidity - 1.676331)
    term_4 = 0.00391838 * relative_humidity ** (3/2) * atan(0.023101 * relative_humidity)
    term_5 = - 4.686035
    wet_temperature =  term_1 + term_2  + term_3 + term_4 + term_5

    return(wet_temperature)

def habitability_analyser(dry_temperatures, relative_humidities):
    for dry_temperature, relative_humidity in zip(dry_temperatures, relative_humidities):
        if wet_bulb_stull(dry_temperature, relative_humidity) > 30:
            return(False)
        
    return(True)

def find_hot_indexes(dry_temperatures, relative_humidities):
    wet_temperatures = tuple(wet_bulb_stull(dry_temperature, relative_humidity) for dry_temperature, relative_humidity in zip(dry_temperatures, relative_humidities))

    hot_indexes = [index for index, wet_temperature in enumerate(wet_temperatures) if wet_temperature > 30]

    return(hot_indexes)