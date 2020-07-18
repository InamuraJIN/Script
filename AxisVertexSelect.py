x = [None,'under']
y = [None,'under']
z = [-0.1,'under'] #プラス方向の場合は'above'に変更

import bpy
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action='DESELECT')

bpy.ops.object.mode_set(mode="OBJECT")

obj = bpy.context.active_object
obj.update_from_editmode()

def under(value, axis):
    for v in obj.data.vertices:
        if v.co[axis] < value:
            v.select = True
        print(v.select)
            
def above(value, axis):
    for v in obj.data.vertices:
        if v.co[axis] > value:
            v.select = True
                
if x[0] is not None:
    if x[1] == 'under':
        under(x[0], 0)
    elif x[1] == 'above':
        above(y[0], 0)
if y[0] is not None:
    if y[1] == 'under':
        under(y[0], 1)
    elif y[1] == 'above':
        above(y[0], 1)
if z[0] is not None:
    if z[1] == 'under':
        under(z[0], 2)
    elif z[1] == 'above':
        above(z[0], 2)

bpy.ops.object.mode_set(mode="EDIT")