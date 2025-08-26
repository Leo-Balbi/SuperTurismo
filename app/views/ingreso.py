import flet as ft
from app.components.navbar import navbar
from app.components.forms import ingreso_form

def ingreso_view(page):
    return ft.View(
        "/ingreso",
        [
            ft.Text("📝 Ingreso Manual de Registro", size=28, weight="bold", color="red"),
            ingreso_form(page),
            navbar(page)
        ]
    )
