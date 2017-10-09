
# Created by: Younes Elfeitori
# Created on: Oct 2017
# Created for: ICS3U
# This program shows how to use if, else and much more

import ui
from numpy import random

# random number to guess
number_to_guess = random.randint(1, 10)
print(number_to_guess)

def check_touch_up_inside(sender):
    # check the number vs what user selects
    
    # input
    number_entered = int(view['guess_textfield'].text)
    
    # process
    global number_to_guess
    if number_entered == number_to_guess:
        # output
        view['answer_label'].text = "You are correct"
    else:
        view['answer_label'].text = "You are incorrect"

view = ui.load_view()
view.present('full_screen')

