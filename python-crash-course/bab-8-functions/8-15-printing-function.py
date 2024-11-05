def print_models(unprinted_design, complete_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"My list {current_design}")
        complete_models.append(current_design)

def show_complete_models(complete_models):
    for complete_model in complete_models:
        print(f"My design now {complete_model}")