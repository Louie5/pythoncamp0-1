# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import random
draw_list = []
step = 0
review_list = ['pls give me your number']
a1win = 0
a2win = 0
even = 0
# Handler for mouse click

# Handler to draw on canvas
def draw(canvas):
    o = DrawText(draw_list)
    p = o.draw(canvas,[20,20])
    
def ai_input_handler(txt):
    timer.stop()
    global draw_list
    global review_list,a1win,a2win,even
    #验证input是否符合要求
    error_input_message = ['pls input POSITIVE number[0,1000]']
    if  not is_int(txt):
        draw_list = error_input_message 
        return
    else:
        guess_number = int(txt)
        if guess_number<0 or guess_number>1000:
            draw_list = error_input_message 
            return
#重置提示，开始计算
    draw_list = []
    review_list = []
    
    guess_time1 = alg1(guess_number)
    draw_list.append('     ')
    guess_time2 = alg2(guess_number)
    if guess_time1>guess_time2:
        msg = 'Algorithm 2 Win'
        a2win+=1
    elif guess_time1<guess_time2:
        msg = 'Algorithm 1 Win'
        a1win+=1
    else:
        msg = 'Algorithms ended in a draw'
        even+=1
    draw_list.append('     ')    
    draw_list.append(msg)
    draw_list.append('     ')
    draw_list.append('we played ' + str(a1win+a2win+even) + ' times')
    draw_list.append('Algorithm1 win: ' + str(a1win))
    draw_list.append('Algorithm2 win: ' + str(a2win))
    draw_list.append('Algorithms play even :  ' + str(even))
    review_list = draw_list
    pass

def alg1(guess_number):
#直接二分法
    global draw_list
    ai_number = 500
    lower_number = 0
    upper_number = 1000
    i = 0
#    draw_list.append(u'算法一：')
    draw_list.append('Algorithm 1:Direct Dichotomy')
    while ai_number <> guess_number:
        i+=1
        if ai_number>guess_number:
#            draw_list.append(u'第' + str(i) + u'次猜'+str(ai_number)+ u',猜高了')
            draw_list.append('The ' + str(i) + ' guess:'+str(ai_number)+ u',too high')
            upper_number = ai_number
            ai_number = (ai_number+lower_number)/2
        else:
#            draw_list.append(u'第' + str(i) + u'次猜'+str(ai_number)+ u',猜低了')
            draw_list.append('The ' + str(i) + ' guess:'+str(ai_number)+ u',too lower')
            lower_number = ai_number
            ai_number = (ai_number+upper_number)/2   
#    draw_list.append(u'第' + str(i+1) + u'次猜'+str(ai_number)+ u',猜对了')
    draw_list.append('Bingo! The ' + str(i+1) + ' guess: '+str(ai_number)+ ' is correct')
    return i+1
def alg2(guess_number):
#随机二分法
    global draw_list
    ai_number = 500
    lower_number = 0
    upper_number = 1000
    i = 0
#    draw_list.append(u'算法二：')
    draw_list.append('Algorithm 2:Random Dichotomy')
    while ai_number <> guess_number:
        i+=1
        if ai_number>guess_number:
#            draw_list.append(u'第' + str(i) + u'次猜'+str(ai_number)+ u',猜高了')
            draw_list.append('The ' + str(i) + ' guess:'+str(ai_number)+ u',too high')
            upper_number = ai_number
            ai_number = random.randint(lower_number+1,ai_number-1)
        else:
#            draw_list.append(u'第' + str(i) + u'次猜'+str(ai_number)+ u',猜低了')
            draw_list.append('The ' + str(i) + ' guess:'+str(ai_number)+ u',too lower')
            lower_number = ai_number
            ai_number = random.randint(ai_number+1,upper_number-1)   
#    draw_list.append(u'第' + str(i+1) + u'次猜'+str(ai_number)+ u',猜对了')
    draw_list.append('Bingo! The ' + str(i+1) + ' guess:'+str(ai_number)+ ' is correct')
    return i+1
    pass
    
def ai_handler():
#可点击此按钮等同于用户input后按回车   
    ai_input_handler(obj_ai_input.get_text())
    pass

def review_handler():
    if timer.is_running():
        timer.stop()
    else:
        timer.start()
    pass

def is_int(txt):
    global draw_list
    _is_int = all(c in "0123456789" for c in txt)
    if _is_int and txt<>'':     
        return True
    else:
        return False
    pass

def timer_handler():
    global draw_list
    global step
    if step<=len(review_list)+1:
        step+=1
        draw_list = review_list[0:step]
    pass
class DrawText():
#此类用于在画布上写文字，支持多行
    def __init__(self,ls):
        self.ls = ls
        
    def __str__(self):
        return ls
    
    def draw(self,canvas,pos):
        ls = self.ls
        for l in ls:
            pos[1] = pos[1] + 15
            canvas.draw_text(str(l), pos, 15, "Red")
#            canvas.draw_text(u'打印', pos, 20, "Red")
        return pos
    def set_ls(self,ls):
        self.ls = ls
        



# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 800   )
frame.set_canvas_background('white')
#frame.add_button(u"我猜", ai_guess_handler)
obj_ai_input = frame.add_input(u"输入你的数字[0,1000]让电脑猜猜",ai_input_handler,50)
timer = simplegui.create_timer(600,timer_handler)

frame.add_button(u"回车或者点击此处开始", ai_handler)
frame.add_button(u"回放", review_handler)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
