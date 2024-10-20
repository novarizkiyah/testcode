#Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'.
'''
    Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
    Use a loop to print the name of each river included in the dictionary.
    Use a loop to print the name of each country included in the dictionary.

'''
    
Rivers_flow_in_you = {
    "Nile" : "Egypt",
    "gangga" : "India",
    "Aare" : "Swizzerland"
}

for river, country in Rivers_flow_in_you.items():
    print(f"{river} run through {country}")

for river in Rivers_flow_in_you:
    print(river)

for country in Rivers_flow_in_you:
    print(country)