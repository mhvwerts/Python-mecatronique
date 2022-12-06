#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import warnings
import numpy as np

def secant(func, x0, x1=None, args=(), tol=1e-8, ftol=None, maxiter=50):
    """
    Find a zero of the function `func` given nearby starting points `x0`
    and `x1`, using the secant method

    (based on scipy.optimize.zeros.newton)

    Parameters
    ----------
    func : function
        The function whose zero is wanted. It must be a function of a
        single variable of the form f(x,a,b,c...), where a,b,c... are extra
        arguments that can be passed in the `args` parameter.
    x0, x1 : floats 
        Initial estimates of the zero that should be somewhere near the
        actual zero. Two separate points are needed to begin the search.
        It is not necessary to bracket an interval where `func` changes sign.
        If `x1` is not specified, an initial guess will be constructed.
    args : tuple, optional
        Extra arguments to be used in the function call.
    tol : float, optional
        The allowable error on the `x` position of the zero of `func(x)`. This
        provides the stopping convergence criterion for the method.
    ftol : float, optional
        If specified, secant will check the result after convergence, and raise
        an error if `func(x)` is not within tolerance `ftol` of zero. If not 
        specified, there is no guarantuee that a zero was found even when 
        secant successfully terminates.
    maxiter : int, optional
        Maximum number of iterations.
    
    Returns
    -------
    zero : float
        Estimated `x` location where function `func(x)` is zero.
        
    See Also
    --------
    newton, brentq, brenth, ridder, bisect
    fsolve : find zeroes in n dimensions.
    
    Notes
    -----
    The stopping criterion used here is the step size and if `ftol` is not 
    specified there is no guarantee that a zero has been found. 
    Safer algorithms are brentq, brenth, ridder, and bisect, but they all 
    require that the root first be bracketed in an interval where the function
    changes sign. The brentq algorithm is recommended for general use in one
    dimensional problems when such an interval has been found.
    """
    if tol <= 0:
        raise ValueError("tol too small (%g <= 0)" % tol)
    if maxiter < 1:
        raise ValueError("maxiter must be greater than 0")

    p0 = x0
    if x1 == None: 
        p1 = x0 * 1.001 # construct initial guess for `x1` from `x0`
    else:
        p1 = x1
    if np.abs(p1 - p0) < tol: # if initial step small compared to `tol`
        p1 = x0 + 10.*tol
        msg = ("`x1` too close to `x0`. Initial step for secant method was "
               "increased to 10 times 'tol'.")
        warnings.warn(msg, RuntimeWarning)

    q0 = func(*((p0,) + args))
    q1 = func(*((p1,) + args))
    for i in range(maxiter):
        if q1 == q0:
            msg = ("Secant method failed to converge: no further progress "
                   "possible after {0} iterations: "
                   "x = {1}, f(x) = {2}").format(i, p1, q1)
            raise RuntimeError(msg)
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        p0 = p1
        q0 = q1
        p1 = p
        q1 = func(*((p1,) + args))
        if np.abs(p1 - p0) < tol:
            if ftol==None:
                return p1
            elif np.abs(q1) < ftol:
                return p1
            else:
                msg = "Result not close enough to zero."
                raise RuntimeError(msg)

    msg = "Secant failed to converge after %d iterations, x = %s"\
         % (maxiter,p)
    raise RuntimeError(msg)


### RUN SOME TESTS
if __name__=='__main__':

    
    # Test 1 (GGurthner)
    def f(x):
        return x**4 - x**2 + 1
    
    try:
        x = secant(f, 0.001)
    except:
        print('secant failed...')
    else:
        print('secant did not fail... x=', x, 'f(x)=',f(x))
   
    try:
        x = secant(f, 0.001, ftol=1e-2)
    except:
        print('secant failed as expected')
    else:
        print('secant did not fail... x=', x, 'f(x)=',f(x))

        
    # Test 2
    def g(x, k, xoff):
        y = 1./(1.+np.exp(-k*(x-xoff))) - 0.5
        return y
      
    for k in [1e6, 1e7, 1e10, 1e13, 1e20]:
        # parametrize curve and initial guess
        xoff=np.sqrt(2)/k
        x0guess=xoff*1.01 # start from a point already close
        # calculate f(x)=0 from secant and compare to analytical
        x_s = secant(g, x0guess, args=(k, xoff), tol=1e-3/k)
        print('analytical = ',xoff, '; secant = ', x_s)
    
    
    # add additional tests
    

        