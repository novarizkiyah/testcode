#Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py,
#  and modify the file to use the imported functions.


from printing_function import print_models, show_complete_models

# Create lists of designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design
print_models(unprinted_designs, completed_models)

# Display all completed models
show_complete_models(completed_models)