from fbm2d import FBM2D
import matplotlib.pyplot as plt


#iniate fbm2d simulator with :
#    H=1/3 (Hurst Index)
#    N=2**10 ( size of generated field = (N x N) )
#    L=20 (Number of oneD fbm's used in construction)
a = FBM2D(H=1/3,N=2**10,L=20) 

field = a.fbs() #generate one field

plt.imshow(field,origin='lower')
plt.show()
