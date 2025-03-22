from tkinter import Tk, Label, Entry, Button, Frame, ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime


# Función para agregar un evento
def agregar_evento():
    fecha = calendario.get_date()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Validar que todos los campos estén llenos
    if not fecha or not hora or not descripcion:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    # Validar el formato de la hora (HH:MM)
    try:
        datetime.strptime(hora, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Formato de hora inválido. Use HH:MM.")
        return

    # Agregar el evento al Treeview
    tree.insert("", "end", values=(fecha, hora, descripcion))
    entrada_hora.delete(0, 'end')
    entrada_descripcion.delete(0, 'end')


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showerror("Error", "Seleccione un evento para eliminar.")
        return

    # Confirmar la eliminación
    confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento seleccionado?")
    if confirmar:
        for item in seleccion:
            tree.delete(item)


# Crear la ventana principal
ventana = Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x400")

# Frame para la selección de fecha
frame_fecha = Frame(ventana)
frame_fecha.pack(pady=10)

Label(frame_fecha, text="Seleccionar Fecha:").pack(side="left", padx=5)
calendario = Calendar(frame_fecha, selectmode="day", date_pattern="dd/mm/yyyy")
calendario.pack(side="left")

# Frame para los campos de entrada
frame_entrada = Frame(ventana)
frame_entrada.pack(pady=10)

Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=0, padx=5)
entrada_hora = Entry(frame_entrada)
entrada_hora.grid(row=0, column=1, padx=5)

Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5)
entrada_descripcion = Entry(frame_entrada)
entrada_descripcion.grid(row=1, column=1, padx=5)

# Frame para los botones
frame_botones = Frame(ventana)
frame_botones.pack(pady=10)

Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento).grid(row=0, column=1, padx=5)
Button(frame_botones, text="Salir", command=ventana.quit).grid(row=0, column=2, padx=5)

# TreeView para mostrar los eventos
tree = ttk.Treeview(ventana, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()



