#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n < 2:
        return n
    
    n_1 = 0 # term 0
    n_2 = 1 # term 1
    n_th = 1    # term 2
    position = 2
    while position != n:
        n_1, n_2 = n_2, n_th
        n_th = n_2 + n_1
        position += 1
    return n_th




# print fibonacci(36)
#>>> 14930352

# print fibonacci(1)
# print fibonacci(2)
# print fibonacci(3)
# print fibonacci(4)
print fibonacci(36)

