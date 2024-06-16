import os
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import font, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import datetime
import babel.numbers

paises_europa = ["Alemania", "Austria", "Bélgica", "Bulgaria", "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia", "España", "Estonia", "Finlandia", "Francia", "Grecia", "Hungría", "Irlanda", "Italia", "Letonia", "Lituania", "Luxemburgo", "Malta", "Noruega", "Países Bajos", "Polonia", "Portugal", "Reino Unido", "República Checa", "Rumania", "Serbia", "Suecia", "Suiza"]
conn = sqlite3.connect('Base de Datos/JBC_Database.db')
cursor = conn.cursor()

class HotelReservationApp:

    @staticmethod
    def get_resource_path(relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def __init__(self):
        # Inicialización de la aplicación
        self.root = tk.Tk()
        self.root.title("Hoteles de lujo | JBC Hoteles, Resorts")
        self.root.configure(bg="#BCA57F")
        
        # Creación de la ventana principal
        self.create_main_window()
        
        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición central de la ventana
        window_width = 1200
        window_height = 800
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.root.mainloop()
        
    def create_main_window(self):
        # Configuración de la ventana principal y carga de una imagen
        img = Image.open(HotelReservationApp.get_resource_path("anantaraJPG.jpg"))
        img_width, img_height = img.size

        self.frame = Frame(self.root, width=img_width, height=img_height)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        self.img = ImageTk.PhotoImage(img)
        self.label = Label(self.frame, image=self.img)
        self.label.pack()

        self.root.geometry("{}x{}".format(img_width, img_height))
        

        # Creación de elementos de la interfaz de usuario
        i1 = Label(self.root, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Trebuchet MS', 30))
        i2 = Label(self.root, text="Hotels-Resorts-Spas", fg="white", bg="#BCA57F", font=('Century Gothic', 11))
        i1.pack(fill="x")
        i2.pack(fill="x")
        
        
        self.frame = Frame(self.root)
        self.frame.place(relx=0.5, rely=0.40, anchor="center")
        bf = Frame(self.root)
        bf.pack(side="bottom")
        bf1 = Frame(self.root)
        bf1.pack(side="bottom", anchor="sw")
        bf2 = Frame(self.root)
        bf2.place(relx=0.178, rely=0.9995, anchor="se")
        bf3 = Frame(self.root)
        bf3.place(relx=0.176, rely=0.978, anchor="se")
        bf4 = Frame(self.root)
        bf4.place(relx=0.5, rely=0.45900005, anchor="center")
        bottomframe = Frame(self.root)
        bottomframe.place(relx=0.9997, rely=0.9995, anchor="se")


        i5 = Label(bf, text="© 2024 JBC Hoteles, Resorts & Spas", bg="#7A5C30", fg="white")
        i5.pack(side=LEFT)
        i6 = Button(bottomframe, text="Terminos de privacidad", bg="#7A5C30", fg="white")
        i6.pack(side=RIGHT)
        i7 = Button(bottomframe, text="Cookies", bg="#7A5C30", fg="white")
        i7.pack(side=RIGHT)
        i8 = Button(bottomframe, text="Terminos y condiciones", bg="#7A5C30", fg="white")
        i8.pack(side=RIGHT)
        i9 = Button(bottomframe, text="Preguntas", bg="#7A5C30", fg="white")
        i9.pack(side=RIGHT)
        i12 = Label(bf2, text="Contacta con nosotros: +34 674 649 638", bg="#7A5C30", fg="white")
        i12.pack(side=LEFT)
        i12 = Label(bf3, text="Email: reservacontacto@jbchotels.com", bg="#7A5C30", fg="white")
        i12.pack(side=LEFT)

        i3 = Button(self.frame, text="REGISTRO DE CLIENTES", command=self.sign_up, font=('Trebuchet MS', 15), bg="#BCA57F", fg="white")
        i3.pack(side=RIGHT)

        i4 = Button(self.frame, text="RESERVA", command=self.login, font=('Trebuchet MS', 15), bg="#BCA57F", fg="white")
        i4.pack(side=RIGHT)

        cancel_button = Button(bf4, text="GESTION RESERVAS", command=self.cancel_reservation, font=('Trebuchet MS', 15), bg="#BCA57F", fg="white")
        cancel_button.pack(side=BOTTOM)

    def cancel_reservation(self):
        d = Toplevel()
        d.title("Habitaciones JBC Hoteles")
        d.configure(bg="#F0F0FF")
        
        screen_width = d.winfo_screenwidth()
        screen_height = d.winfo_screenheight()

        window_width = 1000
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        d.geometry(f"{window_width}x{window_height}+{x}+{y}")

        i10 = Label(d, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Dotum', 25))
        i11 = Label(d, text="Merida Resort", fg="white", bg="#BCA57F", font=('Dotum', 12))
        i10.pack(fill="x")
        i11.pack(fill="x")

        estado_cancelada = BooleanVar()
        estado_confirmada = BooleanVar()

    def cancel_reservation(self):
        d = Toplevel()
        d.title("Habitaciones JBC Hoteles")
        d.configure(bg="#F0F0FF")
        
        screen_width = d.winfo_screenwidth()
        screen_height = d.winfo_screenheight()

        window_width = 1000
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        d.geometry(f"{window_width}x{window_height}+{x}+{y}")

        i10 = Label(d, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Dotum', 25))
        i11 = Label(d, text="Merida Resort", fg="white", bg="#BCA57F", font=('Dotum', 12))
        i10.pack(fill="x")
        i11.pack(fill="x")

        estado_cancelada = BooleanVar()
        estado_confirmada = BooleanVar()

        def buscar():
            def buscar_en_bd(dni, estado_cancelada, estado_confirmada):

                # Ejecuta la consulta
                query = "SELECT id, cliente_dni, habitacion_id, personas, adultos, menores, fecha_inicio, fecha_fin, estado, cod_empleado FROM RESERVAS WHERE cliente_dni=?"
                if estado_cancelada == True and estado_confirmada == True:
                    cursor.execute(query, (dni,))
                    # Obtiene los resultados
                    resultados = cursor.fetchall()
                    return resultados
                else:
                    if estado_cancelada:
                        query += " AND estado='CANCELADA'"
                    if estado_confirmada:
                        query += " AND estado='CONFIRMADA'"
                
                cursor.execute(query, (dni,))
                # Obtiene los resultados
                resultados = cursor.fetchall()
                return resultados

            # Obtener el DNI ingresado
            dni = dni_entry.get()
            # Realizar la consulta en la base de datos
            # (reemplaza esto con tu propia lógica)
            resultados = buscar_en_bd(dni, estado_cancelada.get(), estado_confirmada.get())
            # Limpiar la lista actual
            for i in lista.get_children():
                lista.delete(i)
            # Llenar la lista con los resultados
            for resultado in resultados:
                lista.insert('', END, values=resultado)

        # Elementos de la ventana
        Label(d, text="Buscar por DNI:", bg="#F0F0FF").pack(pady=10)
        dni_entry = Entry(d)
        dni_entry.pack()

        Checkbutton(d, text="CANCELADA", variable=estado_cancelada).pack()
        Checkbutton(d, text="CONFIRMADA", variable=estado_confirmada).pack()

        buscar_button = Button(d, text="Buscar", command=buscar)
        buscar_button.pack(pady=5)

        lista = ttk.Treeview(d, columns=("id", "cliente_dni", "habitacion_id", "personas", "adultos", "menores", "fecha_inicio", "fecha_fin", "estado", "cod_empleado"), show="headings")
        lista.heading("id", text="ID", anchor="center")
        lista.heading("cliente_dni", text="DNI", anchor="center")
        lista.heading("habitacion_id", text="ID Habitación", anchor="center")
        lista.heading("personas", text="Personas", anchor="center")
        lista.heading("adultos", text="Adultos", anchor="center")
        lista.heading("menores", text="Menores", anchor="center")
        lista.heading("fecha_inicio", text="Fecha de inicio", anchor="center")
        lista.heading("fecha_fin", text="Fecha de fin", anchor="center")
        lista.heading("estado", text="Estado", anchor="center")
        lista.heading("cod_empleado", text="Código Empleado", anchor="center")

        lista.column("id", width=50, anchor="center")
        lista.column("cliente_dni", width=50, anchor="center")
        lista.column("habitacion_id", width=100, anchor="center")
        lista.column("personas", width=75, anchor="center")
        lista.column("adultos", width=75, anchor="center")
        lista.column("menores", width=75, anchor="center")
        lista.column("fecha_inicio", width=100, anchor="center")
        lista.column("fecha_fin", width=100, anchor="center")
        lista.column("estado", width=100, anchor="center")
        lista.column("cod_empleado", width=100, anchor="center")

        lista.pack(fill=BOTH, expand=True)

        def cancelar_reserva_seleccionada():
            # Obtener el índice de la reserva seleccionada
            seleccion = lista.selection()
            if seleccion:
                # Obtener la ID de la reserva seleccionada
                id_reserva = lista.item(seleccion)['values'][0]  # Suponiendo que el ID de la reserva está en la primera columna
                # Actualizar el estado de la reserva a "CANCELADA" en la base de datos
                try:
                    cursor.execute("UPDATE RESERVAS SET estado='CANCELADA' WHERE id=?", (id_reserva,))
                    conn.commit()
                except sqlite3.Error as e:
                    print(e)
                    return
                # Actualizar la lista después de la cancelación
                buscar()

        # Botón para cancelar la reserva seleccionada
        cancelar_button = Button(d, text="Cancelar reserva seleccionada", command=cancelar_reserva_seleccionada)
        cancelar_button.pack(pady=5)
        

        
    def sign_up(self):
        # Función para registrar nuevos usuarios
        c = Toplevel()
        c.title("REGISTRO")
        c.configure(bg="#BCA57F")
        
        # Obtener dimensiones de la pantalla
        screen_width = c.winfo_screenwidth()
        screen_height = c.winfo_screenheight()

        # Calcular la posición central de la ventana
        window_width = 550
        window_height = 550
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana
        c.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        i45 = Label(c, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Trebuchet MS', 25))
        i46 = Label(c, text="Hotels-Resorts-Spas", fg="white", bg="#BCA57F", font=('Century Gothic', 12))
        i45.pack(fill="x")
        i46.pack(fill="x")

        Nombre = StringVar()
        direccion = StringVar()
        Numero = IntVar()
        Email = StringVar()
        dni = StringVar()
        pais = StringVar()
        cod_empleado = IntVar()

        def database_registro():
            dNombre = Nombre.get()
            ddireccion = direccion.get()
            dNumero = Numero.get()
            dEmail = Email.get()
            ddni = dni.get()
            dpais = pais.get()
            dcod_empleado = cod_empleado.get()

            if not dNombre or not ddireccion or not dNumero or not dEmail or not ddni or not dpais or not dcod_empleado:
                messagebox.showerror('Error', 'Se requiere rellenar todos los campos.')
                return

            with conn:
                try:
                    cursor.execute('INSERT INTO CLIENTES (nombre, direccion, telefono, email, cliente_dni, pais, cod_empleado) VALUES (?, ?, ?, ?, ?, ?, ?)', (dNombre, ddireccion, dNumero, dEmail, ddni, dpais, dcod_empleado))
                    conn.commit()
                except sqlite3.Error as e:
                    messagebox.showerror('Error', 'Error al introducir los datos en la base de datos')
                    print(e)
                    return
                else:
                    messagebox.showinfo('Information', 'REGISTRO COMPLETADO')


        c1 = Label(c, text="Nombre:").place(x=120, y=100)
        c2 = Label(c, text="Direccion:").place(x=120, y=150)
        c3 = Label(c, text="Numero de telefeno:").place(x=120, y=200)
        c4 = Label(c, text="Email:").place(x=120, y=250)
        c5 = Label(c, text="DNI:").place(x=120, y=300)
        c6 = Label(c, text="Pais:").place(x=120, y=350)
        c7 = Label(c, text="Codigo Empleado:").place(x=120, y=400)
        
        ce1 = Entry(c, textvar=Nombre, bd=3)
        ce1.place(x=260, y=100)
        ce2 = Entry(c, textvar=direccion, bd=3)
        ce2.place(x=260, y=150)
        ce3 = Entry(c, textvar=Numero, bd=3)
        ce3.place(x=260, y=200)
        ce4 = Entry(c, textvar=Email, bd=3)
        ce4.place(x=260, y=250)
        ce5 = Entry(c, textvar=dni, bd=3)
        ce5.place(x=260, y=300)
        ce6 = ttk.Combobox(c, textvar=pais, values=paises_europa, state="readonly")
        ce6.place(x=260, y=350)
        ce7 = Entry(c, textvar=cod_empleado, bd=3)
        ce7.place(x=260, y=400)
        
        ce3 = Button(c, text="REGISTRAR", command=database_registro, font=('Dotum', 10))
        ce3.place(x=280, y=450)
            
    def login(self):
        # Función para iniciar sesión
        b = Tk()
        b.title("INICIO")
        b.configure(bg="#BCA57F")
        
        # Obtener dimensiones de la pantalla
        screen_width = b.winfo_screenwidth()
        screen_height = b.winfo_screenheight()

        # Calcular la posición central de la ventana
        window_width = 330
        window_height = 355
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana
        b.geometry(f"{window_width}x{window_height}+{x}+{y}")

        i47 = Label(b, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Dotum', 25))
        i48 = Label(b, text="Hotels-Resorts-Spas", fg="white", bg="#BCA57F", font=('Dotum', 12))
        i47.pack(fill="x")
        i48.pack(fill="x")

        def LOGin():
            cliente_dni = e1.get()
            cod_empleado = e2.get()

            try: 
                # Verificar si el empleado existe
                query=f"SELECT * FROM EMPLEADOS WHERE cod_empleado={cod_empleado};"
                cursor.execute(query)
                empleado = cursor.fetchone()

                # Verificar si el cliente existe
                query=f"SELECT * FROM CLIENTES WHERE cliente_dni='{cliente_dni}';"
                cursor.execute(query)
                cliente = cursor.fetchone()

            except sqlite3.Error as e:
                messagebox.showerror('Error', 'Error al introducir los datos en la base de datos')
                print(e)
            
            if cliente and empleado:
                self.hotel_log(cliente_dni, cod_empleado)
                b.destroy()
            elif cliente_dni == "" or cod_empleado == "": 
                messagebox.showinfo('message', "Introduce los campos")
            else:
                messagebox.showerror('error', "Credenciales incorrectas")



        L1 = Label(b, text="NIF Cliente").place(x=48, y=80)
        L2 = Label(b, text="COD Empleado").place(x=25, y=140)

        e1 = Entry(b, bd=3)
        e1.place(x=120, y=80)

        e2 = Entry(b, bd=3)
        e2.place(x=120, y=140)

        ce20 = Button(b, text="INICIAR", command=LOGin)
        ce20.place(x=150, y=200)

    def hotel_log(self, dni, cod_empleado, previous_window=None):
        # Función para mostrar información sobre habitaciones de hotel

        if previous_window:
            previous_window.destroy()

        d = Toplevel()
        d.title("Habitaciones JBC Hoteles")
        d.configure(bg="#F0F0FF")
        
        # Obtener dimensiones de la pantalla
        screen_width = d.winfo_screenwidth()
        screen_height = d.winfo_screenheight()

        # Calcular la posición central de la ventana
        window_width = 1600
        window_height = 800
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer la geometría de la ventana
        d.geometry(f"{window_width}x{window_height}+{x}+{y}")

        b = Label(d, bg="#F0F0FF", bd=2, relief=RIDGE)
        b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)

        a = Label(d, bg="#F0F0FF", bd=2, relief=RIDGE)
        a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

        i10 = Label(d, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Dotum', 25))
        i11 = Label(d, text="Merida Resort", fg="white", bg="#BCA57F", font=('Dotum', 12))
        i10.pack(fill="x")
        i11.pack(fill="x")

        i30 = Label(d, text="TEMPLUM MINERVAE", font=('Dotum', 22, 'bold'))
        i30.place(x=430, y=120)

        image = Image.open(HotelReservationApp.get_resource_path("pool.jpg"))
        image = image.resize((350, 200), Image.LANCZOS)
        test = ImageTk.PhotoImage(image)
        labell = Label(d, image=test)
        labell.image = test
        labell.place(x=70, y=120)

        i31 = Label(d, text="*Mejor flexibilidad con desayuno y cena", font=('Dotum', 10, 'bold'), bg="#F0F0FF")
        i31.place(x=430, y=170)

        i32=Label(d,text="*Dos comidas incluidas",font=('Dotum',10),bg="#F0F0FF")
        i32.place(x=430,y=210)

        i33=Label(d,text="*No reembolsable",font=('Dotum',10,'bold'),bg="#F0F0FF")
        i33.place(x=430,y=250)

        i34=Label(d,text="*Los niños se alojan gratis",font=('Dotum',10),bg="#F0F0FF")
        i34.place(x=430,y=290)

        i35=Label(d,text="- WI-FI GRATIS",font=('Dotum',10),bg="#F0F0FF")
        i35.place(x=70,y=380)

        i36=Label(d,text="- TAMAÑO DE LA HABITACIÓN 50 M2",font=('Dotum',10),bg="#F0F0FF")
        i36.place(x=70,y=410)

        i37=Label(d,text="- MÁXIMO 3 ADULTOS",font=('Dotum',10),bg="#F0F0FF")
        i37.place(x=70,y=440)


        i38 = Label(d, text="- SERVICIO DE HABITACIONES", font=('Dotum', 10), bg="#F0F0FF")
        i38.place(x=70, y=470)


        image = Image.open(HotelReservationApp.get_resource_path("Rate-1.jpg"))
        test = ImageTk.PhotoImage(image)
        labell = Label(d, image=test)
        labell.image = test
        labell.place(x=450, y=380)

        i30=Label(d,text="VILLA AUGUSTA",font=('Dotum',22,'bold'))
        i30.place(x=1210,y=120)
    
        image = Image.open(HotelReservationApp.get_resource_path("sv_room.jpg"))
        image = image.resize((350, 200), Image.LANCZOS)
        test=ImageTk.PhotoImage(image)
        labell=Label(d,image=test)
        labell.image=test
        labell.place(x=850,y=120)

        i31=Label(d,text="*Mejor flexibilidad con desayuno y cena",font=('Dotum',10,'bold'),bg="#F0F0FF")
        i31.place(x=1210,y=170)

        i32=Label(d,text="*Dos comidas incluidas",font=('Dotum',10),bg="#F0F0FF")
        i32.place(x=1210,y=210)

        i33=Label(d,text="*No reembolsable",font=('Dotum',10,'bold'),bg="#F0F0FF")
        i33.place(x=1210,y=250)

        i34=Label(d,text="*Los niños se alojan gratis",font=('Dotum',10),bg="#F0F0FF")
        i34.place(x=1210,y=290)

        i35=Label(d,text="- WI-FI GRATIS",font=('Dotum',10),bg="#F0F0FF")
        i35.place(x=850,y=380)

        i36=Label(d,text="- TAMAÑO DE LA HABITACIÓN 35 M2",font=('Dotum',10),bg="#F0F0FF")
        i36.place(x=850,y=410)

        i37=Label(d,text="- MÁXIMO 2 ADULTOS",font=('Dotum',10),bg="#F0F0FF")
        i37.place(x=850,y=440)

        i38=Label(d,text="- SERVICIO DE HABITACIONES",font=('Dotum',10),bg="#F0F0FF")
        i38.place(x=850,y=470)


        image = Image.open(HotelReservationApp.get_resource_path("Rate-2.jpg"))
        test=ImageTk.PhotoImage(image)
        labell=Label(d,image=test)
        labell.image=test
        labell.place(x=1230,y=380)


        def hotel_log_A():
            # Función para mostrar información sobre otras habitaciones de hotel
            f = Toplevel()
            f.title("Habitaciones JBC Hoteles")
            f.configure(bg="#F0F0FF")

            # Obtener dimensiones de la pantalla
            screen_width = f.winfo_screenwidth()
            screen_height = f.winfo_screenheight()

            # Calcular la posición central de la ventana
            window_width = 1600
            window_height = 800
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Establecer la geometría de la ventana
            f.geometry(f"{window_width}x{window_height}+{x}+{y}")

            b = Label(f, bg="#F0F0FF", bd=2, relief=RIDGE)
            b.place(relx=0.032, rely=0.1, relheight=0.85, relwidth=0.45)

            a = Label(f, bg="#F0F0FF", bd=2, relief=RIDGE)
            a.place(relx=0.52, rely=0.1, relheight=0.85, relwidth=0.45)

            i101 = Label(f, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Dotum', 25))
            i111 = Label(f, text="Merida Resort", fg="white", bg="#BCA57F", font=('Dotum', 12))
            i101.pack(fill="x")
            i111.pack(fill="x")

            i301 = Label(f, text="PALATIUM MERIDAE", font=('Dotum', 22, 'bold'))
            i301.place(x=430, y=120)

            image = Image.open(HotelReservationApp.get_resource_path("Pool_Villa.jpg"))
            image = image.resize((350, 200), Image.LANCZOS)
            test = ImageTk.PhotoImage(image)
            labell1 = Label(f, image=test)
            labell1.image = test
            labell1.place(x=70, y=120)

            i311 = Label(f, text="*Mejor flexibilidad con desayuno y cena", font=('Dotum', 10, 'bold'), bg="#F0F0FF")
            i311.place(x=430, y=170)

            i321=Label(f,text="*Dos comidas incluidas",font=('Dotum',10),bg="#F0F0FF")
            i321.place(x=430,y=210)

            i331=Label(f,text="*No reembolsable",font=('Dotum',10,'bold'),bg="#F0F0FF")
            i331.place(x=430,y=250)

            i341=Label(f,text="*Los niños se alojan gratis",font=('Dotum',10),bg="#F0F0FF")
            i341.place(x=430,y=290)

            i351=Label(f,text="- WI-FI GRATIS",font=('Dotum',10),bg="#F0F0FF")
            i351.place(x=70,y=380)

            i361=Label(f,text="- TAMAÑO DE LA HABITACIÓN 40 M2",font=('Dotum',10),bg="#F0F0FF")
            i361.place(x=70,y=410)

            i371=Label(f,text="- MÁXIMO 2 ADULTOS",font=('Dotum',10),bg="#F0F0FF")
            i371.place(x=70,y=440)



            i381 = Label(f, text="- SERVICIO DE HABITACIONES", font=('Dotum', 10), bg="#F0F0FF")
            i381.place(x=70, y=470)

            image = Image.open(HotelReservationApp.get_resource_path("Rate-3.jpg"))
            test = ImageTk.PhotoImage(image)
            labell1 = Label(f, image=test)
            labell1.image = test
            labell1.place(x=450, y=380)

            i301=Label(f,text="CIRCUS MAXIMUS",font=('Dotum',22,'bold'))
            i301.place(x=1210,y=120)
    
            image = Image.open(HotelReservationApp.get_resource_path("bedroom.jpg"))
            image = image.resize((350, 200), Image.LANCZOS)
            test=ImageTk.PhotoImage(image)
            labell1=Label(f,image=test)
            labell1.image=test
            labell1.place(x=850,y=120)

            i311=Label(f,text="*Mejor flexibilidad con desayuno y cena",font=('Dotum',10,'bold'),bg="#F0F0FF")
            i311.place(x=1210,y=170)

            i321=Label(f,text="*Dos comidas incluidas",font=('Dotum',10),bg="#F0F0FF")
            i321.place(x=1210,y=210)

            i331=Label(f,text="*No reembolsable",font=('Dotum',10,'bold'),bg="#F0F0FF")
            i331.place(x=1210,y=250)
    
            i341=Label(f,text="*Los niños se alojan gratis",font=('Dotum',10),bg="#F0F0FF")
            i341.place(x=1210,y=290)

            i351=Label(f,text="- WI-FI GRATIS",font=('Dotum',10),bg="#F0F0FF")
            i351.place(x=850,y=380)

            i361=Label(f,text="- TAMAÑO DE LA HABITACIÓN 60 M2",font=('Dotum',10),bg="#F0F0FF")
            i361.place(x=850,y=410)

            i371=Label(f,text="- MÁXIMO 4 ADULTOS",font=('Dotum',10),bg="#F0F0FF")
            i371.place(x=850,y=440)

            i381=Label(f,text="- SERVICIO DE HABITACIONES",font=('Dotum',10),bg="#F0F0FF")
            i381.place(x=850,y=470)

            image = Image.open(HotelReservationApp.get_resource_path("Rate-4.jpg"))
            test=ImageTk.PhotoImage(image)
            label1l=Label(f,image=test)
            label1l.image=test
            label1l.place(x=1230,y=380)


            ce30 = Button(f, text="RESERVA", command=lambda: [book(habitacion_id = "003")], font=('Dotum', 14, 'bold'))
            ce30.place(x=500, y=550)

            ce30 = Button(f, text="RESERVA", command=lambda: [book(habitacion_id = "004")], font=('Dotum', 14, 'bold'))
            ce30.place(x=1250, y=550)

            ce600 = Button(f, text="<<", command=lambda: self.hotel_log(f), font=('Dotum', 10))
            ce600.pack(side="left")

        def book(habitacion_id):
            # Función para realizar una reserva
            e = Toplevel()
            e.title("PAGINA DE RESERVA")
            e.configure(bg="#F0F0FF")

            # Obtener dimensiones de la pantalla
            screen_width = e.winfo_screenwidth()
            screen_height = e.winfo_screenheight()

            # Calcular la posición central de la ventana
            window_width = 887
            window_height = 900
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Establecer la geometría de la ventana
            e.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            i51 = Label(e, text="JBC HOTELES", bg="#BCA57F", fg="white", font=('Dotum', 25))
            i52 = Label(e, text="Hotels-Resorts-Spas", fg="white", bg="#BCA57F", font=('Dotum', 12))
            i51.pack(fill="x")
            i52.pack(fill="x")

            i39 = Label(e, text="Detalles de tu reserva", font=('Dotum', 22))
            i39.place(x=370, y=120)

            # Marco para el calendario
            calendar_frame = Frame(e, bg="#F0F0FF")
            calendar_frame.place(x=50, y=200)

            PERSONAS = IntVar()
            ADULTS = IntVar()
            MENORES = IntVar()
            CHECK_IN = StringVar()
            CHECK_OUT = StringVar()

            def database_reserva(PERSONAS, ADULTS, MENORES, CHECK_IN, CHECK_OUT):
                dpersonas = PERSONAS.get()
                dadults = ADULTS.get()
                dmenores = MENORES.get()
                dcheck_in_date = CHECK_IN.get()
                dcheck_out_date = CHECK_OUT.get()

                if not dpersonas or not dadults or not dcheck_in_date or not dcheck_out_date:
                    messagebox.showerror('Error', 'Todas las filas son rqueridas')
                    e.destroy()
                    return
                else:
                    with conn:
                        try:
                            cursor.execute('INSERT INTO RESERVAS (cliente_dni, cod_empleado, habitacion_id, personas, adultos, menores, fecha_inicio, fecha_fin, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',(dni, cod_empleado, habitacion_id, dpersonas, dadults, dmenores, dcheck_in_date, dcheck_out_date, 'CONFIRMADA'))
                            conn.commit()
                        except sqlite3.Error as l:
                            messagebox.showerror('Error', 'Error al introducir los datos de reserva en la base de datos')
                            e.destroy()
                            print(l)
                            print(dni, cod_empleado, habitacion_id, dpersonas, dadults, dmenores, dcheck_in_date, dcheck_out_date)

                            return
                        else:
                            messagebox.showinfo('Information', 'RESERVADO CORRECTAMENTE')
                            e.destroy()

              

            L51 = Label(e, text="PERSONAS:").place(x=370, y=200)
            L52 = Label(e, text="ADULTOS:").place(x=370, y=250)
            L53 = Label(e, text="MENORES:").place(x=370, y=300)

            e51 = Entry(e, bd=3, textvariable=PERSONAS)
            e51.place(x=470, y=200)

            e52 = Entry(e, bd=3, textvariable=ADULTS)
            e52.place(x=470, y=250)

            e53 = Entry(e, bd=3, textvariable=MENORES)
            e53.place(x=470, y=300)
         

            def get_selected_date():
                selected_date_str = cal.get_date()
                # Convertir la cadena a un objeto datetime
                selected_date = datetime.strptime(selected_date_str, '%m/%d/%y')
                # Formatear la fecha en el formato deseado (año-mes-día)
                formatted_date = selected_date.strftime('%Y-%m-%d')
                date_var.set(formatted_date)

            cal = Calendar(calendar_frame, selectmode="day", year=2023, month=8, day=3)
            cal.pack()

            select_date_button = Button(e, text="SELECCIONA FECHA", command=get_selected_date)
            select_date_button.place(x=220,y=400)
    
            date_var = tk.StringVar()
            selected_date_label = Label(e, textvariable=date_var)
            selected_date_label.place(x=150,y=400)

            def update_checkin_date():
                checkin_entry.delete(0, tk.END)
                checkin_entry.insert(0, date_var.get())
                CHECK_IN.set(date_var.get())
        
            def update_checkout_date():
                checkout_entry.delete(0, tk.END)
                checkout_entry.insert(0, date_var.get())
                CHECK_OUT.set(date_var.get()) 
                
            checkin_label = Label(e, text="CHECK-IN:")
            checkin_label.place(x=370,y=350)
            
            checkin_entry = tk.Entry(e, textvariable=CHECK_IN)
            checkin_entry.place(x=470,y=350)
            
            update_checkin_button = Button(e, text="CONFIRMA CHECK-IN", command=update_checkin_date)
            update_checkin_button.place(x=470,y=385)

            checkout_label = Label(e, text="CHECK-OUT:")
            checkout_label.place(x=370,y=435)
            
            checkout_entry = tk.Entry(e, textvariable=CHECK_OUT)
            checkout_entry.place(x=470,y=435)
            
            update_checkout_button = Button(e, text="CONFIRMA CHECK-OUT", command=update_checkout_date)
            update_checkout_button.place(x=470,y=470)

            insert_button = Button(e, text="CONFIRMA", command=lambda:database_reserva(PERSONAS, ADULTS, MENORES, CHECK_IN, CHECK_OUT), font=('Dotum', 14, 'bold')) 
            insert_button.place(x=450, y=600)

        ce30 = Button(d, text="RESERVA", command=lambda: [book(habitacion_id = "002")], font=('Dotum', 14, 'bold'))
        ce30.place(x=500, y=550)

        ce30 = Button(d, text="RESERVA", command=lambda: [book(habitacion_id = "001")], font=('Dotum', 14, 'bold'))
        ce30.place(x=1250, y=550)

        ce60 = Button(d, text=">>",command=lambda: [hotel_log_A(), d.destroy()],font=('Dotum', 10))
        ce60.pack(side="right")

if __name__ == "__main__":
    app = HotelReservationApp()







        
