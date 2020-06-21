#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年12月10日
@author: Irony."[讽刺]
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: GetCookie
@description: 
'''
import sys

from PyQt5.QtCore import QUrl, QByteArray
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtWidgets import QApplication, QTextEdit


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class WebEngineView(QWebEngineView):

    DomainCookies = {}  # 存放domain的key-value
    PathCookies = {}  # 存放domain+path的key-value

    def __init__(self, *args, **kwargs):
        super(WebEngineView, self).__init__(*args, **kwargs)
        self.cookieView = QTextEdit()
        self.cookieView.resize(800, 400)
        self.cookieView.move(400, 400)
        self.cookieView.setWindowTitle('Cookies')
        self.cookieView.show()
        # 绑定cookie被添加的信号槽
        QWebEngineProfile.defaultProfile().cookieStore(
        ).cookieAdded.connect(self.onCookieAdd)
        self.loadFinished.connect(self.onLoadFinished)

    def closeEvent(self, event):
        self.cookieView.close()
        super(WebEngineView, self).closeEvent(event)

    def bytestostr(self, data):
        if isinstance(data, str):
            return data
        if isinstance(data, QByteArray):
            data = data.data()
        if isinstance(data, bytes):
            data = data.decode(errors='ignore')
        else:
            data = str(data)
        return data

    def onLoadFinished(self):
        print("*****AllDomainCookies:", self.getAllDomainCookies())
        print("*****AllPathCookies:", self.getAllPathCookies())
        self.cookieView.append(
            "AllDomainCookies: " + self.bytestostr(self.getAllDomainCookies()))
        self.cookieView.append('')
        self.cookieView.append(
            "AllPathCookies: " + self.bytestostr(self.getAllPathCookies()))
        self.cookieView.append('')

        print("*****pyqt5.com cookie:", self.getDomainCookies(".pyqt5.com"))
        print("*****pyqt5.com / path cookie:",
              self.getPathCookies(".pyqt5.com/"))

    def getAllDomainCookies(self):
        return self.DomainCookies

    def getDomainCookies(self, domain):
        return self.DomainCookies.get(domain, {})

    def getAllPathCookies(self):
        return self.PathCookies

    def getPathCookies(self, dpath):
        return self.PathCookies.get(dpath, {})

    def onCookieAdd(self, cookie):
        '''
        :param cookie: QNetworkCookie
        '''
        domain = cookie.domain()
        path = cookie.path()
        name = cookie.name().data()
        value = cookie.value().data()
        if domain in self.DomainCookies:
            _cookie = self.DomainCookies[domain]
            _cookie[name] = value
        else:
            self.DomainCookies[domain] = {name: value}
        domain_path = domain + path
        if domain_path in self.PathCookies:
            _cookie = self.PathCookies[domain_path]
            _cookie[name] = value
        else:
            self.PathCookies[domain_path] = {name: value}
#         print("add cookie:", cookie.domain(),
#               cookie.path(), cookie.name(), cookie.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WebEngineView()
    w.show()
    w.load(QUrl("https://pyqt5.com"))
    sys.exit(app.exec_())
