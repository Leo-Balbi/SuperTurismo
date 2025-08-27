import flet as ft
import pandas as pd
from app.components.navbuttons import nav_buttons

def excel_view(page):
    result_text = ft.Text("", size=16, color="green")
    table = ft.DataTable(
        columns=[ft.DataColumn(ft.Text("Esperando archivo..."))],
        rows=[]
    )

    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            try:
                df = pd.read_excel(file_path)
                page.session.set("excel_data", df)
                table.columns = [ft.DataColumn(ft.Text(str(col))) for col in df.columns]
                table.rows = [
                    ft.DataRow([ft.DataCell(ft.Text(str(cell))) for cell in row])
                    for row in df.values
                ]
                result_text.value = f"Archivo {e.files[0].name} cargado correctamente ✅"
            except Exception as ex:
                result_text.value = f"Error al leer el archivo: {ex}"
                table.columns = [ft.DataColumn(ft.Text("Esperando archivo..."))]
                table.rows = []
            page.update()

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    return ft.View(
        "/excel",
        [
            ft.Text("📂 Cargar archivo Excel", size=28, weight="bold", color="red"),
            nav_buttons(page),
            ft.ElevatedButton(
                "Seleccionar archivo Excel",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: file_picker.pick_files(allowed_extensions=["xlsx"])
            ),
            result_text,
            table,
        ],
        bgcolor="#111"
    )