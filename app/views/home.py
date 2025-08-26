import flet as ft
from app.components.navbar import navbar

def home_view(page):
    return ft.View(
        "/",
        [
            ft.Text("SuperTurismo", size=40, weight="bold", color="red"),
            ft.Text("Gestión de Precintos y Piezas", size=22, color="white"),
            navbar(page)
        ],
        vertical_alignment="center",
        horizontal_alignment="center"
    )
