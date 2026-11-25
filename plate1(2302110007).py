import numpy as np
from scipy.optimize import minimize_scalar

D, L, f = 50, 200, 0.25     # mm, mm, mm/rev
n, C = 0.25, 300            # Taylor constants
Cm, Ct, tc = 5, 100, 2      # Rs/min, Rs/edge, min

def cost(V):
    tm = np.pi * D * L / (1000 * V * f)   # machining time, min
    T = (C / V) ** (1 / n)                # tool life, min
    return Cm * tm + (Cm * tc + Ct) * tm / T

res = minimize_scalar(cost, bounds=(30, 290), method="bounded")
print("Optimum speed:", round(res.x, 1), "m/min")
print("Min cost per part: Rs", round(res.fun, 2))