import flet as ft

def nav_buttons(page):
    return ft.Row(
        [
            ft.ElevatedButton("Inicio", icon=ft.icons.HOME, bgcolor="#e10600", color="white", on_click=lambda _: page.go("/")),
            ft.ElevatedButton("Dashboard", icon=ft.icons.DASHBOARD, bgcolor="#111", color="white", on_click=lambda _: page.go("/dashboard")),
            ft.ElevatedButton("Ingreso", icon=ft.icons.ADD, bgcolor="#111", color="white", on_click=lambda _: page.go("/ingreso")),
            ft.ElevatedButton("Cargar Excel", icon=ft.icons.UPLOAD_FILE, bgcolor="#111", color="white", on_click=lambda _: page.go("/excel")),
            ft.ElevatedButton("Atrás", icon=ft.icons.ARROW_BACK, bgcolor="#111", color="white", on_click=lambda _: page.go(page.route_history[-2] if len(page.route_history) > 1 else "/")),
        ],
        alignment="center",
        spacing=18
    )