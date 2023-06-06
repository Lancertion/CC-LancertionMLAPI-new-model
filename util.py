# TODO
# Menyesuaikan input dengan model machine learning.

def parseInput(json):
    input = [1 for _ in range(16)]

    for _, value in json.items():
        input.append(value)

    return input
