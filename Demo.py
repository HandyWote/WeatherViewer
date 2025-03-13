# coding:utf-8

import sys
import Weather
from PyQt5.QtWidgets import QApplication, QDialog
import requests


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Weather.Ui_Dialog()
        self.ui.setupUi(self)

    def queryWeather(self):
        cityName = self.ui.comboBox.currentText()
        cityCode = self.getCode(cityName)
        if cityCode == '-1':
            weatherMsg = '\t\t想不到吧\n\t我找不到免费的Api可以展示汕头天气\n\t\t   QAQ！'
        else:
            r = requests.get("http://t.weather.sojson.com/api/weather/city/{}".format(cityCode))

            if r.json().get('status') == 200:
                weatherMsg = '\t城市：{}\n\t日期：{}\n\t天气：{}\n\tPM 2.5：{} {}\n\t温度：{}\n\t湿度：{}\n\t风力：{}\n\t小牢弟，阳光明媚呢~\n'.format(
                    r.json()['cityInfo']['city'],
                    r.json()['data']['forecast'][0]['ymd'],
                    r.json()['data']['forecast'][0]['type'],
                    int(r.json()['data']['pm25']),
                    r.json()['data']['quality'],
                    r.json()['data']['wendu'],
                    r.json()['data']['shidu'],
                    r.json()['data']['forecast'][0]['fl'],
                    r.json()['data']['forecast'][0]['notice'],
                )
            else:
                weatherMsg = '天气查询失败，请稍后再试！QAQ!'

        self.ui.textEdit.setText(weatherMsg)

    def getCode(self, cityName):
        cityDict = {"北京": "101010100",
                    "上海": "101020100",
                    "天津": "101030100",
                    "汕头": "-1",}

        return cityDict.get(cityName, '101010100')

    def myName(self):
        myInformation = '    谢谢赏光，晚上睡不着请发邮件给我[玫瑰]：24yhhuang2@stu.edu.en 我是个负责任的男人[玫瑰][玫瑰]'
        self.ui.textEdit.setText(myInformation)

    def clearText(self):
        self.ui.textEdit.clear()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())