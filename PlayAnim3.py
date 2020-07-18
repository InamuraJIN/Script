import bpy
bpy.ops.screen.animation_play()

def my_handler(scene):
    
    paus=3
    
    print("Frame Change", scene.frame_current)
    if bpy.context.scene.frame_current ==paus-1:
        
        bpy.ops.screen.animation_cancel()
        bpy.context.scene.frame_current = paus

#remove all handlers
for i in range( len( bpy.app.handlers.frame_change_pre ) ):
        bpy.app.handlers.frame_change_pre.pop()

#append handler
bpy.app.handlers.frame_change_pre.append(my_handler)