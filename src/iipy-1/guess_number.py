# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#
# 待解决的问题：很想将生成100和生成1000的合在一起。
# 如何隐藏或者删除已有的控件
# 画布各类绘制信息希望能整合
# 画布操作需要一定时间，会多次调用同一个function，并且与后续的代码并行，如果调用到全局变量将可能出错
# 全局变量用前 缀g_
# 禁止使用回车,貌似监控键盘状态用到的库，还木有找到
#handle_input:input控件
# frame : frame控件
# secret_number : 系统自动生成的随机数
# input_number: 用户输入的数字，已经转换成有效数值
# user_range:用户选择的随机数上限值
# has_ok: 是否有开始计算按钮，此按钮在用户生成随机数后出现，在用户猜成功后消失
# status: 标记程序运行6个状态，可用于向用户输出不同信息。

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
        g_handle_ok = g_frame.add_button('click me to guess',guess_input)
        g_has_ok = True
#     print 'Number with range[0,100] has been generated ,pls input a number into input_box'
    print ('secret number is ' + str(g_secret_number)+', haha do not tell anyone')

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
        g_handle_ok = g_frame.add_button('click me to guess',guess_input)
        g_has_ok = True
#    print 'Number with range[0,1000] has been generated ,pls input a number into input_box'
    print 'secret number is ' + str(g_secret_number)+', haha do not tell anyone'
    
def guess_input():
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
#        print 'Sorry, Lower, please try again'
        g_frame.set_draw_handler(draw_lower_text)
    elif camp<0:
#         print 'Sorry, Higher, please try again'
        g_frame.set_draw_handler(draw_higher_text)
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
    message = 'Press Guessing Button'
    canvas.draw_text(message,(5,90),20,'white')
    message = 'Good Luck'
    canvas.draw_text(message,(5,120),20,'white')
    
def draw_cheat_text(canvas):
    message = 'HAHA, no cheating'
    canvas.draw_text(message,(5,90),20,'red')
    
def draw_wrong_text(canvas):
    message = 'POSITIVE NUMBER needed'
    canvas.draw_text(message,(5,90),20,'red')

def draw_lower_text(canvas):
    message = 'Higher, try again'
    canvas.draw_text(message,(5,90),20,'red')

def draw_higher_text(canvas):
    message = 'Lower, try again'
    canvas.draw_text(message,(5,90),20,'red')
    
def draw_success_text(canvas):
    global g_guess_num
    message = 'Your are amazing!'
    canvas.draw_text(message,(5,90),25,'white')
    message = 'click generate button to play again'
    canvas.draw_text(message,(5,150),20,'white')
    g_guess_num=-1
    
#响应键盘回车事件


# create frame
g_frame = simplegui.create_frame("Let's gusss number",600,300)
g_frame.add_button('Generate Number!Range [0,100]',set_range100)
g_frame.add_button('Generate Number!nRange [0,1000]',set_range1000)


g_frame.add_label("Do not press ENTER, or it'll get wrong")
#label.set_text('new lable')
#frame.set_draw_handler(draw_sucess_image)
g_frame.set_draw_handler(draw_started_text)
g_frame.start()




