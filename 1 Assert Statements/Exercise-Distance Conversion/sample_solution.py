from distance_conversion import metres_to_miles

assert metres_to_miles(2000) == 1.242742, "2000m should have been converted to 1.242742 miles"

assert metres_to_miles(1000.0) == 0.621371, "1000.0m should have been converted to 0.621371 miles"

assert abs(metres_to_miles(1500) - 0.9320565) < 1e-5 , "1500m should have been converted to 0.9320565 miles"
