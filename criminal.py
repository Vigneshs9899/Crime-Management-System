import matplotlib
matplotlib.use('Agg')

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox 





root=Tk()
class criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("CRIME MANAGEMENT SYSTEM")

        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_wanted=StringVar()
        self.var_gender=StringVar()





        lbl_title=Label(root,text='CRIME MANAGEMENT SYSTEM DATABASE',font=('times new roman',40,'bold'),fg='royal blue',bg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        #logo
        img_logo=Image.open('image/icons8-police-badge.png')
        img_logo=img_logo.resize((70,70),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=100,y=5,width=70,height=60)

        #img_frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='gold')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1=Image.open('image/bck.png')
        img1=img1.resize((1530,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=1530,height=160)
        
    
        #mainframe
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='gold')
        Main_frame.place(x=0,y=200,width=1530,height=590)
        #upperframe
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION',font=('times new roman',11,'bold'),fg='royal blue',bg='gold')
        upper_frame.place(x=10,y=10,width=1500,height=270)
       
        #Labels
        #case id
        caseid=Label(upper_frame,text='Case ID:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        #criminalno
        lbl_criminal_no=Label(upper_frame,text='Criminal No:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        #criminalname
        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        #nickname
        lbl_nickname=Label(upper_frame,text='Nick Name:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        #arrestdate
        lbl_arrestdate=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_arrestdate.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_arrestdate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold'))
        txt_arrestdate.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #dateofcrime
        lbl_dateofcrime=Label(upper_frame,text='Date Of Crime:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_dateofcrime.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_dateofcrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',11,'bold'))
        txt_dateofcrime.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #address
        lbl_address=Label(upper_frame,text='Address:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        #age
        lbl_age=Label(upper_frame,text='Age:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        #occupation
        lbl_occupation=Label(upper_frame,text='Occupation:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        #birthmark
        lbl_birthmark=Label(upper_frame,text='Birthmark:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_birthmark.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold'))
        txt_birthmark.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        
        #crimetype
        lbl_crimetype=Label(upper_frame,text='Crime Type:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_crimetype.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_crimetype=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',11,'bold'))
        txt_crimetype.grid(row=0,column=5,padx=2,pady=7,sticky=W)

        
        #fathername
        lbl_fathername=Label(upper_frame,text='Father Name:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_fathername.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_fathername=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',11,'bold'))
        txt_fathername.grid(row=1,column=5,padx=2,pady=7,sticky=W)

        #Gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_gender.grid(row=2,column=4,padx=2,pady=7,sticky=W)




        #Wanted
        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('arial',11,'bold'),fg='royal blue',bg='gold')
        lbl_wanted.grid(row=4,column=4,padx=2,pady=7,sticky=W)



        #Radiobuttongender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=710,y=80,width=190,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)


        #Radiobutton wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=710,y=150,width=190,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)



        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION TABLE',font=('times new roman',11,'bold'),fg='royal blue',bg='gold')
        down_frame.place(x=10,y=280,width=1500,height=280)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='SEARCH CRIMINAL RECORD',font=('times new roman',11,'bold'),fg='royal blue',bg='gold')
        search_frame.place(x=2,y=0,width=1480,height=60)  

        search_by=Label(search_frame,text='Search By:',font=('arial',11,'bold'),fg='gold',bg='royal blue')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('select option','case_id','criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,padx=5,sticky=W)
        
        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,padx=5,sticky=W)

        #searchbutton
        btn_search=Button(search_frame,command=self.search_data,text="Search",font=('times new roman',11,'bold'),width=14,bg='royal blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,sticky=W)

        
        #allbutton
        btn_all=Button(search_frame,command=self.fetch_data,text="Show All",font=('times new roman',11,'bold'),width=14,bg='royal blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,sticky=W)

        crimeagency=Label(search_frame,text='NATIONAL CRIME FILES',font=('arial',30,'bold'),fg='royal blue',bg='gold')
        crimeagency.grid(row=0,column=5,padx=30,sticky=W,pady=0)
        
        
        

        #bgrightside
        img_crime=Image.open('image/aaa.jpg')
        img_crime=img_crime.resize((560,280),Image.LANCZOS)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=940,y=-6,width=560,height=280)

        
        #tableframe


        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1500,height=200)

        #buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='gold')
        button_frame.place(x=5,y=200,width=570,height=45)

        #updatebutton
        btn_update=Button(button_frame,command=self.update_data,text="Update",font=('times new roman',11,'bold'),width=14,bg='royal blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        
        #deletebutton
        btn_delete=Button(button_frame,command=self.delete_data,text="Delete",font=('times new roman',11,'bold'),width=14,bg='royal blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        
        #clearbutton
        btn_clear=Button(button_frame,command=self.clear_data,text="Clear",font=('times new roman',11,'bold'),width=14,bg='royal blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)




        #addbutton
        btn_add=Button(button_frame,command=self.add_data,text="Record Save",font=('times new roman',11,'bold'),width=14,bg='royal blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)



        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='crime.No')
        self.criminal_table.heading('3',text='CriminalName')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='CrimeOfDate')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='BirthMark')
        self.criminal_table.heading('11',text='CrimeType')
        self.criminal_table.heading('12',text='FatherName')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')


        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=50)
        self.criminal_table.column('2',width=50)
        self.criminal_table.column('3',width=50)
        self.criminal_table.column('4',width=50)
        self.criminal_table.column('5',width=50)
        self.criminal_table.column('6',width=50)
        self.criminal_table.column('7',width=50)
        self.criminal_table.column('8',width=50)
        self.criminal_table.column('9',width=50)
        self.criminal_table.column('10',width=50)
        self.criminal_table.column('11',width=50)
        self.criminal_table.column('12',width=50)
        self.criminal_table.column('13',width=50)
        self.criminal_table.column('14',width=50)




        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #add function
    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='vicky',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(   
                                                                                                                self.var_case_id.get(),
                                                                                                                self.var_criminal_no.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_nickname.get(),
                                                                                                                self.var_arrest_date.get(),
                                                                                                                self.var_date_of_crime.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_occupation.get(),
                                                                                                                self.var_birthmark.get(),
                                                                                                                self.var_crime_type.get(),
                                                                                                                self.var_father_name.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_wanted.get()
                                                                                                                )
                                                                                                                )
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'due to{str(es)} ')       

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='vicky',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()




    #get cursor
    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])


    #update
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('update','are you sure update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='vicky',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal1 set criminal_no=%s,name=%s,nickname=%s,arrest_date=%s,date_of_crime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,crime_type=%s,father_name=%s,gender=%s,wanted=%s where case_id=%s',(
                                                                                                                                                                                                                                                        self.var_criminal_no.get(),
                                                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                                                        self.var_nickname.get(),
                                                                                                                                                                                                                                                        self.var_arrest_date.get(),
                                                                                                                                                                                                                                                        self.var_date_of_crime.get(),
                                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                                        self.var_age.get(),
                                                                                                                                                                                                                                                        self.var_occupation.get(),
                                                                                                                                                                                                                                                        self.var_birthmark.get(),
                                                                                                                                                                                                                                                        self.var_crime_type.get(),
                                                                                                                                                                                                                                                        self.var_father_name.get(),
                                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                                        self.var_wanted.get(),
                                                                                                                                                                                                                                                        self.var_case_id.get(),
                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                        )
                                                                                                                                                                                                                                                        )
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record successfully updated')
            except Exception as es:
                messagebox.showerror('Error',f'due to{str(es)} ')

    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                delete=messagebox.askyesno('delete','are you sure delete this criminal record')
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='vicky',database='management')
                    my_cursor=conn.cursor()
                    sql=('delete from criminal1 where case_id=%s')
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('success','criminal record successfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'due to{str(es)} ')


    # clear 
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='vicky',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select* from criminal1 where '+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'due to{str(es)} ')

                



           







                

        
        


if __name__=="__main__":
    obj=criminal(root)
    root.mainloop()
