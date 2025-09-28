#  账号：yangran  密码：123

import sys

from PyQt5.QtWidgets import QApplication

from login import Login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = Login()
    Login.show()
    sys.exit(app.exec_())
