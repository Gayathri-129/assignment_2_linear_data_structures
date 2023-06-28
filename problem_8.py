def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string


if __name__ == "__main__":
    string = input("Enter the string: ")
    reversed_string = reverse_string(string)
    print(reversed_string)