## 机器人助手
## 可能目前还不算是机器人，不过先其上一个名字，叫着。

import tkinter as tk
import tkinter.font as tkFont
import time
from myUtil import StrUtil
from myUtil import RandUtil
import threading

# http://effbot.org/tkinterbook/
# https://www.runoob.com/python3/python3-errors-execptions.html

class RobotAssistant():
    def __init__(self):        
        self.name = "Robert" # 谐音梗
        pass
    
    def __goal(self):
        print("=== 尽职尽责，不负使命！ ===")
        print("=== 简单明了，不断进化！ ===")
    
    def Hi(self):
        print("==================================================")
        greeting = "== Hello! I am "+self.name+"! Nice to meet you! =="
        print( greeting )
        greeting = "== 你好！我是"+self.name+"! 很高兴我们见面了！  =="
        print(greeting)
        print("==================================================")
        
class Jarvis(RobotAssistant):
    def __init__(self,master):
        # 这里的master 应该是根应用的tk.Tk()组件。        
        super().__init__()
        self.name = "Jarvis."+ self.name
        self.master = master
        
        self.top = tk.Toplevel(self.master)
        
        self.create()
        
    def create(self):
        
        self.top.minsize(600,500)
        self.top.title(self.name)        
        self.createMenu()        
        self.createFrames()
        tk.Grid.rowconfigure(self.top,0,weight=1) 
        tk.Grid.columnconfigure(self.top,0,weight = 1)
        
    
    def createMenu(self):
        # 生成一个菜单栏
        self.menuBar = tk.Menu()
        self.top.config(menu=self.menuBar)
        # 菜单栏的各菜单项
        
        # == 文件菜单 ==
        self.menuFile = tk.Menu(self.menuBar,tearoff = False)
        self.menuBar.add_cascade(label='文件',menu = self.menuFile)
        self.menuFile.add_command(label='打开',command = self.openFile)
        self.menuFile.add_separator()
        self.menuFile.add_command(label='退出',command = self.quit)
        
        # == 帮助菜单 ==
        self.menuHelp = tk.Menu(self.menuBar,tearoff = False)
        self.menuBar.add_cascade(label='帮助',menu = self.menuHelp)
        self.menuHelp.add_command(label='说明',command = self.info)
        

    def createFrames(self):
        #frame
        self.frame = tk.Frame(self.top)
        tk.Grid.rowconfigure(self.frame,0,weight=1) 
        tk.Grid.columnconfigure(self.frame,0,weight = 1)
        self.frame.grid(row=0,column=0,sticky='NEWS')        
        # 垂直滚动条
        self.txtVerScrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        
        # 实例化一个文本显示区域
        self.txtArea = tk.Text(self.frame,  \
                            yscrollcommand=self.txtVerScrollbar.set )

        self.txtVerScrollbar['command'] =  self.txtArea.yview         
        self.txtArea.grid(row=0,column=0,sticky='NEWS')
        self.txtArea.config(state=tk.DISABLED)
        self.txtVerScrollbar.grid(row = 0,column=1,sticky='NS')
        
        # frame2
        self.frame2 = tk.Frame(self.top)        
        tk.Grid.columnconfigure(self.frame2,0,weight = 1)
        tk.Grid.columnconfigure(self.frame2,1,weight = 1)
        tk.Grid.columnconfigure(self.frame2,2,weight = 2)
        tk.Grid.columnconfigure(self.frame2,3,weight = 1)
        tk.Grid.columnconfigure(self.frame2,4,weight = 2)
        tk.Grid.columnconfigure(self.frame2,5,weight = 1)
        tk.Grid.columnconfigure(self.frame2,6,weight = 2)
        self.frame2.grid(row=1,column=0,sticky="NEWS")
        
        self.buttonFont = tkFont.Font(family='微软雅黑',size = '16')
        
        self.buttonRun   = tk.Button(self.frame2,text='Run',  width=8, \
                   font=self.buttonFont, fg='Green',command = self.bRun)
        self.buttonStop  = tk.Button(self.frame2,text='Stop', width=8, 
                   font=self.buttonFont, fg='Red',command = self.bStop)
       
        
        # 设置以上三个按键的位置
        self.buttonRun.grid(column=6,row=0,columnspan=2,sticky='E')
        self.buttonStop.grid(column=4,row=0,columnspan=2,sticky='E')
        
        self.bRunFlag = False
        
        
        
    def bRun(self):
        self.bRunFlag = True
        #_thread.start_new_thread(self.taskRun,())
        threading.Thread(target=self.taskRun,args=()).start()
    
    def bStop(self):
        self.bRunFlag = False
    
    def __txtAreaOutput(self,infoStr):
        self.txtArea.config(state=tk.NORMAL)
        self.txtArea.insert(tk.END,infoStr)                
        self.txtArea.config(state=tk.DISABLED)
        self.txtArea.see(tk.END) # 一直显示最新的一行
        self.txtArea.update()
    
    def taskRun(self):
        try:
            while(self.bRunFlag ):               
                infoStr = StrUtil.getTimeStr()+'|'+RandUtil.getRandWords()+"\n"
                self.__txtAreaOutput(infoStr)
                time.sleep(0.1)
        except :
            pass
            
        
        
        
        
    
    def openFile(self):
        pass
    
    def quit(self):
        pass
    
    def info(self):
        pass
        
    

if __name__ == "__main__":
    root = tk.Tk()
    myJarvis = Jarvis(root)
    
    myJarvis.Hi()
    root.mainloop()
        