def metres_to_miles(dist_metres):
    # Calculate the distance in km
    dist_km = dist_metres // 1000

    # Calculate the distance in miles
    dist_miles = 0.621371 * dist_km

    return (dist_miles)
