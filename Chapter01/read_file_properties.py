file_descryptor = open("read_file_properties.py", "r+")

print(f"Content: {file_descryptor.read()}")
print(f"Name: {file_descryptor.name}")
print(f"Mode: {file_descryptor.mode}")
print(f"Encoding: {file_descryptor.encoding}")

file_descryptor.close()
