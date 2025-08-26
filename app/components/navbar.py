import flet as ft

def navbar(page):
    return ft.Row([
        ft.ElevatedButton("🏠 Home", on_click=lambda e: page.go("/")),
        ft.ElevatedButton("📝 Ingreso Manual", on_click=lambda e: page.go("/ingreso")),
        ft.ElevatedButton("📂 Cargar Excel", on_click=lambda e: page.go("/excel")),
        ft.ElevatedButton("📊 Dashboard", on_click=lambda e: page.go("/dashboard")),
    ], spacing=20)
