import re


def find_first_digit(string):
    match = re.search(r"\d", string)
    if match:
        return match.group()
    return None


def reverse(string):
    string = string[::-1]
    return string


def main():
    counter = 0

    with open("data.txt", "r") as file:
        for line in file:
            backward = reverse(line)
            first = find_first_digit(line)
            second = find_first_digit(backward)

            a = str(first) + str(second)
            a = int(a)
            counter += a

            pass

    print(counter)


if __name__ == "__main__":
    main()
