from tkinter import *
from tkinter import ttk,filedialog,messagebox
from PIL import Image, ImageTk
import os,shutil

class SortingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Files Arranging App by Muhammad Zaki Ul Hassan Khan")
        self.root.geometry("1350x700+0+0")
        self.root.maxsize(1280,720)
        self.root.minsize(1280,720)
        self.root.config(bg="white")
        self.logo_icon = ImageTk.PhotoImage(file="images/folder.jpg")

        # ******************************************************************************************************
        #                                                          TITLE IN SCREEN
        # ******************************************************************************************************
        title = Label(self.root,text="File Sorting Application",font=("impact",40,),fg="black",bg="light blue",anchor="w",image=self.logo_icon,compound=LEFT,padx=10).place(x=0,y=0,relwidth=1)

        # ******************************************************************************************************
        #                                                          SECTION 1
        # ******************************************************************************************************
        #******************************************************************************************************
        #                                                          VARIABLE FOR FOLDER NAME DEIFINED
        # ******************************************************************************************************
        self.var_FolderName = StringVar()

        lbl_Select_Folder = Label(self.root,text="Select Folder",font=("Times New Roman",25),bg="white",fg="blue").place(x=50,y=80)

        self.txt_folder_name=Entry(self.root,textvariable=self.var_FolderName,font=("Times New Roman",15),state="readonly",bg="lightyellow")
        self.txt_folder_name.place(x=230,y=80,width=600,height=40)

        btn_Browse = Button(self.root,command=self.browse_folder,text="Browse",font=("Times New Roman",15,"bold"),bg="#262626",fg="white",activeforeground="white",activebackground="#262626",cursor="hand2").place(x=850,y=80)

        horizontal_line = Label(self.root,bg="lightgray").place(x=50,y=140,height=2,width=1200)

        # ******************************************************************************************************
        #                                                          SECTION 2
        # ******************************************************************************************************
        # **********************************************************************************************************
        #                                                          ALL EXTENTIONS DEFINED AND ASSOCIATED WITH FOLDERS DICTIONARY
        # *********************************************************bro*************************************************
        self.image_extentions=["Image Extentions",".jpg",".png",'.webp','.PNG']
        self.audio_extentions=["Audio Extentions",".amr",".mp3"]
        self.video_extentions=["Video Extentions",".mp4",".avi",".mpeg4",".3gp",".mkv",".hevc"]
        self.document_extentions=["Document Extentions",".doc",".docx",".xlsx",".ppt",".xls",".pptx",".pdf",".zip",".rar",".csv",".txt"]

        self.folders={
                    'videos':self.video_extentions,
                    'audios':self.audio_extentions,
                    'images':self.image_extentions,
                    'documents':self.document_extentions
              }


        lbl_supported_extentions = Label(self.root,text="Various Supported Extentions",font=("Times New Roman",25),bg="white").place(x=50,y=150)
        self.image_combo_box=ttk.Combobox(self.root,values=self.image_extentions,font=("Times New Roman",20),state="readonly",justify=CENTER)
        self.image_combo_box.place(x=50,y=210,width=250)
        self.image_combo_box.current(0)

        self.audio_combo_box=ttk.Combobox(self.root,values=self.audio_extentions,font=("Times New Roman",20),state="readonly",justify=CENTER)
        self.audio_combo_box.place(x=360,y=210,width=250)
        self.audio_combo_box.current(0)

        self.video_combo_box=ttk.Combobox(self.root,values=self.video_extentions,font=("Times New Roman",20),state="readonly",justify=CENTER)
        self.video_combo_box.place(x=670,y=210,width=250)
        self.video_combo_box.current(0)

        self.document_combo_box=ttk.Combobox(self.root,values=self.document_extentions,font=("Times New Roman",20),state="readonly",justify=CENTER)
        self.document_combo_box.place(x=980,y=210,width=250)
        self.document_combo_box.current(0)


        # ******************************************************************************************************
        #                                                          SECTION 3
        # ******************************************************************************************************
        # ******************************************************************************************************
        #                                                          NOW ALL IMAGES DEFINED WHICH IS USED IN FRAME
        # ******************************************************************************************************
        self.photo_icon = ImageTk.PhotoImage(file="images/photo.jpg")
        self.audio_icon = ImageTk.PhotoImage(file="images/music.jpg")
        self.video_icon = ImageTk.PhotoImage(file="images/video.jpg")
        self.document_icon = ImageTk.PhotoImage(file="images/document.jpg")
        self.other_icon = ImageTk.PhotoImage(file="images/other.jpg")
        # ******************************************************************************************************
        #                                                          NOW FRAME DEFINED AND PLACED
        # ******************************************************************************************************
        frame1 = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame1.place(x=50,y=270,width=1180,height=250)

        # ******************************************************************************************************
        #                                                          NOW LABELS IN FRAME DEFINED AND PLACED
        # ******************************************************************************************************
        self.lbl_total_files = Label(frame1,text='Total Files ',font=('Times New Roman',20),bg='white')
        self.lbl_total_files.place(x=10,y=10)

        self.total_photos = Label(frame1,text='',font=('Times New Roman',17,'bold'),compound=TOP,bg='white',fg='black',bd=1,relief=RIDGE,image=self.photo_icon)
        self.total_photos.place(x=10,y=40,width=230,height=200)


        self.total_audios = Label(frame1,text='',font=('Times New Roman',17,'bold'),compound=TOP,bg='white',fg='black',bd=1,relief=RIDGE,image=self.audio_icon)
        self.total_audios.place(x=250,y=40,width=230,height=200)


        self.total_videos = Label(frame1,text='',font=('Times New Roman',17,'bold'),compound=TOP,bg='white',fg='black',bd=1,relief=RIDGE,image=self.video_icon)
        self.total_videos.place(x=490,y=40,width=230,height=200)


        self.total_documents = Label(frame1,text='',font=('Times New Roman',17,'bold'),compound=TOP,bg='white',fg='black',bd=1,relief=RIDGE,image=self.document_icon)
        self.total_documents.place(x=730,y=40,width=230,height=200)


        self.total_other_files = Label(frame1,text='',font=('Times New Roman',17,'bold'),compound=TOP,bg='white',fg='black',bd=1,relief=RIDGE,image=self.other_icon)
        self.total_other_files.place(x=970,y=40,width=200,height=200)

        # ******************************************************************************************************
        #                                                          SECTION 3
        # ******************************************************************************************************

        self.lbl_status = Label(self.root,text="Status  ",font=('Times New Roman',20),bg='white',fg='black')
        self.lbl_status.place(x=50,y=530)

        self.lbl_total = Label(self.root,text='',font=('Times New Roman',20),bg='white',fg='green')
        self.lbl_total.place(x=170,y=530)

        self.lbl_moved = Label(self.root,text='',font=('Times New Roman',20),bg='white',fg='blue')
        self.lbl_moved.place(x=400,y=530)

        self.lbl_left = Label(self.root,text='',font=('Times New Roman',20),bg='white',fg='orange')
        self.lbl_left.place(x=630,y=530)

        # ******************************************************************************************************
        #                                                          NOW BUTTONS DEFINED AND PLACED
        # ******************************************************************************************************
        self.btn_clear = Button(self.root,command=self.clear_funtion,text="Clear",font=("Times New Roman",15,"bold"),bd=5,relief=RAISED,bg="#262046",fg="white",activeforeground="yellow",activebackground="#262046",cursor="hand2")
        self.btn_clear.place(x=800,y=530,height=40,width=200)

        self.btn_start = Button(self.root,command=self.start_funtion,state=DISABLED,text="Start",font=("Times New Roman",15,"bold"),bd=5,relief=RAISED,bg="#262046",fg="white",activeforeground="yellow",activebackground="#262046",cursor="hand2")
        self.btn_start.place(x=1010,y=530,height=40,width=200)



    #******************************************************************************************************
    #                                                          NOW ALL FUNCTIONS DEFINED ---------TOTAL COUNT
    #******************************************************************************************************
    def total_count(self):
        images=0
        audios = 0
        videos = 0
        documents = 0
        others = 0
        self.count = 0
        combile_list = []
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                extention = '.'+i.split('.')[-1]
                for folder_name in self.folders.items():
                    for x in folder_name[1]:
                        combile_list.append(x)
                    if extention.lower() in folder_name[1] and folder_name[0]=='images':
                        images += 1
                    if extention.lower() in folder_name[1] and folder_name[0] == 'audios':
                        audios += 1
                    if extention.lower() in folder_name[1] and folder_name[0] == 'videos':
                        videos += 1
                    if extention.lower() in folder_name[1] and folder_name[0]=='documents':
                        documents += 1
            #=============THIS IS FOR CALCULATING OTHER FILES ONLY
            for j in self.all_files:
                if os.path.isfile(os.path.join(self.directry,j))==True:
                    extention = '.'+j.split('.')[-1]
                    if extention.lower() not in combile_list:
                        others += 1

        self.total_photos.config(text='Total Images\n'+str(images))
        self.total_audios.config(text='Total Audios\n'+str(audios))
        self.total_videos.config(text='Total Videos\n'+str(videos))
        self.total_documents.config(text='Total Documents\n'+str(documents))
        self.lbl_total_files.config(text='Total Files : '+str(self.count))
        self.total_other_files.config(text='Other Files\n'+str(self.count-(documents+videos+audios+images)))


    #******************************************************************************************************
    #                                                          NOW BROWSE FUNCTION
    #******************************************************************************************************
    def browse_folder(self):
        op = filedialog.askdirectory(title='Select Folder for Sorting')
        if op != None:
            # print(op)
            self.btn_start.config(state=NORMAL)
            self.var_FolderName.set(str(op))
            self.directry = self.var_FolderName.get()
            self.other_name = "Other Files"
            self.rename_folder()
            self.all_files = os.listdir(self.directry)
            length = len(self.all_files)
            count = 1
            self.total_count()
            # print(self.all_files)
            self.btn_start.config(state=NORMAL)
            #print(self.all_files)

    #******************************************************************************************************
    #                                                          NOW RENAME FOLDER FUNCTION
    #******************************************************************************************************

    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry, folder)) == True:
                os.rename(os.path.join(self.directry, folder), os.path.join(self.directry, folder.lower()))

    #******************************************************************************************************
    #                                                          NOW CREATE MOVE FOLDER FUNCTION
    #******************************************************************************************************

    def create_move(self,extention, file_name):
        find = False
        for folder_name in self.folders:
            if '.' + extention in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry, folder_name))
                shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, folder_name))
                find = True
                break
        if find != True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry, self.other_name))
            shutil.move(os.path.join(self.directry, file_name), os.path.join(self.directry, self.other_name))

    #******************************************************************************************************
    #                                                          NOW START FUNCTION
    #******************************************************************************************************

    def start_funtion(self):
        if self.var_FolderName.get()!='':
            self.btn_clear.config(state=DISABLED)
            countt = 0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry, i)) == True:
                    countt += 1
                    self.create_move(i.split('.')[-1], i)

                    self.lbl_total.config(text='Total :'+str(self.count))
                    self.lbl_moved.config(text='Moved :'+str(countt))
                    self.lbl_left.config(text='Left :'+str(self.count - countt))

                    self.lbl_total.update()
                    self.lbl_moved.update()
                    self.lbl_left.update()
            messagebox.showinfo('Success',"Successfully Done :)")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showerror('Error', "Please Select Folder ")

    #******************************************************************************************************
    #                                                          NOW CLEAR FUNCTION
    #******************************************************************************************************

    def clear_funtion(self):
        self.btn_start.config(state=DISABLED)
        self.var_FolderName.set("")
        self.lbl_total.config(text='')
        self.lbl_moved.config(text='')
        self.lbl_left.config(text='')
        self.total_photos.config(text='')
        self.total_audios.config(text='')
        self.total_videos.config(text='')
        self.total_documents.config(text='')
        self.lbl_total_files.config(text='Total Files')
        self.total_other_files.config(text='')

root = Tk()
obj = SortingApp(root)
root.mainloop()
