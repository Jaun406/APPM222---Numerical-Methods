PROC IML;
    /* Defiine function */
	start f(x);
		f = x**2 + 6*x -3;
		return f;
	finish;

	tol = 10**-5;
	a = -5;
	b = 10;
	/* Get number of iterations needed */
	n = CEIL((log(abs(b-a))-log(tol))/log(2));

	do i = 1 to n;
		c = (a+b)/2;
		IF (f(a)*f(c) < 0) THEN b = c;
		ELSE; 
			IF (f(b)*f(c) < 0) THEN a = c;
			ELSE print("Error in roots");
	end;

	root = c;
	print(root);
RUN;
