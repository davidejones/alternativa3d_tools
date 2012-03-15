bl_addon_info = {
	'name': 'Export: Alternativa3d Actionscript Class',
	'author': 'Invisible Man',
	'version': (1, 0, 0),
	'blender': (2, 5, 5),
	'location': 'File > Export',
	'description': 'Export a Alternativa 3D actionscript class',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://www.davidejones.co.uk',
	'category': 'Import/Export'}

import bpy
from bpy.props import *
import mathutils
import struct
from mathutils import *
from array import array

import os
import os.path

def WritePackageHeader(file):
	file.write("//Alternativa3D 7.5 Class Export For Blender 2.55 and above\n")
	file.write("//Plugin Author: Invisible Man, http://www.davidejones.co.uk & http://www.limeydesigns.com\n\n")
	file.write("package {\n\n\timport alternativa.engine3d.objects.Mesh;\n\timport alternativa.engine3d.materials.FillMaterial;\n\timport alternativa.engine3d.materials.TextureMaterial;\n\timport alternativa.engine3d.core.Geometry;\n\timport alternativa.engine3d.core.Vertex;\n\timport __AS3__.vec.Vector;\n\n")
	
def WritePackageEnd(file):
	file.write("}")
	
def WriteTexMaterial(file,Face,id):
	file.write("\t\t\t//"+os.path.basename(Face.image.filepath)+"\n")
	file.write("\t\t\tvar material:TextureMaterial = new TextureMaterial();\n")
	file.write("\t\t\tmaterial.repeat = true;\n");
	
def WriteFillMaterial(file,color):
	file.write("\t\t\tvar material:FillMaterial = new FillMaterial("+color+");\n\n")
	
def WriteClass(file,obj):
	#base=os.path.basename(file.name)
	#basename, extension = os.path.splitext(base)
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tvar g:Geometry = new Geometry();\n\n")
	
	mesh = obj.data;
	
	myUV = []
		
	#if we have any uv textures
	if len(mesh.uv_textures) > 0:
		UVCoordinates = None
		for UV in mesh.uv_textures:
			if UV.active_render:
				UVCoordinates = UV.data
				break
		x=0
		for Face in UVCoordinates:
			for Vertex in Face.uv:
				vert = tuple(Vertex)
				WriteTexMaterial(file,Face,"material"+x)
				myUV.append([vert[0],vert[1],"material"+x])
				x += 1
	else:
		WriteFillMaterial(file,"0xFF0000")
	
	print(myUV)
	
	for meshface in mesh.faces:
		file.write("\t\t\tg.addFace( Vector.<Vertex>([\n")
		l = len(meshface.vertices)
		i = 0
		for vert in meshface.vertices:
			#file.write('%i' % (vert) )
			#file.write('\t\t\t\tg.addVertex(%f, %f, %f, 0, 0)' % (mesh.vertices[meshface.index].co.x, mesh.vertices[meshface.index].co.y, mesh.vertices[meshface.index].co.z) )
			#file.write('\t\t\t\tg.addVertex(%f, %f, %f, %f, %f)' % (mesh.vertices[vert].co.x, mesh.vertices[vert].co.y, mesh.vertices[vert].co.z, myUV[vert][0], myUV[vert][1]) )
			file.write('\t\t\t\tg.addVertex(0, 0, 0, 0, 0)')
			if i == len(meshface.vertices)-1:
				file.write("]),\n")
			else:
				file.write(",\n")
			i += 1
		#file.write("\t\t\t\t"+myUV[vert][2]+"\n")
		file.write("\t\t\t);\n\n")
				
	file.write("\t\t\t//g.weldVertices();\n")
	file.write("\t\t\t//g.weldFaces();\n")
	file.write("\t\t\tgeometry = g;\n\n")
	
	file.write("\t\t}\n")
	file.write("\t}\n")

def export(file):
	print('Export to Alternativa3d Class started...')
	
	#write as3 package header
	WritePackageHeader(file)
		
	#get all meshes
	objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
	
	#write each mesh class
	for obj in objs:
		WriteClass(file,obj)
	
	#close off package
	WritePackageEnd(file)
	
	print('Export Completed...')
#-------------------------------------------------------------------------------
class ASExporter(bpy.types.Operator):
	bl_idname = 'ASExporter'
	bl_label = 'Export to AS (Alternativa)'
	bl_description = 'Export to AS (Alternativa)'
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		if not filePath.lower().endswith('.as'):
			filePath += '.as'
		try:
			print('Output file : %s' %filePath)
			#file = open(filePath, 'wb')
			file = open(filePath, 'w')
			export(file)
			file.close()
		except Exception as e:
			print(e)
			file.close()
		return 'FINISHED'
	def invoke (self, context, event):		
		context.window_manager.add_fileselect(self)
		return {'RUNNING_MODAL'}
		
def func(self, context):
	default_path = bpy.data.filepath.replace('.blend', '.as')
	self.layout.operator(ASExporter.bl_idname, text='Alternativa3D Class (.as)').filepath = default_path
def register():
	bpy.types.INFO_MT_file_export.append(func)
def unregister():
	bpy.types.INFO_MT_file_export.remove(func)
if __name__ == '__main__':
	register()