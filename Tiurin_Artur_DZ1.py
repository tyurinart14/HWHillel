# fixture = [
#     {"foo": "foo", "bar": "bar"},
#     {"foo": "bar", "bar": "bar"},
#     {"foo": "bar", "bar": "foo"},
#     {"foo": "foo", "bar": "foo"},
# ]
# origin = [
#     {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
#     {"foo": "F", "bar": "BAR", "foobar": "fb"},
#     {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
# ]

def filter_by_first_met_value(dataset, keys):
    result = dict()
    for Dict in dataset:
        temp = tuple([Dict[item] for item in keys if Dict[item] not in result])
        if temp not in result:
            result[temp] = Dict
    return list(result.values())


# print(filter_by_first_met_value(origin, ['foobar']))