# app/views/home.py
import flet as ft
from app.components.navbar import appbar, top_buttons

def home_view(page: ft.Page):
    # Contenido central
    hero = ft.Column(
        [
            ft.Row(
                [ft.Text("Super", size=44, weight="w900", color="red"),
                 ft.Text("Turismo", size=44, weight="w900", color="white")],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text("Gestión de Precintos y Piezas", size=20, opacity=0.9, text_align=ft.TextAlign.CENTER),
            top_buttons(page),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=16,
    )

    # FAB a Inicio (aquí ya estamos en inicio; lo dejamos como refresh)
    fab_home = ft.FloatingActionButton(icon=ft.icons.HOME, on_click=lambda e: page.go("/"))

    return ft.View(
        route="/",
        controls=[
            appbar(page),
            ft.Container(
                content=ft.Stack(
                    controls=[
                        ft.Container(hero, alignment=ft.alignment.center),
                        ft.Container(fab_home, alignment=ft.alignment.bottom_right, padding=16),
                    ]
                ),
                expand=True,
                padding=20,
            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
