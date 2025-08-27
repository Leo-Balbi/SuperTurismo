# app/components/notify.py
import flet as ft

def notify(page: ft.Page, msg: str, success: bool = True):
    color = ft.colors.GREEN if success else ft.colors.RED_400
    page.snack_bar = ft.SnackBar(
        content=ft.Text(msg),
        bgcolor=color,
        show_close_icon=True,
    )
    page.snack_bar.open = True
    page.update()
