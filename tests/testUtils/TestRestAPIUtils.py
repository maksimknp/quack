

def compare_two_json(first_json, second_json):
    sorted_1 = sorted([repr(x) for x in first_json])
    sorted_2 = sorted([repr(x) for x in second_json])
    return sorted_1 == sorted_2
