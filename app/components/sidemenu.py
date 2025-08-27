# app/components/sidemenu.py
import flet as ft

DESTS = [
    ("Inicio", ft.icons.HOME, "/"),
    ("Ingreso", ft.icons.NOTE_ADD, "/ingreso"),
    ("Excel", ft.icons.UPLOAD_FILE, "/excel"),
    ("Dashboard", ft.icons.ANALYTICS, "/dashboard"),
]

def sidemenu(page: ft.Page, selected_index: int = 0):
    return ft.NavigationRail(
        selected_index=selected_index,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=72,
        group_alignment=-0.9,
        leading=ft.FloatingActionButton(icon=ft.icons.SPEED, mini=True, tooltip="SuperTurismo"),
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icon(icon), label=label) for label, icon, _ in DESTS
        ],
        on_change=lambda e: page.go(DESTS[e.control.selected_index][2]),
    )
