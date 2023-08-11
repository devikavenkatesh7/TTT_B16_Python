def solution(input_string: str):
    if "(" in input_string:
        for ch in input_string:
            if ch == "(":
                first_idx = input_string.index(ch)
                break

        for ch in input_string[::-1]:
            if ch == ")":
                last_idx = input_string.index(ch)
                break
        return solution(
            input_string[:first_idx] + input_string[first_idx + 1:last_idx][::-1] + input_string[last_idx + 1:])
    else:
        return input_string


if __name__ == "__main__":
    input_string = "harish(abc(def)ghi)somsole"
    print(solution(input_string))
