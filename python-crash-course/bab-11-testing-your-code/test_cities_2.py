from city_functions_2 import get_formatted_name

def test_city_country():
    formatted_name = get_formatted_name('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'