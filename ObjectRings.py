bl_info = {
    "name": "Ring of Objects",
    "description": "Creates a ring of duplicate objects around the selected one.",
    "author": "Andrew L'Italien",
    "blender": (2, 80, 0),
    "location": "3D View > Object",
    "version": (0, 1, 0),
    "category": "Object",
}

import math
import bpy
from bpy import context

class ObjectRing(bpy.types.Operator):
    bl_idname = "object.create_ring"
    bl_label = "Create Ring of Objects"
    bl_options = {'REGISTER', 'UNDO'}
    
    numDuplicates: bpy.props.IntProperty(name="Duplicates", min=2)
    radius: bpy.props.FloatProperty(name="Radius (m)", min=0)
    placement_offset: bpy.props.FloatProperty(name="Offset")
    degrees: bpy.props.BoolProperty(name="Degrees", default=True)
    
    def execute(self, context):
        obj = context.active_object
        scene = context.scene
        start_loc = obj.location

        for i in range(self.numDuplicates):
            duplicate = obj.copy()
            if(self.degrees):
                angle = i / self.numDuplicates * math.tau + self.placement_offset * math.tau / 360
            else:
                angle = i / self.numDuplicates * math.tau + self.placement_offset
            duplicate.location.y = start_loc.y + self.radius * math.sin(angle)
            duplicate.location.x = start_loc.x + self.radius * math.cos(angle)
            duplicate.rotation_euler.z = duplicate.rotation_euler.z + angle
            scene.collection.objects.link(duplicate)

        obj = context.active_object
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def menu_option(self, context):
    self.layout.operator(ObjectRing.bl_idname)

def register():
    bpy.types.VIEW3D_MT_object.append(menu_option)
    bpy.utils.register_class(ObjectRing)

def unregister():
    bpy.utils.unregister_class(ObjectRing)

if __name__ == "__main__":
    register()