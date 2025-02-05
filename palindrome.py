def is_palindrom(s):
    s = s.lower(). replace(" ", "")
    return s == s[::-1]


def main():
    input_s = input("Enter a string: ")
    if is_palindrom(input_s):
        return 1
    else:
        return 0

