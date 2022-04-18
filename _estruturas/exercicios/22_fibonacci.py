def fibonacci_recursivo(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci_recursivo(numero - 1) + fibonacci_recursivo(numero - 2)

def fibonacci_iterativo(numero):
    if numero <= 1:
        return numero
    elif numero == 2:
        return 1
    else:
        a = 0
        b = 1
        c = 0
        i = 2

        while i <= numero:
            c = a + b
            a = b
            b = c
            i += 1
        
        return c

print('fib(0)')
print(fibonacci_iterativo(0))
print(fibonacci_recursivo(0))

print('fib(2)')
print(fibonacci_iterativo(2))
print(fibonacci_recursivo(2))

print('fib(5)')
print(fibonacci_iterativo(5))
print(fibonacci_recursivo(5))

print('fib(6)')
print(fibonacci_iterativo(6))
print(fibonacci_recursivo(6))

print('fib(25)')
print(fibonacci_iterativo(25))
print(fibonacci_recursivo(25))
