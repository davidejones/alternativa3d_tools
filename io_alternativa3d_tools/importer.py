from struct import unpack, calcsize

import bpy
from bpy_extras.io_utils import ImportHelper

from .alternativa.version import A3DVersion


class A3DImporterSettings:
    """Encapsulates settings for the importer"""
    def __init__(self, file_path="", apply_transforms=1, import_lighting=1, import_cameras=1):
        self.file_path = str(file_path)
        self.apply_transforms = int(apply_transforms)
        self.import_lighting = int(import_lighting)
        self.import_cameras = int(import_cameras)


class A3DImporter(bpy.types.Operator, ImportHelper):
    bl_idname = "a3d.importer"
    bl_label = "Import A3D (Alternativa)"

    filename_ext = ".a3d"
    filter_glob: bpy.props.StringProperty(default="*.a3d", options={'HIDDEN'})
    files: bpy.props.CollectionProperty(name="A3D files", type=bpy.types.OperatorFileListElement)

    def execute(self, context):
        import_settings = A3DImporterSettings()
        version = A3DVersion.from_file_path(self.properties.filepath)
        if version.major == 1:
            # A3DImport1(file, import_settings)
            print("A3DImport1")
        else:
            # A3DImport2(file, import_settings)
            print("A3DImport2")
        return {"FINISHED"}


classes = (
    A3DImporter,
)

