from sortable_column import SortableColumn
from nicegui import ui

def on_change(ni,oi,nl,ol):
    print(f"New Index: {type(ni)}, Old Index: {oi}, New List: {nl.id}, Old List {ol.id}")

def refresh():
    draw.refresh()

@ui.refreshable
def draw():
    ui.button('reset').on_click(refresh)
    with ui.row():
        with ui.column():
            with SortableColumn(on_change=on_change,group='test') as c1:
                for i in range(10):
                    with ui.card():
                        ui.label(f"Card {i}")
            ui.label(c1.id)

        with ui.column():
            with ui.card().classes('bg-gray-200'):
                with SortableColumn(on_change=on_change,group='test') as c2:
                    pass
            ui.label(c2.id)

draw()


ui.run()