import sys
import requests
from PyQt5.Qt import QDesktopServices, QUrl
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Add the icon
icon = QIcon("bunker.png")

# Get block count from api.bunkercoin.xyz
blockcount = requests.get('http://api.bunkercoin.xyz/blockcount')
blockcountjson = blockcount.json()
blockcountstr = blockcountjson['result']['blockcount']
print(blockcountstr)

# Open web browser with http://api.bunkercoin.xyz/blockcount
#def open_browser():
# url = QUrl("http://api.bunkercoin.xyz/blockcount")
#g QDesktopServices.openUrl(url)

# Adding item to the system tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the "menu"
menu = QMenu()
blockcount = QAction("Blockcount: " + str(blockcountstr))
quit = QAction("Exit")
quit.triggered.connect(app.quit)
menu.addAction(blockcount)
menu.addAction(quit)

# Add options to the system tray
tray.setContextMenu(menu)

app.exec_()
