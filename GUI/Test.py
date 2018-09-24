# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StereoscopicConfiguration(object):
    def setupUi(self, StereoscopicConfiguration):
        StereoscopicConfiguration.setObjectName("StereoscopicConfiguration")
        StereoscopicConfiguration.resize(881, 472)
        self.formLayout = QtWidgets.QFormLayout(StereoscopicConfiguration)
        self.formLayout.setObjectName("formLayout")
        self.widget = QtWidgets.QWidget(StereoscopicConfiguration)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gBStereoscopyParams = QtWidgets.QGroupBox(self.widget)
        self.gBStereoscopyParams.setEnabled(True)
        self.gBStereoscopyParams.setObjectName("gBStereoscopyParams")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gBStereoscopyParams)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_StereoscopyOnOff = QtWidgets.QGroupBox(self.gBStereoscopyParams)
        self.gb_StereoscopyOnOff.setObjectName("gb_StereoscopyOnOff")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.gb_StereoscopyOnOff)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBoxStereoscopyOnOff = QtWidgets.QCheckBox(self.gb_StereoscopyOnOff)
        self.checkBoxStereoscopyOnOff.setObjectName("checkBoxStereoscopyOnOff")
        self.verticalLayout_9.addWidget(self.checkBoxStereoscopyOnOff)
        self.verticalLayout.addWidget(self.gb_StereoscopyOnOff)
        self.gbEyeSeparation = QtWidgets.QGroupBox(self.gBStereoscopyParams)
        self.gbEyeSeparation.setObjectName("gbEyeSeparation")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbEyeSeparation)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.doubleSBEyeSeparation = QtWidgets.QDoubleSpinBox(self.gbEyeSeparation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSBEyeSeparation.sizePolicy().hasHeightForWidth())
        self.doubleSBEyeSeparation.setSizePolicy(sizePolicy)
        self.doubleSBEyeSeparation.setDecimals(3)
        self.doubleSBEyeSeparation.setMinimum(-999999999999999.0)
        self.doubleSBEyeSeparation.setMaximum(999999999999999.0)
        self.doubleSBEyeSeparation.setObjectName("doubleSBEyeSeparation")
        self.horizontalLayout.addWidget(self.doubleSBEyeSeparation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblStepES = QtWidgets.QLabel(self.gbEyeSeparation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStepES.sizePolicy().hasHeightForWidth())
        self.lblStepES.setSizePolicy(sizePolicy)
        self.lblStepES.setObjectName("lblStepES")
        self.horizontalLayout.addWidget(self.lblStepES)
        self.doubleSBESStep = QtWidgets.QDoubleSpinBox(self.gbEyeSeparation)
        self.doubleSBESStep.setDecimals(3)
        self.doubleSBESStep.setSingleStep(1.0)
        self.doubleSBESStep.setProperty("value", 1.0)
        self.doubleSBESStep.setObjectName("doubleSBESStep")
        self.horizontalLayout.addWidget(self.doubleSBESStep)
        self.verticalLayout.addWidget(self.gbEyeSeparation)
        self.gbEyeSeparationDegreeOfAdjustment = QtWidgets.QGroupBox(self.gBStereoscopyParams)
        self.gbEyeSeparationDegreeOfAdjustment.setObjectName("gbEyeSeparationDegreeOfAdjustment")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.gbEyeSeparationDegreeOfAdjustment)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.doubleSBEyeSeparationDegreeOfAdjustment = QtWidgets.QDoubleSpinBox(self.gbEyeSeparationDegreeOfAdjustment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSBEyeSeparationDegreeOfAdjustment.sizePolicy().hasHeightForWidth())
        self.doubleSBEyeSeparationDegreeOfAdjustment.setSizePolicy(sizePolicy)
        self.doubleSBEyeSeparationDegreeOfAdjustment.setDecimals(3)
        self.doubleSBEyeSeparationDegreeOfAdjustment.setMinimum(-999999999999999.0)
        self.doubleSBEyeSeparationDegreeOfAdjustment.setMaximum(999999999999999.0)
        self.doubleSBEyeSeparationDegreeOfAdjustment.setObjectName("doubleSBEyeSeparationDegreeOfAdjustment")
        self.horizontalLayout_5.addWidget(self.doubleSBEyeSeparationDegreeOfAdjustment)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lblStepESDegree = QtWidgets.QLabel(self.gbEyeSeparationDegreeOfAdjustment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStepESDegree.sizePolicy().hasHeightForWidth())
        self.lblStepESDegree.setSizePolicy(sizePolicy)
        self.lblStepESDegree.setObjectName("lblStepESDegree")
        self.horizontalLayout_5.addWidget(self.lblStepESDegree)
        self.doubleSBESDegreeStep = QtWidgets.QDoubleSpinBox(self.gbEyeSeparationDegreeOfAdjustment)
        self.doubleSBESDegreeStep.setDecimals(3)
        self.doubleSBESDegreeStep.setProperty("value", 1.0)
        self.doubleSBESDegreeStep.setObjectName("doubleSBESDegreeStep")
        self.horizontalLayout_5.addWidget(self.doubleSBESDegreeStep)
        self.verticalLayout.addWidget(self.gbEyeSeparationDegreeOfAdjustment)
        self.gbFocalDistance = QtWidgets.QGroupBox(self.gBStereoscopyParams)
        self.gbFocalDistance.setObjectName("gbFocalDistance")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.gbFocalDistance)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.doubleSBFocalDistance = QtWidgets.QDoubleSpinBox(self.gbFocalDistance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSBFocalDistance.sizePolicy().hasHeightForWidth())
        self.doubleSBFocalDistance.setSizePolicy(sizePolicy)
        self.doubleSBFocalDistance.setDecimals(3)
        self.doubleSBFocalDistance.setMinimum(-999999999999999.0)
        self.doubleSBFocalDistance.setMaximum(999999999999999.0)
        self.doubleSBFocalDistance.setObjectName("doubleSBFocalDistance")
        self.horizontalLayout_6.addWidget(self.doubleSBFocalDistance)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.lblStepFD = QtWidgets.QLabel(self.gbFocalDistance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStepFD.sizePolicy().hasHeightForWidth())
        self.lblStepFD.setSizePolicy(sizePolicy)
        self.lblStepFD.setObjectName("lblStepFD")
        self.horizontalLayout_6.addWidget(self.lblStepFD)
        self.doubleSBFDStep = QtWidgets.QDoubleSpinBox(self.gbFocalDistance)
        self.doubleSBFDStep.setDecimals(3)
        self.doubleSBFDStep.setProperty("value", 1.0)
        self.doubleSBFDStep.setObjectName("doubleSBFDStep")
        self.horizontalLayout_6.addWidget(self.doubleSBFDStep)
        self.verticalLayout.addWidget(self.gbFocalDistance)
        self.gbFocalDistanceDegreeOfAdjustment = QtWidgets.QGroupBox(self.gBStereoscopyParams)
        self.gbFocalDistanceDegreeOfAdjustment.setObjectName("gbFocalDistanceDegreeOfAdjustment")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.gbFocalDistanceDegreeOfAdjustment)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.doubleSBFocalDistanceDegreeOfAdjustment = QtWidgets.QDoubleSpinBox(self.gbFocalDistanceDegreeOfAdjustment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSBFocalDistanceDegreeOfAdjustment.sizePolicy().hasHeightForWidth())
        self.doubleSBFocalDistanceDegreeOfAdjustment.setSizePolicy(sizePolicy)
        self.doubleSBFocalDistanceDegreeOfAdjustment.setDecimals(3)
        self.doubleSBFocalDistanceDegreeOfAdjustment.setMinimum(-999999999999999.0)
        self.doubleSBFocalDistanceDegreeOfAdjustment.setMaximum(999999999999999.0)
        self.doubleSBFocalDistanceDegreeOfAdjustment.setObjectName("doubleSBFocalDistanceDegreeOfAdjustment")
        self.horizontalLayout_7.addWidget(self.doubleSBFocalDistanceDegreeOfAdjustment)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.lblStepFDDegree = QtWidgets.QLabel(self.gbFocalDistanceDegreeOfAdjustment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStepFDDegree.sizePolicy().hasHeightForWidth())
        self.lblStepFDDegree.setSizePolicy(sizePolicy)
        self.lblStepFDDegree.setObjectName("lblStepFDDegree")
        self.horizontalLayout_7.addWidget(self.lblStepFDDegree)
        self.doubleSBFDDegreeStep = QtWidgets.QDoubleSpinBox(self.gbFocalDistanceDegreeOfAdjustment)
        self.doubleSBFDDegreeStep.setDecimals(3)
        self.doubleSBFDDegreeStep.setProperty("value", 1.0)
        self.doubleSBFDDegreeStep.setObjectName("doubleSBFDDegreeStep")
        self.horizontalLayout_7.addWidget(self.doubleSBFDDegreeStep)
        self.verticalLayout.addWidget(self.gbFocalDistanceDegreeOfAdjustment)
        self.gbGlobalFactor = QtWidgets.QGroupBox(self.gBStereoscopyParams)
        self.gbGlobalFactor.setObjectName("gbGlobalFactor")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbGlobalFactor)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        self.doubleSBCameraGlobalFactorStep = QtWidgets.QDoubleSpinBox(self.gbGlobalFactor)
        self.doubleSBCameraGlobalFactorStep.setDecimals(3)
        self.doubleSBCameraGlobalFactorStep.setProperty("value", 1.0)
        self.doubleSBCameraGlobalFactorStep.setObjectName("doubleSBCameraGlobalFactorStep")
        self.gridLayout_3.addWidget(self.doubleSBCameraGlobalFactorStep, 0, 3, 1, 1)
        self.lblGlobalFactorStep = QtWidgets.QLabel(self.gbGlobalFactor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblGlobalFactorStep.sizePolicy().hasHeightForWidth())
        self.lblGlobalFactorStep.setSizePolicy(sizePolicy)
        self.lblGlobalFactorStep.setObjectName("lblGlobalFactorStep")
        self.gridLayout_3.addWidget(self.lblGlobalFactorStep, 0, 2, 1, 1)
        self.doubleSPBCameraFactor = QtWidgets.QDoubleSpinBox(self.gbGlobalFactor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSPBCameraFactor.sizePolicy().hasHeightForWidth())
        self.doubleSPBCameraFactor.setSizePolicy(sizePolicy)
        self.doubleSPBCameraFactor.setDecimals(3)
        self.doubleSPBCameraFactor.setMinimum(-999999999999999.0)
        self.doubleSPBCameraFactor.setMaximum(999999999999999.0)
        self.doubleSPBCameraFactor.setProperty("value", 1.0)
        self.doubleSPBCameraFactor.setObjectName("doubleSPBCameraFactor")
        self.gridLayout_3.addWidget(self.doubleSPBCameraFactor, 0, 0, 1, 1)
        self.pbApplyFactor = QtWidgets.QPushButton(self.gbGlobalFactor)
        self.pbApplyFactor.setObjectName("pbApplyFactor")
        self.gridLayout_3.addWidget(self.pbApplyFactor, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.gbGlobalFactor)
        self.gridLayout_2.addWidget(self.gBStereoscopyParams, 1, 5, 1, 1)
        self.lblContext = QtWidgets.QLabel(self.widget)
        self.lblContext.setObjectName("lblContext")
        self.gridLayout_2.addWidget(self.lblContext, 0, 1, 1, 1)
        self.listViewCamera = QtWidgets.QListView(self.widget)
        self.listViewCamera.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewCamera.sizePolicy().hasHeightForWidth())
        self.listViewCamera.setSizePolicy(sizePolicy)
        self.listViewCamera.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewCamera.setObjectName("listViewCamera")
        self.gridLayout_2.addWidget(self.listViewCamera, 1, 2, 1, 1)
        self.listViewContext = QtWidgets.QListView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewContext.sizePolicy().hasHeightForWidth())
        self.listViewContext.setSizePolicy(sizePolicy)
        self.listViewContext.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewContext.setObjectName("listViewContext")
        self.gridLayout_2.addWidget(self.listViewContext, 1, 1, 1, 1)
        self.lblCamera = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCamera.sizePolicy().hasHeightForWidth())
        self.lblCamera.setSizePolicy(sizePolicy)
        self.lblCamera.setObjectName("lblCamera")
        self.gridLayout_2.addWidget(self.lblCamera, 0, 2, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.widget)

        self.retranslateUi(StereoscopicConfiguration)
        self.doubleSBCameraGlobalFactorStep.valueChanged['double'].connect(self.doubleSPBCameraFactor.setValue)
        QtCore.QMetaObject.connectSlotsByName(StereoscopicConfiguration)

    def retranslateUi(self, StereoscopicConfiguration):
        _translate = QtCore.QCoreApplication.translate
        self.gBStereoscopyParams.setTitle(_translate("StereoscopicConfiguration", "Stereoscopy Parameters"))
        self.gb_StereoscopyOnOff.setTitle(_translate("StereoscopicConfiguration", "Stereoscopy on/off"))
        self.checkBoxStereoscopyOnOff.setText(_translate("StereoscopicConfiguration", "Stereoscopy on/off"))
        self.gbEyeSeparation.setTitle(_translate("StereoscopicConfiguration", "Eye Separation"))
        self.lblStepES.setText(_translate("StereoscopicConfiguration", "Step"))
        self.gbEyeSeparationDegreeOfAdjustment.setTitle(_translate("StereoscopicConfiguration", "Eye Separation Degree Of Adjustment"))
        self.lblStepESDegree.setText(_translate("StereoscopicConfiguration", "Step"))
        self.gbFocalDistance.setTitle(_translate("StereoscopicConfiguration", "Focal Distance"))
        self.lblStepFD.setText(_translate("StereoscopicConfiguration", "Step"))
        self.gbFocalDistanceDegreeOfAdjustment.setTitle(_translate("StereoscopicConfiguration", "Focal Distance Degree Of Adjustment"))
        self.lblStepFDDegree.setText(_translate("StereoscopicConfiguration", "Step"))
        self.gbGlobalFactor.setTitle(_translate("StereoscopicConfiguration", "Factor"))
        self.lblGlobalFactorStep.setText(_translate("StereoscopicConfiguration", "Step"))
        self.pbApplyFactor.setText(_translate("StereoscopicConfiguration", "ApplyFactor"))
        self.lblContext.setText(_translate("StereoscopicConfiguration", "Context"))
        self.lblCamera.setText(_translate("StereoscopicConfiguration", "Camera"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StereoscopicConfiguration = QtWidgets.QWidget()
    ui = Ui_StereoscopicConfiguration()
    ui.setupUi(StereoscopicConfiguration)
    StereoscopicConfiguration.show()
    sys.exit(app.exec_())

