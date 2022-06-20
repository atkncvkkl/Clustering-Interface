# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:51:03 2022

@author: atknc
"""

from PyQt5 import  QtGui
import pyqtgraph as pg
import pyqtgraph.exporters


class Show_text:
    
    """This class include functions for showing the output on interface. Both plot operations and writing information to text, were done here.
    For plotting operations PlotWidget used. Also text browser was used for info panel."""
    
    
    def show_output_on_graph(self):
        
        self.graph.clear()
        
        colors = [pg.intColor(i, self.n_cluster, alpha=150) for i in self.pred]
        pens = [QtGui.QPen(pg.intColor(i, self.n_cluster), 0) for i in self.pred]
        self.graph.scatterPlot(self.points, pen=pens, symbolBrush=colors)
        self.graph.scatterPlot(self.center,pen=None, color = 'r', symbol=  'x', s=60)
    
    def show_output_on_text(self):
        
        self.T_Output.setText("there are " + str(self.n_cluster) + " clusters")
        self.T_Output.append("clustering labels: ")
        self.T_Output.append(str(self.labels))

        
        for i in range(self.n_cluster):
            self.T_Output.append("cluster " + str(i) +" ----" + str(self.clusters[i]))
            
        self.T_Output.append("cluster center nodes ---" + str(self.center_nodes_final))
        
        for i in range(self.n_cluster):
            self.T_Output.append("farhest hub distances : " + str(self.center_nodes_final[i]) + "----" + str(self.farhest[self.center_nodes_final[i]]))
        

        self.T_Output.append("All Possible pairs : ------> "+str(self.possible_pairs))
        
        self.T_Output.append("Pair Objectives : ----->"+str(self.obj_list))
        
        self.T_Output.append("Objective Function : "+str(max(self.obj_list)))
        
            
        
