import sympy as sp

x = sp.symbols("x")


def taylor_polynomial(f_expr, x0, n):
    P = 0
    deriv = f_expr
    for k in range(n + 1):
        if k > 0:
            deriv = sp.diff(deriv, x)
        coeff = deriv.subs(x, x0) / sp.factorial(k)
        P += coeff * (x - x0) ** k
    return sp.expand(P)


def taylor_value(f_expr, x0, n, x_val):
    P = taylor_polynomial(f_expr, x0, n)
    return float(P.subs(x, x_val))


def taylor_integral(f_expr, x0, n, a, b):
    P = taylor_polynomial(f_expr, x0, n)
    integral = sp.integrate(P, (x, a, b))
    return float(integral)


def true_value(f_expr, x_val):
    return float(f_expr.subs(x, x_val))


def true_integral(f_expr, a, b):
    integral = sp.integrate(f_expr, (x, a, b))
    return float(integral)


def absolute_error(approx, exact):
    return abs(exact - approx)
