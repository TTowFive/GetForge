import re
import sys
import threading
import time
import urllib.parse
import urllib.request as urlRe
import webbrowser as webbr

from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *

from getforgeui import *


class mainwin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        self.setupUi(self)
        self.button_connect()

    def button_connect(self):
        self.getBut.clicked.connect(self.getBut_button_event)
        self.downBut.clicked.connect(self.downBut_button_event)

    def getBut_button_event(self):
        self.disFrame.clear()
        self.selVersion = self.comboBox_1.currentText()
        self.selType = self.comboBox_2.currentText()

        self.depth = 0  # define the depth of get
        k = 0
        length = len(list(self.depthLine.text()))
        for i in list(self.depthLine.text()):
            self.depth += int(i) * (10**(length - k - 1))
            k += 1
        print(type(self.depth))

        # get the html depend on 'depth'
        self.forgeUrl = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_' + \
                        self.selVersion + '.html'
        print(self.forgeUrl)
        self.disFrame.append('Collectting from:<br>' + '<a href =' + \
                            self.forgeUrl + ">" + self.forgeUrl + "</a>" + \
                            '<br>')
        QMessageBox.information(self, 'Infomation', 'Find forge now...',
                                QMessageBox.Yes | QMessageBox.No)
        self.rootSiteResp = urlRe.urlopen(url=self.forgeUrl)

        with open("rootSiteResp.html", 'w') as file:
            html = ''
            while self.depth > 0:
                self.depth -= 1
                html = self.rootSiteResp.readline().decode('utf-8')
                file.write(html)
                if not html:
                    break

        print(self.selType)
        print(self.selVersion)

        with open('rootSiteResp.html', 'r') as file:
            html = file.read()

        SelRuler = r"https://files.minecraftforge.net/maven/net/minecraftforge/forge/.*" + self.selType  # 筛选规则
        print(SelRuler)
        ob = re.compile(SelRuler)
        self.ForgeAddressList = ob.findall(html)

        i = 1
        #print(self.ForgeAddressList[0])
        for addr in self.ForgeAddressList:
            self.disFrame.append(
                str(i) + ': <br>' + "<a href='" + addr + "'>" + addr + "</a>")
            i += 1

    def downBut_button_event(self):
        print('down')
        webbr.open(self.ForgeAddressList[0], new=0, autoraise=True)


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = mainwin()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
