import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

store_all = []

with open('1au1.pdb') as protein:
    for lines in protein:
        if lines.startswith("ATOM"):
            lines = lines.split()
            store_all.append(map(float, lines[6:9]))


x,y,z = zip(*store_all)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z, "o")
# ax.axis("Off")
plt.show()
