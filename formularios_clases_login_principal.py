import tkinter
from tkinter import messagebox
import tkinter as tk


class FrmPrincipal(tkinter.Frame):
    nombre = 'usuario'

    def __init__(self, nombre):
        def abrirventana():
            obj_ventana.destroy()
            nuevaventana = FrmLogin()
            nuevaventana.mainloop()

        obj_ventana = tkinter.Tk()
        super().__init__(obj_ventana)
        obj_ventana.title(" Ventana Principal  !!!!")
        obj_ventana.geometry("500x300")

        e3 = tk.Label(obj_ventana, text='bienvenido ' + nombre, bg="gray21", fg="white")
        e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

        boton2 = tk.Button(obj_ventana, bg="silver", text=' Cerrar ', command=abrirventana)
        boton2.place(x=440, y=10)


class FrmLogin(tkinter.Frame):
    def __init__(self):
        global obj_ventana
        obj_ventana = tkinter.Tk()
        super().__init__(obj_ventana)
        obj_ventana.title("Login de Acceso !!!!")
        obj_ventana.geometry("500x300")
        self.iniciarComponentes()

    def iniciarComponentes(self):
        lblusuario = tkinter.Label(obj_ventana, text="Usuario :")
        lblusuario.place(x=70, y=60)
        self.txtusuario = tkinter.Entry(obj_ventana, width=30)
        self.txtusuario.place(x=150, y=60)
        lblclave = tkinter.Label(obj_ventana, text="Clave :")
        lblclave.place(x=70, y=90)
        texto = tkinter.StringVar()
        self.txtpassword = tkinter.Entry(obj_ventana, width=30, textvariable=texto)
        self.txtpassword.place(x=150, y=90)
        self.txtpassword.config(show="*")
        btnentrar = tkinter.Button(obj_ventana, text="Entrar", command=self.entrar)
        btnentrar.place(x=210, y=130)
        return texto.get()

    def entrar(self):

        n1 = self.txtusuario.get()
        n2 = self.txtpassword.get()

        if (n1 == "" and n2 == ""):
            messagebox.showinfo("", "Ningun campo rellenado")
        elif (len(n1) == 0):
            messagebox.showinfo(message="Ingrese Usuario", title="Mensaje")
            self.txtusuario.focus()
        elif (len(n2) == 0):
            messagebox.showinfo(message="Ingrese Clave", title="Mensaje")
            self.txtpassword.focus()




        elif ((n1 != "cesar" or n2 != "123") and
              (n1 != "terrible" or n2 != "124") and
              (n1 != "jorge" or n2 != "125") and
              (n1 != "kevin" or n2 != "126") and
              (n1 != "sonrisa" or n2 != "127")):

            messagebox.showinfo(message="Usuario o Clave Incorrecta", title="Mensaje")

            self.txtusuario.focus()
        else:
            cerrarventana()

            nuevaventana = FrmPrincipal(nombre=n1)
            nuevaventana.mainloop()


def cerrarventana():
    obj_ventana.destroy()


objeto = FrmLogin()
objeto.mainloop()
