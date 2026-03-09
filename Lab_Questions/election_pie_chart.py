"""Question 12(B)
Display India Election Results 2024 using a pie chart.
ABC: 160 seats, XYZ: 200 seats, MNP: 40 seats (out of 400).
"""

import matplotlib.pyplot as plt

parties = ["ABC", "XYZ", "MNP"]
seats = [160, 200, 40]
colors = ["#ff9999", "#66b3ff", "#99ff99"]

plt.pie(seats, labels=parties, autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("India Election Results 2024 (Total 400 Seats)")
plt.show()
