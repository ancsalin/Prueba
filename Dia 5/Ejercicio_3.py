def cantidad_idefinida(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return  True
        return False

print(cantidad_idefinida(5, 0, 0, 3))      # True
print(cantidad_idefinida(1, 2, 0, 1, 0))   # False
print(cantidad_idefinida(0, 0))            # True
print(cantidad_idefinida())