def f(x) -> float:
    return x**2 - 6*x + 5


def x_prime(x) -> float:
    return 2*x - 6


def newton_method(x0, tol=1e-6, max_iter=100) -> float:
    real_error: float = float('inf')
    iter: int = max_iter

    while iter > 0 or real_error > tol:
        x1: float = x0 - f(x0)/x_prime(x0)
        iter -= 1
        real_error = abs(x1-x0)
        x0 = x1
    return x1

def main():
    print('My function is: x**2 - 6x + 5')
    print('Derivative: 2x - 6')
    root: float = newton_method(float(input("Enter initial guess:")))
    print('The root of this function is: '+root)


if __name__ == '__main__':
    main()








