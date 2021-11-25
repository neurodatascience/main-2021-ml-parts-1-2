import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Question: what is the issue in the code below?

# +
X, y = make_regression(n_samples=80, n_features=600, noise=10, random_state=0)

model = Ridge(alpha=1e-8)
model.fit(X, y)
predictions = model.predict(X)
mse = mean_squared_error(y, predictions)

print(f"\nMean Squared Error: {mse}")
print("MSE is 0 up to machine precision:", np.allclose(mse, 0))
# -

# Let's compare training and testing performance

# +
X, y = make_regression(n_samples=160, n_features=600, noise=10, random_state=0)
X_train, X_test = X[:80], X[80:]
y_train, y_test = y[:80], y[80:]

model = Ridge(alpha=1e-8)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"\nOn a separate test set:\nOut-of-sample Mean Squared Error: {mse}")
# -
