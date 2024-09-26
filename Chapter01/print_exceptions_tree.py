def print_exceptions_tree(ExceptionClass, level = 0):
    if level > 1:
        print("   |" * (level - 1), end="")
    
    if level > 0:
        print("   +---", end="")

    print(ExceptionClass.__name__)

    for subclass in ExceptionClass.__subclasses__():
        print_exceptions_tree(subclass, level + 1)

print_exceptions_tree(BaseException)
