from fbm2d import FBM2D
import matplotlib.pyplot as plt

a = FBM2D(H=1/3,N=2**10,L=20) 
field = a.fbs()

plt.imshow(field,origin='lower')
plt.show()

