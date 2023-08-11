def solution(inputString):
    stack = []
    result = []

    for char in inputString:
        if char == '(':
            stack.append(result)
            result = []
        elif char == ')':
            current = result
            result = stack.pop()
            result.extend(reversed(current))
        else:
            result.append(char)

    return ''.join(result)


print(solution('foo(bar(baz))blim'))
