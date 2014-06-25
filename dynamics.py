from vroom import Solver

@Solver.vectorfield
def lorenz(x, y, z):
   (sigma, beta, rho) = (10.0, 8.0/3.0, 28.0)
   return [sigma*(y-x), x*(rho-z)-y, x*y-beta*z]

@Solver.vectorfield
def rossler(x, y, z):
   (a, b, c) = (0.2, 0.2, 5.7)
   return [-y-z, x+a*y, b+z*(x-c)]

equations = {
   'lorenz': lorenz,
   'rossler': rossler,
}

__all__ = ['equations'] + equations.keys()

