from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from ui import Ui_MainWindow
from PIL import Image,ImageFilter,ImageEnhance
import os

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir=""
        self.ui.btn_dir.clicked.connect(self.open)
        self.filename = None
        self.photo = None
        self.save_dir = "changed"
        self.ui.list_files.itemClicked.connect(self.showchosenimage)
        self.ui.btn_bw.clicked.connect(self.do_bw)
        self.ui.btn_blur.clicked.connect(self.do_blur)
        self.ui.btn_left.clicked.connect(self.do_right)
        self.ui.btn_right.clicked.connect(self.do_left)
        self.ui.miror_1.clicked.connect(self.do_mirror)
        self.ui.btn_kontrast.clicked.connect(self.do_contrast)
        self.ui.btn_1.clicked.connect(self.do_mirror_tb)
        self.ui.btn_2.clicked.connect(self.do_diagonal)

    def loadimage(self,filename):
        try:
            self.filename = filename
            path = os.path.join(self.workdir,self.filename)
            self.photo = Image.open(path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()
    def do_bw(self):
        try: 
            self.photo = self.photo.convert("L")
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()

    def do_blur(self):
        try:    
            self.photo = self.photo.filter(ImageFilter.BLUR)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()

    def do_mirror(self):
        try:    
            self.photo = self.photo.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()


    def do_contrast(self):
        try:    
            self.photo = ImageEnhance.Contrast(self.photo).enhance(1.5)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()



    def do_left(self):
        try:    
            self.photo = self.photo.transpose(Image.ROTATE_90)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()

    def do_mirror_tb(self):
        try:    
            self.photo = self.photo.transpose(Image.FLIP_TOP_BOTTOM)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()

    def do_diagonal(self):
        try:    
            self.photo = self.photo.rotate(45)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()

    def do_right(self):
        try:    
            self.photo = self.photo.transpose(Image.ROTATE_270)
            self.saveimage()
            image_path = os.path.join(self.workdir,self.save_dir,self.filename)
            self.showImage(image_path)
        except:
            win=QtWidgets.QMessageBox()
            win.setText("Не вдалося відкрити зображення!")
            win.exec()

    def saveimage(self):
        path = os.path.join(self.workdir,self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        new_path = os.path.join(path,self.filename)
        self.photo.save(new_path)


    def showImage(self,path):
        self.ui.image.hide()
        pix = QtGui.QPixmap(path)
        w,h = self.ui.image.width(), self.ui.image.height()
        pix = pix.scaled(w,h,QtCore.Qt.KeepAspectRatio)
        self.ui.image.setPixmap(pix)
        self.ui.image.show()


    def showchosenimage(self):
        if self.ui.list_files.selectedItems():
            filename = self.ui.list_files.selectedItems()[0].text()
            self.loadimage(filename)
            path = os.path.join(self.workdir,filename)
            self.showImage(path)
    
    
    
    def open(self):
        try:
            self.workdir=QtWidgets.QFileDialog.getExistingDirectory()
            print(self.workdir)
            files=os.listdir(self.workdir)
            files_new=self.sort_files(files)
            self.ui.list_files.clear()
            for file in files_new:
                self.ui.list_files.addItem(file)
        except:
                alert=QtWidgets.QMessageBox()
                alert.setText("Шлях до папки не вибрано!")
                alert.exec()
    def sort_files(self,files):
        extentions=[".jpg",".bmp",".png",".jpeg"]
        result=[]
        for file in files:
            for ex in extentions:
                if file.endswith(ex):
                    result.append(file)
        return result





app=QtWidgets.QApplication([])
ex=ImageEditor()
ex.show()
app.exec()
