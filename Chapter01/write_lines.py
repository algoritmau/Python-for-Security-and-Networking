try:
    my_file = open('new_file.txt', 'wt')

    for i in range(10):
        my_file.write(f'Line #{i + 1}\n')

    my_file.close()
except IOError as e:
    print(f'An I/O Error has occurred: {e.errno}')
