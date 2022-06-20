# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:12:19 2022

@author: atknc
"""

import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt5.QtWidgets import QFileDialog,QMessageBox



class File_Menu:
    
    """This class were used for file menu where we can open,save,export and manuel solution."""
    
    def open_data(self):
        

        fname = QFileDialog.getOpenFileName(self,"Open File", "c:\Desktop", "Text Files (*.txt)")
        self.points = np.loadtxt(fname[0])
        self.graph.plot(self.points, pen = None, symbol = 'o') 
        self.graph.saveState()
        
        
        
        """This part used to enable all disabled buttons when file opened and plotted on graph."""
        
        self.G_box_initial.setEnabled(True)
        self.G_box_clustering.setEnabled(True)
        self.G_box_heuristics.setEnabled(True)
        self.kmeans_push.setEnabled(True)
        self.export_initial_push.setEnabled(True)
        self.M_Clustering.setEnabled(True)
        self.M_Heuristic.setEnabled(True)
        self.M_Edit.setEnabled(True)

        
        
        
    def export_inital_as_png(self, event):
        
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","All Files (*)")
        exporter = pg.exporters.ImageExporter(self.graph.plotItem)
        exporter.export(fileName+'.jpg')
        
    def save_initial_as_txt(self):
        
        ref_list = []

        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","All Files (*)")
        for i in range(self.n_cluster):
            ref_list.append(self.clusters[i])
            ref_list[i].remove(self.center_nodes_final[i])
        

        ref_list.append(self.center_nodes_final)
        
        arr = np.array(ref_list)
        
        np.savetxt(fileName+".txt", arr, fmt='%s')
        
    def save_final_as_txt(self):
        
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","All Files (*)")
        ref_list = []

        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","All Files (*)")
        for i in range(self.n_cluster):
            ref_list.append(self.clusters[i])
            ref_list[i].remove(self.center_nodes_final[i])
            
        arr = np.array(ref_list)
        
        np.savetxt(fileName, arr)
        

        
    def export_final_as_png(self):
        
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Image","H:\Image","All Files (*)")
        exporter = pg.exporters.ImageExporter(self.graph2.plotItem)
        exporter.export(fileName+'.png')

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def saveEvent(self, event):
        
        reply = QMessageBox.question(self, 'Save', 'Are you sure you want to save?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
        
    def data_manuel(self):
        

        points_str = self.T_points_fromtext.toPlainText()
        
        ref_list = points_str.split()
        k = 0 
        
        arr = np.zeros((len(ref_list)//2,2))
        
        for i in range(len(ref_list)//2):
            for j in range(2):
                arr[i][j] = ref_list[k]
                k +=1
        
        self.points = arr
        
        
        self.graph.plot(self.points, pen = None, symbol = 'o') 
        self.graph.saveState()
        
        
        """This part used to enable all disabled buttons when file opened and plotted on graph."""
                
        self.G_box_initial.setEnabled(True)
        self.G_box_clustering.setEnabled(True)
        self.G_box_heuristics.setEnabled(True)
        self.kmeans_push.setEnabled(True)
        self.export_initial_push.setEnabled(True)
        self.M_Clustering.setEnabled(True)
        self.M_Heuristic.setEnabled(True)
        self.M_Edit.setEnabled(True)
        self.A_Save_Initial_Soultion(True)
        self.A_Save_Final_Solution(True)
        self.A_Export_Initial_Soultion(True)
        self.A_Export_Final_Soultion(True)