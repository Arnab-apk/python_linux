"""Question 12(A)
Plot the curves O(n) and O(n^2).
"""

try:
	import matplotlib.pyplot as plt
except ImportError:
	print("matplotlib is not installed. Install it using: pip install matplotlib")
	raise SystemExit(1)

n = list(range(1, 101))
linear = n
quadratic = [x * x for x in n]

plt.plot(n, linear, label="O(n)")
plt.plot(n, quadratic, label="O(n^2)")
plt.xlabel("n")
plt.ylabel("Complexity")
plt.title("O(n) vs O(n^2)")
plt.legend()
plt.grid(True)
plt.show()
