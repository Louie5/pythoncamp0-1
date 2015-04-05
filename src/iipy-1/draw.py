# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.
#第二个提交版本
# import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simplegui
import math
import time
draw_para = []
color = 'red'
shape = 'circle'
radius = 20
order = 0
step_order = 0
line = 2
interval = 500
review_para = []
auto_step_order = 0
# Handler for mouse click
def square():
    global shape 
    shape = 'square'
    pass

def circle():
    global shape 
    shape = 'circle'
    pass

def triangle():
    global shape 
    shape = 'triangle'
    pass

def color_input(col):
    global color
    color = col
    pass

def distance(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
    pass

def auto_review():
    global timer
#点击自动回放开关   
    if timer.is_running():      
        timer.stop()
    else:
        timer = simplegui.create_timer(interval,timer_handler)
        timer.start()
    pass

def review_step():
#点击手动回放    
    global draw_para,order,step_order
    draw_para = []
    order = len(review_para)
    if step_order<order:
        step_order+=1
        for j in range(0,step_order):
            if j<len(review_para):
                draw_para.append(review_para[j])                
    else:
        step_order = 0


    pass


def click(position):
    global draw_para,order,interval,step_order,review_para,re_step_order

#    if distance(position,obj_pos) < radius:
        # 删掉这个图案
#        pass  
    x = position[0]
    y = position[1]
    if shape == 'circle':
        p = [x,y]
    elif shape == 'square':
        p = [(x-radius,y-radius),(x+radius,y-radius),(x+radius,y+radius),(x-radius,y+radius)]
    elif shape == 'triangle':
        p = [(x,y+radius),(x-radius,y-radius/2),(x+radius,y-radius/2)]
    else:
        pass
    order += 1
    if order <=1024:
        draw_para.append([p,color,shape])
    review_para = draw_para


def set_interval(txt):
    global interval
    interval = int(txt)
    pass

def timer_handler():
    global draw_para,order,review_para,auto_step_order
    draw_para= []
    order = len(review_para)
    if auto_step_order<order:
        auto_step_order+=1
        for j in range(0,auto_step_order):
            if j<len(review_para):
                draw_para.append(review_para[j])                
    else:
        auto_step_order = 0       
    pass       
# Handler to draw on canvas
def draw(canvas):
#    print draw_para
# draw_para has three parameter :position  color shape
    for tmp_para in draw_para:        
        if tmp_para[2]=='circle':
            canvas.draw_circle(tmp_para[0] , radius , line , tmp_para[1], tmp_para[1])
        else:
            canvas.draw_polygon(tmp_para[0] , line , tmp_para[1], tmp_para[1])
        
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Draw", 500, 500)
frame.set_canvas_background('white')
frame.add_label('- Please select shape - ')
frame.add_button('circle',circle,100)
frame.add_button("square", square,100)
frame.add_button("triangle", triangle,100)
frame.add_label('   ')
color_input = frame.add_input('- Please input color as red/blue/#FF00EE',color_input,100)
color_input.set_text('red')
frame.add_label('   ')
frame.add_button('review-by-step',review_step,200)
frame.add_label('  ')
interval_input = frame.add_input('- review interval as millisecond',set_interval,100)
interval_input.set_text('500')
frame.add_button('auto review/stop review',auto_review,200)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(interval,timer_handler)
# Start the frame animation
frame.start()
