import matplotlib.pyplot as plt

x = [k for k in range(-6, 7)]
y = [k * k for k in x]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("x^2")
plt.title("Annotated Parabola")
plt.annotate(
    "Minimum at (0, 0)",
    xy=(0, 0),
    xytext=(1.5, 12),
    arrowprops=dict(arrowstyle="->"),
)
plt.show()