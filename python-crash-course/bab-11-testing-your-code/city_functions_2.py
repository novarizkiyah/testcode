def get_formatted_name(city,country, populations=0):
    if populations:
        full_name = f"{city}, {country} - Population {populations}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()