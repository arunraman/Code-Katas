def json_parser(input):
    result = {}

    is_dict = input[0] == '{'
    pos = 0
    length = len(input)
    while pos < length:
        test1 = input[pos]
        keyStartPos = pos+2
        keyEndPos = input.find('"', keyStartPos)

        keyStart = input[keyStartPos]
        keyEnd = input[keyEndPos]

        key = input[keyStartPos:keyEndPos]

        valueStartPos = keyEndPos + 3
        valueEndPos = input.find('"', valueStartPos)
        value = input[valueStartPos:valueEndPos]

        pos = valueEndPos + 2

        result[key] = value

    if not is_dict:
        result = [[key, value] for key, value in result.items()]
        result = [item for sublist in result for item in sublist]

    print(result)
    return result

json_parser('{"foo":"bar"}')