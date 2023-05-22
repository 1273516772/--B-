import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from tkinter.filedialog import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests

from BvToAv import *
from Object import *





class Application(Frame):
    ##GUI定义
    def __init__(self,master=None):
        super().__init__(master)       ##super()代表父类定义
        self.master=master
        self.grid()
        self.createWidget()
        ##新组件##

    def createWidget(self):

        defautfont = ("幼圆", 11, 'bold')
        Style = ttk.Style()
        Style.configure("Treeview.Heading", font=defautfont)

        ##视频号label
        self.labelav = ttk.Label(self, text="视频号",font=defautfont)
        self.labelav.grid(row=0,column=0)

        ##av/bv号输入
        global abv
        abv= StringVar()
        self.entry01 = ttk.Entry(self, textvariable=abv,style=EntryStyle)
        self.entry01.grid(row=1,column=0,sticky=W+E)
        self.entry01.bind("<Button-1>", lambda a: self.entry01.delete(0, tk.END))
        abv.set("输入带av/bv的视频号")

        ##获取标题
        global title0
        title0 = StringVar()
        self.entrytitle = ttk.Entry(self, textvariable=title0,style='dark',state="readonly")
        self.entrytitle.grid(row=2, column=1,sticky="W")
        title0.set("转换后获得视频名字")

        ##页数
        self.labelpage = ttk.Label(self, text="总页数",font=defautfont)
        self.labelpage.grid(row=0, column=1)

        global mpage
        mpage = StringVar()
        self.entry02 = ttk.Entry(self,textvariable=mpage,style=EntryStyle)
        self.entry02.grid(row=1,column=1,sticky="W")
        self.entry02.bind("<Button-1>", lambda a: self.entry02.delete(0, tk.END))
        mpage.set("输入想查看的页数")


        ##热词
        global hot
        defaulthot=['考研','求职','创新创业','up']
        hot = StringVar()
        self.comhot = ttk.Combobox(self, state='normal', textvariable=hot,values=defaulthot,style=EntryStyle)
        self.comhot.grid(row=2, column=0,sticky=W+E)
        self.comhot.bind("<Button-1>", lambda a: self.comhot.delete(0, tk.END))
        hot.set("输入关键词,仅查看评论请留空")



        ##检测视频号是否正确
        self.btnifvalid = ttk.Button(self, text='检测与转换',bootstyle=(PRIMARY, "outline-toolbutton"),command=lambda: self.Isvalid(abv.get(), mpage))
        self.btnifvalid.grid(row=1, column=2,sticky="W")


        ##运行并保存
        self.btn01 = ttk.Button(self,text='运行并保存', bootstyle=(PRIMARY, "outline-toolbutton"), command=lambda: self.RunAndSave(mpage, abv.get()))
        self.btn01["state"]=DISABLED
        self.btn01.grid(row=2, column=2,sticky="W")

        ##作者##
        ##self.Author=ttk.Label(self,text="作者：  MgrainL\n邮箱: 1273516772@qq.com",borderwidth=1,relief="solid",justify="left")
        ##self.Author.grid(row=2,column=1,sticky=E)

        ##创建退出按钮
        self.btnQuit = ttk.Button(self, text="退出",bootstyle=(DANGER, "solid-button"),command=root.destroy)
        self.btnQuit.grid(row=2, column=3,sticky="W")

        ##显示文本
        self.result = ttk.Treeview(self,columns=[0, 1],show=HEADINGS,height=5,style='secondary')
        self.result.heading(0, text='昵称')
        self.result.heading(1, text='评论')
        self.result.column(0, width=75)
        self.result.column(1, width=465)
        self.result.grid(row=3,column=0,rowspan=1,columnspan=4)






    def Isvalid(self,bv,tpage):
        ##页码检查
        if (tpage.get().isdigit()==False):
            messagebox.showwarning('警告','页数输入错误')
        else:
            if (bv[0:2] == "AV" or bv[0:2] == "av" or bv[0:2] == "Av" or bv[0:2] == "aV"):
                bv = bv[2:]
                abv.set(bv)
                self.btn01["state"]=NORMAL
                messagebox.showinfo(title="注意",message="输入av不需要转换")
                url0 = f"https://www.bilibili.com/video/av%s/" % (str(bv))
                resp0 = requests.get(url0, headers=hds)
                result0 = objtitle.finditer(resp0.text)
                title0.set(result0)
                for i in result0:
                    title0.set(i.group('title'))
            elif (bv[0:2] == "BV" or bv[0:2] == "bv" or bv[0:2] == "Bv" or bv[0:2] == "bV"):
                if (len(bv)!=12):
                    messagebox.showwarning(title="警告",message="输入长度错误")
                else:
                    bv = dec(bv)
                    abv.set(bv)
                    self.btn01["state"] = NORMAL
                    messagebox.showinfo(title="转换完成",message="转换后为：AV"+str(bv))
                    url0 = f"https://www.bilibili.com/video/av%s/" % (str(bv))
                    resp0 = requests.get(url0, headers=hds)
                    result0 = objtitle.finditer(resp0.text)
                    for i in result0:
                        title0.set(i.group('title'))
            else:
                messagebox.showwarning(title="警告",message="输入错误")


    ##爬取数据并保存
    def RunAndSave(self, mpage, av0):

        ##asksaveasfile不能指定打开文件编码
        filename = SaveAs(title="选择保存文件",defaultextension=".csv",initialdir=curr_path,initialfile=title0.get(),filetypes=[('all files','*'),('文本文档','.txt'),('表格','.csv')]).show()
        if filename:
             with open(filename, 'w',encoding='utf-8',errors='ignore',newline="") as f:        #newline消除空行

                f.seek(0)  ##清空上次的数据
                f.truncate()

                csvwriter = csv.writer(f)
                csvwriter.writerow(["识别","uid", "昵称", "评论"])
                for page in range(1, int(mpage.get())):
                    url = f'https://api.bilibili.com/x/v2/reply/main?csrf=89b5d0778165109e6ea6614405f5a480&mode=3&next=%d&oid=%s&plat=1&type=1' % (
                        page, av0)
                    resp = requests.get(url, headers=hds)
                    # print(resp.text)   #打印源代码
                    result = obj.finditer(resp.text)               #result迭代器
                    lstresult=list(result)
                    new_lstresult=lstresult[:-6]                   #清除后几位（置顶）
                    result=iter(new_lstresult)

                    for i in result:

                            if(hot.get() in i.group('comment')):
                                dic = i.groupdict()
                                csvwriter.writerow(dic.values())
                                dicvalues=(dic['name'],dic['comment'])
                                self.result.insert('', END, values=dicvalues)               ##树形图显示
                                ##print("%s\t\t\t\t\t%s\t\t\t\t%s"%(i.group('uid'),i.group('name'),i.group('comment')))
                            else:
                                continue



                messagebox.showinfo("message", "运行完毕！已保存在%s,要查看评论请退出"%f.name)
                resp.close()
                f.close()


if __name__ == '__main__':
##窗口初始化
    root = ttk.Window(themename="litera")
    root.title('火眼金睛-B站评论滤镜')
    root.iconbitmap('logo.ico')
    root.geometry("544x205+500+300")
    app=Application(master=root)
    root.mainloop()
##窗口初始化
