def fib_recursivo(n):

    # condições de parada
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # F(n) = F(n - 1) + F(n - 2)
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)


#print(fib_recursivo(0))
#print(fib_recursivo(1))
#print(fib_recursivo(2))

#print(fib_recursivo(5))
    # fib_recursivo(4)
        # fib_recursivo(3)
            # fib_recursivo(2)
                # fib_recursivo(1)
                # fib_recursivo(0)
            # fib_recursivo(1)
        # fib_recursivo(2)

#print(fib_recursivo(8))


def fib_iterativo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0 # n - 2
        b = 1 # n - 1
        c = 0 # n

        i = 2

        while (i <= n):
            # F(n) = F(n - 1) + F(n - 2)
            c = b + a

            a = b
            b = c

            i += 1

        return c


#print(fib_iterativo(0))
#print(fib_iterativo(1))

#print(fib_iterativo(2))
#print(fib_iterativo(5))
#print(fib_iterativo(6))

print('Iterativo')
print(fib_iterativo(35))

print('Recursivo')
print(fib_recursivo(35))

