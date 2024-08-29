import numpy as np
import statsmodels.api as sm

np.random.seed(0)
t = np.arange(100)
y = 2 + 0.5 * t + np.random.normal(0, 1, size=t.shape)

X = sm.add_constant(t)

model = sm.OLS(y, X)
results = model.fit()

# PRINTING OF REGRESSION IN PYTHON
print(results.summary())
