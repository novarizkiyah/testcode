def get_formatted_name(city,country, populations=''):
    if populations:
        full_name = f"{city}, {country} - population {populations}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()