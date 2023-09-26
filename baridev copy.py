def solution(n, actions):
    state_transitions = {
        'A': {'event1': 'B', 'event2': 'C'},
        'B': {'event1': 'C', 'event2': 'D'},
        'C': {'event1': 'D', 'event2': 'A'},
        'D': {'event1': 'A', 'event2': 'B'}
    }

    current_state = 'A'
    result = []

    for action in actions:
        if current_state not in state_transitions:
            return "ERROR"
        
        if action not in state_transitions[current_state]:
            return "ERROR"

        new_state = state_transitions[current_state][action]
        result.append(new_state)
        current_state = new_state

    return ", ".join(result)


n = int(input())
actions = list(map(str, input().split()))

out_ = solution(n, actions)
print(out_)
