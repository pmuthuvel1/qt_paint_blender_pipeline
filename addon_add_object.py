bl_info = {"name" : "MuthuvelTestAddon",   "category": "3D View",   "author": "Muthuvel Periyasamy"}
import bpy
class TestAddon(bpy.types.Menu):
    bl_label = "MuthuvelTestAddon"
    bl_idname = "MuthuvelTestAddonId"
    def draw(self, context):
        layout = self.layout
        
        """ EVERYTHING BELOW IS YOUR KINGDOM """
        layout.operator("mesh.primitive_cube_add")
        layout.operator("mesh.primitive_circle_add")
        layout.operator("object.duplicate_move")
        layout.operator("object.delete")
        layout.operator("object.armature_add")
        layout.operator("object.posemode_toggle")
        layout.operator("mesh.primitive_monkey_add")
        """ EXCEPT THE STUFF UNDER HERE """
        
def register(): bpy.utils.register_class(TestAddon)
def unregister(): bpy.utils.unregister_class(TestAddon)
if __name__ == "__main__": register()

