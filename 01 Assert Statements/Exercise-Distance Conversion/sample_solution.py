from distance_conversion import metres_to_miles

# For the first two, we know the exact answer, so we can use the equality operator
assert metres_to_miles(2000) == 1.242742, "2000m should have been converted to 1.242742 miles"

assert metres_to_miles(1000.0) == 0.621371, "1000.0m should have been converted to 0.621371 miles"

# For the third, the floating operation is not exact, so we need to use an approximate comparison
# We could have also taken a similar approach in the first two checks
assert abs(metres_to_miles(1500) - 0.9320565) < 1e-5, "1500m should have been converted to 0.9320565 miles"
