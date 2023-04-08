import tkinter as tk
import sqlite3

# Función para crear la tabla de usuarios en la base de datos
def crear_tabla():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  usuario TEXT,
                  contraseña TEXT)''')
    conn.commit()
    conn.close()

# Función para registrar un usuario en la base de datos
def registrar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
              (usuario, contraseña))
    conn.commit()
    conn.close()
    label_estado.config(text="Usuario registrado correctamente")

# Función para iniciar sesión con un usuario registrado
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE usuario=? AND contraseña=?",
              (usuario, contraseña))
    resultado = c.fetchone()
    conn.close()
    if resultado is None:
        label_estado.config(text="Usuario o contraseña incorrectos")
    else:
        label_estado.config(text="Inicio de sesión correcto")

# Función para mostrar los usuarios registrados en la base de datos
def ver_usuarios():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    conn.close()
    for usuario in usuarios:
        print(usuario)

# Crear la ventana principal
root = tk.Tk()
root.title("Menú de usuarios")
root.geometry("500x500")
root['bg'] = '#008000'

# Crear el menú
menu = tk.Menu(root)
root.config(menu=menu)

# Crear las opciones del menú
opcion_registrar = tk.Menu(menu)
menu.add_cascade(label="Registrar", menu=opcion_registrar)
opcion_registrar.add_command(label="Registrar usuario", command=registrar_usuario)

opcion_iniciar_sesion = tk.Menu(menu)
menu.add_cascade(label="Iniciar sesión", menu=opcion_iniciar_sesion)
opcion_iniciar_sesion.add_command(label="Iniciar sesión", command=iniciar_sesion)

opcion_ver_usuarios = tk.Menu(menu)
menu.add_cascade(label="Ver usuarios", menu=opcion_ver_usuarios)
opcion_ver_usuarios.add_command(label="Ver usuarios registrados", command=ver_usuarios)

# Crear los widgets de la ventana principal
label_usuario = tk.Label(root, text="Usuario:")
entry_usuario = tk.Entry(root)
label_contraseña = tk.Label(root, text="Contraseña:")
entry_contraseña = tk.Entry(root, show="*")
boton_registrar = tk.Button(root, text="Registrar", command=registrar_usuario)
boton_iniciar_sesion = tk.Button(root, text="Iniciar sesión", command=iniciar_sesion)
label_estado = tk.Label(root, text="")

# Colocar los widgets en la ventana principal
label_usuario.grid(row=0, column=0)
entry_usuario.grid(row=0, column=1)
label_contraseña.grid(row=1, column=0)
entry_contraseña.grid(row=1, column=1)
boton_registrar.grid(row=2, column=0)
boton_iniciar_sesion.grid(row=2, column=1)
label_estado.grid(row=3, column=0, columnspan=2)

# Ejecutar la aplicación
root.mainloop()

