import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")

##First: Raw Scatterplot
for game in data["game"].unique():
    subset = data[data["game"] == game]
    plt.scatter(subset["players"], subset["recent_rating"], label=game)

plt.xlabel("Player Count")
plt.ylabel("Rating (%)")
plt.legend()
plt.title("Player Count vs Rating")
plt.show()

##Second: Linear Regression 

X = data[["players"]]
y = data["recent_rating"]

model = LinearRegression()
model.fit(X, y)

#Predict rating for new player counts
future_players =  pd.DataFrame({"players":[25000, 50000, 100000, 150000, 200000]})
predicted_ratings = model.predict(future_players)

print(predicted_ratings)

for game in data["game"].unique():
    subset = data[data["game"] == game]
    plt.scatter(subset["players"], subset["recent_rating"], label=game)

#Get range of player count
x_range = np.linspace(
    data["players"].min(),
    data["players"].max(),
    100
)

#Convert to frame
x_range_df = pd.DataFrame({"players": x_range})

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(data[["players"]])

model.fit(X_poly, data["recent_rating"])

y_range = model.predict(poly.transform(x_range_df))

#Plot regression line
plt.plot(x_range, y_range, label="Regression Line")

plt.xlabel("Player Count")
plt.ylabel("Rating (%)")
plt.title("Player Count vs Rating")
plt.legend()
plt.show()

##Third: Linear Regression of Rating Difference

data["rating_diff"] = data["recent_rating"] - data["total_rating"]

# --- Plot scatter by game ---
for game in data["game"].unique():
    subset = data[data["game"] == game]
    plt.scatter(subset["players"], subset["rating_diff"], label=game, alpha=0.7)

# --- Prepare model ---
X = data[["players"]]
y = data["rating_diff"]

# Polynomial transformation
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)

# --- Create smooth prediction line ---
x_range = np.linspace(
    data["players"].min(),
    data["players"].max(),
    100
)

x_range_df = pd.DataFrame({"players": x_range})
x_range_poly = poly.transform(x_range_df)

y_range = model.predict(x_range_poly)

# --- Plot regression line ---
plt.plot(x_range, y_range, linewidth=2, color="black", label="Trend")

# Zero reference line
plt.axhline(0, linestyle="dashed")

# Labels
plt.xlabel("Player Count")
plt.ylabel("Recent - Total Rating (%)")
plt.title("Player Count vs Rating Shift")

plt.legend()
plt.show()