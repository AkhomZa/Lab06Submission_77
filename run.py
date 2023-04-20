import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.color = (255,0,0)
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
        self.color = (255,0,0)
    
    def isMouseOn(self):
        (mx,my) = pg.mouse.get_pos()
        if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
            return True
        else:
            return False
        
    def isMousePress(self):
        (mx,my) = pg.mouse.get_pos()
        if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
            if pg.mouse.get_pressed()[0] == 1:
                return True
        else:
            return False

#EX1#
# pg.init()
# run = True
# win_x, win_y = 800, 480
# screen = pg.display.set_mode((win_x, win_y))
# btn = Button(win_x/2,win_y/2,100,100)

# while(run):
#     screen.fill((255, 255, 255))
#     if btn.isMousePress():
#         btn.color = (164,66,220)
#     elif btn.isMouseOn():
#         btn.color = (134,136,138)
#     else:
#         btn.color = (255,0,0)
#     btn.draw(screen)
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False





#EX2#
# pg.init()
# run = True
# win_x, win_y = 800, 480
# screen = pg.display.set_mode((win_x, win_y))
# sq = Rectangle(win_x/2,win_y/2,100,100)

# while(run):
#     screen.fill((255,255,255))
#     sq.draw(screen)
#     pg.display.update()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False
#         elif event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
#             sq.x += 10
#         elif event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม S
#             sq.y += 10
#         elif event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม A
#             sq.x -= 10
#         elif event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
#             sq.y -= 10
            

class InputBox:
    def __init__(self, x, y, w, h, isnum, isalpha,text='' ):
        self.rect =  pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.num = isnum
        self.char = isalpha

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.num == True:
                        if event.unicode.isnumeric():
                            self.text += event.unicode
                        else:
                            pass
                    if self.char == True:
                        if event.unicode.isalpha():
                            self.text += event.unicode
                        else:
                            pass
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('black') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('green')     # ^^^
FONT = pg.font.Font(None, 32)

firstname_box = InputBox(100, 100, 200, 32, False ,True)
lastname_box = InputBox(500, 100, 200, 32, False ,True)
age_box = InputBox(100, 200, 200, 32, True ,False)

input_boxes = [firstname_box, lastname_box,age_box] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize

firstname = font.render('FirstName', True, 'green', (49,51,53)) # (text,is smooth?,letter color,background color)
textRect = firstname.get_rect() # text size
lastname = font.render('LastName', True, 'green', (49,51,53)) # (text,is smooth?,letter color,background color)
textRect = firstname.get_rect() # text size
age = font.render('Age', True, 'green', (49,51,53)) # (text,is smooth?,letter color,background color)
textRect = firstname.get_rect() # text size
textRect.center = (win_x // 2, win_y // 2)

submit = Button(450,200,150,100)
submittext = font.render('SUBMIT', True, 'white', 'red') # (text,is smooth?,letter color,background color)
textRect = firstname.get_rect() # text size
submitpress = False

run = True

while run:
    screen.fill((49,51,53))
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    submit.draw(screen)

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    screen.blit(firstname,(100,60))
    screen.blit(lastname,(500,60))
    screen.blit(age,(100,160))
    screen.blit(submittext,(462.5,235))
    
    if submit.isMouseOn():
        if submit.isMousePress():
            submitpress = True
    if submitpress:
        screen.blit(font.render('Hello ' + firstname_box.text + '  '+ lastname_box.text +'! '+ 'You are ' + age_box.text + ' year olds', True, 'green', (49,51,53)),(50,400))

    pg.time.delay(1)
    pg.display.update()