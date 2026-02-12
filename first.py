import matplotlib.pyplot as plt

price = [100, 200, 300, 400, 500, 600]
discount = [5, 10, 15, 20, 25, 30]

plt.scatter(price, discount)
plt.xlabel("Price")
plt.ylabel("Discount (%)")
plt.show()