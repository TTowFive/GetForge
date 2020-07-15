from getforgeui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
import urllib.request
import re

class WIN( Ui_MainWindow,QtWidgets.QMainWindow ):
    text = ''
    ForgeVersion = ''
    FILETYPE = ''
    Content = ['']# 用来储存网页信息等
    def __init__( self ):
        super(WIN,self).__init__()
        self.setupUi( self )
        self.text = ''
        self.ButtonSolve()
        self.NewestAddr = ''
        #self.textBrowser.append("1." "<a href='#'>https://files.minecraftforge.net/maven/net/minecraftforge/f""orge/1.12.2-14.23.5.2838/forge-1.12.2-14.23.5.2838-installer-win.exe</a><br>" )

    def ButtonSolve(self): #检查事件
        self.pushButton.clicked.connect(self.Get)
        self.pushButton_2.clicked.connect(self.Dowload_Laster)

    
    def Dowload_Laster(self):   #点击下载时的操作
        self.Content[0] = ''#初始化Content

        try:
            self.NewestAddr = self.ForgeAddressList[-1]
        except:
            print ("请先“获取”再点击下载")
            QtWidgets.QMessageBox.question(self, '警告!', '请先“获取”再点击下载',
                                           QtWidgets.QMessageBox.Yes |
                                           QtWidgets.QMessageBox.No,
                                           QtWidgets.QMessageBox.Yes)
            return 0;

        res = urllib.request.urlopen( self.NewestAddr )
        print ( self.NewestAddr )
        with open("Forge" + self.ForgeVersion + "." + self.FILETYPE, "wb") as file:
            QtWidgets.QMessageBox.question(self, '提示', '文件下载中...'
                                           , QtWidgets.QMessageBox.Yes |
                                           QtWidgets.QMessageBox.No,
                                           QtWidgets.QMessageBox.No)
            while True:
                theForgeData = res.readline()
                file.write(theForgeData)
                self.Content[0] += str(theForgeData)
                if not theForgeData:
                    break



        QtWidgets.QMessageBox.question(self,'提示','文件下载完毕'
                                       ,QtWidgets.QMessageBox.Yes |
                                       QtWidgets.QMessageBox.No,
                                       QtWidgets.QMessageBox.No)
        print('done')

    def Get(self):  #取得combobox的内容并判断
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


    def SELECT(self,FILETYPE):# 指定内容爬取
        self.FILETYPE = FILETYPE
        self.textBrowser.clear()

        self.URL = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_' + self.ForgeVersion + '.html'
        print (self.URL)
        print ( FILETYPE )
        print ( self.ForgeVersion )
        
        try:
            respond = urllib.request.urlopen( self.URL )
            #respond = urllib.request.urlopen( url=self.URL )

            QtWidgets.QMessageBox.question(self, '提示', '查找'+ self.ForgeVersion +'版本forge中...'
                                           , QtWidgets.QMessageBox.Yes |
                                           QtWidgets.QMessageBox.No,
                                           QtWidgets.QMessageBox.No)

            while True:#逐行取得网页内容
                websiteInfo = respond.readline().decode('utf-8')
                self.Content[0] += websiteInfo
                if not websiteInfo:#检查到文件尾时退出读取
                    break

            SelRuler = r"https*://file.*" + FILETYPE  # 筛选规则
            ob = re.compile(SelRuler)
            self.ForgeAddressList = ob.findall(self.Content[0])


            print(self.ForgeAddressList[0])
            ForgeAddressList = sorted(self.ForgeAddressList,reverse=True)
        
            count = 1
            for i in self.ForgeAddressList:
                self.textBrowser.append( str( count ) + '.' + '<a href =' + i + ">" + i + "</a>" + '<br>' )
                count += 1
        except:
            QtWidgets.QMessageBox.question(self,'警告!','版本输入有误或文件类型不存在，请选择其他类型',
                                   QtWidgets.QMessageBox.Yes |
                                   QtWidgets.QMessageBox.No ,
                                   QtWidgets.QMessageBox.Yes)

if __name__ == "__main__":
    app = QtWidgets.QApplication( sys.argv )
    window = WIN()
    window.show()
    sys.exit( app.exec_() )
