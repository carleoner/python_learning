from asyncio.windows_events import NULL
from cgitb import text
from distutils.util import execute
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def GUI():
    def insertData():
        Id = writeId.get()
        Name = writeName.get()
        Dept = writeDept.get()

        if(Id=="" or Name=="" or Dept==""):
            messagebox.showwarning(title="Warning!", message="All fields must be filled")
        else:
            #open database and add emp
            myDB = mysql.connector.connect(host = "localhost", 
                user = "root", passwd = "Howtobasics123!", database = "employee")
            cursor = myDB.cursor()
            strCom = "INSERT INTO empDetails VALUES(" + str(Id) + ",\""+ str(Name) + "\",\""+ str(Dept) + "\")"
            try:
                cursor.execute(strCom)
                myDB.commit()
            except:
                myDB.rollback()
            myDB.close()

            #clear the fields
            writeId.delete(0,"end")
            writeName.delete(0,"end")
            writeDept.delete(0,"end")

            label.config(text = "Insert Status: Success")
            showDB()
    
    def updateData():
        Id = writeId.get()
        Name = writeName.get()
        Dept = writeDept.get()

        if(Id=="" or Name=="" or Dept==""):
            messagebox.showwarning(title="Warning!", message="All fields must be filled")
        else:
            #open database and add emp
            myDB = mysql.connector.connect(host = "localhost", 
                user = "root", passwd = "Howtobasics123!", database = "employee")
            cursor = myDB.cursor()
            strCom = "UPDATE empDetails SET empName=\"" + str(Name) + "\", empDept=\""+ str(Dept) + "\" WHERE empID=\""+ str(Id) + "\""
            try:
                cursor.execute(strCom)
                myDB.commit()
            except:
                myDB.rollback()
            myDB.close()

            #clear the fields
            writeId.delete(0,"end")
            writeName.delete(0,"end")
            writeDept.delete(0,"end")

            label.config(text = "Update Status: Success")
            showDB()

    def fetchData():
        Id = writeId.get()

        if(Id == ""):
            messagebox.showwarning(title="Warning!", message="Employee ID field must be filled to fetch data")
        else:
            #open database and add emp
            myDB = mysql.connector.connect(host = "localhost", 
                user = "root", passwd = "Howtobasics123!", database = "employee")
            cursor = myDB.cursor()
            strCom = "SELECT * FROM empDetails WHERE empID=\""+ str(Id) + "\""
            try:
                cursor.execute(strCom)
                data_rows = cursor.fetchall()
                if not len(data_rows):
                    label.config(text = "Fetch Status: Failure")
                else:
                    label.config(text = "Fetch Status: Success")
                    writeName.delete(0,"end")
                    writeDept.delete(0,"end")
                    for row in data_rows:
                        writeName.insert(0, row[1])
                        writeDept.insert(0, row[2])

            except:
                myDB.rollback()
            myDB.close()
            
    def deleteData():
        Id = writeId.get()

        if(Id == ""):
            messagebox.showwarning(title="Warning!", message="Employee ID field must be filled to delete data")
        else:
            #open database and add emp
            myDB = mysql.connector.connect(host = "localhost", 
                user = "root", passwd = "Howtobasics123!", database = "employee")
            cursor = myDB.cursor()
            strCom = "DELETE FROM empDetails WHERE empID=\""+ str(Id) + "\""
            try:
                cursor.execute(strCom)
                myDB.commit()
                writeId.delete(0,"end")
                writeName.delete(0,"end")
                writeDept.delete(0,"end")
            except:
                myDB.rollback()
            myDB.close()
            label.config(text = "Delete Status: Success")
            showDB()

    def resetData():
        writeId.delete(0,"end")
        writeName.delete(0,"end")
        writeDept.delete(0,"end")
        showDB()

    def showDB():
        myDB = mysql.connector.connect(host = "localhost", 
                user = "root", passwd = "Howtobasics123!", database = "employee")
        cursor = myDB.cursor()
        strCom = "SELECT * FROM empDetails"
        cursor.execute(strCom)
        
        rawData = cursor.fetchall()
        showData.delete(0,showData.size())

        for row in rawData:
            newData = str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2])
            showData.insert(showData.size()+1, newData)
        myDB.close()
    
    window = Tk()
    window.geometry("480x250")
    window.title("Employee CRUD App")
    
    empId = Label(window, text="Employee ID", font=("Serif", 12))
    empId.place(x=20,y=30)
    empName = Label(window, text="Employee Name", font=("Serif", 12))
    empName.place(x=20,y=60)
    empDept = Label(window, text="Employee Dept", font=("Serif", 12))
    empDept.place(x=20,y=90)

    writeId = Entry(window)
    writeId.place(x=170, y=30)
    writeName = Entry(window)
    writeName.place(x=170, y=60)
    writeDept = Entry(window)
    writeDept.place(x=170, y=90)

    frame = Frame(window)
    insertBtn = Button(frame, text="Insert", font=("Serif", 12), bg='white', command=insertData)
    insertBtn.pack(side=LEFT)
    updateBtn = Button(frame, text="Update", font=("Serif", 12), bg='white', command=updateData)
    updateBtn.pack(side=LEFT)
    getBtn = Button(frame, text="Fetch", font=("Serif", 12), bg='white', command=fetchData)
    getBtn.pack(side=LEFT)
    deleteBtn = Button(frame, text="Delete", font=("Serif", 12), bg='white', command=deleteData)
    deleteBtn.pack(side=LEFT)
    resetBtn = Button(frame, text="Reset", font=("Serif", 12), bg='white', command=resetData)
    resetBtn.pack(side=LEFT)
    frame.place(x=20,y=160)

    showData = Listbox(window)
    showData.place(x=330,y=30)

    label = Label(window)
    label.pack(side=BOTTOM)
    
    window.mainloop()

if __name__ == '__main__':
    GUI()