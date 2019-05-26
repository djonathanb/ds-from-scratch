from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def decile(grade): return grade // 10 * 10


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(decile(grade) for grade in grades)

bar_width = 8
plt.bar(histogram.keys(), histogram.values(), bar_width)

# x start, x end, y start, y end
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel('Decile')
plt.ylabel('# of Students')
plt.title('Distribution of Exam 1 Grades')

plt.show()
