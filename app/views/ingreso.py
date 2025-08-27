import flet as ft
import sqlite3
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from app.components.navbuttons import nav_buttons

DB_FILE = "data/superturismo.db"

def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    img_bytes = buf.getvalue()
    base64_str = base64.b64encode(img_bytes).decode("utf-8")
    return base64_str

def obtener_datos():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            df = pd.read_sql_query("SELECT fecha, nombre, valor FROM registros", conn)
        return df
    except Exception:
        return pd.DataFrame()

def ingreso_view(page: ft.Page):
    fecha_label = ft.Text("Fecha", size=16, weight="bold")
    fecha_picker = ft.DatePicker()
    page.overlay.append(fecha_picker)

    nombre_label = ft.Text("Nombre", size=16, weight="bold")
    nombre_input = ft.TextField(hint_text="Ingrese el nombre")

    valor_label = ft.Text("Valor", size=16, weight="bold")
    valor_input = ft.TextField(hint_text="Ingrese el valor", keyboard_type=ft.KeyboardType.NUMBER)

    mensaje = ft.Text("", color="green")

    def guardar_datos(e):
        fecha = fecha_picker.value
        nombre = nombre_input.value
        valor = valor_input.value

        if not fecha or not nombre or not valor:
            mensaje.value = "Completa todos los campos."
            mensaje.color = "red"
        else:
            try:
                with sqlite3.connect(DB_FILE) as conn:
                    cur = conn.cursor()
                    cur.execute(
                        "INSERT INTO registros (fecha, nombre, valor) VALUES (?, ?, ?)",
                        (fecha, nombre, valor)
                    )
                    conn.commit()
                mensaje.value = "Datos guardados correctamente ✅"
                mensaje.color = "green"
                nombre_input.value = ""
                valor_input.value = ""
                fecha_picker.value = None
            except Exception as ex:
                mensaje.value = f"Error al guardar: {ex}"
                mensaje.color = "red"
        page.update()

    fecha_btn = ft.ElevatedButton(
        "Seleccionar fecha",
        icon=ft.icons.DATE_RANGE,
        on_click=lambda _: fecha_picker.pick_date()
    )

    form = ft.Column(
        [
            ft.Text("Ingreso de datos", size=28, weight="bold", color="#e10600"),
            nav_buttons(page),
            ft.Divider(),
            ft.Row([fecha_label, fecha_btn], alignment="start"),
            nombre_label,
            nombre_input,
            valor_label,
            valor_input,
            ft.ElevatedButton("Guardar", icon=ft.icons.SAVE, bgcolor="#e10600", color="white", on_click=guardar_datos),
            mensaje
        ],
        spacing=18,
        width=400,
        horizontal_alignment="center"
    )

    # Sección de gráficas
    df_graficas = obtener_datos()
    graficas = []

    if not df_graficas.empty:
        df_graficas['valor'] = pd.to_numeric(df_graficas['valor'], errors='coerce')
        if 'fecha' in df_graficas.columns:
            df_graficas = df_graficas.sort_values('fecha')

        # Gráfica de barras
        fig_bar, ax_bar = plt.subplots(facecolor="#111")
        suma_por_nombre = df_graficas.groupby('nombre')['valor'].sum()
        ax_bar.bar(suma_por_nombre.index, suma_por_nombre.values, color="#e10600", edgecolor="black")
        ax_bar.set_title("Valores por Nombre", color="white", fontsize=16)
        ax_bar.set_xlabel("Nombre", color="white")
        ax_bar.set_ylabel("Valor", color="white")
        ax_bar.tick_params(axis='x', colors='white', rotation=45)
        ax_bar.tick_params(axis='y', colors='white')
        ax_bar.set_facecolor("#222")
        for spine in ax_bar.spines.values():
            spine.set_color("white")
        img_bar_base64 = fig_to_base64(fig_bar)
        graficas.append(ft.Image(src_base64=img_bar_base64, width=400, height=250))

        # Gráfica lineal
        fig_line, ax_line = plt.subplots(facecolor="#111")
        ax_line.plot(df_graficas['fecha'], df_graficas['valor'], marker='o', color="#e10600", linewidth=2)
        ax_line.set_title("Valor a lo largo del tiempo", color="white", fontsize=16)
        ax_line.set_xlabel("Fecha", color="white")
        ax_line.set_ylabel("Valor", color="white")
        ax_line.tick_params(axis='x', colors='white', rotation=45)
        ax_line.tick_params(axis='y', colors='white')
        ax_line.set_facecolor("#222")
        for spine in ax_line.spines.values():
            spine.set_color("white")
        img_line_base64 = fig_to_base64(fig_line)
        graficas.append(ft.Image(src_base64=img_line_base64, width=400, height=250))

    return ft.View(
        "/ingreso",
        [
            ft.Container(form, alignment=ft.alignment.center, padding=40, bgcolor="#111", border_radius=12),
            ft.Container(
                ft.Row(graficas, alignment="center", spacing=30),
                alignment=ft.alignment.center,
                padding=20,
                bgcolor="#222",
                border_radius=12
            )
        ],
        bgcolor="#222"
    )