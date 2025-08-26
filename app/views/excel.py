import flet as ft
from app.components.navbar import navbar

def excel_view(page):
    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            ft.toast(f"Archivo {e.files[0].name} cargado correctamente ✅")

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    return ft.View(
        "/excel",
        [
            ft.Text("📂 Cargar archivo Excel", size=28, weight="bold", color="red"),
            ft.ElevatedButton(
                "Seleccionar archivo Excel",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: file_picker.pick_files(allowed_extensions=["xlsx"])
            ),
            navbar(page)
        ]
    )
