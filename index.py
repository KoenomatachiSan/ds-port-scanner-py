from tkinter import*
import tkinter as tk
import clipboard as cp
import webbrowser
import dudesec
from datetime import datetime

root = Tk()
root.geometry('1000x200')
root.title("DudeSecurity - Port Scanner")

host_title = Label(root, text="Host",width=20,font=("bold", 10))
host_title.place(x=0,y=10)

input_host = Entry(root)
input_host.place(x=200,y=10)

port_title_start = Label(root, text="Porta inicial",width=20,font=("bold", 10))
port_title_start.place(x=0,y=40)

input_start_port = Entry(root)
input_start_port.place(x=200,y=40)

port_title_final = Label(root, text="Porta final",width=20,font=("bold", 10))
port_title_final.place(x=0,y=70)

input_final_port = Entry(root)
input_final_port.place(x=200,y=70)

listbox = Listbox(root, 
                  height = 7,  
                  width = 63,  
                  bg = "grey", 
                  font = "Helvetica", 
                  fg = "white")

listbox.pack()
listbox.place(x=400,y=5)   

def success_menu_render():
    listbox.delete(0, 5)
    now = datetime.now()
    hora_data = now.strftime("%d/%m/%Y %H:%M:%S")
    host = input_host.get()
    listbox.insert(1, str("[")+str(hora_data)+str("] Escaneando host => ")+str(host)) 

    now = datetime.now()
    hora_data = now.strftime("%d/%m/%Y %H:%M:%S")
    port_start = input_start_port.get()
    listbox.insert(2, str("[")+str(hora_data)+str("] Porta inicial => ")+str(port_start)) 

    now = datetime.now()
    hora_data = now.strftime("%d/%m/%Y %H:%M:%S")
    port_end = input_final_port.get()
    listbox.insert(3, str("[")+str(hora_data)+str("] Porta final => ")+str(port_end)) 


    listbox.insert(4, ("----------------------------------------------------------------")) 
    listbox.insert(5, str("[")+str(hora_data)+str("] Portas abertas => ")+str(dudesec.portScanner(host,port_start,port_end)))
    

tk.Button(root, text='Salvar Resultado',width=17,bg='green',fg='white',command=success_menu_render).place(x=400,y=140)

tk.Button(root, text='Acessar Repositório',width=17,bg='grey',fg='white',command=lambda: webbrowser.open('https://github.com/KoenomatachiSan/ds-port-scanner-py')).place(x=570,y=140)

tk.Button(root, text='Acessar Comunidade',width=17,bg='blue',fg='white',command=lambda: webbrowser.open('https://dudesecurity.darwinproject.online/forum/')).place(x=740,y=140)

Button(root, text='Escanear',width=17,bg='brown',fg='white',command=success_menu_render).place(x=200,y=100)


root.resizable(False, False) 
root.mainloop()