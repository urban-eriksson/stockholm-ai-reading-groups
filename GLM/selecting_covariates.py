import numpy as np
from sklearn.linear_model import LinearRegression

# For creating some random data instead of hand crafting
# The size of the data is not relevant as long as it is unique
# and larger than two in the first case and one in the second case
N = 100

# 1) Classical confounding
print(f"""
*** Classical confounding example ***
Linear regression without the confounding variable included gives 
the wrong coefficient for identifying the causal effect of X1 (set
to 2 in this example)
""")
X2 = np.random.random((N,1))
X1 = np.random.random((N,1)) + 0.1 * X2 
Y = 2 * X1 + 3 * X2
regression1 = LinearRegression().fit(X1, Y)
regression2 = LinearRegression().fit(np.column_stack((X1, X2)), Y)
print(f"Using X1 only   => X1 coefficient = {regression1.coef_[0][0]:g}")
print(f"Using X1 and X2 => X1 coefficient = {regression2.coef_[0][0]:g}")

# 2) Collider bias
print(f"""
*** Collider bias example ***
Linear regression with the collider variable included gives
the wrong coefficient for identifying the causal effect of X1 (set
to two in this example)
""")
X1 = np.random.random((N,1)) 
Y = 2 * X1
X2 = X1 + Y 
regression1 = LinearRegression().fit(X1, Y)
regression2 = LinearRegression().fit(np.column_stack((X1, X2)), Y)
print(f"Using X1 only   => X1 coefficient = {regression1.coef_[0][0]:g}")
print(f"Using X1 and X2 => X1 coefficient = {regression2.coef_[0][0]:g}")




