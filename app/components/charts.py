import flet as ft
import matplotlib.pyplot as plt
import io
import base64

def chart_piezas(df):
    if df.empty:
        return ft.Text("No hay datos para mostrar gráficos")

    counts = df["pieza"].value_counts()

    fig, ax = plt.subplots()
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Reemplazos por pieza")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return ft.Image(src_base64=img_b64, width=600, height=400)
