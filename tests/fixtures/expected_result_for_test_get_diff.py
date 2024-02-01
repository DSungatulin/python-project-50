expected_result = [
    {'key': 'a', 'action': 'UNCHANGED', 'old value': 1, 'new value': 1},
    {'key': 'b', 'action': 'CHANGED', 'old value': 2, 'new value': 3},
    {'key': 'c', 'nested': [
        {'key': 'x', 'action': 'UNCHANGED', 'old value': 10, 'new value': 10},
        {'key': 'y', 'action': 'REMOVED', 'old value': 20, 'new value': None},
        {'key': 'z', 'action': 'ADDED', 'old value': None, 'new value': 30}
    ]},
    {'key': 'd', 'action': 'ADDED', 'old value': None, 'new value': 4}
]