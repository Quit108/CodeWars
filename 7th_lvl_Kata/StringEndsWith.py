def solution(text, ending):
    return text.endswith(ending)

print(solution('abc', 'bc')) # True
print(solution('abc', 'd'))  # False