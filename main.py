import flet as ft
from app.routes import route_change
from app.db.database import init_db

def main(page: ft.Page):
    page.title = "SuperTurismo"
    page.theme_mode = "dark"
    page.scroll = "auto"
    page.window_width = 1280
    page.window_height = 840

    init_db()

    page.on_route_change = lambda e: route_change(page)
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)
