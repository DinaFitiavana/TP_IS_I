import sympy as sp
from taylor import (
    x,
    taylor_polynomial,
    taylor_value,
    taylor_integral,
    true_value,
    true_integral,
    absolute_error,
)

f = (1 + 2 * x) ** sp.Rational(1, 2)   
x0 = 0
n = 3                                   


def question_1():
    print("=" * 70)
    print("QUESTION 1 : Polynôme de Taylor de degré 3 de f(x) = (1+2x)^(1/2) en x0=0")
    print("=" * 70)
    P3 = taylor_polynomial(f, x0, n)
    print(f"f(x)  = {f}")
    print(f"P3(x) = {P3}")
    print(f"P3(x) (numérique) = {sp.nsimplify(P3)} = "
          f"{sp.N(P3, 6)}")
    return P3


def question_2(P3):
    print()
    print("=" * 70)
    print("QUESTION 2 : Approximation de sqrt(1.2) via P3, et erreur")
    print("=" * 70)
    # sqrt(1.2) = f(0.1) puisque 1 + 2*0.1 = 1.2
    x_val = sp.Rational(1, 10)

    approx = taylor_value(f, x0, n, x_val)
    exact = true_value(f, x_val)
    err = absolute_error(approx, exact)

    print(f"1 + 2*x = 1.2  =>  x = {float(x_val)}")
    print(f"Approximation P3(0.1)      = {approx:.10f}")
    print(f"Valeur exacte  sqrt(1.2)   = {exact:.10f}")
    print(f"Erreur absolue |exacte-approx| (E2) = {err:.10e}")
    return err


def question_3(P3, err2):
    print()
    print("=" * 70)
    print("QUESTION 3 : Approximation de l'intégrale de f entre 0 et 0.1, et erreur")
    print("=" * 70)
    a, b = 0, sp.Rational(1, 10)

    approx_int = taylor_integral(f, x0, n, a, b)
    exact_int = true_integral(f, a, b)
    err3 = absolute_error(approx_int, exact_int)

    print(f"Intégrale approchée  ∫0^0.1 P3(x) dx        = {approx_int:.10f}")
    print(f"Intégrale exacte     ∫0^0.1 (1+2x)^(1/2) dx = {exact_int:.10f}")
    print(f"Erreur absolue |exacte-approx| (E3)          = {err3:.10e}")

    print()
    print("-" * 70)
    print("Comparaison des erreurs (rapport E3 / E2) :")
    ratio = err3 / err2
    print(f"E2 (erreur question 2) = {err2:.10e}")
    print(f"E3 (erreur question 3) = {err3:.10e}")
    print(f"Rapport E3 / E2 = {ratio:.6e}  "
          f"(l'erreur d'intégration est environ {1/ratio:.1f} fois plus "
          f"petite que l'erreur d'évaluation ponctuelle)"
          if ratio < 1 else
          f"Rapport E3 / E2 = {ratio:.6e}")
    return err3


if __name__ == "__main__":
    P3 = question_1()
    err2 = question_2(P3)
    err3 = question_3(P3, err2)
