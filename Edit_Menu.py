# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 22:00:23 2022

@author: atknc
"""

from PyQt5.QtWidgets import QGraphicsView


class editmenu:
    
    """This class were used for edit menu."""
    
    def clear_initial(self):
        
        self.graph.clear()
        self.T_Output.clear()
        
    def clear_final(self):
        
        self.graph2.clear()
        self.T_Output.clear()