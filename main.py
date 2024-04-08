from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl


import os
import sys
import functools
import random


os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\sabir\\anaconda3\\Lib\\site-packages\\PySide2\\plugins\\platforms'
PATH = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.LEVEL_MAX = 10
        self.HEIGHT = 100

        self.level = 1
        self.round = 0
        
        self.setWindowTitle("Enigmatic Number Quest | SABIR Ilyass Copyright © 2024")
        self.setFixedSize(1200, 600)
        self.setWindowIcon(QIcon(PATH + "/Images/icon.png"))

        # create a centralWidget
        self.centralWidget = QWidget(self)
        self.centralWidget.setFixedSize(1200, 600)
        self.centralWidget.setStyleSheet("background-color: #212129;")

        self.setCentralWidget(self.centralWidget)
        
        self.titleLabel = QLabel("Enigmatic Number Quest", self)
        self.show_Window_title(80, 0, 150)
        self.show_help_button1()

        self.show_start_game("Start Game", 450, 400, 300, 50)

        self.number_choose = -1
        self.list_number = [-1] * self.level

        self.list_main_number = [random.randint(0, 9) for _ in range(self.level)]
       
        self.list_of_numbers_without_background = [QPushButton("", self) for _ in range(10)]
        for number in range(10):
            self.list_of_numbers_without_background[number].setGeometry(75 + 110 * number, 450, 70, 85)
            
            """ 
            self.list_of_numbers_without_background[number].setStyleSheet(
                    f"background-image : url({PATH}/Images/{number}_without.png);"
                    "background-color: transparent;"
                    "border-style: solid;"
                    "border-width: 1px;"
                    "border-color: #12A2D7;"
                    "border-radius: 12px;"
                    "QPushButton:hover {"
                    f"   background-image : url({PATH}/Images/{number}.png);"
                    "}"
            )
            """

            self.list_of_numbers_without_background[number].setStyleSheet(
                        "QPushButton{"
                        f"background-image : url({PATH}/Images/{number}_without.png);"
                        "background-color: transparent;"
                        "border-style: solid;"
                        "border-width: 0px;"
                        "border-color: #12A2D7;"
                        "border-radius: 12px;"
                        "}"
                        f"QPushButton:hover {{ background-image : url({PATH}/Images/{number}.png); }}"
                    )

            self.list_of_numbers_without_background[number].clicked.connect(functools.partial(self.get_number_choose, number))
            self.list_of_numbers_without_background[number].hide()

        self.list_of_numbers_check = [QPushButton("", self) for _ in range(self.LEVEL_MAX)]
        for number in range(self.LEVEL_MAX):
            # self.list_of_numbers_check[number].setGeometry(377 + 120 * number, 150, 70, 85)
            self.list_of_numbers_check[number].setStyleSheet(f"""background-image : url({PATH}/Images/White.png);
                                                                border-style: solid;
                                                                border-width: 0px;
                                                                border-color: #282B2E;
                                                                border-radius: 12px;""")

            self.list_of_numbers_check[number].clicked.connect(functools.partial(self.set_number, number))
            self.list_of_numbers_check[number].hide()

        self.list_of_check_value = [QPushButton("", self) for _ in range(self.LEVEL_MAX)]
        for number in range(self.LEVEL_MAX):
            self.list_of_check_value[number].clicked.connect(functools.partial(self.set_number, number))
            self.list_of_check_value[number].hide()

        for number in range(self.level):
            x = 615 + self.HEIGHT * (number - self.level / 2)
            self.list_of_numbers_check[number].setGeometry(x, 150, 70, 85)
            self.list_of_check_value[number].setGeometry(x, 250, 70, 85)

        self.check_button = QPushButton('Check !', self)
        self.check_button.setGeometry(500, 300, 200, 50)

         # Set the button style using CSS
        self.check_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #12A2D7;"
            "   border-style: solid;"
            "   border-width: 0px;"
            "   border-color: #3E5EAB;"
            "   border-radius: 10px;"
            "   color: #282B2E;"
            "   font-size: 36px;"
            "   font-weight: bold;"
            "   font-family: Gabriola;"
            "}"
            "QPushButton:hover {"
            "   background-color: #3E5EAB;"
            "   color: white;"
            "}"
        )
        self.check_button.hide()
        self.check_button.clicked.connect(self.check_function)

        self.round_Label = QLabel(f"level : {self.level}, Round : {self.round}", self)
        self.round_Label.setGeometry(0, -10, 1200, 200)
        font = QFont()
        font.setPointSize(20)
        font.setFamily("Gabriola")
        font.setBold(True)
        self.round_Label.setFont(font)
        self.round_Label.setAlignment(Qt.AlignCenter)
        self.round_Label.setStyleSheet("color: #12A2D7;")
        self.round_Label.hide()

        self.End_game_Label = QLabel("Congratulations, go to the next level", self)
        self.End_game_Label.setGeometry(0, 250, 1200, 200)
        font = QFont()
        font.setPointSize(50)
        font.setFamily("Gabriola")
        font.setBold(True)
        self.End_game_Label.setFont(font)
        self.End_game_Label.setAlignment(Qt.AlignCenter)
        self.End_game_Label.setStyleSheet("color: #12A2D7;")
        self.End_game_Label.hide()

        self.end_game = False

        self.next_round = QPushButton('Next round', self)
        self.next_round.setGeometry(450, 400, 300, 50)

         # Set the button style using CSS
        self.next_round.setStyleSheet(
            "QPushButton {"
            "   background-color: #12A2D7;"
            "   border-style: solid;"
            "   border-width: 0px;"
            "   border-color: #3E5EAB;"
            "   border-radius: 10px;"
            "   color: #282B2E;"
            "   font-size: 36px;"
            "   font-weight: bold;"
            "   font-family: Gabriola;"
            "}"
            "QPushButton:hover {"
            "   background-color: #3E5EAB;"
            "   color: white;"
            "}"
        )
        self.next_round.hide()
        self.next_round.clicked.connect(self.next_round_function)

        self.next_level_button = QPushButton('Next level', self)
        self.next_level_button.setGeometry(450, 450, 300, 50)

         # Set the button style using CSS
        self.next_level_button.setStyleSheet(
            "QPushButton {"
            "   background-color: #12A2D7;"
            "   border-style: solid;"
            "   border-width: 0px;"
            "   border-color: #3E5EAB;"
            "   border-radius: 10px;"
            "   color: #282B2E;"
            "   font-size: 36px;"
            "   font-weight: bold;"
            "   font-family: Gabriola;"
            "}"
            "QPushButton:hover {"
            "   background-color: #3E5EAB;"
            "   color: white;"
            "}"
        )
        self.next_level_button.hide()
        self.next_level_button.clicked.connect(self.next_level)

        # Créer un lecteur multimédia
        self.media_player0 = QMediaPlayer()
        self.media_player1 = QMediaPlayer()
        self.media_player2 = QMediaPlayer()
        self.media_player3 = QMediaPlayer()
        self.media_player4 = QMediaPlayer()
        self.media_player5 = QMediaPlayer()
        self.media_player6 = QMediaPlayer()
        self.media_player7 = QMediaPlayer()
        self.media_player8 = QMediaPlayer()
        self.media_player9 = QMediaPlayer()

        self.media_player0.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/chick_false.mp3")))
        self.media_player1.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/click.mp3")))
        self.media_player2.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/Error.mp3")))
        self.media_player3.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/help.mp3")))
        self.media_player4.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/next_round.mp3")))
        self.media_player5.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/put.wav")))
        self.media_player6.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/start_game.mp3")))
        self.media_player7.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/Congratulation.mp3")))
        self.media_player8.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/next_level.mp3")))
        self.media_player9.setMedia(QMediaContent(QUrl.fromLocalFile(f"{PATH}/Images/success.mp3")))


    def next_level(self):
        if self.level == self.LEVEL_MAX:
            self.level = 0       
            for number in range(self.LEVEL_MAX):
                self.list_of_numbers_check[number].hide()
                self.list_of_check_value[number].hide()
                self.media_player6.play()
        else:
            self.media_player8.play()

        self.level += 1
        self.list_main_number = [random.randint(0, 9) for _ in range(self.level)]

        self.round = 0
        self.number_choose = -1
        self.list_number = [-1] * self.level
        for number in range(self.level):
            self.list_of_numbers_check[number].setStyleSheet(f"""background-image : url({PATH}/Images/White.png);
                                                                border-style: solid;
                                                                border-width: 0px;
                                                                border-color: #282B2E;
                                                                border-radius: 12px;""")
            
            x = 615 + self.HEIGHT * (number - self.level / 2)
            self.list_of_numbers_check[number].setGeometry(x, 150, 70, 85)
            self.list_of_check_value[number].setGeometry(x, 250, 70, 85)

            self.list_of_numbers_check[number].show()
                
        for number in range(10):
            self.list_of_numbers_without_background[number].show()
        
        self.check_button.show()
        self.next_level_button.hide()
        self.End_game_Label.hide()
        self.round_Label.setText(f"Level : {self.level}, Round : {self.round}")
        self.end_game = False
        self.end_level = False
        
    
    def next_round_function(self):
        self.media_player4.play()
        self.list_number = [-1] * self.level
        self.next_round.hide()
        self.check_button.show()
        for number in range(self.level):
            self.list_of_check_value[number].hide()
        
        for number in range(10):
            self.list_of_numbers_without_background[number].show()

        for number in range(self.level):
            self.list_of_numbers_check[number].setStyleSheet(f"""background-image : url({PATH}/Images/White.png);
                                                                border-style: solid;
                                                                border-width: 0px;
                                                                border-color: #282B2E;
                                                                border-radius: 12px;""")



    def end_game_function(self):
        self.end_game = True
        for i in range(self.level):
            if self.list_number[i] != self.list_main_number[i]:
                self.end_game = False



    def check_function(self):
        if -1 in self.list_number:
            self.media_player2.play()
            help_dialog = QDialog(self)
            help_dialog.setWindowTitle("Caution !")
            help_dialog.setModal(True)

            help_label = QLabel("""
                                Please fill in all digits.
                                """)
            help_layout = QVBoxLayout()
            help_layout.addWidget(help_label)
            help_dialog.setLayout(help_layout)

            # display the dialog window
            help_dialog.show()
        else:
            self.number_choose = -1
            self.end_game_function()

            self.round += 1
            self.round_Label.setText(f"Level : {self.level}, Round : {self.round}")

            for number in range(10):
                    self.list_of_numbers_without_background[number].hide()

            self.check_button.hide()

            if self.end_game and self.level < self.LEVEL_MAX:
                self.media_player9.play()
                self.End_game_Label.show()
                self.next_level_button.show()
            
            elif self.end_game and self.level >= self.LEVEL_MAX:
                self.media_player7.play()
                self.End_game_Label.setText("Congratulations, you win !")
                self.next_level_button.setText("Start a new game")
                self.End_game_Label.show()
                self.next_level_button.show()

            else:
                self.media_player0.play()
                self.next_round.show()
                for number in range(self.level):
                    if self.list_number[number] == self.list_main_number[number]:
                        self.list_of_check_value[number].setStyleSheet(f"""background-image : url({PATH}/Images/V.png);
                                                                        border-style: solid;
                                                                        border-width: 0px;
                                                                        border-color: #282B2E;
                                                                        border-radius: 12px;""")
                        
                    elif self.list_number[number] in self.list_main_number:
                        self.list_of_check_value[number].setStyleSheet(f"""background-image : url({PATH}/Images/E.png);
                                                                        border-style: solid;
                                                                        border-width: 0px;
                                                                        border-color: #282B2E;
                                                                        border-radius: 12px;""")
                        
                    else:
                        self.list_of_check_value[number].setStyleSheet(f"""background-image : url({PATH}/Images/F.png);
                                                                        border-style: solid;
                                                                        border-width: 0px;
                                                                        border-color: #282B2E;
                                                                        border-radius: 12px;""")
                        
                    self.list_of_check_value[number].show()


    def get_number_choose(self, num):
        self.media_player1.play()
        self.number_choose = num
    
    def set_number(self, num):
        if self.number_choose >= 0:
            self.media_player5.play()
            self.list_of_numbers_check[num].setStyleSheet(f"""background-image : url({PATH}/Images/{self.number_choose}.png);
                                                                    border-style: solid;
                                                                    border-width: 0px;
                                                                    border-color: #282B2E;
                                                                    border-radius: 12px;""")
            self.list_number[num] = self.number_choose
        else:
            self.media_player2.play()
            

    def show_Window_title(self, font_size, position_x, positions_y):
        self.titleLabel.setGeometry(position_x, positions_y, 1200, 200)
        font = QFont()
        font.setPointSize(font_size)
        font.setFamily("Gabriola")
        font.setBold(True)



        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setStyleSheet("color: #12A2D7;")

    def hide_window_title(self):
        self.titleLabel.hide()

    def show_help_button1(self):
        # Create a button
        self.help_button1 = QPushButton("Help!", self)

        # Set the button position and size
        self.help_button1.setGeometry(1100, 20, 80, 25)

         # Set the button style using CSS
        self.help_button1.setStyleSheet(
            "QPushButton {"
            "   background-color: #12A2D7;"
            "   border-style: solid;"
            "   border-width: 0px;"
            "   border-color: #282B2E;"
            "   border-radius: 12px;"
            "   color: #212129;"
            "   font-size: 16px;"
            "   font-weight: bold;"
            "}"
            "QPushButton:hover {"
            "   background-color: #3E5EAB;"
            "   color: white;"
            "}"
        )

        # Connect a function to the button click event
        self.help_button1.mousePressEvent = self.show_help
    
    def show_help(self, event):
        # create a new dialog window
        self.media_player3.play()
        help_dialog = QDialog(self)
        help_dialog.setWindowTitle("Help !")
        help_dialog.setModal(True)

        # add some text to the dialog
        help_label = QLabel("""
                            Rules of the game:
                            • You need to find a 4-digit number.
                            • If a digit is correct and in the right position, 'V' is displayed.
                            • If a digit is correct but in the wrong position, 'E' is displayed.
                            • If a digit does not exist in the target number, 'F' is displayed.
                            • The game ends when the number is found.
                            Example:
                            Target Number: 7582
                            Guess: 7284
                            Response: VEVF 
                            (7 is correctly placed, 2 and 8 are correct but misplaced, 5 is absent in the target number)
                            """)
        help_layout = QVBoxLayout()
        #help_layout.setGeometry(300)

        help_layout.addWidget(help_label)
        help_dialog.setLayout(help_layout)

        # display the dialog window
        help_dialog.show()

    def show_start_game(self, title, position_x, positions_y, size_x, size_y):
        # Create a button

        self.button1 = QPushButton(title, self)

        # Set the button position and size
        self.button1.setGeometry(position_x, positions_y, size_x, size_y)

         # Set the button style using CSS
        self.button1.setStyleSheet(
            "QPushButton {"
            "   background-color: #12A2D7;"
            "   border-style: solid;"
            "   border-width: 0px;"
            "   border-color: #12A2D7;"
            "   border-radius: 10px;"
            "   color: #212129;"
            "   font-size: 36px;"
            "   font-weight: bold;"
            "   font-family: Gabriola;"
            "}"
            "QPushButton:hover {"
            "   background-color: #3E5EAB;"
            "   color: white;"
            "}"
        )
        self.button1.mousePressEvent = self.start_game

    def start_game(self, event):
        self.media_player6.play()
        self.show_Window_title(30, 0, -70)
        self.round_Label.show()
        for number in range(10):
            self.list_of_numbers_without_background[number].show()

        for number in range(self.level):
            self.list_of_numbers_check[number].show()
        
        self.button1.hide()

        self.check_button.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    mainWindow = Main()

    mainWindow.show()

    sys.exit(app.exec_())