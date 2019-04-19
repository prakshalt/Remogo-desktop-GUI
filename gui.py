import wx
import  wx.lib.intctrl
import urllib2
import cookielib
from getpass import getpass
import sys
import webbrowser
import os
from stat import *
class MainWindow(wx.Frame):
    def __init__(self):
        btnfont = wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD)
        lbfont = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        title='Remogo'
        wx.Frame.__init__(self, None, wx.ID_ANY,title)
        #icon = wx.EmptyIcon()
        icon=wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Centre()
        self.SetSize(500, 600)
        self.Show(True)
        wx.Frame.SetBackgroundColour(self,(255,255,255))
        #wx.Frame.SetTransparent(self,200)
        self.HBox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.vBox = wx.BoxSizer(wx.VERTICAL) 
        self.Submit = wx.Button(self.panel, id=wx.ID_ANY, name="Submit",label="Submit")
        self.Submit.SetBackgroundColour((104,154,146))
        self.Submit.SetFont(btnfont)
        self.Submit.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOversub)
        self.Submit.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavesub)
        self.Submit.Bind(wx.EVT_BUTTON, self.onButton)
        self.t1=wx.lib.intctrl.IntCtrl(self.panel)
        self.t1.SetLongAllowed(True)
        #self.t1.SetNoneAllowed(True)
        #self.t1.SetValue()
        self.t2=wx.TextCtrl(self.panel,style = wx.TE_PASSWORD)
        self.t1.SetBackgroundColour((240,230,140))
        self.t2.SetBackgroundColour((240,230,140))
        self.t1.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOvernum)
        self.t1.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavenum)
        self.t2.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOverpwd)
        self.t2.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavepwd)
        self.l1 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="Enter Phone Number")
        self.l1.SetFont(lbfont)
        self.l2 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="Enter Password")
        self.l2.SetFont(lbfont)
        self.l3 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="Note:10 digits number only")
        self.l3.SetFont(lbfont)
        self.l3.SetForegroundColour((255,0,0))
        self.HBox1.Add(self.l1,0,0)
        self.HBox1.AddSpacer(10) 
        self.HBox1.Add(self.t1,0,   wx.ALIGN_RIGHT,0)
        self.HBox2.Add(self.l2,0,wx.ALL,0)
        self.HBox2.AddSpacer(44)
        self.HBox2.Add(self.t2,0,wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT,0)
        self.HBox3.AddSpacer(100)
        self.HBox3.Add(self.Submit,0,wx.ALIGN_CENTRE_HORIZONTAL,0)
        self.vBox.Add(self.HBox1)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.l3,0,0)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.HBox2)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.HBox3)
        #self.vBox.Add(self.Submit,1,wx.ALIGN_CENTER_HORIZONTAL,10)
       # self.panel.SetSizer(self.HBox)
        self.panel.SetSizer(self.vBox)
        self.makeMenuBar()
        #self.MenuBar.SetFont(btnfont)
        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((255,255,255))
        self.SetStatusText("Welcome to Remogo!")
       
        
    def OnSize(self, event):
       # hsize = event.GetSize()[0] 
        #self.SetSizeHints(minW=-1, minH=hsize, maxH=hsize)
        #self.SetTitle(str(event.GetSize()))
        self.SetSize(500,600)
        self.Centre()
        
    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutitem=helpMenu.Append(-1,"About","about")
        helpMenu.AppendSeparator()
        docItem = helpMenu.Append(-1,"Docs\tCtrl-H","docs")
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.Ondocs, docItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutitem)

    def OnExit(self, event):
        self.Close(True)
    def OnAbout(self, event):
        wx.MessageBox("Remogo",
                      "About Remogo",
                      wx.OK|wx.ICON_INFORMATION)
    
    def Ondocs(self, event):
        wx.MessageBox("Redirecting you to website")
        url='www.google.com'
        webbrowser.open(url, new=0, autoraise=True)

    def OnHello(self, event):
        wx.MessageBox("Hello from Remogo")

    def onMouseOversub(self, event):
        self.Submit.SetBackgroundColour((94,121,116))
        self.SetStatusText("Submit Button") 
        event.Skip()

    def onMouseLeavesub(self, event):
        self.Submit.SetBackgroundColour((104,154,146))
        self.SetStatusText("Welcome to Remogo!")
        event.Skip()

    def onMouseOvernum(self, event):
        self.t1.SetBackgroundColour((211,211,211))
        self.SetStatusText("Enter Phone number to send sms to") 
        event.Skip()

    def onMouseLeavenum(self, event):
        self.t1.SetBackgroundColour((240,230,140))
        self.SetStatusText("Welcome to Remogo!")

    def onMouseOverpwd(self, event):
        self.t2.SetBackgroundColour((211,211,211))
        self.SetStatusText("Enter its password set on the mobile app") 
        event.Skip()

    def onMouseLeavepwd(self, event):
        self.t2.SetBackgroundColour((240,230,140))
        self.SetStatusText("Welcome to Remogo!")
        
    def Exit(self):
        self.Close(True)

    def onButton(self, event):
        global t1_val
        t1_val=self.t1.GetValue()
        global t2_val
        t2_val=self.t2.GetValue()
        def isNotBlank(myString):
            return bool(myString and myString.strip())
        if isNotBlank(t2_val) and t1_val!=0:
            global win
            win = sendwindow()
            win.Show()
            frame.Exit()
        else:
            wx.MessageBox("Mobile Number or password left blank")
       # print "The button you pressed was labeled: " + button_by_id.GetLabel()
       # print "The button's name is " + button_by_id.GetName()
        #print t1_val



