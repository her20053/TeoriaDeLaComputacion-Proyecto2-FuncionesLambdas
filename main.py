def programa():
    operacion_alpha = lambda x: x + 1
    # operacion_beta  = lambda x: 2 * x

    num_cero   = lambda f: lambda x: x
    num_uno    = lambda f: lambda x: f(x)
    num_dos    = lambda f: lambda x: f(f(x))
    num_tres   = lambda f: lambda x: f(f(f(x)))
    num_cuatro = lambda f: lambda x: f(f(f(f(x))))
    num_cinco  = lambda f: lambda x: f(f(f(f(f(x)))))

    sucesor        = lambda n: lambda f: lambda x: f(n(f)(x))
    potencia       = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)
    multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
    suma           = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))

    print("3 + 2:", suma(num_tres)(num_dos)(operacion_alpha)(num_cero(operacion_alpha)(0)))
    print("5 * 1:", multiplicacion(num_cinco)(num_uno)(operacion_alpha)(num_cero(operacion_alpha)(0)))
    print("4 ^ 4:", potencia(num_cuatro)(num_cuatro)(operacion_alpha)(num_cero(operacion_alpha)(0)))
    print("Numero proximo a 4 (Sucesor):", sucesor(num_cuatro)(operacion_alpha)(num_cero(operacion_alpha)(0)))

if __name__ == '__main__':
    programa()