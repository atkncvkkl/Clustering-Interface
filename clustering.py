# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:05:10 2022

@author: atknc
"""


from PyQt5 import QtWidgets
from sklearn.cluster import KMeans,AffinityPropagation,MeanShift,SpectralClustering,AgglomerativeClustering,DBSCAN
from operationclass import calculation_operations
from Show_Output import Show_text


class clustering_op(calculation_operations,Show_text):
    
    
    """In this class clustering operations were done with taken parameters from user. For parameters QInputdialog was used"""
    
    
    def k_means(self):
        
        self.n_cluster, done1 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter n_clusters:')

        init = ['k-means++','random']
        self.initv , done2 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'Enter init:',init) 
        
        self.max_iters, done3 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter max_iter:')
        
        algorithm =['auto','full','elkan']
        self.alg, done4 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'enter algortihm:', algorithm)
                
        
        
        if done1 and done2 and done3 and done4 :

            
            self.kmeans = KMeans(self.n_cluster,init=self.initv,n_init=10,max_iter=self.max_iters,algorithm=self.alg) 
            self.pred = self.kmeans.fit_predict(self.points)
            self.center = self.kmeans.cluster_centers_
            self.labels = self.kmeans.labels_
            
            self.find_clusters()
            self.find_center_nodes()
            self.find_farhest()   
            self.find_pairs()
            self.obj_func()
            
            self.show_output_on_graph()
            self.show_output_on_text()
            
    def aff_prop(self):
        
        
        self.damping , done2 = QtWidgets.QInputDialog.getDouble(self, 'Input Dialog', 'Enter damping:')
        
        self.max_iters , done3 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter max_iter:')
        
        affinities = ["euclidean", "precomputed"]
        self.affiniti, done4 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'enter affinity type:', affinities)
        
        self.random_s , done5 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter randomstate:')

        
        if done2 and done3 and done4 and done5: 
            
            self.afprop = AffinityPropagation(damping=self.damping,max_iter=self.max_iters,affinity=self.affiniti)
            self.pred = self.afprop.fit_predict(self.points)
            self.n_cluster = max(self.pred)+1
            self.labels = self.afprop.predict(self.points)
            self.center = self.afprop.cluster_centers_

            
            self.find_clusters()
            self.find_center_nodes()
            self.find_farhest()
            self.find_pairs()
            self.obj_func()
            
            
            self.show_output_on_graph()
            self.show_output_on_text()

    def mean_shift(self):
        

        
        self.max_iters, done3 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter max_iter:')
        
        self.cluster_alls, done2 = QtWidgets.QInputDialog.getText(self, 'Input Dialog', "Enter cluster all preference: True or False")

        if done2 and done3 :
            
            self.means = MeanShift( max_iter=self.max_iters, cluster_all=self.cluster_alls)
            self.pred = self.means.fit_predict(self.points)
            self.center = self.means.cluster_centers_
            self.labels = self.means.labels_
            self.n_cluster = max(self.labels)+1
        

            self.find_clusters()
            self.find_center_nodes()
            self.find_farhest()
            self.find_pairs()
            self.obj_func()
            
            self.show_output_on_graph()
            self.show_output_on_text()
            
    def spec_clustering(self):
        
        self.n_cluster , done1 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter n_clusters:')
        eigens = ["arpack", "lobpcg", "amg"]
        self.eigen_select , done2 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'enter affinity type:', eigens)
        
        if done1 and done2: 
            
            self.spec = SpectralClustering(n_clusters=self.n_cluster,eigen_solver=self.eigen_select,affinity='nearest_neighbors')
            self.pred = self.spec.fit_predict(self.points)
            self.labels = self.spec.labels_

            
            self.find_clusters()
            self.find_center_points()
            self.find_center_nodes()
            self.find_farhest()
            self.find_pairs()
            self.obj_func()
            
            self.show_output_on_graph()
            self.show_output_on_text()
    
    def hier_clustering(self): 
        
        self.n_cluster , done1 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter n_clusters:')
        
        linkages = ["ward", "complete" , "average", "single"]
        
        self.linkages_s , done2 = QtWidgets.QInputDialog.getItem(self, 'Input Dialog', 'enter linkage type:', linkages)
        
        if done1 and done2: 
            
            self.hier = AgglomerativeClustering(n_clusters= self.n_cluster, linkage=self.linkages_s)
            self.pred = self.hier.fit_predict(self.points)
            self.labels = self.hier.labels_
            
            
            self.find_clusters()
            self.find_center_points()
            self.find_center_nodes()
            self.find_farhest()
            self.find_pairs()
            self.obj_func()
            
            self.show_output_on_graph()
            self.show_output_on_text()
            
    def dbscan_clustering(self):
        
        self.epsilon , done1 = QtWidgets.QInputDialog.getDouble(self, 'Input Dialog', 'Enter eps value:')
        
        if done1:
            
            self.dbsc = DBSCAN(eps=self.epsilon)
            self.pred = self.dbsc.fit_predict(self.points)
            self.labels = self.dbsc.labels_
            self.n_cluster = max(self.labels)+1
            
            self.find_clusters()
            self.find_center_points()
            self.find_center_nodes()
            self.find_farhest()
            self.find_pairs()
            self.obj_func()
            
            self.show_output_on_graph()
            self.show_output_on_text()
            
            

    
        