

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from Robot import Jarvis

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        
        root = self.root = master
        root.title("Tool")
        root.geometry( '200x360')
        root.resizable(0,1)
        root.config(bg="steelblue")
                
        self.create()
        
        
        
    def create(self):        
        '''
        将主界面设计成一个竖条形状，分成两个区域：自主研发功能区+退出按键区。
        自主研发功能区：目前里面放置三个功能按键，后续按下每一个按键弹出一个界面。
        退出按键区：就放置一个按键，用来退出。
        '''
        self.inputFrameFont = tkFont.Font(family='微软雅黑',size = '16')
        
        # 整个区域划分成两个窗体，一个用来放功能按键，一个专门用来放退出按键。
        # 我还想给这个中间加条线。现在还不会。不过应该可以加，如何能让他明显一点？
        self.funcFrame = tk.Frame(self.root);
        self.separatorLine = ttk.Separator(self.root,orient='horizontal',style='red.TSeparator')
        self.quitFrame = tk.Frame(self.root);
        
        # ==start==
        # 设置上面三个顶层组件的位置
        self.funcFrame.grid(row = 0, column=0, sticky='NWES')
        self.separatorLine.grid(row = 1, column=0, sticky='NWES') # 这条分割线没有显示出来，没起作用？
        self.quitFrame.grid(row = 2, column=0, sticky='NWES')
        
        tk.Grid.rowconfigure(self.root,0,weight=15)
        # tk.Grid.rowconfigure(self.root,1,weight=15) #还是看不到这条线
        tk.Grid.rowconfigure(self.root,2,weight=1) # 甚至应该考虑这个窗体是否应该固定大小
        tk.Grid.columnconfigure(self.root,0,weight = 1)
        # ==end==
        
        # 实例化在funcFrame里面的三个函数按键
        self.button1 = tk.Button(self.funcFrame,text='功能1',font=self.inputFrameFont, command = self.func1)
        self.button2 = tk.Button(self.funcFrame,text='功能2',font=self.inputFrameFont, command = self.func2)
        self.button3 = tk.Button(self.funcFrame,text='功能3',font=self.inputFrameFont, command = self.func3)
        
        # ==start==
        # 设置以上三个按键的位置
        self.button1.grid(row=0,column=0,rowspan=1,sticky='NWES')
        self.button2.grid(row=1,column=0,rowspan=1,sticky='NWES')
        self.button3.grid(row=2,column=0,rowspan=1,sticky='NWES')
        
        tk.Grid.rowconfigure(self.funcFrame,0,weight=1)
        tk.Grid.rowconfigure(self.funcFrame,1,weight=1)
        tk.Grid.rowconfigure(self.funcFrame,2,weight=1)
        
        tk.Grid.columnconfigure(self.funcFrame,0,weight=1)
        # ==end==
        
        # 实例化一个退出按键
        self.buttonQuit = tk.Button(self.quitFrame,text='退 出',font=self.inputFrameFont)       
        self.buttonQuit.config(bg='gray',fg='black',command=self.quit)
        
        # ==start==
        # == 设置quitFrame中按键的大小和位置 ==
        self.buttonQuit.grid(row=0,column=0,sticky='NWES')
        tk.Grid.rowconfigure(self.quitFrame,0,weight=1)        
        tk.Grid.columnconfigure(self.quitFrame,0,weight=1)        
        # ==end==
        pass
        


    def quit(self):
        # self.root.quit()
        self.root.destroy() # 这两个有什么区别？
        
    
    def func1(self):
        print("Jarvis欢迎您！")
        # 使用withdraw和update，deiconify是一种隐藏主窗口的方法
        # 能不能在toplevel的创建和结束时调用隐藏主窗口？
        self.root.withdraw()
        
        #assistantJarvis = Jarvis(self.root)
        #self.root.wait_window(assistantJarvis.top)
        self.root.wait_window(Jarvis(self.root).top)
        
        self.root.update()
        self.root.deiconify()
        


    def func2(self):
        print("MP3，MP4播放器？")
        

        
    def func3(self):
        print("网络工具？")
        



'''
1, 是否需要加上logging？
2，多文件处理。
'''


if __name__== "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()

    