import bpy
import random

constrain = (-4, 4) # 最低、最高値
use_3DCursor = True #False

for target_obj in bpy.context.selected_objects: #小文字推奨
  target_obj.location.x = random.uniform(*constrain) #X_constrain
  target_obj.location.y = random.uniform(*constrain) #Y_constrain
  if use_3DCursor:
      target_obj.location.x += bpy.context.scene.cursor.location[0]
      target_obj.location.y += bpy.context.scene.cursor.location[1]
      target_obj.location.z += 8 + bpy.context.scene.cursor.location[2] #高さ設定