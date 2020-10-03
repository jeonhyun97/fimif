import abc
import numpy as np
from scipy.spatial import ConvexHull, Delaunay
from qpsolvers import solve_qp


# Convex Hull Interface
class ConvexHullABC:

    __metaclass__ = abc.ABCMeta

    def __init__(self, data):
        self.data = np.array(data)     # initial data set
        self.size = len(data)
        self.dim  = len(data[0])
        self.hull = None       # final convex hull

    @abc.abstractmethod
    def __compute_convex_hull(self):
        pass

    ## INPUT  arbitrary point
    ## OUTPUT True if convex hull contains point. False if not
    @abc.abstractmethod
    def is_in_hull(self, points):
        pass


## NOTE Convex Hull implementation with scipy
## Quite Scalable for until... ( < 1 seconds in mac mini 2018)
## dimension: 5
## Convex hull candidate: 10000
## Convex hull test: 100000
class ConvexHullWithScipy(ConvexHullABC):
    def __init__(self, data):
        ConvexHullABC.__init__(self, data)
        self.__compute_convex_hull()

    def __compute_convex_hull(self):
        self.hull = ConvexHull(self.data)
        self.hull_vertices = self.hull.points[np.unique(self.hull.simplices)]
        hull_vertices = [self.data[i] for i in self.hull.vertices]
        self.delaunay = Delaunay(hull_vertices)
 
    def is_in_hull(self, points):
        return self.delaunay.find_simplex(points) >= 0


## NOTE Approximate Convex Hull implementation
## Assumes n dimension
## Based on "Conputing the approximate convex hull in high dimensions". Sartuouzadeh et al.
class ConvexHullApprox(ConvexHullABC):
    def __init__(self, data):
        ConvexHullABC.__init__(self, data)
        self.__compute_convex_hull()

    def __compute_convex_hull(self):
        z = np.random.rand(3)
        S = np.random.rand(30, 3)
        x = self.__distance_to__hull(z, S)
        print(x)
    
    # INPUT  z: target point (d), S: points set (n X d)
    # OUTPUT distance (the result of quadratic programming)
    def __distance_to__hull(self, z, S):
        
        S = np.array(S)
        z = np.array(z)
        n, d = S.shape

        P = np.dot(S, S.T)
        P += np.eye(P.shape[0]) * 0.0000000000001
        q = - np.dot(S, z).reshape((n,))
        A = np.ones(n)
        b = np.array([1.])
        lb = np.zeros(n)

       
        x = solve_qp(P=P, q=q, A=A, b=b, lb=lb)
        return x


        
    
    def is_in_hull(self, points):
        pass
