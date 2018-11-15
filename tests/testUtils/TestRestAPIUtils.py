# pyhamcrest посмотреть!


def compare_two_json(first_json, second_json):
    sorted_1 = sorted([repr(x) for x in first_json])
    sorted_2 = sorted([repr(x) for x in second_json])
    return sorted_1 == sorted_2


def get_request_json(method_name, **kwargs):
    response_pattern = '"jsonrpc": "2.0", "method": "{}", '.format(str(method_name))
    parameters = ''
    for key, value in kwargs.items():
        parameter = '"{}": "{}"'.format(key, value)
        parameters += parameter + ', '

    response = '{' + response_pattern + '"params": {' + parameters[:-2] + '}, "id": "1"}'
    return response
