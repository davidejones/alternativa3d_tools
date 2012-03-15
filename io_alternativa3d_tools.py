bl_info = {
	'name': 'Export: Alternativa3d Actionscript Class',
	'author': 'Invisible Man, http://www.davidejones.co.uk',
	'version': (1, 0, 4),
	'blender': (2, 5, 7),
	'location': 'File > Export > Alternativa3D Class (.as)',
	'description': 'Export a Alternativa 3D actionscript class',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://www.davidejones.co.uk',
	'category': 'Import-Export'}

import math, os, time, bpy, random, mathutils, re, ctypes
from bpy import ops
from bpy.props import *

#Container for the exporter settings
class ASExporterSettings:
	def __init__(self,A3DVersionSystem=1,CompilerOption=1,ExportMode=1):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.CompilerOption = int(CompilerOption)
		self.ExportMode = int(ExportMode)

def WritePackageHeader(file,Config):
	file.write("//Alternativa3D Class Export For Blender 2.57 and above\n")
	file.write("//Plugin Author: Invisible Man, http://www.davidejones.co.uk\n\n")
	file.write("package {\n\n")
	if Config.A3DVersionSystem == 3:
		file.write("\timport alternativa.engine3d.core.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.types.Texture;\n")
		file.write("\timport flash.display.BlendMode;\n")
		file.write("\timport flash.geom.Point;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif Config.A3DVersionSystem == 2:
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport alternativa.engine3d.core.Geometry;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	else:
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	
def WritePackageEnd(file):
	file.write("}")
	
def WriteTexMaterial(file,image,id,Config):
	base=os.path.basename(image.filepath)
	basename, extension = os.path.splitext(base)
	
	if Config.A3DVersionSystem == 3:
		if Config.CompilerOption == 1:
			file.write('\t\t[Embed(source="'+base+'")] private static const bmp'+basename+':Class;\n')
			file.write('\t\tprivate static const '+id+':Texture = new Texture(new bmp'+basename+'().bitmapData, "'+basename+'");\n\n')
		else:
			file.write("\t\t//"+base+"\n")
			file.write("\t\tprivate var bmp"+basename+":Bitmap = new Bitmap(new bd"+basename+"(0,0));\n")
			file.write('\t\tprivate var "+id+":Texture = new Texture(bmp'+basename+'.bitmapData, "'+basename+'");\n\n')
	else:
		if Config.CompilerOption == 1:
			file.write('\t\t[Embed(source="'+base+'")] private static const bmp'+basename+':Class;\n')
			file.write('\t\tprivate static const '+id+':TextureMaterial = new TextureMaterial(new bmp'+basename+'().bitmapData, true, true);\n\n')
		else:
			file.write("\t\t//"+base+"\n")
			file.write("\t\tprivate var bmp"+basename+":Bitmap = new Bitmap(new bd"+basename+"(0,0));\n")
			file.write("\t\tprivate var "+id+":TextureMaterial = new TextureMaterial(bmp"+basename+".bitmapData, true, true);\n\n")
	
def WriteFillMaterial(file,color):
	file.write("\t\t\tvar material:FillMaterial = new FillMaterial("+color+");\n\n")
	
def WriteClass76(file,obj,Config):
	#base=os.path.basename(file.name)
	#basename, extension = os.path.splitext(base)
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data;
	#mesh = Mesh(obj.name)
	#mesh = bpy.data.meshes[obj.name]
	
	verts = mesh.vertices
	
	faces = []
	uvimages = []
	uvimagevars = []
	uvimagevarrefs = []
	check = False
	
	hasFaceUV = len(mesh.uv_textures) > 0
	
	j=0
	for f in mesh.faces:
		faces.append( f )
		if hasFaceUV:
			if len(uvimages) > 0:
				if uvimages.count(mesh.uv_textures.active.data[f.index].image) > 0:
					#uvimagevars.append('material'+str(j))
					p = uvimages.index(mesh.uv_textures.active.data[f.index].image)
					#uvimagevars.append(uvimagevars[p])
					#uvimagevars.append('test'+str(j))
					uvimagevarrefs.append(uvimagevars[p])
				else:
					uvimages.append(mesh.uv_textures.active.data[f.index].image)
					uvimagevars.append('material'+str(j))
					uvimagevarrefs.append('material'+str(j))
			else:
				uvimages.append(mesh.uv_textures.active.data[f.index].image)
				uvimagevars.append('material'+str(j))
				uvimagevarrefs.append('material'+str(j))
		j += 1
		
	x=0	
	for im in uvimages:
		WriteTexMaterial(file,im,uvimagevars[x],Config)
		x += 1
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	
	cn=-1
	for face in faces:
		cn +=1
		file.write('\t\t\t\taddFace(Vector.<Vertex>([\n')
		if len(face.vertices) > 0:
			for i in range(len(face.vertices)):
				hasFaceUV = len(mesh.uv_textures) > 0
				if hasFaceUV:
					uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
					uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
					file.write('\t\t\t\t\taddVertex(%f, %f, %f, %f, %f),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z, uv[0], uv[1]) )
				else:
					file.write('\t\t\t\t\taddVertex(%f, %f, %f, 0, 0),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z) )
		if hasFaceUV:
			file.write('\t\t\t\t]),'+uvimagevarrefs[face.index]+');\n\n')
		else:
			file.write('\t\t\t\t]), new FillMaterial(0xFF0000));\n\n')
	
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass75(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	mesh = obj.data;
	verts = mesh.vertices
	
	faces = []
	uvimages = []
	uvimagevars = []
	check = False
	
	j=0
	for f in mesh.faces:
		faces.append( f )
		if len(uvimages) > 0:
			p=0
			for im in uvimages:
				if im == mesh.uv_textures.active.data[f.index].image:
					check = True
					uvimagevars.append(uvimagevars[p])	
				p += 1
			if check == False:
				uvimages.append(mesh.uv_textures.active.data[f.index].image)
				uvimagevars.append('material'+str(j))
				check = False
		else:
			uvimages.append(mesh.uv_textures.active.data[f.index].image)
			uvimagevars.append('material'+str(j))
		j += 1
			
	x=0	
	for im in uvimages:
		WriteTexMaterial(file,im,uvimagevars[x],Config)
		x += 1
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tvar g:Geometry = new Geometry();\n\n")
	
	for face in faces:
		file.write('\t\t\t\tg.addFace(Vector.<Vertex>([\n')
		for i in range(len(face.vertices)):
			hasFaceUV = len(mesh.uv_textures) > 0
			if hasFaceUV:
				uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
				uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
				file.write('\t\t\t\t\tg.addVertex(%f, %f, %f, %f, %f),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z, uv[0], uv[1]) )
		file.write('\t\t\t\t]),'+uvimagevars[face.index]+');\n\n')
	
	file.write("\t\t\t//g.weldVertices();\n")
	file.write("\t\t\t//g.weldFaces();\n")
	file.write("\t\t\tgeometry = g;\n\n")
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass5(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	
	mesh = obj.data;
	verts = mesh.vertices
	
	faces = []
	uvimages = []
	uvimagevars = []
	check = False
	
	j=0
	for f in mesh.faces:
		faces.append( f )
		if len(uvimages) > 0:
			p=0
			for im in uvimages:
				if im == mesh.uv_textures.active.data[f.index].image:
					check = True
					uvimagevars.append(uvimagevars[p])	
				p += 1
			if check == False:
				uvimages.append(mesh.uv_textures.active.data[f.index].image)
				uvimagevars.append('material'+str(j))
				check = False
		else:
			uvimages.append(mesh.uv_textures.active.data[f.index].image)
			uvimagevars.append('material'+str(j))
		j += 1
			
	x=0	
	for im in uvimages:
		WriteTexMaterial(file,im,uvimagevars[x],Config)
		x += 1
	
	count=0
	for vert in mesh.vertices:
		file.write('\t\t\t\tcreateVertex(%f, %f, %f, %i);\n' % (vert.co.x, vert.co.y, vert.co.z, count))
		count += 1
	file.write('\n')
	
	x=0
	for meshface in mesh.faces:
		file.write('\t\t\t\tcreateFace([')
		k=0
		for vert in meshface.vertices:
			file.write('%i ' % (vert) )
			if k != len(meshface.vertices)-1:
				file.write(",")
			k += 1
		file.write('], '+str(x)+');\n')
		file.write('\t\t\t\tsetUVsToFace(new Point(%f,%f), new Point(%f,%f), new Point(%f,%f), %i);\n' % (x,x,x,x,x,x,x))
		x += 1
	
	file.write("\t\t}\n")
	file.write("\t}\n")

def export(file,Config):
	print('Export to Alternativa3d Class started...\n')
	
	#write as3 package header
	WritePackageHeader(file,Config)
		
	if Config.ExportMode == 1:
		#get selected objects that are mesh
		objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
		print('Export selection only...\n')
	else:
		#get all objects that are mesh
		objs = [obj for obj in bpy.data.objects if obj.type == 'MESH']
		print('Export all meshes...\n')
	
	#write each mesh class
	for obj in objs:
		if Config.A3DVersionSystem == 1:
			WriteClass76(file,obj,Config)
		elif Config.A3DVersionSystem == 2:
			WriteClass76(file,obj,Config)
		elif Config.A3DVersionSystem == 2:
			WriteClass75(file,obj,Config)
		elif Config.A3DVersionSystem == 4:
			WriteClass5(file,obj,Config)
		else:
			print("No Alternativa Version\n")
	
	#close off package
	WritePackageEnd(file)
	
	print('Export Completed...\n')
#-------------------------------------------------------------------------------
class ASExporter(bpy.types.Operator):
	bl_idname = "ops.asexporter"
	bl_label = "Export to AS (Alternativa)"
	bl_description = "Export to AS (Alternativa)"
	
	#export options
	#alternativa3d versions
	A3DVersions = []
	A3DVersions.append(("1", "7.7.0", ""))
	A3DVersions.append(("2", "7.6.0", ""))
	A3DVersions.append(("3", "7.5.1", ""))
	#A3DVersions.append(("3", "5", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D to export to", items=A3DVersions, default="1")
	#flash or flex?
	Compilers = []
	Compilers.append(("1", "Flex", ""))
	Compilers.append(("2", "Flash", ""))
	CompilerOption = EnumProperty(name="Use With", description="Select the compiler you will be using", items=Compilers, default="1")
	#export selection
	ExportModes = []
	ExportModes.append(("1", "Selected Objects", ""))
	ExportModes.append(("2", "All Objects", ""))
	ExportMode = EnumProperty(name="Export", description="Select which objects to export", items=ExportModes, default="1")
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		if not filePath.lower().endswith('.as'):
			filePath += '.as'
		try:
			print('Output file : %s' %filePath)
			#file = open(filePath, 'wb')
			file = open(filePath, 'w')
			Config = ASExporterSettings(A3DVersionSystem=self.A3DVersionSystem,CompilerOption=self.CompilerOption,ExportMode=self.ExportMode)
			export(file,Config)
			
			file.close()
		except Exception as e:
			print(e)
			file.close()
		return 'FINISHED'
	def invoke (self, context, event):		
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}
		
def menu_func(self, context):
	default_path = bpy.data.filepath.replace('.blend', '.as')
	self.layout.operator(ASExporter.bl_idname, text='Alternativa3D Class (.as)').filepath = default_path
	
def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_file_export.append(menu_func)
	
def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_file_export.remove(menu_func)
	
if __name__ == '__main__':
	register()