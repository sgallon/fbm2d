import numpy as np
from fbm import FBM
import math
import fortranfbm as f

class FBM2D:
    def __init__(self,H,N,L):
        """
        init of FBM2D
        
        parameters:
        H : Hurst index with 0 < H < 1
        N : number of observations along both dimensions, constructed field will contain (N x N) points
        L : number of one dimensional fbm used in construction of 2D Fields
        """
        if H <= 0 or  H >= 1:
            raise ValueError("Hurst parameter must be in interval (0, 1).")
        self.H = H
        self.N = N
        self.L = L
        self.fbb_gen = FBM(n=int(1.5*self.N), hurst=self.H, length=1.5) #init generator for fractional Brownian motion
    
    def fbs(self):
        """
        returnes fractional Brownian surface (scalar fractional Brownian motion) in 2D
        """
        #generate self.L bands with equidistant angles theta between band and x-axis
        theta_i = np.linspace(0,np.pi,self.L+1)[:-1] #angles
        oneDfbm = np.zeros((self.L,int(1.5*self.N)+1))    
        for i in range(self.L):
            fGn =  self.fbb_gen.fgn()
            oneDfbm[i,1:] = np.sqrt(np.sqrt(np.pi)*math.gamma(1+self.H)/math.gamma(1/2+self.H))* np.cumsum(fGn)
        
        # perform turbing band algortihm in fortran
        return f.turningband2d(oneDfbm,theta_i,self.N)
