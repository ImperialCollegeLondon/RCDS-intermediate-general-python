def process(raw_results):
    # Receive the list of results from our equipment
    # Use a list comprehension to loop over the raw results
    # If the reading is negative, the "if" will prevent the value being used to calculate the processed results
    # Otherwise, we convert the value to kg and add it to the list of processed results
    processed_results = [result * 0.454 for result in raw_results if result >= 0]

    # Return the list of processed results
    return (processed_results)