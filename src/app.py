"""
Image Acquisition for Intrinsic Calibration

Author: Jaimen Aza
Email: userjjat00@gmail.com

"""

from PySide2 import QtWidgets
import sys
import os


"""
Directories app
"""
dirs = ['views', 'views/styles', 'controllers', 'acquisition']


"""
Add directories to path
"""
for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)


""" 
Add controller to main widget and run QApplication
"""
from MainControllerIntrisicAcqWidget import MainControllerIntrisicAcqWidget
from IntrinsicAcquisitionWidget import IntrinsicAcquisitionWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    intrinsicAcquisitionWidget = IntrinsicAcquisitionWidget()
    MainControllerIntrisicAcqWidget(intrinsicAcquisitionWidget)
