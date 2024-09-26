try:
    countlines = countchars = 0
    file = open('count_lines_chars.py', 'r')
    lines = file.readlines()

    for line in lines:
        countlines += 1

        for char in line:
            countchars += 1

    file.close()

    print(f"Characters in file: {countchars}")
    print(f"Lines in file: {countlines}")
except IOError as error:
    print(f"I/O Error occurred: {error}")
