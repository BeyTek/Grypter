from typing import Match
from PySide2 import QtWidgets,QtGui,QtCore
from cryptosteganography import CryptoSteganography
from secure_delete import secure_delete
from PIL import Image
import glob, os
import numpy as np
import shutil
import uuid

home =os.environ["HOMEPATH"]
directory = "Grypter"
parent_dir = home +"/Desktop"
path = os.path.join(parent_dir, directory) 
unique_filename = str(uuid.uuid4())


def generate_random_image(width=58, height=58):
    data=np.random.randint(low=0,high=256,size=128*128*3, dtype=np.uint8)
    data=data.reshape(128,128,3)
    Image.fromarray(data,'RGB').save("base.jpg")



class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
      
            
        
    def setup_ui(self):
        self.create_Widgets()
        self.create_systray()
        self.modify_widgets()
        self.create_layouts()    
        self.add_widgets_layouts()
        self.setup_connexions()
        self.te_contenu.toPlainText()
        self.setup_css()
        self.imp_pass.text()
        self.imp_pass.setPlaceholderText("Password")
        self.te_contenu.setPlaceholderText("Message")
    
    def create_Widgets(self):
        self.btn_enc =QtWidgets.QPushButton("Encrypt")
        self.btn_dec =QtWidgets.QPushButton("Decrypt")
        self.te_contenu =QtWidgets.QTextEdit()
        self.imp_pass =QtWidgets.QLineEdit()
        self.imp_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_quit =QtWidgets.QPushButton('Quit')
        self.btn_mini =QtWidgets.QPushButton("Hide")
        self.btn_clean =QtWidgets.QPushButton('Clean')
        
    
    def create_systray(self):
        self.tray =QtWidgets.QSystemTrayIcon()
        icon_path ="C:\\Grypter\\icon.ico"
        self.tray.setIcon(QtGui.QIcon(icon_path))
        self.tray.setVisible(True)
    
    def tray_icon_click(self):
        if self.isHidden():
            self.showNormal()
        else:
            self.hide()
    
    def modify_widgets(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.86)
        
        radius = 60

        
        self.setStyleSheet( """
        background-color: rgb(38, 38, 38);
        color:  rgb(38, 38, 38);
        border-top-left-radius:{0}px;
        border-bottom-left-radius:{0}px;
        border-top-right-radius:{0}px;
        border-bottom-right-radius:{0}px;                 
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                    """.format(radius) 
            )
    
    def setup_css(self):

        
        self.btn_enc.setStyleSheet( """
        background-color: #1a1a1a;
        color: rgb(1, 255, 98);
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
            
                        """)
                        
        self.btn_dec.setStyleSheet( """
        background-color: #1a1a1a;
        color: rgb(0, 147, 255);
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                 """)
    
        self.te_contenu.setStyleSheet( """
        background-color: #1a1a1a;
        color: beige;
        border-style: outset;
        border-width: 20px;
        border-radius: 90px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)  
        self.btn_mini.setStyleSheet( """
        background-color: #1a1a1a;
        color: yellow;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)
        self.btn_quit.setStyleSheet( """
        background-color: #1a1a1a;
        color: red;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)    
        self.imp_pass.setStyleSheet( """
        background-color: #1a1a1a;
        color: beige;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)    
        self.btn_clean.setStyleSheet( """
        background-color: #1a1a1a;
        color: beige;
        border-style: outset;
        border-width: 5px;
        border-radius: 10px;
        border-color: #1a1a1a;
        font: bold 14px;
        min-width: 2em;
        padding: 6px;
                          """)    
    
   
    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)
     
    
    def  add_widgets_layouts(self): 
        self.main_layout.addWidget(self.btn_enc,0,1,1,1)
        self.main_layout.addWidget(self.btn_dec,0,3,1,1)
        self.main_layout.addWidget(self.te_contenu,1,1,1,3)
        self.main_layout.addWidget(self.imp_pass,0,2,1,1)
        self.main_layout.addWidget(self.btn_quit,3,1,1,1)
        self.main_layout.addWidget(self.btn_mini,3,3,1,1)
        self.main_layout.addWidget(self.btn_clean,3,2,1,1)
        
        
    
    def  setup_connexions(self):
        self.btn_enc.clicked.connect(self.bouton_enc_clic)  
        self.btn_dec.clicked.connect(self.bouton_dec_clic)
        self.tray.activated.connect(self.tray_icon_click)
        self.btn_quit.clicked.connect(self.close)
        self.btn_mini.clicked.connect(self.tray_icon_click)
        self.btn_clean.clicked.connect(self.bouton_clean)
        

    
    def bouton_clean(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("succes!")
        secure_delete.secure_delete('file.png')
        for n,file in enumerate(home+"\\Downloads\\Telegram Desktop\\"):
            os.remove(file, f'*.png')
            
        secure_delete.secure_delete(home + "\\Desktop\\Grypter")
        secure_delete.secure_delete('file.png')
        secure_delete.secure_delete('base.jpg')
        self.te_contenu.clear()
        self.imp_pass.clear()
        message_box.setText('Folders And Pictures Cleaned!')
        message_box.exec_()
    
    def bouton_enc_clic(self):
        
        try:
            os.mkdir(path)
        except OSError:
            print ("directory %s already exist" % path)
        else:
            print ("Successfully created the directory %s " % path)
                
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("succes!")
        
        mdp_in_box = self.imp_pass.text()
        msg_in_box = self.te_contenu.toPlainText()
        if not msg_in_box:
            aver_box = QtWidgets.QMessageBox()
            aver_box.setIcon(QtWidgets.QMessageBox.Warning)
            aver_box.setWindowTitle(" WARNING!")
            aver_box.setText("need message!")
            aver_box.exec_()
            return False
        if not mdp_in_box:
            aver_box = QtWidgets.QMessageBox()
            aver_box.setIcon(QtWidgets.QMessageBox.Warning)
            aver_box.setWindowTitle("WARNING!")
            aver_box.setText("need password!")
            aver_box.exec_()
            return False
        generate_random_image()
        mdp_sec = mdp_in_box
        msg_secret = msg_in_box
        crypto_steganography = CryptoSteganography(mdp_sec)
        crypto_steganography.hide('base.jpg',str(unique_filename +'.png'), msg_secret)
        src1_dir = "C:/Grypter/"
        dst1_dir = home+"/Desktop/Grypter/"
       
        secure_delete.secure_delete('base.jpg')
        for pngfile in glob.iglob(os.path.join(src1_dir, "*.png")):
            shutil.copy(pngfile,dst1_dir)
        for n,file in enumerate(glob.glob("*.png")):
            os.rename(file, f'file.png')
        self.imp_pass.clear()
        self.te_contenu.clear()
        secure_delete.secure_delete('file.png')
        secure_delete.secure_delete("*.png")
        message_box.setText('Message Encrypted!\nlook your Desktop, Grypter folder :)')
        message_box.exec_()
        

    
    def bouton_dec_clic(self):  # sourcery skip: remove-redundant-fstring
           
        try:
            os.mkdir(path)
        except OSError:
            print ("directory %s already exist" % path)
        else:
            print ("Successfully created the directory %s " % path) 
        mdp_in_box = self.imp_pass.text()
        src2_dir = home+"/Desktop/Grypter/"
        dst2_dir = "C:/Grypter/"       
        file_type = '\*png'
        files = glob.glob(src2_dir + file_type)
        
     
        max_file = max(files, key=os.path.getctime)
        if not max_file: 
            aver_box = QtWidgets.QMessageBox()
            aver_box.setIcon(QtWidgets.QMessageBox.Warning)
            aver_box.setWindowTitle("Warning!")
            aver_box.setText("The folder is empty!")
            aver_box.exec_()
            for n,file in enumerate(glob.glob("*.png")):
                os.rename(file, f'file.png')
            secure_delete.secure_delete('file.png') 
            return False
        
        shutil.copy(max_file,dst2_dir)
        for n,file in enumerate(glob.glob("*.png")):
                os.rename(file, f'file.png')
  
        secret = mdp_in_box
        if not mdp_in_box:
            aver_box = QtWidgets.QMessageBox()
            aver_box.setIcon(QtWidgets.QMessageBox.Warning)
            aver_box.setWindowTitle("WARNING!")
            aver_box.setText("need password!")
            aver_box.exec_()
            secure_delete.secure_delete('file.png')
            self.imp_pass.clear()
            return False
        
        crypto_steganography = CryptoSteganography(secret)
        secret = crypto_steganography.retrieve('file.png')  
        self.te_contenu.setText(secret)
        if  not secret:
            bdpw = QtWidgets.QMessageBox()
            bdpw.setIcon(QtWidgets.QMessageBox.Warning)
            bdpw.setWindowTitle("WARNING!")
            bdpw.setText("BAD password! for security all data wiped!")
            bdpw.exec_()
            secure_delete.secure_delete('file.png')
            secure_delete.secure_delete(home + "\\Desktop\\Grypter")
            self.imp_pass.clear()
            return False
        
        self.imp_pass.clear()
        secure_delete.secure_delete(home + "\\Desktop\\Grypter")
        secure_delete.secure_delete('file.png')
        
       
        
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)   

app = QtWidgets.QApplication([])
win = App()
win.show()
win.resize(380,380)
app.exec_()    