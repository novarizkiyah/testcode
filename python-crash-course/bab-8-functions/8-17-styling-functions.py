# Choose ant three programs you wrote for this chapter
# and make sure they follow the styling guidelines describes in this section


# printing_functions.py




def print_models(unprinted_design, complete_models):
    """
    Simulate printing each design until none are left.
    Move each design to complete_models after printing.
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"My list {current_design} ")
        complete_models.append(current_design)

def show_complete_models(complete_models):
    """Display all completed models."""
    for complete_model in complete_models:
        print(f"My design now {complete_model}")


#printing_models.py





