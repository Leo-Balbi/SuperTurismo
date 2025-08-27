# app/components/navbar.py
import flet as ft

APP_TITLE = ft.Row(
    controls=[
        ft.Text("Super", size=26, weight="bold", color="red"),
        ft.Text("Turismo", size=26, weight="bold", color="white"),
    ],
    spacing=4,
)

def appbar(page: ft.Page):
    return ft.AppBar(
        leading=ft.Icon(ft.icons.SPEED),
        title=APP_TITLE,
        center_title=False,
        bgcolor=ft.colors.BLACK87,
        actions=[
            ft.IconButton(ft.icons.HOME, tooltip="Inicio", on_click=lambda e: page.go("/")),
            ft.IconButton(ft.icons.PERSON_ADD, tooltip="Ingreso", on_click=lambda e: page.go("/ingreso")),
            ft.IconButton(ft.icons.UPLOAD_FILE, tooltip="Cargar Excel", on_click=lambda e: page.go("/excel")),
            ft.IconButton(ft.icons.ANALYTICS, tooltip="Dashboard", on_click=lambda e: page.go("/dashboard")),
        ],
    )

def top_buttons(page: ft.Page):
    # Botones “bonitos” reutilizables para bloques o vistas sin AppBar
    return ft.Row(
        [
            ft.ElevatedButton("🏠 Home", on_click=lambda e: page.go("/"), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16))),
            ft.ElevatedButton("📝 Ingreso Manual", on_click=lambda e: page.go("/ingreso"), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16))),
            ft.ElevatedButton("📂 Cargar Excel", on_click=lambda e: page.go("/excel"), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16))),
            ft.ElevatedButton("📊 Dashboard", on_click=lambda e: page.go("/dashboard"), style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=16))),
        ],
        spacing=16,
        wrap=True,
    )
