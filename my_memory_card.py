#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import randint 
from PyQt5.QtWidgets import QMessageBox, QButtonGroup,  QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,QRadioButton, QGroupBox
class Question():
    def __init__(self, q, r_ans, w_ans1, w_ans2, w_ans3):
        self.q = q
        self.r_ans= r_ans
        self.w_ans1 = w_ans1
        self.w_ans2 = w_ans2
        self.w_ans3 = w_ans3
spisok = list()
serf = Question('Какой-нибудь вопрос','ответ1','ответ2','ответ3','ответ4')
spisok.append(serf)
serf = Question('Кто ты?','человек','фея','ведьма','фея2')
spisok.append(serf)
serf = Question('Сколько будет 3*3','9','33','16','0')
spisok.append(serf)
serf = Question('Сколько букв в англ.алфавите','26','36','32','25')
spisok.append(serf)
serf = Question('Сколько лет Путину','70','67','56','25')
spisok.append(serf)
serf = Question('Какое животное самое крупное на Земле','синий кит','кашалот','лев','лимур')
spisok.append(serf)
serf = Question('Какое млекопитающее умеет летать','Летучая мышь','Белка-летяга','Колуго','Белоголовый орлан')
spisok.append(serf)
z = 0
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(500,500)
question = QLabel('Какой национальности не существует?')
box1 = QGroupBox('Варианты ответов')
group = QButtonGroup()
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('смурфы')
ans3 = QRadioButton('чулымцы')
ans4 = QRadioButton('Алеуты')
group.addButton(ans1)
group.addButton(ans2)
group.addButton(ans3)
group.addButton(ans4)
h1 = QHBoxLayout()
h1.addWidget(ans1, alignment = Qt.AlignLeft)
h1.addWidget(ans3, alignment = Qt.AlignLeft)
h2 = QHBoxLayout()
h2.addWidget(ans2, alignment = Qt.AlignLeft)
h2.addWidget(ans4, alignment = Qt.AlignLeft)
v1 = QVBoxLayout()
v1.addLayout(h1)
v1.addLayout(h2)
box1.setLayout(v1)
box2 = QGroupBox('Результат теста')
label1 = QLabel('Правильно, не првильно')
label2 = QLabel('Ответ')
v3 = QVBoxLayout()
v3.addWidget(label1, alignment = Qt.AlignLeft)
v3.addWidget(label2, alignment = Qt.AlignCenter)
box2.setLayout(v3)
box2.hide()
button = QPushButton('Ответить')
v2 = QVBoxLayout()
v2.addWidget(question, alignment = Qt.AlignVCenter)
v2.addWidget(box1, alignment = Qt.AlignVCenter)
v2.addWidget(box2, alignment = Qt.AlignVCenter)
v2.addWidget(button, alignment = Qt.AlignVCenter)

def show_result():
    try:
        check_answer()
        box1.hide()
        box2.show()
        button.setText('Следующий вопрос')
    except:
        win = QMessageBox()
        win.setText('Сначала выбери ответ')
        win.exec_()
def show_question():
    box1.show()
    box2.hide()
    button.setText('Ответить')
    group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    group.setExclusive(True)
    ask(spisok[randint(0,len(spisok)-1)])
def ask(q: Question):
    question.setText(q.q)
    rand = randint(0,3)
    if rand == 0:
        ans1.setText(q.r_ans)
        ans2.setText(q.w_ans1)
        ans3.setText(q.w_ans2)
        ans4.setText(q.w_ans3)
    elif rand == 1:
        ans2.setText(q.r_ans)
        ans1.setText(q.w_ans1)
        ans3.setText(q.w_ans2)
        ans4.setText(q.w_ans3)
    elif rand == 2:
        ans3.setText(q.r_ans)
        ans2.setText(q.w_ans1)
        ans1.setText(q.w_ans2)
        ans4.setText(q.w_ans3)
    else:
        ans4.setText(q.r_ans)
        ans2.setText(q.w_ans1)
        ans3.setText(q.w_ans2)
        ans1.setText(q.w_ans3)
    label2.setText(q.r_ans)
def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()
        window.total += 1
def check_answer():
    if label2.text() == group.checkedButton().text():
        label1.setText('Правильно')
        window.score += 1
    else:
        label1.setText('Неверно')
    print('-Всего вопросов:',window.total )
    print('-Правильных ответов:', window.score)
    print('Рейтинг:', window.score/window.total*100)
    

ask(spisok[z])
window.total = 1
window.score = 0
button.clicked.connect(start_test)
window.setLayout(v2)
window.show()
app.exec_()
