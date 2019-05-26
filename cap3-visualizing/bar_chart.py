import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

x = range(5)

plt.bar(x, num_oscars)

plt.ylabel('# of Academy Awards')
plt.title('My Favorite Movies')

plt.xticks(x, movies)

plt.show()
