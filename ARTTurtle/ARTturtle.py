from tkinter import *
from tkinter import  messagebox
import turtle as tr
from random import randint
from PIL import Image , ImageGrab







def MAIN(working_width,working_height,isfullscreen=False):

    
    mywindow = Tk()
    mywindow.title("ARTTurtle")
    mywindow.geometry(f"{working_width}x{working_height}+0+0")
    mywindow.resizable(False, False)
    mywindow.iconphoto(False,PhotoImage(file='ARTicon.png'))

    if isfullscreen:
        mywindow.attributes("-fullscreen",True)
        mywindow.bind("<F11>",lambda event: mywindow.attributes("-fullscreen",True))
        mywindow.bind("<Escape>",lambda event: mywindow.attributes("-fullscreen",False))
    else:
        pass

    def background_resizing():
        background_size = (mywindow.winfo_width(), mywindow.winfo_height())
        backgroundimg_original = Image.open(r"Original_Images/3dbackground2.png")
        backgroundimg = backgroundimg_original.copy()
        backgroundimg = backgroundimg.resize(background_size)
        backgroundimg.save(r"Images/3dbackground2.png")
    background_resizing()



    backgroundimg=PhotoImage(file='Images/3dbackground2.png',height=mywindow.winfo_height(),width = mywindow.winfo_width())
    back_label = Label(mywindow,image=backgroundimg)
    back_label.place(relx=0,rely=0)

    window_width=int(mywindow.winfo_width())
    window_height=int(mywindow.winfo_height())
    global h_2 , w_2
    h_2 =  window_height/2
    w_2 = window_width/2
    button_relheight=int(window_height*0.05)
    button_relwidth=int(window_width*0.125)

    canvas_width=int(window_width*0.6875)
    canvas_height=int(window_height*0.8666)
    global mean

    mean=(canvas_width+canvas_height)/2

    mycanvas = Canvas(mywindow ,width=canvas_width ,height= canvas_height)
    mycanvas.place(relx=0.15625,rely=0.13333)


    myscreen = tr.TurtleScreen(mycanvas)



    FONT=("times", 10, "bold")
    Majortext=StringVar()
    Majortext.set("Welcome to ArtTurtle...")
    Rvar=IntVar()
    Rvar.set(0)
    colorselectionbyuser=StringVar()
    colorselectionbyuser.set('red')
    colorlabel=StringVar()
    colorlabel.set("Select a color:")
    notesinframe=StringVar()
    notesinframe.set("ArtTurtle by MAT.")
    designname=StringVar()
    designname.set('')




    def images_resizing():
        button_size = (button_relwidth, button_relheight)

        blueshadesimg_original = Image.open(r"Original_Images/blueshadesimg.png")
        blueshadesimg = blueshadesimg_original.copy()
        blueshadesimg = blueshadesimg.resize(button_size)
        blueshadesimg.save(r"Images/blueshadesimg.png")
        
        sunflowerimg_original = Image.open(r"Original_Images/sunflowerimg.png")
        sunflowerimg = sunflowerimg_original.copy()
        sunflowerimg = sunflowerimg.resize(button_size)
        sunflowerimg.save(r"Images/sunflowerimg.png")

        endimg_original = Image.open(r"Original_Images/endimg.png")
        endimg = endimg_original.copy() 
        endimg = endimg.resize(button_size)
        endimg.save(r"Images/endimg.png")

        
        hexa2img_original = Image.open(r"Original_Images/hexa2img.png")
        hexa2img = hexa2img_original.copy()
        hexa2img = hexa2img.resize(button_size)
        hexa2img.save(r"Images/hexa2img.png")

        pentagonsimg_oroginal = Image.open(r"Original_Images/pentagonsimg (3).png")
        pentagonsimg = pentagonsimg_oroginal.copy()
        pentagonsimg = pentagonsimg.resize(button_size)
        pentagonsimg.save(r"Images/pentagonsimg (3).png")

        squaresimg_original = Image.open(r"Original_Images/squaresimg.png")
        squaresimg = squaresimg_original.copy()
        squaresimg = squaresimg.resize(button_size)
        squaresimg.save(r"Images/squaresimg.png")

        hexagonsimg_original = Image.open(r"Original_Images/hexagonsimg.png")
        hexagonsimg = hexagonsimg_original.copy()
        hexagonsimg = hexagonsimg.resize(button_size)
        hexagonsimg.save(r"Images/hexagonsimg.png")
        
        spiralimg_original = Image.open(r"Original_Images/spiralimg.png")
        spiralimg = spiralimg_original.copy()
        spiralimg = spiralimg.resize(button_size)
        spiralimg.save(r"Images/spiralimg.png")

        starsimg_original = Image.open(r"Original_Images/starsimg.png")
        starsimg = starsimg_original.copy()
        starsimg = starsimg.resize(button_size)
        starsimg.save(r"Images/starsimg.png")

        
        screenshoticon_width = int(0.0375*window_width)
        screenshoticon_height = int(0.05*window_height)
        screenshoticon_original = Image.open(r"Original_Images/screenshoticon.png")
        screenshoticon = screenshoticon_original.copy()
        screenshoticon = screenshoticon.resize((screenshoticon_width,screenshoticon_height))
        screenshoticon.save(r"Images/screenshoticon.png")

        repairicon_original = Image.open(r"Original_Images/repair_icon.png")
        repairicon = repairicon_original.copy()
        repairicon = repairicon.resize((screenshoticon_width,screenshoticon_height))
        repairicon.save(r"Images/repair_icon.png")

        
    images_resizing()

    screenshoticon_width = int(0.0375*window_width)
    screenshoticon_height = int(0.05*window_height)

    blueshadesimg=PhotoImage(file='Images/blueshadesimg.png',height=button_relheight,width=button_relwidth)
    sunflowerimg=PhotoImage(file='Images/sunflowerimg.png',height=button_relheight,width=button_relwidth)
    endimg=PhotoImage(file='Images/endimg.png',height=button_relheight,width=button_relwidth)
    pentagonsimg=PhotoImage(file='Images/pentagonsimg (3).png',height=button_relheight,width=button_relwidth)
    squaresimg=PhotoImage(file='Images/squaresimg.png',height=button_relheight,width=button_relwidth)
    hexagonsimg=PhotoImage(file='Images/hexagonsimg.png',height=button_relheight,width=button_relwidth)
    spiralimg=PhotoImage(file='Images/spiralimg.png',height=button_relheight,width=button_relwidth)
    starsimg=PhotoImage(file='Images/starsimg.png',height=button_relheight,width=button_relwidth)
    repairimg = PhotoImage(file='Images/repair_icon.png',width = screenshoticon_width, height= screenshoticon_height)
    hexa2img=PhotoImage(file='Images/hexa2img.png',height=button_relheight,width=button_relwidth)
    screenshotimg = PhotoImage(file= 'Images/screenshoticon.png',width = screenshoticon_width, height= screenshoticon_height)


    
    
    Label_fontsize = int(0.0425*window_width)
    master_label= Label(mywindow, textvariable= Majortext,
                        fg="white",relief='flat',bg='#9F9C9C'
                        , font=("times",Label_fontsize,"bold italic"))
    master_label.place(relx=0.15875,rely=0.005)

    Bpurplepentagons= Button(image=pentagonsimg , activebackground="#C0C0C0",bd=4,
            command=lambda:myturtle.purplepentagons(),bg='#808080',cursor = "cross_reverse")
    Bpurplepentagons.place(relx=0.0125,rely=0.1416)

    BSquares= Button(activebackground="#C0C0C0",bd=4,cursor = "cross_reverse"
            ,image =squaresimg,command=lambda:myturtle.square24(),bg='#808080')
    BSquares.place(relx=0.0125,rely= 0.233)

    BHexagons= Button( activebackground="#C0C0C0",cursor = "cross_reverse",
            bd=4,image=hexagonsimg,font=FONT,command=lambda:myturtle.hexagons(),bg='#808080')
    BHexagons.place(relx= 0.0125,rely= 0.33)

    BSpiral= Button( activebackground="#C0C0C0",image=spiralimg,cursor = "cross_reverse",
            bd=4,font=FONT,command=lambda:myturtle.spiralsquares(),bg='#808080')
    BSpiral.place(relx=0.0125,rely= 0.433)

    BHexa2= Button( activebackground="#C0C0C0",image=hexa2img,cursor = "cross_reverse",
            bd=4,bg='#808080',font=FONT,command=lambda:myturtle.hexagons2())
    BHexa2.place(relx= 0.0125,rely= 0.533)

    BStars= Button(image=starsimg, activebackground="#C0C0C0",cursor = "cross_reverse",
            font=FONT,bd=4,bg='#808080',command = lambda:myturtle.bigspiral())
    BStars.place(relx= 0.0125,rely= 0.633)

    Bcircles= Button(image=blueshadesimg, activebackground="#C0C0C0",cursor = "cross_reverse",
            bd=4,font=FONT,command= lambda:myturtle.Blue_shades(),bg='#808080')
    Bcircles.place(relx= 0.0125,rely= 0.733)

    Bsunflower= Button(image=sunflowerimg, activebackground="#C0C0C0",cursor = "cross_reverse",
            bd=4,font=FONT,command= lambda:myturtle.sunflower(),bg='#808080')
    Bsunflower.place(relx= 0.0125,rely= 0.8333)

    Bdone = Button(image=endimg,bd=4,font=FONT,activebackground="#C0C0C0",command=lambda:myturtle.done(),bg='#808080',cursor = "cross_reverse")
    Bdone.place(relx=0.0125,rely=0.9166)



    radiolabel=Label(text="Color mode:",bg="silver",font=FONT)
    radiolabel.place(relx=0.85625,rely=0.14166)

    Radio0= Radiobutton(mywindow,text="Mode1",bg="silver",value=0,variable=Rvar,cursor = "dot",font=FONT,command=lambda:Rvar.set(0))
    Radio0.place(relx=0.85625,rely=0.16666)

    Radio1= Radiobutton(mywindow,text="Mode2",bg="silver",value=1,variable=Rvar,cursor = "dot",font=FONT,command=lambda:Rvar.set(1))
    Radio1.place(relx=0.85625,rely=0.21666)

    Radio2= Radiobutton(mywindow,text="Mode3",bg="silver",value=2,variable=Rvar,cursor = "dot",font=FONT,command=lambda:Rvar.set(2))
    Radio2.place(relx=0.85625,rely=0.26666)

    Radio3= Radiobutton(mywindow,bg="silver",text="Mode4",value=3,variable=Rvar,cursor = "dot",font=FONT,command=lambda:Rvar.set(3))
    Radio3.place(relx=0.85625,rely=0.31666)

    colorselectionlabel=Label(font=FONT,bg="silver",textvariable=colorlabel,fg="black")
    colorselectionlabel.place(relx=0.85625,rely=0.36666)

    colorEntry = Entry (font=FONT , bd=4, textvariable=colorselectionbyuser,width=(int(0.0125*window_width)))
    colorEntry.place(relx=0.85625,rely=0.41666)

    notesframe = LabelFrame(text="Notes",bd=3,width=(int(0.13*window_width)),height=int(0.5*window_height),bg="#E0E0E0")
    notesframe.place(relx=0.85625,rely=0.46666)

    FONT_SIZE = int(0.01*window_width)
    notes = Label(master=notesframe,textvariable=notesinframe,font=("times",FONT_SIZE,"italic"),)
    notes.place(relx=0,rely=0.01666)

    Binfo = Button(bitmap="info",bd=2,fg="gray",width=(int(0.0375*window_width)),height=(int(0.05*window_height)),command=lambda:messagebox.showinfo("Information","Welcome to ARTTurtle By MAT\nYou will find any information you need in README.txt in ARTturtle folder\nIf you are in fullscreenmode press ESC to exit or F11 to activate fullscreen\nFor any suggestions:\ngmail: MAT.611.MAT@gmail.com"))
    Binfo.place (relx=0.9475,rely=0.03333)

    def repair():
        result=messagebox.askokcancel("Wait","You are about to return to the customization window\n Do you want to continue?")
        if result:
            mywindow.destroy()
            customization()
        else:
            pass


    Brepair = Button(cursor = "cross_reverse",command=repair,bd=3,image=repairimg).place(relx=0.85,rely=0.03333)


    global screenshot_num
    screenshot_num = randint(1,1000)


    def take_screenshot():
        global screenshot_num
        screenshot_relx = int(0.15625*mywindow.winfo_width())
        screenshot_rely = int(0.13333*mywindow.winfo_height())
        taken_screenshot = ImageGrab.grab().save(f"Screenshots/screenshot{screenshot_num}.png")
        screenshot_num += 1


    Btakescreenshot=Button(cursor = "cross_reverse",bd=3,image=screenshotimg,command=take_screenshot).place(relx = 0.90,rely = 0.033333)


    class Design:
    
    
        def __init__(self,name,defualt_color="red",pen_size=2,speed=5,length=150,color_start=0):
            
            
            self.name=name
            self.defualt_color=defualt_color
            self.pen_size=pen_size
            self.speed=speed
            self.length=length
            self.name=tr.RawTurtle(mycanvas)
            self.color_start=color_start
            global free
            free = True

        
        def preparation(self):
            self.name.clear()
            self.name.pu()
            self.name.home()
            self.name.pd()
            self.name.pensize(self.pen_size)
            self.name.speed(self.speed)
            self.name.color(self.defualt_color)     
            self.color_start=0
        
        def colormode_change(self):
            
            Colormode_detection = Rvar.get()
            if Colormode_detection == 0:
                self.name.color(self.defualt_color)
                
                selectedcolor=colorselectionbyuser.get()
                try:
                    if selectedcolor=='':
                        raise Exception
                    self.name.color(selectedcolor)
                    self.defualt_color=selectedcolor
                    notesinframe.set(f'{designname.get()}\ncolormode {Colormode_detection+1}\nColor set to : {selectedcolor}')
                except:
                    self.name.color(self.defualt_color)
                    notesinframe.set("Invalid color...")
                    pass
                    
            elif Colormode_detection == 1:
                
                r = randint(0.0,1.0)
                g = randint(0.0,1.0)
                b = randint(0.0,1.0)
                self.name.color(r,g,b)
                notesinframe.set(f'{designname.get()}\nColormode {Colormode_detection+1}\ncolor set to: Random ')
                
                
            elif Colormode_detection == 2:
                try:
                    colors2=["#FC766A","#5B84B1","#FC766A","#5B84B1"]
                    COLORchoosing=colors2[self.color_start]
                    self.name.color(COLORchoosing)
                    self.color_start+=1
                    notesinframe.set(f'{designname.get()}\nColormode {Colormode_detection+1}\nColor set to :\n{COLORchoosing} ')
                except:
                    self.color_start=0
                
                
            elif Colormode_detection ==3:

                colors = [(1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00),
                (1.00, 0.07, 0.00), (1.00, 0.10, 0.00), (1.00, 0.12, 0.00),
                (1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00),
                (1.00, 0.23, 0.00), (1.00, 0.25, 0.00), (1.00, 0.28, 0.00),
                (1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00),
                (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00),
                (1.00, 0.45, 0.00), (1.00, 0.47, 0.00), (1.00, 0.50, 0.00),
                (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00),
                (1.00, 0.60, 0.00), (1.00, 0.62, 0.00), (1.00, 0.65, 0.00),
                (1.00, 0.68, 0.00), (1.00, 0.70, 0.00), (1.00, 0.72, 0.00),
                (1.00, 0.75, 0.00), (1.00, 0.78, 0.00), (1.00, 0.80, 0.00),
                (1.00, 0.82, 0.00), (1.00, 0.85, 0.00), (1.00, 0.88, 0.00),
                (1.00, 0.90, 0.00), (1.00, 0.93, 0.00), (1.00, 0.95, 0.00),
                (1.00, 0.97, 0.00), (1.00, 1.00, 0.00), (0.95, 1.00, 0.00),
                (0.90, 1.00, 0.00), (0.85, 1.00, 0.00), (0.80, 1.00, 0.00),
                (0.75, 1.00, 0.00), (0.70, 1.00, 0.00), (0.65, 1.00, 0.00),
                (0.60, 1.00, 0.00), (0.55, 1.00, 0.00), (0.50, 1.00, 0.00),
                (0.45, 1.00, 0.00), (0.40, 1.00, 0.00), (0.35, 1.00, 0.00),
                (0.30, 1.00, 0.00), (0.25, 1.00, 0.00), (0.20, 1.00, 0.00),
                (0.15, 1.00, 0.00), (0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
                (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10),
                (0.00, 0.85, 0.15), (0.00, 0.80, 0.20), (0.00, 0.75, 0.25),
                (0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40),
                (0.00, 0.55, 0.45), (0.00, 0.50, 0.50), (0.00, 0.45, 0.55),
                (0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70),
                (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85),
                (0.00, 0.10, 0.90), (0.00, 0.05, 0.95), (0.00, 0.00, 1.00),
                (0.05, 0.00, 1.00), (0.10, 0.00, 1.00), (0.15, 0.00, 1.00),
                (0.20, 0.00, 1.00), (0.25, 0.00, 1.00), (0.30, 0.00, 1.00),
                (0.35, 0.00, 1.00), (0.40, 0.00, 1.00), (0.45, 0.00, 1.00),
                (0.50, 0.00, 1.00), (0.55, 0.00, 1.00), (0.60, 0.00, 1.00),
                (0.65, 0.00, 1.00), (0.70, 0.00, 1.00), (0.75, 0.00, 1.00),
                (0.80, 0.00, 1.00), (0.85, 0.00, 1.00), (0.90, 0.00, 1.00),
                (0.95, 0.00, 1.00)]
                try:
                    idx=int(self.color_start)
                    idx2=colors[idx]
                    self.name.color(idx2)
                    self.color_start+=0.125
                    notesinframe.set(f'{designname.get()}\nColormode {Colormode_detection+1} ')
                except:
                    self.color_start=0
                    pass

        def purplepentagons(self):
            global free
            try:
                if free:
                    Majortext.set('Working...')
                    notesinframe.set('Purple Pentagons\nColormode: Special')
                    self.preparation()
                    self.name.speed(10)
                    # tr.colormode(255)
                    self.name.pencolor("black")
                    h = 7
                    free = False
                    for j in range(18):
                        for i in range(5):
                            self.name.forward(h)
                            self.name.right(75)
                        self.name.forward(5)
                        self.name.right(5)
                    self.name.penup()
                    self.name.goto(-16, 20)
                    self.name.pendown()
                    h = 50
                    self.name.pencolor("plum")
                    for j in range(18):
                        for i in range(5):
                            self.name.forward(h)
                            self.name.right(75)
                        self.name.forward(5)
                        self.name.right(5)
                    self.name.penup()
                    self.name.goto(-36, 44)
                    self.name.pendown()
                    h = 100
                    self.name.pencolor("indigo")
                    for j in range(18):
                        for i in range(5):
                            self.name.forward(h)
                            self.name.right(75)
                        self.name.forward(5)
                        self.name.right(5)
                    self.name.penup()
                    self.name.goto(-71, 86)
                    self.name.pendown()
                    h = 190
                    self.name.pencolor("blueviolet")
                    for j in range(18):
                        for i in range(5):
                            self.name.forward(h)
                            self.name.right(75)
                        self.name.forward(5)
                        self.name.right(5)
                    Majortext.set('Purple Pentagons!')
                    free = True
                else:
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')


        def square24(self) :
        
            global free
            try:
                if free:
                    Majortext.set("Working...")
                    self.preparation()
                    self.name.speed(10)
                    free=False
                    designname.set(f'72 Squares')

                    for I in range (72):
                        self.colormode_change()
                        for I in range (4):
                            self.name.fd(self.length)
                            self.name.right(90)
                        self.name.right(5)
                        continue 
                    Majortext.set("Just warming up.!")
                    free = True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')



        
        

        def hexagons(self):
            global free
            try:
                if free:
                    designname.set(f'Hexagons')
                    Majortext.set("Working!")
                    self.preparation()
                    self.length=150
                    self.name.penup()
                    self.name.rt(45)
                    self.name.forward(45)
                    self.name.rt(135)
                    self.name.pendown()
                    self.name.speed(0)
                    free = False
                    for i in range(120):
                        self.colormode_change()
                        for j in range(6):
                            self.name.forward(self.length)
                            self.name.rt(61)
                        self.name.rt(11.1111)
                    Majortext.set("Hexagons!")
                    free =True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')

    

        def spiralsquares(self):
            global free
            try:
                if free:
                    designname.set(f'Spiral')
                    Majortext.set("Working!")
                    self.preparation()
                    free = False
                    for i in range(700):
                        self.colormode_change()
                        self.name.speed(0)
                        self.name.forward(50 + i)
                        self.name.rt(90.5)
                    Majortext.set("Spiral by Squares!")
                    free=True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')


    

        def hexagons2(self):
            global free
            try:
                if free:
                    
                    side=1
                    self.preparation()
                    self.name.pensize(4)
                    self.name.speed(10)
                    result=messagebox.askyesno('Wait','If this is the first time We recommend to set the colormode to 4 \n do you wanna do that?')
                    if result ==True:
                        Rvar.set(3)
                    else:
                        pass         
                    free=False
                    designname.set(f'Hexagons2')
                    Majortext.set("WORKING!")
                    for I in range (70):
                        for I in range (6):
                            self.colormode_change()
                            self.name.fd(side)
                            self.name.rt(60)
                            side+=1
                    Majortext.set("Hexagons2")
                    free=True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')





        def bigspiral (self):
            global free
            try:
                if free:
                    result=messagebox.askyesno('Wait','We recommend to set the colormode to 4 \n do you wanna do that?')
                    if result ==True:
                        Rvar.set(3)
                    else:
                        pass
                    self.preparation()
                    designname.set(f'Stars')

                    self.name.speed(0)
                    self.name.hideturtle()
                    free=False                
                    Majortext.set("Working!")
                    for I in range (800):
                        self.colormode_change()
                        self.name.fd(I)
                        self.name.right(98)
                        I+=1
                    Majortext.set("Stars?!")
                    free=True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')




        def Blue_shades(self):
            global free
            try:
                if free:
                    
                    self.preparation()
                    Majortext.set("Working...")
                    self.name.hideturtle()
                    self.name.speed(0)
                    clrs =["MidnightBlue", "Navy", "DarkBlue", "MediumBlue", "RoyalBlue", "MediumSlateBlue", "CornflowerBlue", "DodgerBlue", "DeepskyBlue", "LightSkyBlue", "SkyBlue", "LightBlue"]
                    free=False
                    notesinframe.set(f'Blue Shades\nColormode: Special')
                    for I in range (121):
                        length=50
                        r=20
                        idx1=0
                        for I in range (12):
                    
                            self.name.pencolor(clrs[idx1])
                            self.name.circle(r)
                            self.name.lt(90)
                            self.name.penup()
                            self.name.forward(length)
                            self.name.right(90)
                            self.name.pendown()
                            r *= 0.8
                            length *= 0.8 
                            self.name.circle(r)
                            idx1+=1
                            
                        self.name.penup()
                        self.name.goto(0,0)
                        self.name.fd(5)
                        self.name.right(3)
                        self.name.pendown()
                    Majortext.set("Blue Shades!")
                    free= True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')

            


        def sunflower(self):
            global free
            try:
                if free:
                    
                    Majortext.set("Working...")
                    self.preparation()
                    self.name.speed(0)
                    self.name.hideturtle()
                    free= False
                    notesinframe.set(f'Sunflower \nColormode: Special')
                    clrs = ["saddlebrown", "saddlebrown", "gold", "gold", "darkorange", "forestgreen", "forestgreen"]
                    length = 220
                    a=5
                    cn=6
                    for i in range(7):

                        self.name.pencolor(clrs[cn])

                        for j in range(72):

                            self.name.left(90)
                            self.name.forward(length)
                            self.name.circle(15)
                            self.name.right(180)
                            self.name.forward(length)
                            self.name.left(90)
                            self.name.forward(2)
                            self.name.right(a)

                        length = length/1.5
                        cn = cn-1
                    Majortext.set("Sunflower!")
                    free= True
                else :
                    notesinframe.set('Please wait...')
            except:
                Majortext.set('  ArtTurtle BY :')
                notesinframe.set('DONE!')

    


        def done (self):
            global free
            if free:
        
                result=messagebox.askyesno('END','Are you sure you wanna exit?\nBefore going on make sure you have tried each design and color mode.')
                if result:
                    mycanvas.destroy()
                    Majortext.set('  ArtTurtle BY :')
                    master_label.config(fg="#5C2863")
                    result=messagebox.showinfo('End','You have reached the end...\n I really hope you enjoyed.\n  For more information press info button in the NE corner of the app.')
                    notesinframe.set(' The END!')
                else:
                    pass

            else :
                notesinframe.set('Please wait...')

        
        
        
    myturtle=Design(name="myturtle",defualt_color="red")
    mywindow.mainloop()


####



def customization():
    global window_width, window_height


    customization_window = Tk()
    customization_window.resizable(False,False)

    customization_window.geometry("280x200")
    choosed_width=IntVar()
    choosed_height=IntVar()
    



    def customized():
        
        try:
            if choosed_width.get() == 0 or choosed_height.get() == 0:
                Label(customization_window,text='Cant be zero...      ',fg="red").place(x=70,y=130)

            elif isinstance((choosed_width.get()),int) and isinstance((choosed_height.get()),int):
                customization_window.destroy()
                MAIN(choosed_width.get(),choosed_height.get())

        except:
            Label(customization_window,text='Must be a number',fg="red").place(x=70,y=130)

    
    def fullscreen():
        window_width = customization_window.winfo_screenwidth()
        window_height = customization_window.winfo_screenheight()
        customization_window.destroy()
        MAIN(window_width,window_height,True)

        


    def defualt():
        window_width = 800
        window_height = 600
        customization_window.destroy()
        MAIN(window_width,window_height)
        



    Label(customization_window,text="Customization",font=("times",18,"bold")).place(x=65,y=5)
    Label(customization_window,text= 'To get the best result please keep the aspect ratio 4:3',fg="red",font=("times",7,"bold")).place(x=5,y=110)
    Label(customization_window,text="Enter screen width: ").place(x=0,y=50)
    Entry(customization_window,textvariable=choosed_width,width=10).place(x=200,y=50)
    Label(customization_window,text="Enter screen height: ").place(x=0,y=80)
    Entry(customization_window,textvariable=choosed_height,width=10).place(x=200,y=80)
    

    Button(customization_window,bitmap="info",width=20,height=20,command=lambda:messagebox.showinfo('info','Please enter the reselution you want the program to display in\n The defualt is 800x600!')).place(x=240,y=5)
    Button(customization_window,text= "Fullscreen", command = fullscreen).place(x=10,y=160)
    Button(customization_window,text= "Defualt",command = defualt).place(x=190,y=160)
    Button(customization_window,text="Start Customized",command=customized).place(x=80,y=160)



    customization_window.mainloop()

customization()


