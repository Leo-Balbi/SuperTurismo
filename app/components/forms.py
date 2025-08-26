import flet as ft
from app.utils.constants import EQUIPOS, PIEZAS, SITUACIONES
from app.db.queries import insert_registro

def ingreso_form(page):
    temporada_tf = ft.TextField(label="Temporada (ej: Temporada 1)", width=250)
    fecha_picker = ft.DatePicker(label="Fecha", width=250)
    equipo_dd = ft.Dropdown(label="Equipo", width=250,
        options=[ft.dropdown.Option(e) for e in EQUIPOS.keys()])
    piloto_dd = ft.Dropdown(label="Piloto", width=250)
    pieza_dd = ft.Dropdown(label="Pieza", width=300,
        options=[ft.dropdown.Option(p) for p in PIEZAS])
    precinto_tf = ft.TextField(label="Número de precinto", width=250)
    motivo_tf = ft.TextField(label="Motivo del reemplazo", width=400, multiline=True)
    situacion_dd = ft.Dropdown(label="Situación", width=250,
        options=[ft.dropdown.Option(s) for s in SITUACIONES])

    def actualizar_pilotos(e):
        piloto_dd.options = [ft.dropdown.Option(p) for p in EQUIPOS[equipo_dd.value]]
        page.update()

    equipo_dd.on_change = actualizar_pilotos

    def guardar(e):
        insert_registro(
            temporada_tf.value,
            str(fecha_picker.value),
            equipo_dd.value,
            piloto_dd.value,
            pieza_dd.value,
            precinto_tf.value,
            motivo_tf.value,
            situacion_dd.value
        )
        ft.toast("Registro guardado ✅")

    return ft.Column([
        ft.Row([temporada_tf, fecha_picker]),
        ft.Row([equipo_dd, piloto_dd]),
        ft.Row([pieza_dd, precinto_tf]),
        motivo_tf,
        situacion_dd,
        ft.ElevatedButton("💾 Guardar", on_click=guardar)
    ])
