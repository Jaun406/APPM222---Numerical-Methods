from sympy import latex,symbols

def f(x: float) -> float:
    '''
    This function defines the function f(x)
    x: float
    f: float
    returns: float
    '''
    f = x**3 - 2*x - 5
    return f


def bisection(a: float, b: float, tol: float) -> list[float,int]:
    '''
    This function implements the bisection method
    a: float
    b: float
    tol: float
    returns: float
    '''
    cur_tol = float('inf')
    iter = 0
    while cur_tol > tol:
        c = (a+b)/2

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        if a == c and b == c:
            return [c,0]

        cur_tol = abs(b-a)

    iter += 1
    return [c,iter]


def main():
    # Print function to get the root of
    x = symbols('x')
    expr = x**3 - 2*x - 5
    print("Function to get the root of: " + latex(expr))
    # Get parameters form user
    a = float(input("Enter the lower bound: "))
    b = float(input("Enter the upper bound: "))
    tol = float(input("Enter the tolerance: "))
    print("--------------------------------")

    # Call bisection method
    root,iter = bisection(a,b,tol)

    if iter == 0:
        print("Function does not converge to the root")
    else:
        # Print results
        print(f"Root: {root}")
        print(f"Iterations: {iter}")
        print(f"Function value at root: {f(root)}")
        print(f"Function value at lower bound: {f(a)}")
        print(f"Function value at upper bound: {f(b)}")


if __name__ == "__main__":
    main()