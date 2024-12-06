### Nicegui Sortable Column

Creates a nice gui sortable column. 


### Usage
To create the most basic column use the following. 
```python
with SortableColumn():
                for i in range(10):
                    with ui.card():
                        ui.label(f"Card {i}")
```

Look at example.py to see a more robust example.   

#### Handle sorting
To handle when a item is moved:
```python
def do_something(new_index,old_index,new_list,old_list):
    pass

SortableColumn(on_change=do_something)
```

Use the on_change to set the function that is called when a sortable item is moved. It takes 4 arguments in the following order: New Index(of the moved item), Old Index, New List, Old List. New and Old Index are intergers and New and Old List are SortableColumn objects. New and Old list will be the same in a column that doesn't have a group. 

#### Multi-column dragging
TO be able to drag inbetween columns use groups.
```python
SortableColumn(group='columns')
SortableColumn(group='columns')
```

You will be able to drag items between the two columns 