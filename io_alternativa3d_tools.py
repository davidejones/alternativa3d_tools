bl_info = {
	'name': 'Export: Alternativa3d Tools',
	'author': 'David E Jones, http://www.davidejones.com',
	'version': (1, 0, 5),
	'blender': (2, 5, 7),
	'location': 'File > Import/Export;',
	'description': 'Importer and exporter for Alternativa3D engine. Supports A3D and Actionscript"',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://www.davidejones.com',
	'category': 'Import-Export'}

import math, os, time, bpy, random, mathutils, re, ctypes, struct
from bpy import ops
from bpy.props import *


#==================================
# EXPORTER - Actionscript (.as)
#==================================

#Container for the exporter settings
class ASExporterSettings:
	def __init__(self,A3DVersionSystem=1,CompilerOption=1,ExportMode=1):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.CompilerOption = int(CompilerOption)
		self.ExportMode = int(ExportMode)

def GetMeshVertexCount(Mesh):
    VertexCount = 0
    for Face in Mesh.faces:
        VertexCount += len(Face.vertices)
    return VertexCount
	
def WritePackageHeader(file,Config):
	file.write("//Alternativa3D Class Export For Blender 2.57 and above\n")
	file.write("//Plugin Author: David E Jones, http://www.davidejones.com\n\n")
	file.write("package {\n\n")
	
	if Config.A3DVersionSystem == 1:
		# version 5.6.0
		file.write("\timport alternativa.engine3d.core.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.types.Texture;\n")
		file.write("\timport flash.display.BlendMode;\n")
		file.write("\timport flash.geom.Point;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif Config.A3DVersionSystem == 2:
		# version 7.5.1
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport alternativa.engine3d.core.Geometry;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif Config.A3DVersionSystem == 3:
		# version 7.6.0
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif Config.A3DVersionSystem == 4:
		# version 7.7.0
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	else:
		# version 8.5.0
		file.write("\timport alternativa.engine3d.core.VertexAttributes;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.resources.Geometry;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	
def WritePackageEnd(file):
	file.write("}")
	
def WriteTexMaterial(file,image,id,Config):
	base=os.path.basename(image.filepath)
	basename, extension = os.path.splitext(base)
	
	if Config.A3DVersionSystem == 1:
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

def WriteClass85(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	mesh = obj.data
	verts = mesh.vertices
	faces = []
	uvt = []
	ind = []
	uvimages = []
	uvimagevars = []
	uvimagevarrefs = []
	hasFaceUV = len(mesh.uv_textures) > 0
	numVertices = GetMeshVertexCount(mesh)
	
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
		
	file.write("\t\tprivate var attributes:Array;\n\n")
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tattributes = new Array();\n")
	file.write("\t\t\tattributes[0] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[1] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[2] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[3] = VertexAttributes.TEXCOORDS[0];\n")
	file.write("\t\t\tattributes[4] = VertexAttributes.TEXCOORDS[0];\n\n")
	
	file.write("\t\t\tvar g:Geometry = new Geometry();\n")
	file.write("\t\t\tg.addVertexStream(attributes);\n")
	file.write("\t\t\tg.numVertices = "+str(numVertices)+";\n\n")
	
	file.write("\t\t\tvar vertices:Array = [\n")
	fl = 0
	Index = 0
	for face in faces:
		if len(face.vertices) > 0:
			for i in range(len(face.vertices)):
				#ind.append(verts[face.vertices[i]].index)
				ind.append(Index)
				hasFaceUV = len(mesh.uv_textures) > 0
				if hasFaceUV:
					uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
					uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
					uvt.append((uv[0],uv[1]))
				file.write('\t\t\t\t%f, %f, %f,\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z) )
				Index += 1
		fl += 1
	file.write("\t\t\t];\n")
		
	if len(uvt) > 0:
		file.write("\t\t\tvar uvt:Array = [\n")
		for u in uvt:
			file.write("\t\t\t\t"+u[0][0]+","+u[0][0]+",")
		file.write("\t\t\t];\n")
	else:
		file.write("\t\t\tvar uvt:Array = new Array();\n")
	
	# verts
	for v in mesh.vertices:
		print("%.6f %.6f %.6f, " % v.co[:])
	
	#write out indices
	mesh_faces = mesh.faces[:]	
	if len(mesh_faces) > 0:
		file.write("\t\t\tvar ind:Array = [\n")
		for i in range(len(mesh_faces)):
			fv = mesh_faces[i].vertices[:]
			if len(fv) == 3:
				file.write("\t\t\t\t%i, %i, %i" % fv)
				#print("%i %i %i -1, " % fv)
				if i != len(mesh_faces)-1:
					file.write(",\n")
			else:
				file.write("\t\t\t\t%i, %i, %i,\n" % (fv[0], fv[1], fv[2]))
				file.write("\t\t\t\t%i, %i, %i" % (fv[0], fv[2], fv[3]))
				#print("%i %i %i -1, " % (fv[0], fv[1], fv[2]))
				#print("%i %i %i -1, " % (fv[0], fv[2], fv[3]))
				if i != len(mesh_faces)-1:
					file.write(",\n")
		file.write("\t\t\t];\n\n")
	else:
		file.write("\t\t\tvar ind:Array = new Array();\n\n")
			
	#
	#if len(ind) > 0:
	#	file.write("\t\t\tvar ind:Array = [\n")
	#	file.write("\t\t\t\t")
	#	for ix in range(len(ind)):
	#		file.write("%i" % (ind[ix]))
	#		if ix != 0:
	#			if (ix+1) % 3 == 0:
	#				file.write(",\n\t\t\t\t")
	#			else:
	#				file.write(",")
	#		else:
	#			file.write(",")
	#	file.write("\t\t\t];\n\n")
	#else:
	#	file.write("\t\t\tvar ind:Array = new Array();\n\n")
	
	file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
	file.write("\t\t\tg.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")
	file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
	
	file.write("\t\t\tthis.geometry = g;\n")
	file.write("\t\t\tthis.addSurface(new FillMaterial(0xFF0000), 0, "+str(len(ind))+");\n")
	file.write("\t\t\tthis.calculateBoundBox();\n")
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass76(file,obj,Config):
	#base=os.path.basename(file.name)
	#basename, extension = os.path.splitext(base)
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data
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

def asexport(file,Config):
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
		if Config.A3DVersionSystem == 5:
			WriteClass85(file,obj,Config)
		elif Config.A3DVersionSystem == 4:
			WriteClass76(file,obj,Config)
		elif Config.A3DVersionSystem == 3:
			WriteClass76(file,obj,Config)
		elif Config.A3DVersionSystem == 2:
			WriteClass75(file,obj,Config)
		elif Config.A3DVersionSystem == 1:
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
	A3DVersions.append(("1", "5.6.0", ""))
	A3DVersions.append(("2", "7.5.1", ""))
	A3DVersions.append(("3", "7.6.0", ""))
	A3DVersions.append(("4", "7.7.0", ""))
	A3DVersions.append(("5", "8.5.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D to export to", items=A3DVersions, default="5")
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
			asexport(file,Config)
			
			file.close()
		except Exception as e:
			print(e)
			file.close()
		return 'FINISHED'
	def invoke (self, context, event):		
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}

#==================================
# EXPORTER - A3d
#==================================
#==================================
# IMPORTER - A3d
#==================================

def loadA3d(filename):	
	# open a3d file
	file = open(filename,'rb')
	
	STRUCT_SIZE_INTEGER = struct.calcsize('i')
	STRUCT_SIZE_1CHAR = struct.calcsize('c')
	STRUCT_SIZE_2FLOAT = struct.calcsize('2f')
	STRUCT_SIZE_3FLOAT = struct.calcsize('3f')
	STRUCT_SIZE_4FLOAT = struct.calcsize('4f')
	STRUCT_SIZE_6FLOAT = struct.calcsize('6f')
	STRUCT_SIZE_9FLOAT = struct.calcsize('9f')
	STRUCT_SIZE_UNSIGNED_SHORT = struct.calcsize('H')
	STRUCT_SIZE_SIGNED_SHORT = struct.calcsize('H')
		
	#read baseversion
	temp_data = file.read(STRUCT_SIZE_UNSIGNED_SHORT)
	baseversion = int(struct.unpack('>H', temp_data)[0])
	
	#read pointversion
	temp_data = file.read(STRUCT_SIZE_UNSIGNED_SHORT)
	pointversion = int(struct.unpack('>H', temp_data)[0])
	
	print('A3D Version %i.%i' %(baseversion,pointversion))
	
	# ???? skip extra bytes if needed
	temp_data = ord(file.read(1))
	tem = temp_data%2
	if tem != 0:
		file.seek(file.tell() + tem)
	
	#skip unknown
	file.seek(file.tell() + 39)
	
	#length of something maybe faces?
	flen = ord(file.read(1))
	print('flen %i' %flen)
	
	#move past faces
	#file.seek(file.tell() + flen)
		
	fc = int(flen/2)

	faces = []
	tupl = []
	for i in range(fc):
		temp_data = file.read(STRUCT_SIZE_SIGNED_SHORT)
		f = int(struct.unpack('H', temp_data)[0])
		tupl.append(f)
		if (i+1)%3 == 0:
			print('%i,%i,%i' % (tupl[0],tupl[1],tupl[2]))
			faces.append((tupl[0],tupl[1],tupl[2]))	
			tupl = []
	
	#read integer, total indexes
	temp_data = file.read(STRUCT_SIZE_INTEGER)
	total_indexes = struct.unpack('i', temp_data)
	
	#read byte, vector size?
	by = ord(file.read(1))
	
	#read next byte
	norm = ord(file.read(1))
	print('norm %i' %norm)
	
	#skip norm length
	file.seek(file.tell() + norm)
	
	#read length of bytes
	bylen = ord(file.read(1))
	print(bylen)
	
	#if bylen has bytes left over then either skip them or read them as part of bytelength
	rem = bylen%2
	if rem != 0:
		#file.seek(file.tell() + rem)
		rembyte = ord(file.read(1))
		bylen = bylen + rembyte
		bylen = bylen * 2
		bylen = bylen - 10
	print(rem)
	
	#how many floats in the length of bytes
	flts = int(bylen/4)
	
	#how many points, each point has 3 (x,y,z)
	if norm == 2:
		#(x, y, z, uva, uvb, uvc)
		points = int(flts/6)
	else:
		#(x, y, z)
		points = int(flts/3)
		
	coords = []
	#faces = []
	#tupls = []
	for i in range(points):
		#read x,y,z
		if norm == 2:
			temp_data = file.read(STRUCT_SIZE_6FLOAT)
			x, y, z, uva, uvb, uvc = struct.unpack('<6f', temp_data)
			print('%f, %f, %f, %f, %f, %f' % (x, y, z, uva, uvb, uvc))
		else:
			temp_data = file.read(STRUCT_SIZE_3FLOAT)
			x, y, z = struct.unpack('<3f', temp_data)
			print('%f, %f, %f' % (x, y, z))
		coords.append((x, y, z))
		#tupls.append(i)
	
	#for x in range(flts):
	#	print('(%i,%i,%i,%i)' % (tupls[0],tupls[1],tupls[2],tupls[3]))
	#	faces.append((tupls[0],tupls[1],tupls[2],tupls[3]))
	
	# move 22 bytes after verts
	file.seek(file.tell() + 22)
		
	#read name of obj
	slen = ord(file.read(1))

	s = ''
	for x in range(slen):
		s = s + chr(ord(file.read(1)))
	print(s)
	
	# move 12 bytes
	file.seek(file.tell() + 12)
	tris = ord(file.read(1))
	
	print('Triangles:%i' % tris)
	
	# add mesh to blender
	#faces = [(0,1,2,3)]
	# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
	#coords=[(-1.0, -1.0, -1.0), (1.0, -1.0, -1.0), (1.0, 1.0 ,-1.0), (-1.0, 1.0,-1.0), (0.0, 0.0, 1.0)]
	#faces=[ (2,1,0,3), (0,1,4,0), (1,2,4,1), (2,3,4,2), (3,0,4,3)]
	
	# create a new mesh  
	me = bpy.data.meshes.new(s) 
	
	# create an object with that mesh
	ob = bpy.data.objects.new(s, me)   
	
	# position object at 3d-cursor
	ob.location = bpy.context.scene.cursor_location   
	
	# Link object to scene
	bpy.context.scene.objects.link(ob)  

	# Fill the mesh with verts, edges, faces 
	me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
	me.update(calc_edges=True)    # Update mesh with new data	
	
	return {'FINISHED'}
	
class A3DImporter(bpy.types.Operator):
	bl_idname = "ops.a3dimporter"
	bl_label = "Import A3D (Alternativa)"
	bl_description = "Import A3D (Alternativa)"
	
	filepath= StringProperty(name="File Path", description="Filepath used for importing the A3D file", maxlen=1024, default="")

	def execute(self, context):
		loadA3d(self.filepath)
		return {'FINISHED'}
	def invoke (self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}	

#==================================
# REGISTRATION
#==================================

def menu_func_import(self, context):
	self.layout.operator(A3DImporter.bl_idname, text='Alternativa3D Binary (.a3d)')

def menu_func_export(self, context):
	default_path = bpy.data.filepath.replace('.blend', '.as')
	self.layout.operator(ASExporter.bl_idname, text='Alternativa3D Class (.as)').filepath = default_path
	
def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_file_import.append(menu_func_import)
	bpy.types.INFO_MT_file_export.append(menu_func_export)
	
def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_file_import.remove(menu_func_import)
	bpy.types.INFO_MT_file_export.remove(menu_func_export)

	
if __name__ == '__main__':
	register()