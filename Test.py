import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# randomly generate our initial seeds with a skewness to 0
A = np.random.choice([1,0], (200,200), p = [0.4, 0.6])


# implement conway's rule at here
def generation(A):
    # instead of brute force I used vectorization to compute the surrounding life
    N= np.pad(A[:-1, :-1], ((1, 0), (1, 0))) + \
       np.pad(A[:-1, 0:], ((1, 0), (0, 0))) + \
       np.pad(A[:-1, 1:], ((1, 0), (0, 1))) + \
       np.pad(A[0:, :-1], ((0, 0), (1, 0))) + \
       np.pad(A[0:, 1:], ((0, 0), (0, 1))) + \
       np.pad(A[1:, :-1], ((0, 1), (1, 0))) + \
       np.pad(A[1:, 0:], ((0, 1), (0, 0))) + \
       np.pad(A[1:, 1:], ((0, 1), (0, 1)))
    # conway's rule are following:
    # 1.A live cell dies when there are <2 or >3 alive cells nearby
    # 2.A live cell survives when there are 2~3 alive cells nearby
    # 3.A new cell is born if there are exactly 3 alive cells nearby and the block is empty
    birth = (N == 3) & (A == 0)
    survive = ((N == 2) |(N == 3)) & (A == 1)
    A[...] = 0
    A[birth | survive] = 1
    return A

# plot and animate the matrix
def animate(i):
    generation(A)
    mat.set_data(A)
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(A)
ani = animation.FuncAnimation(fig, animate, interval = 50)
plt.show()