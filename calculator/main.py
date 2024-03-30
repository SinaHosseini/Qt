import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def all_clear():
    global num1, num2, operator
    window.line_edit.setText(None)
    num1 = None
    num2 = None
    operator = None


def dot():
    window.line_edit.setText(window.line_edit.text() + ".")


def numbers(n):
    window.line_edit.text()
    window.line_edit.setText(window.line_edit.text() + n)


def sum():
    global num1, operator
    operator = "sum"
    num1 = float(window.line_edit.text())
    window.line_edit.setText(None)


def sub():
    global num1, operator
    operator = "sub"
    num1 = float(window.line_edit.text())
    window.line_edit.setText(None)


def mul():
    global num1, operator
    operator = "mul"
    num1 = float(window.line_edit.text())
    window.line_edit.setText(None)


def div():
    global num1, operator
    operator = "div"
    num1 = float(window.line_edit.text())
    window.line_edit.setText(None)


def sqrt():
    num1 = float(window.line_edit.text())
    rsl = math.sqrt(num1)
    window.line_edit.setText(str(rsl))


def perc():
    global percent
    percent = True


def result():
    num2 = float(window.line_edit.text())

    if operator == "sum":
        if percent == True:
            num2 = num1 * num2 / 100
            rsl = num1 + num2
        else:
            rsl = num1 + num2

    elif operator == "sub":
        if percent == True:
            num2 = num1 * num2 / 100
            rsl = num1 - num2
        else:
            rsl = num1 - num2

    elif operator == "mul":
        if percent == True:
            num2 = num1 * num2 / 100
            rsl = num1 * num2
        else:
            rsl = num1 * num2

    elif operator == "div":
        if percent == True:
            num2 = num1 * num2 / 100
            rsl = num1 / num2
        else:
            rsl = num1 / num2

    window.line_edit.setText(str(rsl))


app = QApplication([])

loader = QUiLoader()
window = loader.load("mainwindow.ui")
window.show()


percent = False

window.btn_sum.clicked.connect(sum)
window.btn_sub.clicked.connect(sub)
window.btn_mul.clicked.connect(mul)
window.btn_div.clicked.connect(div)
window.btn_sqrt.clicked.connect(sqrt)
window.btn_percent.clicked.connect(perc)
window.btn_result.clicked.connect(result)
window.btn_0.clicked.connect(partial(numbers, "0"))
window.btn_1.clicked.connect(partial(numbers, "1"))
window.btn_2.clicked.connect(partial(numbers, "2"))
window.btn_3.clicked.connect(partial(numbers, "3"))
window.btn_4.clicked.connect(partial(numbers, "4"))
window.btn_5.clicked.connect(partial(numbers, "5"))
window.btn_6.clicked.connect(partial(numbers, "6"))
window.btn_7.clicked.connect(partial(numbers, "7"))
window.btn_8.clicked.connect(partial(numbers, "8"))
window.btn_9.clicked.connect(partial(numbers, "9"))
window.btn_dot.clicked.connect(dot)
window.btn_ac.clicked.connect(all_clear)

app.exec()
