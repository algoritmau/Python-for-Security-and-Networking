try:
    file_handle = open('nonexistant_file.txt', 'r')
except IOError as e:
    print(f'IOError Exception raise: Unable to read from nonexistant_file: {e}')
except Exception as e:
    print(f'An error has occurred: {e}')
else:
    print('File read successfully.')
    file_handle.close()
