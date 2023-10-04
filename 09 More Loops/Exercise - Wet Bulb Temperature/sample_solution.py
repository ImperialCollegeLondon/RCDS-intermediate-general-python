from math import atan, sqrt


def wet_bulb_stull(dry_temperature, relative_humidity):
    # This function calculates the wet bulb temperature in Celsius according to the Stull formula
    # dry_temperature is the dry bulb temperature in Celsius (e.g. it might have the value 20)
    # relative humidity is the relative humidity in % (e.g. it might have the value 50)

    # Sometimes when calculating the result of a specific equation, it can be easier to split it into several smaller terms. This can increase readability and make finding errors easier, although it may be slightly slower to execute than using a single long expression
    term_1 = dry_temperature * atan(0.151977 * (sqrt(relative_humidity + 8.313659)))
    term_2 = atan(dry_temperature + relative_humidity)
    term_3 = - atan(relative_humidity - 1.676331)
    term_4 = 0.00391838 * relative_humidity ** (3 / 2) * atan(0.023101 * relative_humidity)
    term_5 = - 4.686035
    wet_temperature = term_1 + term_2 + term_3 + term_4 + term_5

    return (wet_temperature)


# This function receives lists of the dry temperatures and relative humidities at different times
# If at any point the wet bulb temperature exceeds 30 degrees the region is not inhabitable and False is returned
# If the wet bulb temperature never exceeds 30 degrees the region is inhabitable and True is returned
def habitability_analyser(dry_temperatures, relative_humidities):
    # Dry temperatures is a tuple of dry temperatures in Celsius
    # Relative humidities is a tuple of relative humidities in %

    # Loop over the temperatures
    # Each iteration of the loop relates to a specific time
    for dry_temperature, relative_humidity in zip(dry_temperatures, relative_humidities):
        # dry_temperature is the dry bulb temperature at the current time and takes the value of the current element of the dry_temperatures list
        # relative_humidity is the relative humidity at the current time and takes the value of the current element of the relative_humidities list

        # Use the wet_bulb_stull function to calculate the wet bulb temperature at the current time
        if wet_bulb_stull(dry_temperature, relative_humidity) > 30:
            # If it's greater than 30 degrees, the location isn't habitable, so return False
            return (False)
        # If the wet bulb temperature is less than or equal to 30 degrees, the location is habitable at the current time, so continue to the next iteration of the loop to consider the next time

    # If we've examined all times and none of them were uninhabitable, return True as the location is habitable
    return (True)


# This function receives lists of the dry temperatures and relative humidities at different times
# It returns a list of the indexes of the times when the wet bulb temperature exceeds 30 degrees
def find_hot_indexes(dry_temperatures, relative_humidities):
    # Dry temperatures is a tuple of dry temperatures in Celsius
    # Relative humidities is a tuple of relative humidities in %

    # Use a tuple comprehension to calculate the wet bulb temperatures at each time
    # dry_temperature is the dry bulb temperature at the current time and takes the value of the current element of the dry_temperatures list
    # relative_humidity is the relative humidity at the current time and takes the value of the current element of the relative_humidities list
    # These values are passed to the wet_bulb_stull function to calculate the wet bulb temperature at the current time, which is saved to the tuple
    wet_temperatures = tuple(wet_bulb_stull(dry_temperature, relative_humidity) for dry_temperature, relative_humidity in zip(dry_temperatures, relative_humidities))

    # Use a list comprehension to find the indexes of the times when the wet bulb temperature exceeds 30 degrees
    # index is the index of the current element of the wet_temperatures list
    # wet_temperature is the wet bulb temperature at the current time and takes the value of the current element of the wet_temperatures list
    hot_indexes = [index for index, wet_temperature in enumerate(wet_temperatures) if wet_temperature > 30]

    # Return the list of indexes
    # This may be an empty list if there are no times when the wet bulb temperature exceeds 30 degrees
    return (hot_indexes)
