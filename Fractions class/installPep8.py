import pip  # This install is for Windows only, running Python 3.4 or later
# Mac: after installing python3, open terminal, type
# pip3 install pycodestyle
# pip3 install autopep8
# pip3 install pillow

def install(package):
    pip.main(['install', package])


if __name__ == '__main__':
    install('pycodestyle')
    install('autopep8')
    install('pillow')
