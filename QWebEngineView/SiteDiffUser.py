#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年8月23日
@author: Irony
@site: https://pyqt5.com https://github.com/PyQt5
@email: 892768447@qq.com
@file: QWebEngineView.SiteDiffUser
@description: 同个网站不同用户
"""
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage,\
    QWebEngineProfile
from PyQt5.QtWidgets import QTabWidget


__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019'
__Version__ = 'Version 1.0'


class Window(QTabWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # 用户1
        self.webView1 = QWebEngineView(self)
        profile1 = QWebEngineProfile('storage1', self.webView1)
        profile1.setPersistentStoragePath('Tmp/Storage1')
        print(profile1.cookieStore())
        # 如果要清除cookie
        # cookieStore = profile1.cookieStore()
        # cookieStore.deleteAllCookies()
        # cookieStore.deleteSessionCookies()
        page1 = QWebEnginePage(profile1, self.webView1)
        self.webView1.setPage(page1)
        self.addTab(self.webView1, '用户1')

        # 用户2
        self.webView2 = QWebEngineView(self)
        profile2 = QWebEngineProfile('storage2', self.webView2)
        profile2.setPersistentStoragePath('Tmp/Storage2')
        print(profile2.cookieStore())
        page2 = QWebEnginePage(profile2, self.webView2)
        self.webView2.setPage(page2)
        self.addTab(self.webView2, '用户2')

        self.webView1.load(QUrl('https://v.qq.com'))
        self.webView2.load(QUrl('https://v.qq.com'))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
