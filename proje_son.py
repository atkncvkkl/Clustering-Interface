# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:49:16 2022

@author: atknc
"""


from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QFileDialog,QMenu,QTextEdit ,QPushButton,QGraphicsView ,QWidget, QLabel, QMenuBar,QLineEdit,QTextBrowser,QGroupBox
from PyQt5 import uic
import sys
import pyqtgraph as pg
import pyqtgraph.exporters
from file_menu import File_Menu
from clustering import clustering_op
from Edit_Menu import editmenu


    
    
class UI(QMainWindow,File_Menu,clustering_op,editmenu):
    
        
    """This is the interface class that where we define all of the buttons,graphs,labels... Also size of graphs and interface were
    set here."""
    
    def __init__(self):
        super(UI, self).__init__()
        
        
        uic.loadUi("inputd.ui",self)

        self.resize(1100, 780)

        self.T_Output = self.findChild(QTextBrowser,"T_Output")
        self.G_view1 = self.findChild(QGraphicsView,"G_Initial")
        self.G_view2 = self.findChild(QGraphicsView,"G_Final")
        self.L_Output = self.findChild(QLabel, "L_Output")
        self.G_box_clustering = self.findChild(QGroupBox, "groupBox_2")
        self.G_box_heuristics = self.findChild(QGroupBox, "groupBox_3")
        self.G_box_final = self.findChild(QGroupBox, "groupBox_4")
        self.G_box_initial = self.findChild(QGroupBox, "groupBox_5")
        self.M_Clustering = self.findChild(QMenu, "menuClustering")
        self.M_Heuristic = self.findChild(QMenu, "menuHeuristics")
        self.M_Edit = self.findChild(QMenu, "menuEdit")
        self.A_Save_Initial_Soultion  =self.findChild(QAction, "actionSave_Initial_Soultion")
        self.A_Save_Final_Solution  =self.findChild(QAction, "actionSave_Final_Solution")
        self.A_Export_Initial_Soultion  =self.findChild(QAction, "actionExportInitialSolution")
        self.A_Export_Final_Soultion  =self.findChild(QAction, "actionExportFinal_Solution")
        self.L_n_cluster_fromtext = self.findChild(QLineEdit, "L_Clusters")
        self.T_points_fromtext = self.findChild(QTextEdit, "T_Points")
        
        self.B_run = self.findChild(QPushButton, "B_run")
        
        
        self.B_run.clicked.connect(self.data_manuel)
                
        self.opendata = self.findChild(QPushButton,"B_Open")
        self.save_initial_push = self.findChild(QPushButton,"B_Save_initial")
        self.save_final_push = self.findChild(QPushButton,"B_Save_final")
        self.export_initial_push = self.findChild(QPushButton,"B_Export_initial")
        self.export_final_push = self.findChild(QPushButton,"B_Export_Final")
        self.clear_initial_push = self.findChild(QPushButton,"B_Clear_inital")
        self.clear_final_push = self.findChild(QPushButton,"B_Clear_Final")
        
        
        self.kmeans_push = self.findChild(QPushButton,"B_Kmeans")
        self.affprop_push = self.findChild(QPushButton,"B_AffProp")
        self.meanshift_push = self.findChild(QPushButton,"B_MeanShift")
        self.spectral_push = self.findChild(QPushButton,"B_SpectralC")
        self.hierarcical_push = self.findChild(QPushButton,"B_Hierarcial")
        self.dbscan_push = self.findChild(QPushButton,"B_Dbscan")
        
        
        self.opendata.clicked.connect(self.open_data)
        self.save_initial_push.clicked.connect(self.save_initial_as_txt)
        self.save_final_push.clicked.connect(self.save_final_as_txt)
        self.export_initial_push.clicked.connect(self.export_inital_as_png)
        self.export_final_push.clicked.connect(self.export_final_as_png)
        
        self.clear_initial_push.clicked.connect(self.clear_initial)
        self.clear_final_push.clicked.connect(self.clear_final)
        
        self.kmeans_push.clicked.connect(self.k_means)
        self.affprop_push.clicked.connect(self.aff_prop)
        self.meanshift_push.clicked.connect(self.mean_shift)
        self.spectral_push.clicked.connect(self.spec_clustering)
        self.hierarcical_push.clicked.connect(self.hier_clustering)
        self.dbscan_push.clicked.connect(self.dbscan_clustering)
        

        self.graph = pg.PlotWidget(self.G_view1, background='w')
        self.graph.resize(400 ,310)
        self.graph.move(5,20)
        
        self.graph2 = pg.PlotWidget(self.G_view2, background='w')
        self.graph2.resize(360 ,310)
        self.graph2.move(5,20)
        
        

        self.show()
        

        
        

