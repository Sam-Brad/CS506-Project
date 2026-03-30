import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
future_players = [[200], [300], [400]]
predicted_ratings = model.predict(future_players)

print(predicted_ratings)

x_range = np.linspace(data["players"].min(), data["players"].max(), 100).reshape(-1,1)
y_range = model.predict(x_range)

plt.scatter(data["players"], data["recent_rating"], label="Data")
plt.plot(x_range, y_range, label="Trend")

plt.xlabel("Player Count")
plt.ylabel("Rating (%)")
plt.legend()
plt.show()