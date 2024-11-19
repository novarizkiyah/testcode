def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Current design : {current_design}")
        completed_models.append(current_design)

def show_complete_models(completed_models):
    for complete_model in completed_models:
        print(complete_model)