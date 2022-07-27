def process(raw_results):
    processed_results = [result * 0.454 for result in raw_results if result >= 0]

    return(processed_results)