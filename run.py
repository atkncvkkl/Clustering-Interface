# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 09:13:01 2022

@author: atknc
"""

from PyQt5.QtWidgets import QApplication
import sys
from proje_son import UI


"To run application in one simple code"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

