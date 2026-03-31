import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("data.csv")


for game in data["game"].unique():
    subset = data[data["game"] == game]
    plt.scatter(subset["players"], subset["recent_rating"], label=game)

plt.xlabel("Player Count")
plt.ylabel("Rating (%)")
plt.legend()
plt.title("Player Count vs Rating")
plt.show()



from sklearn.linear_model import LinearRegression

X = data[["players"]]
y = data["recent_rating"]

model = LinearRegression()
model.fit(X, y)

# Predict rating for new player counts
future_players =  pd.DataFrame({"players":[100000, 150000, 200000]})
predicted_ratings = model.predict(future_players)

print(predicted_ratings)

for game in data["game"].unique():
    subset = data[data["game"] == game]
    plt.scatter(subset["players"], subset["recent_rating"], label=game)

# Create a smooth range of player values
x_range = np.linspace(
    data["players"].min(),
    data["players"].max(),
    100
)

# Convert to DataFrame (IMPORTANT for sklearn warning fix)
x_range_df = pd.DataFrame({"players": x_range})

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(data[["players"]])

model.fit(X_poly, data["recent_rating"])

y_range = model.predict(poly.transform(x_range_df))

# Plot regression line
plt.plot(x_range, y_range, label="Regression Line")

plt.xlabel("Player Count")
plt.ylabel("Rating (%)")
plt.title("Player Count vs Rating")
plt.legend()

plt.show()
