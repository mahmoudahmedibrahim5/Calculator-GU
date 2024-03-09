from frontend import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui


class Calculator(Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        
        self.state = 0
        
        self.n0.clicked.connect(self.n0_pressed)
        self.n1.clicked.connect(self.n1_pressed)
        self.n2.clicked.connect(self.n2_pressed)
        self.n3.clicked.connect(self.n3_pressed)
        self.n4.clicked.connect(self.n4_pressed)
        self.n5.clicked.connect(self.n5_pressed)
        self.n6.clicked.connect(self.n6_pressed)
        self.n7.clicked.connect(self.n7_pressed)
        self.n8.clicked.connect(self.n8_pressed)
        self.n9.clicked.connect(self.n9_pressed)
        
        self.plus.clicked.connect(self.plus_pressed)
        self.minus.clicked.connect(self.minus_pressed)
        self.multiply.clicked.connect(self.multiply_pressed)
        self.divided.clicked.connect(self.divided_pressed)
        
        self.equal.clicked.connect(self.equal_pressed)
        
        self.dot.clicked.connect(self.dot_pressed)
        self.negative.clicked.connect(self.negative_pressed)
        self.clear.clicked.connect(self.clear_pressed)
        self.backspace.clicked.connect(self.backspace_pressed)
        
        self.window.show()
        
    def n0_pressed(self):
        self.add_character('0')
    def n1_pressed(self):
        self.add_character('1')
    def n2_pressed(self):
        self.add_character('2')
    def n3_pressed(self):
        self.add_character('3')
    def n4_pressed(self):
        self.add_character('4')
    def n5_pressed(self):
        self.add_character('5')
    def n6_pressed(self):
        self.add_character('6')
    def n7_pressed(self):
        self.add_character('7')
    def n8_pressed(self):
        self.add_character('8')
    def n9_pressed(self):
        self.add_character('9')
        
    def plus_pressed(self):
        self.add_character(' ')
        self.add_character('+')
        self.add_character(' ')
    def minus_pressed(self):
        self.add_character(' ')
        self.add_character('-')
        self.add_character(' ')
    def multiply_pressed(self):
        self.add_character(' ')
        self.add_character('x')
        self.add_character(' ')
    def divided_pressed(self):
        self.add_character(' ')
        self.add_character('/')
        self.add_character(' ')
    
    def negative_pressed(self):
        self.add_character('-')
        
    def dot_pressed(self):
        self.add_character('.')
    
    def add_character(self, c):
        if self.state == 1:
            self.clear_pressed()
            self.state = 0
        current_text = self.display.toPlainText()
        if current_text:    # If there is existing text, append the character horizontally
            self.display.setPlainText(current_text + c)
        else:               # If it's the first character, set the plain text
            self.display.setPlainText(c)
        
    def clear_pressed(self):
        self.display.clear()
    def backspace_pressed(self):
        current_text = self.display.toPlainText()
        self.display.setPlainText(current_text[:-1])
        
    def equal_pressed(self):
        current_text = self.display.toPlainText()
        
        start = 0
        counter = 0
        number = []
        operations = []
        
        # Parse the input
        for i in range(len(current_text)):
            if (current_text[i] == '+') | (current_text[i] == '-') | (current_text[i] == 'x') | (current_text[i] == '/'):
                number.append(float(current_text[start:i-1]))
                operations.append(current_text[i])
                counter += 1
                start = i + 2
        number.append(float(current_text[start:]))
          
        # Evaluate the result
        for i in range(counter):
            if(operations[i] == '+'):
                number[i + 1] = number[i] + number[i + 1]
            elif(operations[i] == '-'):
                number[i + 1] = number[i] - number[i + 1]
            elif(operations[i] == 'x'):
                number[i + 1] = number[i] * number[i + 1]
            elif(operations[i] == '/'):
                number[i + 1] = number[i] / number[i + 1]
        
        self.add_character('\n')
        self.add_character('\n')
        self.add_character(str(number[-1]))
        self.state = 1
        