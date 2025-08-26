from app.views.home import home_view
from app.views.ingreso import ingreso_view
from app.views.excel import excel_view
from app.views.dashboard import dashboard_view

def route_change(page):
    page.views.clear()
    if page.route == "/":
        page.views.append(home_view(page))
    elif page.route == "/ingreso":
        page.views.append(ingreso_view(page))
    elif page.route == "/excel":
        page.views.append(excel_view(page))
    elif page.route == "/dashboard":
        page.views.append(dashboard_view(page))
    page.update()
