# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:52:17 2022

@author: atknc
"""


import numpy as np
from scipy.spatial import distance
import itertools


class calculation_operations: 
    
    """This class include some functions to do calculations for clustering operations.The dictionaries were used in this class for better 
    understanding and documentation for info panel and console. Dictionaries are very useful with key indexing. For example to get pair of objectives, 
    the cluster center nodes will be needed. With key indexing this is easier to reach elements with nodes.
    """
    
    def find_clusters(self):
            
        
        """This function used for find clusters for necessary clustering operation. self.labels came from sklearn.clustering library
        """
        
        self.clusters = dict()
        
        
        for j in range (self.n_cluster):
            new_list = []
            for i in range (len(self.points)) :
                if self.labels[i] == j:
                    new_list.append(i)
                    self.clusters[j] = new_list
                    
                    
        print("there are ", self.n_cluster, " clusters")
        
        for i in range(self.n_cluster):
            print("cluster ", i," ----", self.clusters[i])
                
    def find_center_points(self):
        
        """This function is used for finding center points of clusters. np.mean was used"""
        
        
        self.center = dict()
        
        for i in range(self.n_cluster):
            denemelist = np.array(self.clusters[i])
            self.center[i]  = np.mean(self.points[denemelist])
                
    def find_center_nodes(self):
        
        """This function is used for finding center nodes of clusters. Firstly, found distance between cluster center point and all points
        belong to this cluster. After minimum value taken to find the center node of cluster. scipy library used to calculate distance between
        two points."""
        
        self.distances_center = dict()
        self.center_nodes_final = []
        
        for i in range(self.n_cluster):
            new_list = []
            denemelist = np.array(self.clusters[i])
            for j in range(len(denemelist)):
                dst_centers = distance.euclidean(self.points[denemelist[j]], self.center[i])
                new_list.append(dst_centers)
                self.distances_center[i] = new_list
                
            ref_list = self.clusters[i]
            center_nodes = (self.distances_center[i].index(min(self.distances_center[i])))
            self.center_nodes_final.append(ref_list[center_nodes])
            
        print("cluster center nodes ---" , self.center_nodes_final)
        
    def find_farhest(self):
        
        """This function used for finding farhest point of cluster. To get the farhest point, distances between cluster center nodes and
        nodes which are belong to this cluster. After maximum value taken to get farhest point of cluster. scipy library also used to
        calculate euclidiean distance between points."""
        
        self.distances = dict()
        self.farhest = dict()
        
        for i in range(self.n_cluster):
            new_list = []
            denemelist = np.array(self.clusters[i])
            for j in range(len(denemelist)):
                dst = distance.euclidean(self.points[denemelist[j]], self.points[self.center_nodes_final[i]])
                if dst != 0 or len(denemelist) == 1:
                    new_list.append(dst)
                    self.distances[i] = new_list
                    
        for i in range(self.n_cluster):
            self.farhest[self.center_nodes_final[i]] = max(self.distances[i])
            
        for i in range(self.n_cluster):
            print("farhest hub distances : " , self.center_nodes_final[i] , "----", self.farhest[self.center_nodes_final[i]])
    
    def find_pairs(self):
        
        """This function is used for all possible pairs for clustering operation. After founding the cluster center nodes, doing combination
        operation for these points. For this operation itertools library was used."""
        
        self.l = list(itertools.combinations(self.center_nodes_final, 2))
        self.possible_pairs = set(self.l)
        print(self.possible_pairs)
    
    def obj_func(self):
        
        """This function is used for calculating pair objectives. To do this calculation the formula that given were used and to find objective function,
        the maximum value were taken from pair objectives."""
        
        self.obj_list = []
        
        for i in range(len(self.l)):
            obj = self.farhest[self.l[i][0]]+self.farhest[self.l[i][1]]+0.75*distance.euclidean(self.points[self.l[i][0]],self.points[self.l[i][1]])
            self.obj_list.append(obj)
        
        x = max(self.farhest.values())
        
        self.obj_list.append(x)
        
        print("pair objectives : ")
        print(self.obj_list)
        print("objective function : " , max(self.obj_list))