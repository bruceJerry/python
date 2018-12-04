from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import *
import sys
from keras.utils import multi_gpu_model
import tensorflow
import numpy as np
from keras import backend as K

#  numpy, scipy, scikit-learn, pandas..  科学计算包
class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("水平布局")
        self.move(400, 300)
        self.resize(400, 300)
        pal = QPalette()
        pal.setColor(QPalette.ButtonText, Qt.red) #设置按键字体为红色


        print(K.epsilon())
        print(K.backend())
        print(K.floatx())

        """ 
        parallel_model = multi_gpu_model(model, gpus=8)
        parallel_model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

        # This `fit` call will be distributed on 8 GPUs.
        # Since the batch size is 256, each GPU will process 32 samples.
        parallel_model.fit(x, y, epochs=20, batch_size=256)
        """

        layout = QVBoxLayout()
        self.setLayout(layout)
        bt1 = QPushButton(str(1))
        bt2 = QPushButton(str(2))
        bt3 = QPushButton(str(3))
        bt4 = QPushButton(str(4))
        bt5 = QPushButton(str(5))
        layout.addStretch(3)
        layout.addWidget(bt1, 0, Qt.AlignTop)
        layout.addStretch(1)
        layout.addWidget(bt2, 0, Qt.AlignLeft | Qt.AlignTop)
        layout.addStretch(2)
        layout.addWidget(bt3, 0, Qt.AlignLeft | Qt.AlignBottom)
        layout.addStretch(1)
        layout.addWidget(bt4)
        layout.addStretch(1)
        layout.addWidget(bt5)
        layout.addStretch(3)
        bt1.setPalette(pal)
        bt1.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("44444444444444444444444")


app = QApplication(sys.argv)

a = np.array([[1, 2], [3, 4]])
sum0 = np.sum(a, axis=0)  # x
sum1 = np.sum(a, axis=1)  # y
print("sum_x = {}, sum_y = {}".format(sum0, sum1))

form = MyWindow()
form.show()
sys.exit(app.exec())