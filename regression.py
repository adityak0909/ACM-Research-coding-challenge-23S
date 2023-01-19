import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv('stars.csv')

X = df.drop(["Star type", "Star color", "Spectral Class"], axis=1)
Y = df["Star type"]

reg = linear_model.LinearRegression()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.75, random_state=1)
reg.fit(X_train, Y_train)
predictions = reg.predict(X_test)

print("Coefficients: ", reg.coef_)
print("Intercept: ", reg.intercept_)
print("Accuracy Score: ", r2_score(Y_test, predictions)*100)
