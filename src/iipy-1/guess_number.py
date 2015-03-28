# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# 第二版，解决系统崩溃事件
# 待解决的问题：很想将生成100和生成1000的合在一起。

g_secret_number = -1
g_guess_num = 0
#user_range = 100
g_has_ok = False
g_has_input = False
g_status = 'started'

# initialize global variables used in your code here
# if last guess is finished
#last_guess = 0
#  the number of guesses


# define event handlers  
def set_range100():
    global g_frame,g_secret_number,g_guess_num,g_handle_input
    global g_has_ok,g_has_input
    g_frame.set_draw_handler(draw_guessing_text)
    g_guess_num = 0
    g_secret_number=random.randint(0,100)
    if g_has_input == False:
        g_handle_input = g_frame.add_input('Input your guess here', guess_input, 50)
        g_has_input = True    
    if g_has_ok == False:        
#        g_handle_ok = g_frame.add_button('click me to guess',guess_input)
        g_has_ok = True
#     print 'Number with range[0,100] has been generated ,pls input a number into input_box'
#    print ('secret number is ' + str(g_secret_number)+', haha do not tell anyone')

def set_range1000():
    global g_frame,g_secret_number,g_guess_num,g_handle_input
    global g_has_ok,g_has_input
    g_frame.set_draw_handler(draw_guessing_text)
    g_guess_num = 0
    g_secret_number=random.randint(0,1000)
    if g_has_input == False:
        g_handle_input = g_frame.add_input('Input your guess here', guess_input, 50)
        g_has_input = True    
    if g_has_ok == False:        
#        g_handle_ok = g_frame.add_button('click me to guess',guess_input)
        g_has_ok = True
#    print 'Number with range[0,1000] has been generated ,pls input a number into input_box'
#    print 'secret number is ' + str(g_secret_number)+', haha do not tell anyone'
    
def guess_input(canvas):
#def guess_input():
    global g_handle_input,g_secret_number
    if g_secret_number == -1:
        g_frame.set_draw_handler(draw_cheat_text)
#        print 'HAHA, do not cheating, please generate a new number'
        return
    str_input = g_handle_input.get_text()
    if valid_input(str_input):
        input_number=int(str_input)
        campare_input(input_number)
    else:
#        print 'SORRY,Number you guess should be POSITIVE NUMBER'
        g_frame.set_draw_handler(draw_wrong_text)
        
def campare_input(input_number):
    global g_secret_number,g_guess_num
    camp=g_secret_number - input_number
    g_guess_num+=1
    if camp>0:
#        print 'Sorry, too high, please try again'
        g_frame.set_draw_handler(draw_higher_text)
    elif camp<0:
#         print 'Sorry, too low, please try again'
        g_frame.set_draw_handler(draw_lower_text)
    else:
#         print 'BINGO, you did it'
        print 'you took ' + str(g_guess_num)+' times'
        g_frame.set_draw_handler(draw_success_text)
        g_secret_number=-1
        g_guess_num=0        
        
def valid_input(txt):
    if txt == '':
        return False
    is_int = all(c in "0123456789" for c in txt)
    if is_int:
        return True
    else:
        return False

#for draw image ,unused   
def draw_image(canvas):
    image = simplegui.load_image('http://img4.imgtn.bdimg.com/it/u=754650713,954354305&fm=23&gp=0.jpg')
    canvas.draw_image(image,(1521 / 2, 1818 / 2), (1521, 1818), (50, 50), (100, 100))

def draw_started_text(canvas):
    message = 'Welcome to the GUESS NUMBER game'
    canvas.draw_text(message,(5,90),20,'white')
    message = 'pls click generate button to get started!'
    canvas.draw_text(message,(5,120),20,'white')
    
def draw_guessing_text(canvas):
    message = 'Number generated!'
    canvas.draw_text(message,(5,50),20,'white')
    message = 'Press ENTER to press'
    canvas.draw_text(message,(5,90),20,'white')
    message = 'Good Luck'
    canvas.draw_text(message,(5,120),20,'white')
    
def draw_cheat_text(canvas):
    message = 'HAHA, regenerate the number'
    canvas.draw_text(message,(5,90),20,'red')
    
def draw_wrong_text(canvas):
    message = 'POSITIVE NUMBER needed'
    canvas.draw_text(message,(5,90),20,'red')

def draw_lower_text(canvas):
    message = 'too high, try again'
    canvas.draw_text(message,(5,90),20,'red')

def draw_higher_text(canvas):
    message = 'too low, try again'
    canvas.draw_text(message,(5,90),20,'red')
    
def draw_success_text(canvas):
    global g_guess_num
    message = 'Your are amazing!'
    canvas.draw_text(message,(5,90),25,'white')
    message = 'click generate button to play again'
    canvas.draw_text(message,(5,150),20,'white')
    g_guess_num=-1
    



# create frame
g_frame = simplegui.create_frame("Let's gusss number",600,300)
g_frame.add_button('Generate Number!Range [0,100]',set_range100)
g_frame.add_button('Generate Number!nRange [0,1000]',set_range1000)


#g_frame.add_label("Do not press ENTER, or it'll get wrong")
#label.set_text('new lable')
#frame.set_draw_handler(draw_sucess_image)
g_frame.set_draw_handler(draw_started_text)
g_frame.start()




