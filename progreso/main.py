import tkinter as tk
from tkinter import ttk


def incrementar_barra():
    valor = barra_progreso['value']
    if valor < 100:
        barra_progreso['value'] = valor + 10
        actualizar_porcentaje()


def completar_barra():
    valor = barra_progreso['value']
    if valor < 100:
        barra_progreso['value'] = valor + 5
        actualizar_porcentaje()
        ventana.after(100, completar_barra)


def resetear_barra():
    barra_progreso['value'] = 0
    actualizar_porcentaje()


def actualizar_porcentaje():
    valor = barra_progreso['value']
    porcentaje.set(f'{int(valor)}%')


ventana = tk.Tk()
ventana.title('Barra de Progreso')
ventana.geometry('300x250')
ventana.configure(bg='#2c3e50')

# Estilo barra de progreso y botones
style = ttk.Style()
style.theme_use('clam')

# Estilo barra de progreso
style.configure('TProgressbar', troughcolor='#34495e',
                background='#1abc9c', thickness=20)

# Estio botones
style.configure('TButton', font=('Helvetica', 10, 'bold'),
                background='#2980B9', foreground='white')
style.map('TButton', backgruund=[('active', '#3498DB')])

# Creacion de Widgets
barra_progreso = ttk.Progressbar(ventana, orient='horizontal', length=200,
                                 mode='determinate', style='TProgressbar')

barra_progreso.pack(pady=20)

porcentaje = tk.StringVar()
porcentaje.set('0%')

etiqueta_porcentaje = tk.Label(ventana, textvariable=porcentaje,
                               font=('Helvetica', 10, 'bold'), bg="#2c3e50", fg='white')
etiqueta_porcentaje.pack(pady=10)

boton_incremento = ttk.Button(ventana, text='Incremento', command=incrementar_barra,
                              style='TButton')
boton_incremento.pack(pady=5)

boton_completar = ttk.Button(
    ventana, text='Completar', command=completar_barra, style='TButton')
boton_completar.pack(pady=5)

boton_resetear = ttk.Button(
    ventana, text='Resetear', command=resetear_barra, style='TButton')
boton_resetear.pack(pady=5)

ventana.mainloop()
