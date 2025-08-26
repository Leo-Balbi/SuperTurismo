import flet as ft
import pandas as pd
import sqlite3
from app.components.navbar import navbar
from app.components.charts import chart_piezas

DB_FILE = "data/superturismo.db"

def dashboard_view(page):
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql("SELECT * FROM registros", conn)
    conn.close()

    table = ft.DataTable(
        columns=[ft.DataColumn(ft.Text(c)) for c in df.columns],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(v))) for v in row])
            for row in df.values.tolist()
        ],
        expand=True
    )

    return ft.View(
        "/dashboard",
        [
            ft.Text("📊 Dashboard - SuperTurismo", size=28, weight="bold", color="red"),
            table,
            chart_piezas(df),  # gráfico de ejemplo
            navbar(page)
        ]
    )
