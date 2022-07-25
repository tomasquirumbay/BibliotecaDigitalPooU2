from cgitb import text
from itertools import tee
import logging
from sqlite3 import Row
import tkinter as tk
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from urllib.parse import ParseResultBytes
from uuid import getnode

class Usuario:
    """
    Creación de la clase Usuarios en la cual tiene los siguietnes atributos y métodos:

    Atributos:
    ----------
    nombre: str
    apellido:str
    gmail: str
    usuario:str
    contrasena: str
    fechaNacimiento: str
    sexo: str

    Metodos:
    --------
    def __init__(self,nombre,apellido,gmail,usuario,contrasena,fechaNacimiento,sexo):
        Método de contrcutor que contiene los atributos de la clase.
    def iniciarSesion(self,user,login):
        Método de contrcutor que los atributos de inicio de sesión.
    """
    def __init__(self,nombre,apellido,gmail,usuario,contrasena,fechaNacimiento,sexo):
        self.nombre=nombre
        self.apellido=apellido
        self.gmail=gmail
        self.usuario=usuario
        self.contrasena=contrasena
        self.fechaNacimiento=fechaNacimiento
        self.sexo=sexo
    def iniciarSesion(self,user,login):
        self.user=user
        self.login=login
        pass

def baseDatos():
    pass


ventana=Tk()
ventana.title("Bibloteca Virtual Santo Domingo")
ventana.geometry("480x270+0+0")
fondo = PhotoImage(file = "fondo.gif")
lblFondo = Label(ventana, image=fondo ).place(x=0,y=0)
def RegistroMongo():
    """
    Método en el cual es la interfaz donde se ingresa los datos a la Base de datos de mongo
    """
    ventanaRegistro = tkinter.Tk()
    ventanaRegistro.title(" REGISTRARSE EN LA BIBLIOTECA")
    ventanaRegistro.geometry("500x500")
    """ Datos a pedir """
    mostrarTkMessage=tkinter.Label(ventanaRegistro, text="Nombre:")
    mostrarTkMessage.pack()
    """Entrada del nombre"""
    nombreTk = tkinter.Entry(ventanaRegistro)
    nombreTk.pack()
    """Datos a pedir"""
    mostrarTkMessage=tkinter.Label(ventanaRegistro, text="Apellido:")
    mostrarTkMessage.pack()
    """Entrada del apellido"""
    nombre2Tk = tkinter.Entry(ventanaRegistro)
    nombre2Tk.pack()
    """Datos a pedir"""
    mostrarTkMessage=tkinter.Label(ventanaRegistro, text="Gmail:")
    mostrarTkMessage.pack()
    """Entrada del gmail"""
    apellidoTk = tkinter.Entry(ventanaRegistro)
    apellidoTk.pack()
    """Datos a pedir"""
    mostrarTkMessage=tkinter.Label(ventanaRegistro, text="Fecha de Nacimiento:")
    mostrarTkMessage.pack()
    """Entrada de la fecha de nacimiento"""
    apellido2Tk = tkinter.Entry(ventanaRegistro)
    apellido2Tk.pack()
    """Datos a pedir"""
    mostrarTkMessage=tkinter.Label(ventanaRegistro, text="Sexo:")
    mostrarTkMessage.pack()
    """Entrada de la sexualidad"""
    sexoTk = tkinter.Entry(ventanaRegistro)
    sexoTk.pack()

def usuarios():
    coleccionTotal=coleccion.find()
    coleccionUsuario=[]
    coleccionTotal=coleccion.find()
    coleccionContrasena=[]
    for i in coleccionTotal:
        coleccionUsuario.append(i['Usuario'])
        coleccionContrasena.append(i['Usuario'])
    return coleccionUsuario

def Validacion(usuario,contrasena):
    urs=usuarios()
    login=usuarios()
    if (usuario in urs)&(contrasena in login):
        usuario.usuario=usuario
        contrasena.contrasena=contrasena
        print("Bienvenido a nuestra libreria.")
    else:
        messagebox.showwarning("Error, usuario y contrasena no coinciden")


if __name__=="__main__":
    registrar=tk.Button(ventana, text= "Registrarse", cursor="hand1", bg= "white",fg= "black",  width=6, height=1, relief="flat", command = RegistroMongo).place(x=80,y=50)
    inicioSesion=tk.Button(ventana, text= "Inicio de sesion", cursor="hand1", bg= "white",fg= "black",  width=9, height=1, relief="flat", command = Validacion).place(x=80,y=100)
ventana.mainloop()
    

    
    

        