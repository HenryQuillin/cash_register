import simplegui

base = 0

def input_base(b):
    global base 
    base = int(b)
    print (base) 

def add1():
    global base 
    base = base + 1 
    print (base) 
    
def add5():
    global base 
    base = base + 5 
    print (base) 
    
def add25():
    global base 
    base = base + 25
    print (base) 
    
def add50():
    global base 
    base = base + 50
    print (base) 
    
def add100():
    global base 
    base = base + 100 
    print (base) 
    
def add1000():
    global base 
    base = base + 1000 
    print (base) 
    
    
def sub1():
    global base 
    base = base - 1 
    print (base) 
    
def sub10():
    global base 
    base = base - 10 
    print (base)

def sub25():
    global base 
    base = base - 25 
    print (base) 
    
def sub50():
    global base 
    base = base - 50 
    print (base) 
    
def sub100():
    global base 
    base = base - 100 
    print (base) 
    
def sub1000():
    global base 
    base = base - 1000 
    print (base) 

def draw(canvas):
    canvas.draw_text("" + str(base), (366,250), 42, "Aqua", "monospace")
    canvas.draw_text("Cash Register", (250,100), 50, "Red", "monospace")
    canvas.draw_line([0, 150], [900, 150], 20, 'Blue',)



register = simplegui.create_frame('Testing', 800, 700)

register.start()

register.add_input("base", input_base, 100)
register.add_button("add 1", add1, 100) 
register.add_button("add 5", add5, 100) 
register.add_button("add 25", add25, 100) 
register.add_button("add 50", add50, 100) 
register.add_button("add 100", add100, 100) 
register.add_button("add 1000", add1000, 100) 

register.add_button("subtract 1", sub1, 100) 
register.add_button("subtract 10", sub10, 100) 
register.add_button("subtract 25", sub25, 100)
register.add_button("subtract 50", sub50, 100) 
register.add_button("subtract 100", sub100, 100) 
register.add_button("subtract 1000", sub1000, 100) 

register.set_draw_handler(draw)







