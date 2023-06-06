def parseOutput(output):
    output = output[0]
    if output == 1:
        return "Low"
    elif output == 2:
        return "Medium"
    elif output == 3:
        return "High"
    else:
        return "Error"