class sendwindow(wx.Frame):
    def __init__(self):
        btnfont = wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD)
        lbfont = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        wx.Frame.__init__(self, None, wx.ID_ANY, "Remogo")
        icon=wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.Centre()
        self.SetSize(500, 600)
        self.Show(True)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.panel = wx.Panel(self, wx.ID_ANY)
        wx.Frame.SetBackgroundColour(self,(255,255,255))
        self.vBox1 = wx.BoxSizer(wx.VERTICAL)
        self.hBox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.l1 = wx.StaticText(self.panel,-1,style =wx.ST_NO_AUTORESIZE,label="Sending to "+str(t1_val))
        self.l1.SetFont(lbfont)
        self.l1.SetForegroundColour((255,0,0))
        self.findphbtn = wx.Button(self.panel, id=wx.ID_ANY, name="findphbtn",label="Find my phone")
        self.findphbtn.SetBackgroundColour((104,154,146))
        self.findphbtn.SetFont(btnfont)
        self.remsil = wx.Button(self.panel, id=wx.ID_ANY, name="remsilbtn",label="Remote Ringer/Silent")
        self.remsil.SetBackgroundColour((104,154,146))
        self.remsil.SetFont(btnfont)
        self.remlock = wx.Button(self.panel, id=wx.ID_ANY, name="remlockbtn",label="Remote Lock")
        self.remlock.SetBackgroundColour((104,154,146))
        self.remlock.SetFont(btnfont)
        self.back = wx.Button(self.panel, id=wx.ID_ANY, name="back",label="Back")
        self.back.SetBackgroundColour((104,154,146))
        self.back.SetFont(btnfont)
        self.vBox1.AddSpacer(10)
        self.hBox5.Add(self.l1,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)
        self.vBox1.Add(self.hBox5)
        self.vBox1.AddSpacer(10)
        self.hBox1.AddSpacer(70)
        self.hBox1.Add(self.remsil,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)
        self.vBox1.Add(self.hBox1)
        self.vBox1.AddSpacer(10)
        self.hBox2.AddSpacer(70)
        self.hBox2.Add(self.findphbtn,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)
        self.vBox1.Add(self.hBox2)
        self.vBox1.AddSpacer(10)
        self.hBox3.AddSpacer(70)
        self.hBox3.Add(self.remlock,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)
        self.vBox1.Add(self.hBox3)
        self.vBox1.AddSpacer(10)
        self.hBox4.AddSpacer(70)
        self.hBox4.Add(self.back,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)
        self.vBox1.Add(self.hBox4)
        self.panel.SetSizer(self.vBox1)
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Remogo!")
        self.findphbtn.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOverfindph)
        self.findphbtn.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavefindph)
        self.findphbtn.Bind(wx.EVT_BUTTON, self.onButtonfindph)
        self.remsil.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOverremsil)
        self.remsil.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeaveremsil)
        self.remsil.Bind(wx.EVT_BUTTON, self.onButtonremsil)
        self.remlock.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOverremlock)
        self.remlock.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeaveremlock)
        self.remlock.Bind(wx.EVT_BUTTON, self.onButtonremlock)
        self.back.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOverback)
        self.back.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeaveback)
        self.back.Bind(wx.EVT_BUTTON, self.onButtonback) 

    def onMouseOverfindph(self, event):
            # mouseover changes colour of button
            self.findphbtn.SetBackgroundColour((94,121,116))
            self.SetStatusText("Find My Phone Button ")
            event.Skip()

    def OnSize(self, event):
       # hsize = event.GetSize()[0] 
        #self.SetSizeHints(minW=-1, minH=hsize, maxH=hsize)
        #self.SetTitle(str(event.GetSize()))
        self.SetSize(500,600)
        self.Centre()

    def onMouseLeavefindph(self, event):
            # mouse not over button, back to original colour
            self.findphbtn.SetBackgroundColour((104,154,146))
            self.SetStatusText("Welcome to Remogo!")
            event.Skip()
    def onMouseOverremsil(self, event):
            # mouseover changes colour of button
            self.remsil.SetBackgroundColour((94,121,116))
            self.SetStatusText("Remote Ringer/Silent Button ")
            event.Skip()

    def onMouseLeaveremsil(self, event):
            # mouse not over button, back to original colour
            self.remsil.SetBackgroundColour((104,154,146))
            self.SetStatusText("Welcome to Remogo!")
            event.Skip()

    def onMouseOverback(self, event):
            # mouseover changes colour of button
            self.back.SetBackgroundColour((94,121,116))
            self.SetStatusText("Back Button to go to previous activity")
            event.Skip()

    def onMouseLeaveback(self, event):
            # mouse not over button, back to original colour
            self.back.SetBackgroundColour((104,154,146))
            self.SetStatusText("Welcome to Remogo!")
            event.Skip()
    def onMouseOverremlock(self, event):
            # mouseover changes colour of button
            self.remlock.SetBackgroundColour((94,121,116))
            self.SetStatusText("Remote Lock Button ")
            event.Skip()

    def onMouseLeaveremlock(self, event):
            # mouse not over button, back to original colour
            self.remlock.SetBackgroundColour((104,154,146))
            self.SetStatusText("Welcome to Remogo!")
            event.Skip()
    
    def Exit(self):
        self.Close(True)
        win1.exit()
        win2.exit()

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutitem=helpMenu.Append(-1,"About","about")
        helpMenu.AppendSeparator()
        docItem = helpMenu.Append(-1,"Docs\tCtrl-H","docs")
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.Ondocs, docItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutitem)


    def OnExit(self, event):
        self.Close(True)
        win1.exit()
        win2.exit()
    def OnAbout(self, event):
         wx.MessageBox("Remogo",
                      "About Remogo",
                      wx.OK|wx.ICON_INFORMATION)
    
    def Ondocs(self, event):
        wx.MessageBox("Redirecting you to website")
        url='www.google.com'
        webbrowser.open(url, new=0, autoraise=True)


    def OnHello(self, event):
         wx.MessageBox("Hello from Remogo")

        
    def onButtonfindph(self, event):
            self.sendsms(t1_val,t2_val,'3')

    def onButtonremsil(self, event):
            self.sendsms(t1_val,t2_val,'1')
            
    def onButtonremlock(self, event):
            self.sendsms(t1_val,t2_val,'4')
            
    def onButtonback(self, event):
        frame1 = MainWindow()
        frame1.Show()
        win.Exit()
            

    def sendsms(self,num,pwd,msg):
            
            number=str(num)
            #if(username==number):
             #   message=number+":"+"\n"+passwd+msg
            #else:
                #message=passwd+msg

            message=pwd+msg
            

            message = "+".join(message.split(' '))

             #logging into the sms site
            url ='http://site21.way2sms.com/Login1.action?'
            data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

             #For cookies

            cj= cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

             #Adding header details
            opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
            try:
                usock =opener.open(url, data)
            except IOError:
                print "error"
            #return()

            jession_id =str(cj).split('~')[1].split(' ')[0]
            send_sms_url = 'http://site21.way2sms.com/smstoss.action?'
            send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
            opener.addheaders=[('Referer', 'http://site21.way2sms.com/sendSMS?Token='+jession_id)]
            try:
                sms_sent_page = opener.open(send_sms_url,send_sms_data)
            except IOError:
                print "error"
            #return()
            wx.MessageBox("Success")

            #print "success" 
            #return ()

