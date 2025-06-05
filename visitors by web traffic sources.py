import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social_media = [70, 80, 90, 87, 92]

# Bar width and x-axis positions
x = np.arange(len(months))
bar_width = 0.25

# Create bars
plt.bar(x - bar_width, searches, width=bar_width, label='Searches', color='blue')
plt.bar(x, direct, width=bar_width, label='Direct', color='pink')
plt.bar(x + bar_width, social_media, width=bar_width, label='Social Media', color='orange')

# Labels and Title
plt.xlabel('months')
plt.ylabel('visitors in thousands')
plt.title('Visitors by web traffic sources')
plt.xticks(x, months)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()