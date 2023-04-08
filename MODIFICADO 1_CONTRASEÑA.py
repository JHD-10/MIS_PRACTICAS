import tkinter as tk

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "admin" and contrasena == "password":
        resultado.config(text="Inicio de sesión exitoso")
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

ventana = tk.Tk()
ancho_ventana = 620
alto_ventana = 480
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("Inicio de sesión")
ventana['bg'] = '#8FBC8F'   


# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana)
contrasena_usuario = tk.Entry(ventana, show="*")
contrasena_usuario.pack()
nombre_usuario['bg'] = '#F0FFFF'
contrasena_usuario['bg'] = '#F0FFFF'

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=10, pady=10)
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()
iniciar_sesion['bg'] = '#F0FFFF'
salir['bg'] = '#F0FFFF'

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)
resultado['bg'] = '#8FBC8F'
ventana.mainloop()