from typing import Callable, Optional
from nicegui import ui


class SortableColumn(ui.element, component='sortable_column.js'):

    def __init__(self, *, on_change: Optional[Callable] = None, group:str = None) -> None:
        super().__init__()
        self.on('item-drop', self.drop)
        self.on_change = on_change

        self._classes.append('nicegui-column')
        self._props['group'] = group

    def drop(self, e) -> None:
        if self.on_change:
            self.on_change(e)
        else:
            print(e)

    def makeSortable(self) -> None:
        self.run_method('makeSortable')

    def getitems(self) -> None:
        return self.run_method('getitems')



def on_change(e):
    print(e)

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
            with SortableColumn(on_change=on_change,group='test') as c2:
                for i in range(10):
                    with ui.card():
                        ui.label(f"Card {i*10}")
            ui.label(c2.id)

draw()


ui.run()