class loginwindow(wx.Frame):
    def __init__(self):
        btnfont = wx.Font(18, wx.MODERN, wx.NORMAL, wx.BOLD)
        lbfont = wx.Font(16, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        title='Remogo'
        wx.Frame.__init__(self, None, wx.ID_ANY,title)
        #icon = wx.EmptyIcon()
        icon=wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Centre()
        self.SetSize(500, 600)
        self.Show(True)
        wx.Frame.SetBackgroundColour(self,(255,255,255))
        #wx.Frame.SetTransparent(self,200)
        self.HBox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.vBox = wx.BoxSizer(wx.VERTICAL) 
        self.Submit = wx.Button(self.panel, id=wx.ID_ANY, name="Submit",label="Submit")
        self.Submit.SetBackgroundColour((104,154,146))
        self.Submit.SetFont(btnfont)
        self.Submit.Bind(wx.EVT_BUTTON, self.onButton)
        self.Submit.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOversub)
        self.Submit.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavesub)
        self.t1=wx.TextCtrl(self.panel)
        #self.t1.SetNoneAllowed(True)
        #self.t1.SetValue()
        self.Signup = wx.Button(self.panel, id=wx.ID_ANY, name="Signup",label="Signup")
        self.Signup.SetBackgroundColour((104,154,146))
        self.Signup.SetFont(btnfont)
        self.Signup.Bind(wx.EVT_BUTTON, self.onSignupButton)
        self.Signup.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOversignup)
        self.Signup.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavesignup)
        self.t2=wx.TextCtrl(self.panel,style = wx.TE_PASSWORD)
        self.t1.SetBackgroundColour((240,230,140))
        self.t2.SetBackgroundColour((240,230,140))
        self.t1.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOvernum)
        self.t1.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavenum)
        self.t2.Bind(wx.EVT_ENTER_WINDOW, self.onMouseOverpwd)
        self.t2.Bind(wx.EVT_LEAVE_WINDOW, self.onMouseLeavepwd)
        self.l4 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="New Account,Signup here")
        self.l4.SetFont(lbfont)
        self.l1 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="Enter Username")
        self.l1.SetFont(lbfont)
        self.l2 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="Enter Password")
        self.l2.SetFont(lbfont)
        self.l3 = wx.StaticText(self.panel,-1,style = wx.ALIGN_LEFT,label="Enter Way2Sms cridentials here")
        self.l3.SetFont(lbfont)
        self.l3.SetForegroundColour((255,0,0))
        self.l4.SetForegroundColour((255,0,0))
        self.HBox1.Add(self.l1,0,0)
        self.HBox1.AddSpacer(10) 
        self.HBox1.Add(self.t1,0,   wx.ALIGN_RIGHT,0)
        self.HBox2.Add(self.l2,0,wx.ALL,0)
        self.HBox2.AddSpacer(13)
        self.HBox2.Add(self.t2,0,wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT,0)
        self.HBox3.AddSpacer(100)
        self.HBox3.Add(self.Submit,0,wx.ALIGN_CENTRE_HORIZONTAL,0)
        self.HBox4.Add(self.l4,0,0);
        #self.HBox4.AddSpacer(100)
        self.HBox4.Add(self.Signup,0,0);
        self.vBox.Add(self.l3,0,0)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.HBox1)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.HBox2)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.HBox3)
        self.vBox.AddSpacer(10)
        self.vBox.Add(self.HBox4)
        #self.vBox.Add(self.Submit,1,wx.ALIGN_CENTER_HORIZONTAL,10)
       # self.panel.SetSizer(self.HBox)
        self.panel.SetSizer(self.vBox)
        self.makeMenuBar()
        #self.MenuBar.SetFont(btnfont)
        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((255,255,255))
        self.SetStatusText("Welcome to Remogo!")
    def OnSize(self, event):
        # hsize = event.GetSize()[0] 
        #self.SetSizeHints(minW=-1, minH=hsize, maxH=hsize)
        #self.SetTitle(str(event.GetSize()))
        self.SetSize(500,600)
        self.Centre()
    def onSignupButton(self,event):
        wx.MessageBox("Redirecting you to website of way2sms,click on register here there")
        url='www.way2sms.com'
        webbrowser.open(url, new=0, autoraise=True)
        
    def onButton(self, event):
        global username
        username=self.t1.GetValue()
        global passwd
        passwd=self.t2.GetValue()
        def isNotBlank(myString):
            return bool(myString and myString.strip())
        if isNotBlank(username) and isNotBlank(passwd):
            global win1
            win1 = MainWindow()
            win1.Show()
            frame.Exit()
        else:
            wx.MessageBox("Mobile Number or password left blank")
       # print "The button you pressed was labeled: " + button_by_id.GetLabel()
       # print "The button's name is " + button_by_id.GetName()
        #print t1_val
    def onMouseOversub(self, event):
        self.Submit.SetBackgroundColour((94,121,116))
        self.SetStatusText("Submit Button") 
        event.Skip()

    def onMouseLeavesub(self, event):
        self.Submit.SetBackgroundColour((104,154,146))
        self.SetStatusText("Welcome to Remogo!")
        event.Skip()
        
    def onMouseOversignup(self, event):
        self.Submit.SetBackgroundColour((94,121,116))
        self.SetStatusText("Signup button") 
        event.Skip()

    def onMouseLeavesignup(self, event):
        self.Submit.SetBackgroundColour((104,154,146))
        self.SetStatusText("Welcome to Remogo!")
        event.Skip()

    def onMouseOvernum(self, event):
        self.t1.SetBackgroundColour((211,211,211))
        self.SetStatusText("Enter username") 
        event.Skip()

    def onMouseLeavenum(self, event):
        self.t1.SetBackgroundColour((240,230,140))
        self.SetStatusText("Welcome to Remogo!")

    def onMouseOverpwd(self, event):
        self.t2.SetBackgroundColour((211,211,211))
        self.SetStatusText("Enter password") 
        event.Skip()

    def onMouseLeavepwd(self, event):
        self.t2.SetBackgroundColour((240,230,140))
        self.SetStatusText("Welcome to Remogo!")

    def Exit(self):
        self.Close(True)

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        helpMenu = wx.Menu()
        aboutitem=helpMenu.Append(-1,"About","about")
        helpMenu.AppendSeparator()
        docItem = helpMenu.Append(-1,"Docs\tCtrl-H","docs")
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.Ondocs, docItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutitem)


    def OnExit(self, event):
        self.Close(True)
    def OnAbout(self, event):
         wx.MessageBox("Remogo",
                      "About Remogo",
                      wx.OK|wx.ICON_INFORMATION)
    
    def Ondocs(self, event):
        wx.MessageBox("Redirecting you to website")
        url='www.google.com'
        webbrowser.open(url, new=0, autoraise=True)


    def OnHello(self, event):
         wx.MessageBox("Hello from Remogo")



        


if __name__ == "__main__":
    app = wx.App(False)
    frame = loginwindow()
    frame.Show()
    app.MainLoop()
    
