colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
states = ['Telangana', 'Karnataka', 'Tamilnadu', 'Kerala']

neighbors = {
    'Telangana': ['Karnataka', 'Tamilnadu'],
    'Karnataka': ['Telangana', 'Tamilnadu', 'Kerala'],
    'Tamilnadu': ['Telangana', 'Karnataka', 'Kerala'],
    'Kerala': ['Karnataka', 'Tamilnadu']
}

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state, []):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print("Assigned Colors:")
    for s, c in colors_of_states.items():
        print(f"{s}: {c}")

main()
