bl_info = {
    'name': 'Alternativa3d Blender Plugin',
    'category': 'Import-Export',
    'author': 'davidejones',
    'location': 'File > Import/Export',
    'description': 'Allows importing of .a3d models & exporting actionscript or a3d models from Alternativa3D',
    'version': (2, 0, 0),
    'blender': (2, 80, 0),
    'wiki_url': 'https://github.com/davidejones/alternativa3d_tools',
    'tracker_url': 'https://github.com/davidejones/alternativa3d_tools/issues',
    'warning': '',
}

# support reloading sub-modules
if "bpy" in locals():
    from importlib import reload
    _modules_loaded[:] = [reload(val) for val in _modules_loaded]
    del reload

_modules = [
    "importer",
]

import bpy

__import__(name=__name__, fromlist=_modules)
_namespace = globals()
_modules_loaded = [_namespace[name] for name in _modules]
del _namespace


def menu_func_import(self, context):
    self.layout.operator(importer.A3DImporter.bl_idname, text='Alternativa3D Binary (.a3d)')


# def menu_func_export(self, context):
#     as_path = bpy.data.filepath.replace('.blend', '.as')
#     a3d_path = bpy.data.filepath.replace('.blend', '.a3d')
#     self.layout.operator(ASExporter.bl_idname, text='Alternativa3D Class (.as)').filepath = as_path
#     self.layout.operator(A3DExporter.bl_idname, text='Alternativa3D Binary (.a3d)').filepath = a3d_path


def register():
    for mod in _modules_loaded:
        for cls in mod.classes:
            bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    # bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    # bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

    for mod in reversed(_modules_loaded):
        for cls in reversed(mod.classes):
            if cls.is_registered:
                bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
