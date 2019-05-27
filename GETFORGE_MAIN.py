from getforgeui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
import urllib.request
import re

class WIN( Ui_MainWindow,QtWidgets.QMainWindow ):
    text = ''
    ForgeVersion = ''
    def __init__( self ):
        super(WIN,self).__init__()
        self.setupUi( self )
        self.text = ''
        self.ButtonSolve()
        #self.textBrowser.append("1." "<a href='#'>https://files.minecraftforge.net/maven/net/minecraftforge/f""orge/1.12.2-14.23.5.2838/forge-1.12.2-14.23.5.2838-installer-win.exe</a><br>" )

    def ButtonSolve(self):
        self.pushButton.clicked.connect(self.Get)
        self.pushButton_2.clicked.connect(self.Dowload_Laster)

    
    def Dowload_Laster(self):
        print ('sad')

    def Get(self):
        self.text = self.comboBox.currentIndex()


        for i in self.lineEdit.text():
            if i.isalpha() == True:
                reply = QtWidgets.QMessageBox.question(self,'请输入数字！', '请输入数字！',
                                               QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes )
            else:
                self.ForgeVersion = self.lineEdit.text()

        if self.text == 0:  #.exe
            self.SELECT('exe')
        elif self.text == 1:#.zip
            self.SELECT('zip')
        elif self.text == 2:#.jar
            self.SELECT('jar')


    def SELECT(self,FILETYPE):

        self.URL = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_' + self.ForgeVersion + '.html'
        print (self.URL)
        print ( FILETYPE )
        print ( self.ForgeVersion )
        
        try:
            respond = urllib.request.urlopen( self.URL )
            websiteInfo = respond.read().decode('utf-8')
            SelRuler = r"https*://file.*" + FILETYPE  # 筛选规则
            ob = re.compile(SelRuler)
            ForgeAddressList = ob.findall(websiteInfo)


            print(ForgeAddressList[0])
            ForgeAddressList = sorted(ForgeAddressList)
        
            count = 1
            for i in ForgeAddressList:
                self.textBrowser.append( str( count ) + '.' + '<a href =' + i + ">" + i + "</a>" + '<br>' )
                count += 1
        except:
            QtWidgets.QMessageBox.question(self,'警告!','版本输入有误！',
                                   QtWidgets.QMessageBox.Yes |
                                   QtWidgets.QMessageBox.No ,
                                   QtWidgets.QMessageBox.Yes)

if __name__ == "__main__":
    app = QtWidgets.QApplication( sys.argv )
    window = WIN()
    window.show()
    sys.exit( app.exec_() )
