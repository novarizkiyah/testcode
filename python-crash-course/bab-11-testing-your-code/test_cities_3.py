from city_functions_2 import get_formatted_name

def test_city_country_population():
    formatted_name = get_formatted_name('Santiago','Chile', populations = 5000000)
    assert formatted_name == 'Santiago, Chile - Population 5000000'