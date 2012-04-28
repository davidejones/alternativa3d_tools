bl_info = {
	'name': 'Export: Alternativa3d Tools',
	'author': 'David E Jones, http://davidejones.com',
	'version': (1, 1, 5),
	'blender': (2, 6, 2),
	'location': 'File > Import/Export;',
	'description': 'Importer and exporter for Alternativa3D engine. Supports A3D and Actionscript"',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://davidejones.com',
	'category': 'Import-Export'}

import math, os, time, bpy, random, mathutils, re, ctypes, struct, binascii, zlib, tempfile, re, operator
import bpy_extras.io_utils
from bpy import ops
from bpy_extras.image_utils import load_image
from bpy.props import *

#==================================
# Common Functions
#==================================
def toRgb(RGBint):
	Blue =  RGBint & 255
	Green = (RGBint >> 8) & 255
	Red =   (RGBint >> 16) & 255
	return [Red,Green,Blue]

def rgb2hex(rgb):
    #Given a len 3 rgb tuple of 0-1 floats, return the hex string
    return '0x%02x%02x%02x' % tuple([round(val*255) for val in rgb])

def rgbtohtmlcolor(rgb):
	hexcolor = '#%02x%02x%02x' % rgb
	return hexcolor

def cleanupString(input):
	output = input
	#output = output.replace('.','')
	#remove anything that isn't letter number or underscore
	reg = re.compile(r'[^A-Za-z0-9_]+')
	output = re.sub(reg,"",output)
	return output

def ConvertQuadsToTris(obj):
	bpy.ops.object.mode_set(mode="OBJECT", toggle = False)
	bpy.ops.object.mode_set(mode="EDIT", toggle = True)
	bpy.ops.mesh.select_all(action='DESELECT')
	bpy.ops.mesh.select_all(action='SELECT')
	mesh = obj.data
	for f in mesh.faces:
		f.select = True	
	bpy.ops.mesh.quads_convert_to_tris()
	#Return to object mode
	bpy.ops.object.mode_set(mode="EDIT", toggle = False)
	bpy.ops.object.mode_set(mode="OBJECT", toggle = True)

def NumberOfSetBits(i):
	i = i - ((i >> 1) & 0x55555555)
	i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
	return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24
	
def invertNormals(lst):
	newlst = []
	for x in range(len(lst)):
		tmp = []
		for y in range(len(lst[x])):
			if lst[x][y] < 0:
				invertValue(lst[x][y])
			else:
				invertValue(lst[x][y])
			newlst.append(tmp)
	return newlst

def invertValue(val):
	if val < 0:
		return abs(val)
	else:
		return -abs(val)

def checkForOrco(obj):
	has_orco = False
	for mat_slot in [m for m in obj.material_slots if m.material is not None]:
		for tex in [t for t in mat_slot.material.texture_slots if (t and t.texture and t.use)]:
			if tex.texture_coords == 'ORCO':
				has_orco = True
				break  # break tex loop
		if has_orco:
			break  # break mat_slot loop
	return has_orco
	
#==================================
# Incomplete Functions - custom obj shit i made
#==================================
def WriteSkyBox(file,obj,Config):

	mesh = obj.data;

	if Config.A3DVersionSystem == 1:
		# version 5.6.0
		# do nothing
		print()
	elif Config.A3DVersionSystem == 2:
		# version 7.5.1
		# do nothing
		print()
	elif Config.A3DVersionSystem == 3:
		# version 7.6.0
		file.write("\t\t\tvar sbox:SkyBox = new SkyBox();\n")
		file.write('\t\t\tsbox.x = %f; sbox.y = %f; sbox.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 4:
		# version 7.7.0
		file.write("\t\t\tvar sbox:SkyBox = new SkyBox();\n")
		file.write('\t\t\tsbox.x = %f; sbox.y = %f; sbox.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 5:
		# version 7.8.0
		file.write("\t\t\tvar sbox:SkyBox = new SkyBox();\n")
		file.write('\t\t\tsbox.x = %f; sbox.y = %f; sbox.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 6:
		# version 8.5.0
		file.write("\t\t\tvar sbox:SkyBox = new SkyBox();\n")
		file.write('\t\t\tsbox.x = %f; sbox.y = %f; sbox.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10):
		# version 8.8.0
		file.write("\t\t\tvar sbox:SkyBox = new SkyBox();\n")
		file.write('\t\t\tsbox.x = %f; sbox.y = %f; sbox.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	else:
		print("version not found")

def WriteOccluder(file,obj,Config):
	if Config.A3DVersionSystem == 1:
		# version 5.6.0
		# do nothing
		print()
	elif Config.A3DVersionSystem == 2:
		# version 7.5.1
		# do nothing
		print()
	elif Config.A3DVersionSystem == 3:
		# version 7.6.0
		file.write("\t\t\tvar occ:Occluder = new Occluder();\n")
		file.write('\t\t\tocc.x = %f; occ.y = %f; occ.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 4:
		# version 7.7.0
		file.write("\t\t\tvar occ:Occluder = new Occluder();\n")
		file.write('\t\t\tocc.x = %f; occ.y = %f; occ.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 5:
		# version 7.8.0
		file.write("\t\t\tvar occ:Occluder = new Occluder();\n")
		file.write('\t\t\tocc.x = %f; occ.y = %f; occ.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 6:
		# version 8.5.0
		file.write("\t\t\tvar occ:Occluder = new Occluder();\n")
		file.write('\t\t\tocc.x = %f; occ.y = %f; occ.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10):
		# version 8.8.0
		file.write("\t\t\tvar occ:Occluder = new Occluder();\n")
		file.write('\t\t\tocc.x = %f; occ.y = %f; occ.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	else:
		print("version not found")

def WriteSprite3d(file,obj,Config):
	if Config.A3DVersionSystem == 1:
		# version 5.6.0
		file.write("\t\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
		file.write('\t\t\tsp3d.x = %f; sp3d.y = %f; sp3d.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 2:
		# version 7.5.1
		file.write("\t\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
		file.write('\t\t\tsp3d.x = %f; sp3d.y = %f; sp3d.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 3:
		# version 7.6.0
		file.write("\t\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
		file.write('\t\t\tsp3d.x = %f; sp3d.y = %f; sp3d.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 4:
		# version 7.7.0
		file.write("\t\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
		file.write('\t\t\tsp3d.x = %f; sp3d.y = %f; sp3d.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 5:
		# version 7.8.0
		file.write("\t\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
		file.write('\t\t\tsp3d.x = %f; sp3d.y = %f; sp3d.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif Config.A3DVersionSystem == 6:
		# version 8.5.0
		file.write("\t\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
		file.write('\t\t\tsp3d.x = %f; sp3d.y = %f; sp3d.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10):
		# version 8.8.0
		file.write("\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
	else:
		print("version not found")
	
#==================================
# EXPORTER - Actionscript (.as)
#==================================

# Exporter (.as) settings container
class ASExporterSettings:
	def __init__(self,A3DVersionSystem=1,CompilerOption=1,ExportMode=1,DocClass=False,CopyImgs=True,ByClass=False,ExportAnim=0,ExportUV=1,ExportNormals=1,ExportTangents=1):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.CompilerOption = int(CompilerOption)
		self.ExportMode = int(ExportMode)
		self.DocClass = bool(DocClass)
		self.CopyImgs = bool(CopyImgs)
		self.ByClass = bool(ByClass)
		self.ExportAnim = int(ExportAnim)
		self.ExportUV = int(ExportUV)
		self.ExportNormals = int(ExportNormals)
		self.ExportTangents = int(ExportTangents)

# Exporter (.as) class thats called from menu
class ASExporter(bpy.types.Operator):
	bl_idname = "ops.asexporter"
	bl_label = "Export to AS (Alternativa)"
	bl_description = "Export to AS (Alternativa)"
	
	#export options
	#alternativa3d versions
	A3DVersions = []
	A3DVersions.append(("1", "5.6.0", ""))
	A3DVersions.append(("2", "7.5.0", ""))
	A3DVersions.append(("3", "7.5.1", ""))
	A3DVersions.append(("4", "7.6.0", ""))
	A3DVersions.append(("5", "7.7.0", ""))
	A3DVersions.append(("6", "7.8.0", ""))
	A3DVersions.append(("7", "8.5.0", ""))
	A3DVersions.append(("8", "8.8.0", ""))
	A3DVersions.append(("9", "8.12.0", ""))
	A3DVersions.append(("10", "8.17.0", ""))
	A3DVersions.append(("11", "8.27.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D to export to", items=A3DVersions, default="11")
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
	#export document class?
	DocClass = BoolProperty(name="Create Document Class", description="Create document class that makes use of exported data", default=False)
	CopyImgs = BoolProperty(name="Copy Images", description="Copy images to destination folder of export", default=True)
	ByClass = BoolProperty(name="Use ByteArray Data (v8.27+)", description="Exports mesh data to compressed bytearray in as3", default=False)
	
	ExportAnim = BoolProperty(name="Animation", description="Animation", default=False)
	ExportUV = BoolProperty(name="Include UVs", description="Normals", default=True)
	ExportNormals = BoolProperty(name="Include Normals", description="Normals", default=True)
	ExportTangents = BoolProperty(name="Include Tangents", description="Tangents", default=True)
	
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		fp = self.properties.filepath
		if not filePath.lower().endswith('.as'):
			filePath += '.as'
		try:
			print('Output file : %s' %filePath)
			#file = open(filePath, 'wb')
			file = open(filePath, 'w')
			Config = ASExporterSettings(A3DVersionSystem=self.A3DVersionSystem,CompilerOption=self.CompilerOption,ExportMode=self.ExportMode, DocClass=self.DocClass,CopyImgs=self.CopyImgs,ByClass=self.ByClass,ExportAnim=self.ExportAnim,ExportUV=self.ExportUV,ExportNormals=self.ExportNormals,ExportTangents=self.ExportTangents)
			asexport(file,Config,fp)
			
			file.close()
		except Exception as e:
			print(e)
			file.close()
		return {'FINISHED'}
	def invoke (self, context, event):		
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}

# Exporter (.as) function		
def asexport(file,Config,fp):
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
	aobjs = []
	for obj in objs:
	
		ConvertQuadsToTris(obj)

		if "a3dtype" in obj:
			aobjs.append(obj)
		else:
			if (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
				# version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
				WriteClass8270(file,obj,Config)
			elif (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
				# version 7.6.0, 7.7.0, 7.8.0
				WriteClass78(file,obj,Config)
			elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3):
				# version 7.5.0, 7.5.1
				WriteClass75(file,obj,Config)
			elif Config.A3DVersionSystem == 1:
				# version 5.6.0
				WriteClass5(file,obj,Config)
			else:
				print("No Alternativa Version\n")
		
		#Copy images
		if Config.CopyImgs:
			print("copy images...\n")
			copyImages(obj,fp)

	#close off package
	WritePackageEnd(file)
	
	#Create document class
	if Config.DocClass:
		WriteDocuClass(file,objs,aobjs,Config,fp)
	
	print('Export Completed...\n')

def GetMeshVertexCount(Mesh):
    VertexCount = 0
    for Face in Mesh.faces:
        VertexCount += len(Face.vertices)
    return VertexCount
	
def WritePackageHeader(file,Config):
	file.write("//Alternativa3D Class Export For Blender 2.62 and above\n")
	file.write("//Plugin Author: David E Jones, http://davidejones.com\n\n")
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
	elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3):
		# version 7.5.0, 7.5.1
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport alternativa.engine3d.core.Geometry;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
		# version 7.6.0, 7.7.0, 7.8.0
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
		# version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
		file.write("\timport alternativa.engine3d.core.VertexAttributes;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.resources.BitmapTextureResource;\n")
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.resources.Geometry;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n")
		if Config.ByClass == 1:
			file.write("\timport flash.utils.ByteArray;\n")
			file.write("\timport flash.utils.Endian;\n")
		file.write("\n")
	else:
		print("version not found")

def WriteDocPackageHeader(file,Config):
	file.write("//Alternativa3D Class Export For Blender 2.62 and above\n")
	file.write("//Plugin Author: David E Jones, http://davidejones.com\n\n")
	file.write("package {\n\n")
	
	if Config.A3DVersionSystem == 1:
		# version 5.6.0
		file.write("\timport alternativa.engine3d.core.Scene3D;\n")
		file.write("\timport alternativa.engine3d.core.Object3D;\n")
		file.write("\timport alternativa.engine3d.core.Camera3D;\n")
		file.write("\timport alternativa.engine3d.display.View;\n")
		file.write("\timport alternativa.utils.MathUtils;\n")
		file.write("\timport alternativa.utils.FPS;\n")
		file.write("\timport flash.display.Sprite;\n")
		file.write("\timport flash.display.StageAlign;\n")
		file.write("\timport flash.display.StageScaleMode;\n")
		file.write("\timport flash.events.Event;\n")
	elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3)  or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
		# version 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0
		file.write("\timport alternativa.engine3d.core.Camera3D;\n")
		file.write("\timport alternativa.engine3d.core.Object3DContainer;\n")
		file.write("\timport alternativa.engine3d.core.View;\n")
		file.write("\timport flash.display.Sprite;\n")
		file.write("\timport flash.display.StageAlign;\n")
		file.write("\timport flash.display.StageScaleMode;\n")
		file.write("\timport flash.events.Event;\n")
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
		# version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
		file.write("\timport alternativa.engine3d.core.Camera3D;\n")
		file.write("\timport alternativa.engine3d.core.Object3D;\n")
		file.write("\timport alternativa.engine3d.core.Resource;\n")
		file.write("\timport alternativa.engine3d.core.View;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport flash.display.Sprite;\n")
		file.write("\timport flash.display.Stage3D;\n")
		file.write("\timport flash.display.StageAlign;\n")
		file.write("\timport flash.display.StageScaleMode;\n")
		file.write("\timport flash.events.Event;\n")
	else:
		print("version not found")
		
	file.write('\n\t[SWF(backgroundColor="#000000", frameRate="100", width="800", height="600")]\n\n')
		
def WritePackageEnd(file):
	file.write("}")
	
def setupMaterials(file,obj,Config):
	#read the materials from the mesh and output them accordingly
	mesh = obj.data
	verts = mesh.vertices
	mati = {}
	
	#mesh.materials
	#mesh.vertex_colors
	#MeshFace.material_index
	
	Materials = mesh.materials
	if Materials.keys():
		MaterialIndexes = {}
		for Face in mesh.faces:
			if Materials[Face.material_index] not in MaterialIndexes:
				MaterialIndexes[Materials[Face.material_index]] = len(MaterialIndexes)
		Materials = [Item[::-1] for Item in MaterialIndexes.items()]
		Materials.sort()
		x=0
		for Material in Materials:
			#mati[x] = "material"+str(x)
			mati[x] = cleanupString(str(Material[1].name))
			#mati[Material.name] = "material"+str(x)
			#WriteMaterial(file,"material"+str(x),Config, Material[1])
			WriteMaterial(file,mati[x],Config, Material[1])
			x += 1
	return mati
			
def WriteMaterial(file,id,Config,Material=None):
	if Material:
		#print(Material.name)
		nme = cleanupString(str(Material.name))
		
		Texture = GetMaterialTexture(Material)
		if Texture:
			#print(Texture)
			# if version 5.6.0
			if Config.A3DVersionSystem == 1:
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(nme)+':Class;\n')
					#file.write('\t\tprivate static const '+str(id)+':Texture = new Texture(new bmp'+str(nme)+'().bitmapData, "'+str(nme)+'");\n\n')
					file.write('\t\tprivate static const '+str(id)+':TextureMaterial = new TextureMaterial(new Texture(new bmp'+str(nme)+'().bitmapData, "'+str(nme)+'"));\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(nme)+":Bitmap = new Bitmap(new bd"+str(nme)+"(0,0));\n")
					#file.write('\t\tprivate var '+str(id)+':Texture = new Texture(bmp'+str(nme)+'.bitmapData, "'+str(nme)+'");\n\n')
					file.write('\t\tprivate var '+str(id)+':TextureMaterial = new TextureMaterial(new Texture(new bmp'+str(nme)+'().bitmapData, "'+str(nme)+'"));\n\n')
			#if version 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0
			elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3) or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(nme)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':TextureMaterial = new TextureMaterial(new bmp'+str(nme)+'().bitmapData, true, true);\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(nme)+":Bitmap = new Bitmap(new bd"+str(nme)+"(0,0));\n")
					file.write("\t\tprivate var "+str(id)+":TextureMaterial = new TextureMaterial(bmp"+str(nme)+".bitmapData, true, true);\n\n")
			#if version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
			elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(nme)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':TextureMaterial = new TextureMaterial(new BitmapTextureResource(new bmp'+str(nme)+'().bitmapData));\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(nme)+":Bitmap = new Bitmap(new bd"+str(nme)+"(0,0));\n")
					file.write("\t\tprivate var "+str(id)+":TextureMaterial = new TextureMaterial(new BitmapTextureResource(bmp"+str(nme)+".bitmapData));\n\n")
			else:
				print("version not found")
		else:
			#no tex maybe vertex colour?
			Diffuse = list(Material.diffuse_color)
			Diffuse.append(Material.alpha)
			Specularity = Material.specular_intensity
			Specular = list(Material.specular_color)

			file.write('\t\tprivate var '+id+':FillMaterial = new FillMaterial('+rgb2hex((Diffuse[0], Diffuse[1], Diffuse[2]))+');\n\n')
	
def GetMaterialTexture(Material):
    if Material:
        #Create a list of Textures that have type "IMAGE"
        ImageTextures = [Material.texture_slots[TextureSlot].texture for TextureSlot in Material.texture_slots.keys() if Material.texture_slots[TextureSlot].texture.type == "IMAGE"]
        #Refine a new list with only image textures that have a file source
        ImageFiles = [os.path.basename(Texture.image.filepath) for Texture in ImageTextures if Texture.image.source == "FILE"]
        if ImageFiles:
            return ImageFiles[0]
    return None

def copyImages(obj,filepath):
	mesh = obj.data
	source_dir = bpy.data.filepath
	dest_dir = os.path.dirname(filepath)
	copy_set = set()
	
	#print("filepath="+str(filepath))
	#print("source_dir="+str(source_dir))
	#print("dest_dir="+str(dest_dir))
	
	for mat in mesh.materials:
		tex = mat.active_texture
		if tex is not None:
			if "image" in tex:
				img = tex.image
				rel = bpy_extras.io_utils.path_reference(img.filepath, source_dir, dest_dir, 'COPY', "", copy_set)
	bpy_extras.io_utils.path_reference_copy(copy_set)

def writeByteArrayValues(file,verts,uvt,indices):
	file.write("\t\t\tvalues= new <uint>[")

	tfile = tempfile.TemporaryFile(mode ='w+b')
	#length of verts -short
	tfile.write(struct.pack("<H", len(verts)*3))
	for v in verts:
		tfile.write(struct.pack("<f", v[0]))
		tfile.write(struct.pack("<f", v[1]))
		tfile.write(struct.pack("<f", v[2]))
	
	#length of uvts -short
	tfile.write(struct.pack("<H", len(uvt)*2))
	for uv in uvt:
		tfile.write(struct.pack("<f", uv[0]))
		tfile.write(struct.pack("<f", uv[1]))
	
	#length of indices -short
	tfile.write(struct.pack("<H", len(indices)))
	for i in indices:
		tfile.write(struct.pack("<I", i))
	
	#rewind	
	tfile.seek(0)
	
	#compress
	indata = tfile.read()
	outdata = zlib.compress(indata)
	tfile.close()
	tfile = tempfile.TemporaryFile(mode ='w+b')
	tfile.write(outdata)
	tfile.seek(0)
	
	try:
		byte = tfile.read(1)
		while byte != "":
			if len(byte) > 0:
				#file.write("%X," % int(byte))
				file.write("0x%X," % struct.unpack('B', byte))
				byte = tfile.read(1)
			else:
				break
	finally:
		tfile.close()
		
	file.write("];\n")

def WriteObjPosRot(file,obj):
	file.write("\t\t\tthis.rotationX = %.6f;\n" % obj.rotation_euler[0])
	file.write("\t\t\tthis.rotationY = %.6f;\n" % obj.rotation_euler[1])
	file.write("\t\t\tthis.rotationZ = %.6f;\n" % obj.rotation_euler[2])
	file.write("\t\t\tthis.x = %.6f;\n" % obj.location[0])
	file.write("\t\t\tthis.y = %.6f;\n" % obj.location[1])
	file.write("\t\t\tthis.z = %.6f;\n" % obj.location[2])
	file.write("\t\t\tthis.scaleX = %.6f;\n" % obj.scale[0])
	file.write("\t\t\tthis.scaleY = %.6f;\n" % obj.scale[1])
	file.write("\t\t\tthis.scaleZ = %.6f;\n" % obj.scale[2])

def getCommonData(obj,flipUV=1):
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	hasFaceUV = len(mesh.uv_textures) > 0
	vs,uvt,ins,nr,tan,bb,trns = [],[],[],[],[],[],[]
	vertices_list = []
	vertices_co_list = []
	vertices_index_list = []
	normals_list = []
	uv_coord_list = []
	new_index = 0
	uvtex = mesh.uv_textures.active
	has_orco = checkForOrco(obj)
	
	if has_orco:
		print("HAS ORCO")
	
	if hasFaceUV:
		for uv_index, uv_itself in enumerate(uvtex.data):
			uvs = uv_itself.uv1, uv_itself.uv2, uv_itself.uv3, uv_itself.uv4
			for vertex_index, vertex_itself in enumerate(mesh.faces[uv_index].vertices):
				vertex = mesh.vertices[vertex_itself]
				vertices_list.append(vertex_itself)
				vertices_co_list.append(vertex.co.xyz)
				normals_list.append(vertex.normal.xyz)
				vertices_index_list.append(new_index)
				new_index += 1
				uv_coord_list.append(uvs[vertex_index])
				vs.append([vertices_co_list[-1][0],vertices_co_list[-1][1],vertices_co_list[-1][2]])
				if mesh.faces[uv_index].use_smooth:
					nr.append([normals_list[-1][0],normals_list[-1][1],normals_list[-1][2]])
				else:
					nr.append(mesh.faces[uv_index].normal)
				ins.append(vertices_index_list[-1])
				if flipUV == 1:
					uv = [uv_coord_list[-1][0], 1.0 - uv_coord_list[-1][1]]
				else:
					uv = [uv_coord_list[-1][0], uv_coord_list[-1][1]]
				uvt.append(uv)
	else:
		# if there are no image textures, output the old way
		for face in mesh.faces:
			if len(face.vertices) > 0:
				ins.append(face.vertices[0])
				ins.append(face.vertices[1])
				ins.append(face.vertices[2])
				#nr.append([[face.normal[0],face.normal[1],face.normal[2]]])
				for i in range(len(face.vertices)):
					if face.use_smooth:
						v = mesh.vertices[face.vertices[i]]
						nr.append([v.normal[0],v.normal[1],v.normal[2]])
					else:
						nr.append(face.normal)
					hasFaceUV = len(mesh.uv_textures) > 0
					if hasFaceUV:
						uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
						uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
						uvt.append(uv)
		for v in mesh.vertices:
			vs.append([v.co[0],v.co[1],v.co[2]])
			nr.append([v.normal[0],v.normal[1],v.normal[2]])

	#if we have uv's and normals then calculate tangents
	if (len(uvt) > 0) and (len(nr) > 0):
		tan = calculateTangents(ins,vs,uv_coord_list,nr)		
	
	#get bound box
	bb = getBoundBox(obj)
			
	#get transform	
	#trns=[obj.location[0],obj.rotation_euler[0],obj.scale[0],obj.location[1],obj.rotation_euler[1],obj.scale[1],obj.location[2],obj.rotation_euler[2],obj.scale[2],obj.dimensions[0],obj.dimensions[1],obj.dimensions[2]]
		
	trns = getObjTransform(obj)
		
	return vs,uvt,ins,nr,tan,bb,trns

def getObjTransform(obj):
	trns = []
	c=0
	j=0
	for x in obj.matrix_local:
		j=0
		for y in x:
			if j == 3 and c != 3:
				trns.append(obj.location[c])
			else:
				trns.append(y)
			j=j+1
		c=c+1	
	return trns
	
def calculateNormals(ins,verts):
	# based on alternativas code here
	# https://github.com/AlternativaPlatform/Alternativa3D/blob/master/src/alternativa/engine3d/resources/Geometry.as
	normals = []
	x=0
	numIndices = len(ins)
	
	#print("numIndices="+str(numIndices))
	#print("verts="+str(len(verts)))
	
	for i in range(numIndices):
	
		if i >= numIndices/3:
			break
			
		vertIndexA = ins[x]
		vertIndexB = ins[x + 1]
		vertIndexC = ins[x + 2]
		
		#vertex1
		ax = verts[x][0]
		ay = verts[x][1]
		az = verts[x][2]

		#vertex2
		bx = verts[x + 1][0]
		by = verts[x + 1][1]
		bz = verts[x + 1][2]

		#vertex3
		cx = verts[x + 2][0]
		cy = verts[x + 2][1]
		cz = verts[x + 2][2]

		#v2-v1
		abx = bx - ax
		aby = by - ay
		abz = bz - az

		#v3-v1
		acx = cx - ax
		acy = cy - ay
		acz = cz - az
		
		normalX = acz*aby - acy*abz
		normalY = acx*abz - acz*abx
		normalZ = acy*abx - acx*aby
		
		normalLen = math.sqrt(normalX*normalX + normalY*normalY + normalZ*normalZ)
		
		if (normalLen > 0):
			normalX /= normalLen
			normalY /= normalLen
			normalZ /= normalLen
		else:
			print("degenerated triangle")
			print(i/3)
		
		# v1 normal
		if vertIndexA in normals:
			normal = normals[vertIndexA]
			normal.x += normalX
			normal.y += normalY
			normal.z += normalZ
		else:
			normals.append(mathutils.Vector((normalX, normalY, normalZ)))

		# v2 normal
		if vertIndexB in normals:
			normal = normals[vertIndexB]
			normal.x += normalX
			normal.y += normalY
			normal.z += normalZ
		else:
			normals.append(mathutils.Vector((normalX, normalY, normalZ)))

		# v3 normal
		if vertIndexC in normals:
			normal = normals[vertIndexC]
			normal.x += normalX
			normal.y += normalY
			normal.z += normalZ
		else:
			normals.append(mathutils.Vector((normalX, normalY, normalZ)))
		
		x = x + 3
		
	#normalize
	for nor in normals:
		nor.normalize()
		
	return normals
	
def calculateTangents(ins,verts,uvs,nrms):
	# based on alternativas code here
	# https://github.com/AlternativaPlatform/Alternativa3D/blob/master/src/alternativa/engine3d/resources/Geometry.as
	tangents = []
	x=0
	numIndices = len(ins)
	
	#print("numIndices="+str(numIndices))
	#print("verts="+str(len(verts)))
	#print("uvs="+str(len(uvs)))
	#print("normals="+str(len(nrms)))
	
	for i in range(numIndices):
		
		if i >= numIndices/3:
			break
	
		vertIndexA = ins[x]
		vertIndexB = ins[x + 1]
		vertIndexC = ins[x + 2]
			
		#vertex1
		ax = verts[x][0]
		ay = verts[x][1]
		az = verts[x][2]
		#vertex2
		bx = verts[x + 1][0]
		by = verts[x + 1][1]
		bz = verts[x + 1][2]
		#vertex3
		cx = verts[x + 2][0]
		cy = verts[x + 2][1]
		cz = verts[x + 2][2]
		#uv
		au = uvs[x][0]
		av = uvs[x][1]
		#uv
		bu = uvs[x + 1][0]
		bv = uvs[x + 1][1]
		#uv
		cu = uvs[x + 2][0]
		cv = uvs[x + 2][1]
		#nrm
		anx = nrms[x][0]
		any = nrms[x][1]
		anz = nrms[x][2]
		#nrm
		bnx = nrms[x + 1][0]
		bny = nrms[x + 1][1]
		bnz = nrms[x + 1][2]
		#nrm
		cnx = nrms[x + 2][0]
		cny = nrms[x + 2][1]
		cnz = nrms[x + 2][2]
		
		# v2-v1
		abx = bx - ax
		aby = by - ay
		abz = bz - az

		# v3-v1
		acx = cx - ax
		acy = cy - ay
		acz = cz - az

		abu = bu - au
		abv = bv - av

		acu = cu - au
		acv = cv - av

		divisor = (abu*acv - acu*abv)
		if divisor == 0: divisor = 0.01 #prevent 0 div. error
		r = 1.0/divisor

		tangentX = r*(acv*abx - acx*abv)
		tangentY = r*(acv*aby - abv*acy)
		tangentZ = r*(acv*abz - abv*acz)
		
		if vertIndexA in tangents:
			#exists
			#print("va exists")
			tangent = tangents[vertIndexA]
			tangent.x += tangentX - anx*(anx*tangentX + any*tangentY + anz*tangentZ)
			tangent.y += tangentY - any*(anx*tangentX + any*tangentY + anz*tangentZ)
			tangent.z += tangentZ - anz*(anx*tangentX + any*tangentY + anz*tangentZ)
		else:
			#doesn't exist
			#print("va doesn't exist")
			#tangents[vertIndexA] 
			tangents.append(mathutils.Vector((tangentX - anx*(anx*tangentX + any*tangentY + anz*tangentZ),tangentY - any*(anx*tangentX + any*tangentY + anz*tangentZ),tangentZ - anz*(anx*tangentX + any*tangentY + anz*tangentZ))))
			
		if vertIndexB in tangents:
			#exists
			#print("vb exists")
			tangent = tangents[vertIndexB]
			tangent.x += tangentX - bnx*(bnx*tangentX + bny*tangentY + bnz*tangentZ)
			tangent.y += tangentY - bny*(bnx*tangentX + bny*tangentY + bnz*tangentZ)
			tangent.z += tangentZ - bnz*(bnx*tangentX + bny*tangentY + bnz*tangentZ)
		else:
			#doesn't exist
			#print("vb doesn't exist")
			#tangents[vertIndexB] 
			tangents.append(mathutils.Vector((tangentX - bnx*(bnx*tangentX + bny*tangentY + bnz*tangentZ),tangentY - bny*(bnx*tangentX + bny*tangentY + bnz*tangentZ),tangentZ - bnz*(bnx*tangentX + bny*tangentY + bnz*tangentZ))))
			
		if vertIndexC in tangents:
			#exists
			#print("vc exists")
			tangent = tangents[vertIndexC]
			tangent.x += tangentX - cnx*(cnx*tangentX + cny*tangentY + cnz*tangentZ)
			tangent.y += tangentY - cny*(cnx*tangentX + cny*tangentY + cnz*tangentZ)
			tangent.z += tangentZ - cnz*(cnx*tangentX + cny*tangentY + cnz*tangentZ)
		else:
			#doesn't exist
			#print("vc doesn't exist")
			#tangents[vertIndexC] 
			tangents.append(mathutils.Vector((tangentX - cnx*(cnx*tangentX + cny*tangentY + cnz*tangentZ),tangentY - cny*(cnx*tangentX + cny*tangentY + cnz*tangentZ),tangentZ - cnz*(cnx*tangentX + cny*tangentY + cnz*tangentZ))))
		
		
		#Calculate handedness
		
		x = x + 3
	
	#normalize
	for tan in tangents:
		tan.normalize()
	
	return tangents
		
def getBoundBox(obj):
	#https://github.com/subcomandante/Blender-2.5-Exporter/commit/12e463d2e9f95001cc0e9c39524ffdad686b23c5
	#http://projects.blender.org/tracker/?func=detail&atid=498&aid=30864&group_id=9
	v = [list(bb) for bb in obj.bound_box]
	bmin = min(v)
	bmax = max(v)
	minx = max(bmin[0] * obj.scale.x, -1e10)
	miny = max(bmin[1] * obj.scale.y, -1e10)
	minz = max(bmin[2] * obj.scale.z, -1e10)
	maxx = min(bmax[0] * obj.scale.x, 1e10)
	maxy = min(bmax[1] * obj.scale.y, 1e10)
	maxz = min(bmax[2] * obj.scale.z, 1e10)
	#vec = [j for v in mesh.vertices for j in v.co]
	#paramsSetFloat("minX", max(min(vec[0::3]), -1e10))
	#paramsSetFloat("minY", max(min(vec[1::3]), -1e10))
	#paramsSetFloat("minZ", max(min(vec[2::3]), -1e10))
	#paramsSetFloat("maxX", min(max(vec[0::3]), 1e10))
	#paramsSetFloat("maxY", min(max(vec[1::3]), 1e10))
	#paramsSetFloat("maxZ", min(max(vec[2::3]), 1e10))
	return [minx,miny,minz,maxx,maxy,maxz]
	
def WriteClass8270(file,obj,Config):
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	hasFaceUV = len(mesh.uv_textures) > 0
	
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
	
	#if bytearray
	if Config.ByClass == 1:
		file.write("\t\tprivate var values:Vector.<uint>;\n")
		file.write("\t\tprivate var bytedata:ByteArray = new ByteArray();\n")
	
	#write attributes/geom
	file.write("\t\tprivate var attributes:Array;\n\n")
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tattributes = new Array();\n")
	file.write("\t\t\tattributes[0] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[1] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[2] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[3] = VertexAttributes.TEXCOORDS[0];\n")
	file.write("\t\t\tattributes[4] = VertexAttributes.TEXCOORDS[0];\n")
	if Config.ByClass == 0:
		file.write("\t\t\tattributes[5] = VertexAttributes.NORMAL;\n")
		file.write("\t\t\tattributes[6] = VertexAttributes.NORMAL;\n")
		file.write("\t\t\tattributes[7] = VertexAttributes.NORMAL;\n")
		file.write("\t\t\tattributes[8] = VertexAttributes.TANGENT4;\n")
		file.write("\t\t\tattributes[9] = VertexAttributes.TANGENT4;\n")
		file.write("\t\t\tattributes[10] = VertexAttributes.TANGENT4;\n")
		file.write("\t\t\tattributes[11] = VertexAttributes.TANGENT4;\n\n")
	file.write("\t\t\tvar g:Geometry = new Geometry();\n")
	file.write("\t\t\tg.addVertexStream(attributes);\n")
	
	#get data
	vs,uvt,ins,nr,tan,bb,trns = getCommonData(obj)
			
	file.write("\t\t\tg.numVertices = "+str(len(vs))+";\n\n")
	
	if Config.ByClass == 0:
		#write vertices
		if len(vs) > 0:
			file.write("\t\t\tvar vertices:Array = [\n")
			for v in vs:
				#file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % (v[0],v[1],v[2]))
				file.write("\t\t\t\t%.6g, %.6g, %.6g,\n" % (v[0],v[1],v[2]))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar vertices:Array = new Array();\n")
		
		#write uv coords
		if (len(uvt) > 0) and (Config.ExportUV == 1):
			file.write("\t\t\tvar uvt:Array = [\n")
			for u in uvt:
				#file.write("\t\t\t\t"+str(u[0])+","+str(u[1]+","))
				file.write("\t\t\t\t%.4g,%.4g,\n" % (u[0],u[1]))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar uvt:Array = new Array();\n")
		
		#write indices
		if len(ins) > 0:
			file.write("\t\t\tvar ind:Array = [\n")
			x=0
			for t in ins:
				if x == 0:
					file.write("\t\t\t\t")
				file.write("%i," % (t))
				if x >= 2:
					file.write("\n")
					x=-1
				x = x+1
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar ind:Array = new Array();\n")
		
		#write normals
		if (len(nr) > 0) and (Config.ExportNormals == 1):
			file.write("\t\t\tvar normals:Array = [\n")
			for n in nr:
				#file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % (n[0],n[1],n[2]))
				file.write("\t\t\t\t%.6g, %.6g, %.6g,\n" % (n[0],n[1],n[2]))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar normals:Array = new Array();\n")
			
		#write tangents
		if (len(tan) > 0) and (Config.ExportTangents == 1):
			file.write("\t\t\tvar tangent:Array = [\n")
			for t in tan:
				file.write("\t\t\t\t%.6g, %.6g, %.6g, %.6g,\n" % (t[0],t[1],t[2],-1))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar tangent:Array = new Array();\n\n")
		
		#set attributes
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
		if (len(uvt) > 0) and (Config.ExportUV == 1):
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")	
			
		if (len(nr) > 0) and (Config.ExportNormals == 1):
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
			
		if (len(tan) > 0) and (Config.ExportTangents == 1):
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
		
		#set geometry
		file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
		if Config.A3DVersionSystem == 11:
			file.write("\t\t\t//g.calculateNormals();\n")
			file.write("\t\t\t//g.calculateTangents(0);\n")
		file.write("\t\t\tthis.geometry = g;\n")
	else:
		writeByteArrayValues(file,vs,uvt,ins)
		file.write("\t\t\tfor each(var b:uint in values)\n")
		file.write("\t\t\t{\n")
		file.write("\t\t\t\tbytedata.writeByte(b);\n")
		file.write("\t\t\t}\n")
		file.write("\t\t\tvar vertices:Array = new Array();\n")
		file.write("\t\t\tvar uvt:Array = new Array();\n")
		file.write("\t\t\tvar ind:Array = new Array();\n")
		file.write("\t\t\tbytedata.endian = Endian.LITTLE_ENDIAN;\n")
		file.write("\t\t\tbytedata.uncompress();\n")
		file.write("\t\t\tbytedata.position=0;\n")
		file.write("\t\t\tvar vlen:uint = bytedata.readUnsignedShort();\n")
		file.write("\t\t\tg.numVertices = vlen/3;\n")
		file.write("\t\t\tfor(var i:int = 0; i < vlen; i++){vertices.push(bytedata.readFloat());}\n")
		file.write("\t\t\tvar uvlen:uint = bytedata.readUnsignedShort();\n")
		file.write("\t\t\tfor(var x:int = 0; x < uvlen; x++){uvt.push(bytedata.readFloat());}\n")
		file.write("\t\t\tvar ilen:uint = bytedata.readUnsignedShort();\n")
		file.write("\t\t\tfor(var j:int = 0; j < ilen; j++){ind.push(bytedata.readUnsignedInt());}\n")
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
		file.write("\t\t\tif(uvlen > 0){g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));}\n")
		file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
		file.write("\t\t\tg.calculateNormals();\n")
		file.write("\t\t\tg.calculateTangents(0);\n")
		file.write("\t\t\tthis.geometry = g;\n")

	
	start,end,mts,mats = collectSurfaces(mesh)
	
	#set surfaces
	if len(mts) > 0:
		for x in range(len(mts)):
			file.write("\t\t\tthis.addSurface("+mts[x]+", "+str(start[x])+", "+str(end[x])+");\n")
	else:
		file.write("\t\t\t//this.addSurface(new FillMaterial(0xFF0000), 0, "+str(len(ins))+");\n")
	
	#finishup
	file.write("\t\t\tthis.calculateBoundBox();\n")
	file.write("\t\t}\n")
	file.write("\t}\n")

def collectSurfaces(mesh):
	#collect surface data, indexbegin/numtriangles etc
	Materials = mesh.materials
	c=0
	triangles = -1
	lastmat = None
	start,end,items,mts,mats = [],[],[],[],[]
	for face in mesh.faces:
		triangles = triangles + 1
		if face.material_index <= len(Materials)-1:
			srcmat = Materials[face.material_index]
			if srcmat not in items:
				start.append(face.index * 3)
				if c != 0:
					end.append(triangles)
					triangles = 0
				mts.append(cleanupString(str(srcmat.name)))
				mats.append(srcmat)
			else:
				if srcmat != lastmat:
					start.append(face.index * 3)
					if c != 0:
						end.append(triangles)
						triangles = 0
					mts.append(cleanupString(str(srcmat.name)))
					mats.append(srcmat)
			lastmat = srcmat
			items.append(srcmat)
			c = c+1
	end.append(triangles+1)
	return start,end,mts,mats
	
def WriteClass78(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
		
	cn=-1
	for face in mesh.faces:
		cn +=1
		file.write('\t\t\t\taddFace(Vector.<Vertex>([\n')
		if len(face.vertices) > 0:
			for i in range(len(face.vertices)):
				hasFaceUV = len(mesh.uv_textures) > 0
				if (hasFaceUV) and (Config.ExportUV == 1):
					uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
					uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
					file.write('\t\t\t\t\taddVertex(%f, %f, %f, %f, %f),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z, uv[0], uv[1]) )
				else:
					file.write('\t\t\t\t\taddVertex(%f, %f, %f, 0, 0),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z) )
		if hasFaceUV:
			#file.write('\t\t\t\t]),'+uvimagevarrefs[face.index]+');\n\n')
			if mati[face.material_index]:
				file.write('\t\t\t\t]),'+mati[face.material_index]+');\n\n')
			else:
				if len(Materials) > 0:
					Diffuse = list(Materials[face.material_index].diffuse_color)
					Diffuse.append(Materials[face.material_index].alpha)
					file.write('\t\t\t\t]),new FillMaterial('+rgb2hex((Diffuse[0], Diffuse[1], Diffuse[2]))+'));\n\n')
				else:
					file.write('\t\t\t\t]),new FillMaterial(0xFF0000));\n\n')
		else:
			if len(Materials) > 0:
				Diffuse = list(Materials[face.material_index].diffuse_color)
				Diffuse.append(Materials[face.material_index].alpha)
				file.write('\t\t\t\t]),new FillMaterial('+rgb2hex((Diffuse[0], Diffuse[1], Diffuse[2]))+'));\n\n')
			else:
				file.write('\t\t\t\t]),new FillMaterial(0xFF0000));\n\n')

	#calculations
	if Config.A3DVersionSystem == 4:
		#7.6.0
		file.write("\t\tcalculateNormals();\n")
		file.write("\t\tcalculateBounds();\n")
	else:
		#7.7.0 - 7.8.0
		file.write("\t\t\tcalculateFacesNormals();\n")
		file.write("\t\t\tcalculateVerticesNormals();\n")
		file.write("\t\t\tcalculateBounds();\n")
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass75(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tvar g:Geometry = new Geometry();\n\n")
	
	for face in mesh.faces:
		file.write('\t\t\t\tg.addFace(Vector.<Vertex>([\n')
		for i in range(len(face.vertices)):
			hasFaceUV = len(mesh.uv_textures) > 0
			if (hasFaceUV) and (Config.ExportUV == 1):
				uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
				uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
				file.write('\t\t\t\t\tg.addVertex(%f, %f, %f, %f, %f),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z, uv[0], uv[1]) )
			else:
				file.write('\t\t\t\t\tg.addVertex(%f, %f, %f, 0, 0),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z) )
		if hasFaceUV:
			if mati[face.material_index]:
				file.write('\t\t\t\t]),'+mati[face.material_index]+');\n\n')
			else:
				if len(Materials) > 0:
					Diffuse = list(Materials[face.material_index].diffuse_color)
					Diffuse.append(Materials[face.material_index].alpha)
					file.write('\t\t\t\t]),new FillMaterial('+rgb2hex((Diffuse[0], Diffuse[1], Diffuse[2]))+'));\n\n')
				else:
					file.write('\t\t\t\t]),new FillMaterial(0xFF0000));\n\n')
		else:
			if len(Materials) > 0:
				Diffuse = list(Materials[face.material_index].diffuse_color)
				Diffuse.append(Materials[face.material_index].alpha)
				file.write('\t\t\t\t]),new FillMaterial('+rgb2hex((Diffuse[0], Diffuse[1], Diffuse[2]))+'));\n\n')
			else:
				file.write('\t\t\t\t]),new FillMaterial(0xFF0000));\n\n')
	
	file.write("\t\t\t//g.weldVertices();\n")
	file.write("\t\t\t//g.weldFaces();\n")
	file.write("\t\t\tgeometry = g;\n\n")
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass5(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data;
	verts = mesh.vertices
	Materials = mesh.materials
	hasFaceUV = len(mesh.uv_textures) > 0
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	
	#get data
	vs,uvt,ins,nr,tan,bb,trns = getCommonData(obj,False)

	#write vertices
	if len(vs) > 0:
		count = 0
		for v in vs:
			file.write("\t\t\tcreateVertex(%.6g, %.6g, %.6g, %i);\n" % (v[0],v[1],v[2],count))
			count += 1
		file.write('\n')
		
	#write faces
	if len(ins) > 0:
		count = 0
		file.write('\t\t\tcreateFace([')
		x=0
		j=0
		for t in ins:
			file.write("%i" % (t))
			if x==2:
				x=0
				file.write('], '+str(j)+');\n')
				j=j+1
				if count < len(ins)-1:
					file.write('\t\t\tcreateFace([')
			else:
				file.write(',')
				x=x+1
			count += 1
			
	facecount = j
	
	#write face/uvs
	if (len(uvt) > 0) and (Config.ExportUV == 1):
		count = 0
		file.write('\t\t\tsetUVsToFace(')
		x=0
		j=0
		for u in uvt:
			#file.write('new Point(%.4g,%.4g), ' % (u[0],u[1]))
			file.write('new Point(%f,%f), ' % (u[0],u[1]))
			if x==2:
				x=0
				file.write('%i);\n' % j)
				j=j+1
				if count < len(uvt)-1:
					file.write('\t\t\tsetUVsToFace(')
			else:
				x=x+1
			count += 1
		file.write('\n')
		
			
	#write surfaces
	x=0
	lastmat = None
	items,mts,fcs,temp = [],[],[],[]
	for face in mesh.faces:
		if face.material_index <= len(Materials)-1:
			srcmat = Materials[face.material_index]
			if srcmat not in items:
				mts.append(cleanupString(str(srcmat.name)))
				if x == 0:
					temp.append(x)
				else:
					fcs.append(temp)
					temp = []
					temp.append(x)
			else:
				if srcmat != lastmat:
					mts.append(cleanupString(str(srcmat.name)))
					fcs.append(temp)
					temp = []
					temp.append(x)
				else:
					temp.append(x)
		lastmat = srcmat
		items.append(srcmat)
		x=x+1
	fcs.append(temp)	
	
	count = 0
	for x in range(len(mts)):
		file.write('\t\t\tcreateSurface([')
		for i in range(len(fcs[x])):
			file.write("%i" % (count+i))
			if i != len(fcs[x])-1:
				file.write(",")
		count = count + len(fcs[x])
		file.write('], "'+mts[x]+'");\n')
		file.write('\t\t\tsetMaterialToSurface('+mts[x]+', "'+mts[x]+'");\n')
		
		
	#for x in range(len(mati)):
	#	file.write('\t\t\tcreateSurface([')
	#	for i in range(facecount):
	#		file.write("%i" % i)
	#		if i != facecount-1:
	#			file.write(",")
	#	file.write('], "'+mati[x]+'");\n')
	#	file.write('\t\t\tsetMaterialToSurface('+mati[x]+', "'+mati[x]+'");\n')
	
	file.write("\t\t}\n")
	file.write("\t}\n")

def WriteDocuClass(ofile,objs,aobjs,Config,fp):

	#docclass filename
	#fp = os.path.splitext(fp)[0] + "main.as"
	fp = os.path.dirname(fp) + os.sep + "main.as"
	
	if os.path.exists(fp) == True:
		print("Docuclass "+fp+" Already exists")
	else:
		#create new file same location as other
		if not fp.lower().endswith('.as'):
			fp += '.as'
		try:
			file = open(fp, 'w')
		except Exception as e:
			print(e)

		WriteDocPackageHeader(file,Config)
		file.write("\tpublic class main extends Sprite {\n\n")
		
		#variables
		for i, obj in enumerate(objs):
			file.write("\t\tprivate var obj"+str(i)+":"+cleanupString(obj.data.name)+";\n\n")
		
		#for obj in aobjs:
		#	#print(obj["a3dtype"])
		#	if obj["a3dtype"] == "skybox":
		#		WriteSkyBox(file,obj,Config)
		#	if obj["a3dtype"] == "occluder":
		#		WriteOccluder(file,obj,Config)
		#	if obj["a3dtype"] == "sprite3d":
		#		WriteSprite3d(file,obj,Config)
		
		if Config.A3DVersionSystem == 1:
			# version 5.6.0
			file.write("\t\tprivate var scene:Scene3D = new Scene3D();\n")
			file.write('\t\tprivate var rootContainer:Object3D = scene.root = new Object3D("root");\n')
			file.write("\t\tprivate var camera:Camera3D;\n")
			file.write("\t\tprivate var view:View;\n\n")
			
			file.write("\t\tpublic function main() {\n\n")
			
			file.write("\t\t\tstage.align = StageAlign.TOP_LEFT;\n")
			file.write("\t\t\tstage.scaleMode = StageScaleMode.NO_SCALE;\n\n")
			
			file.write('\t\t\tcamera = new Camera3D("camera");\n')
			file.write("\t\t\tcamera.fov = MathUtils.DEG1*100;\n")
			file.write("\t\t\tcamera.z = -10;\n")
			file.write("\t\t\trootContainer.addChild(camera);\n\n")
			
			for i, obj in enumerate(objs):
				file.write("\t\t\tobj"+str(i)+" = new "+cleanupString(obj.data.name)+"();\n")
				file.write("\t\t\trootContainer.addChild(obj"+str(i)+");\n")
			file.write("\n")
			
			file.write("\t\t\tview = new View(camera);\n")
			file.write("\t\t\taddChild(view);\n")
			file.write("\t\t\tview.interactive = true;\n")
			file.write("\t\t\tFPS.init(this);\n\n")
			
			file.write("\t\t\tstage.addEventListener(Event.ENTER_FRAME, onEnterFrame);\n")
			file.write("\t\t\tstage.addEventListener(Event.RESIZE, onResize);\n")
			file.write("\t\t}\n\n")
			
			file.write("\t\tprivate function onEnterFrame(e:Event):void {\n")
			file.write("\t\t\tscene.calculate();\n")
			file.write("\t\t}\n")
		elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3) or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
			# version 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0
			file.write("\t\tprivate var rootContainer:Object3DContainer = new Object3DContainer();\n")
			file.write("\t\tprivate var camera:Camera3D;\n")
			file.write("\t\tprivate var stage3D:Stage3D;\n\n")
			
			file.write("\t\tpublic function main() {\n\n")
			
			file.write("\t\t\tstage.align = StageAlign.TOP_LEFT;\n")
			file.write("\t\t\tstage.scaleMode = StageScaleMode.NO_SCALE;\n\n")
			
			file.write("\t\t\tcamera = new Camera3D(0.1, 10000);\n")
			file.write("\t\t\tcamera.view = new View(stage.stageWidth, stage.stageHeight);\n")
			file.write("\t\t\taddChild(camera.view);\n")
			file.write("\t\t\taddChild(camera.diagram);\n")
			file.write("\t\t\trootContainer.addChild(camera);\n\n")		
			
			for i, obj in enumerate(objs):
				file.write("\t\t\tobj"+str(i)+" = new "+cleanupString(obj.data.name)+"();\n")
				file.write("\t\t\trootContainer.addChild(obj"+str(i)+");\n")
			file.write("\n")
			
			file.write("\t\t\tstage.addEventListener(Event.ENTER_FRAME, onEnterFrame);\n")
			file.write("\t\t}\n\n")
			
			file.write("\t\tprivate function onEnterFrame(e:Event):void {\n")
			file.write("\t\t\tcamera.view.width = stage.stageWidth;\n")
			file.write("\t\t\tcamera.view.height = stage.stageHeight;\n")		
			file.write("\t\t\tcamera.render();\n")
			file.write("\t\t}\n")
		elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
			# version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
			file.write("\t\tprivate var rootContainer:Object3D = new Object3D();\n")
			file.write("\t\tprivate var camera:Camera3D;\n")
			file.write("\t\tprivate var stage3D:Stage3D;\n\n")
			
			file.write("\t\tpublic function main() {\n\n")
			
			file.write("\t\t\tstage.align = StageAlign.TOP_LEFT;\n")
			file.write("\t\t\tstage.scaleMode = StageScaleMode.NO_SCALE;\n\n")
			
			file.write("\t\t\tcamera = new Camera3D(0.1, 10000);\n")
			file.write("\t\t\tcamera.view = new View(stage.stageWidth, stage.stageHeight);\n")
			file.write("\t\t\taddChild(camera.view);\n")
			file.write("\t\t\taddChild(camera.diagram);\n")
			file.write("\t\t\trootContainer.addChild(camera);\n\n")		
			
			for i, obj in enumerate(objs):
				file.write("\t\t\tobj"+str(i)+" = new "+cleanupString(obj.data.name)+"();\n")
				file.write("\t\t\trootContainer.addChild(obj"+str(i)+");\n")
			file.write("\n")
			
			file.write("\t\t\tstage3D = stage.stage3Ds[0];\n")
			file.write("\t\t\tstage3D.addEventListener(Event.CONTEXT3D_CREATE, onContextCreate);\n")
			file.write("\t\t\tstage3D.requestContext3D();\n\n")
			
			file.write("\t\t}\n\n")
			
			file.write("\t\tprivate function onContextCreate(e:Event):void {\n")
			file.write("\t\t\tfor each (var resource:Resource in rootContainer.getResources(true)) {\n")
			file.write("\t\t\t\tresource.upload(stage3D.context3D);\n")
			file.write("\t\t\t}\n")
			file.write("\t\t\tstage.addEventListener(Event.ENTER_FRAME, onEnterFrame);\n")
			file.write("\t\t}\n\n")
			
			file.write("\t\tprivate function onEnterFrame(e:Event):void {\n")
			file.write("\t\t\tcamera.view.width = stage.stageWidth;\n")
			file.write("\t\t\tcamera.view.height = stage.stageHeight;\n")		
			file.write("\t\t\tcamera.render(stage3D);\n")
			file.write("\t\t}\n")
		else:
			print("version not found")
		
		file.write("\t}\n")
		WritePackageEnd(file)
		
		file.close()

#==================================
# A3D EXPORTER
#==================================

#Container for the exporter settings
class A3DExporterSettings:
	def __init__(self,A3DVersionSystem=4,ExportMode=1,CompressData=1,ExportAnim=0,ExportUV=1,ExportNormals=1,ExportTangents=1):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.ExportMode = int(ExportMode)
		self.CompressData = int(CompressData)
		self.ExportAnim = int(ExportAnim)
		self.ExportUV = int(ExportUV)
		self.ExportNormals = int(ExportNormals)
		self.ExportTangents = int(ExportTangents)
		
class A3DExporter(bpy.types.Operator):
	bl_idname = "ops.a3dexporter"
	bl_label = "Export to A3D (Alternativa)"
	bl_description = "Export to A3D (Alternativa)"
	
	A3DVersions = []
	A3DVersions.append(("1", "2.6", ""))
	A3DVersions.append(("2", "2.5", ""))
	A3DVersions.append(("3", "2.4", ""))
	A3DVersions.append(("4", "2.0", ""))
	A3DVersions.append(("5", "1.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D .A3D to export to", items=A3DVersions, default="4")
	
	ExportModes = []
	ExportModes.append(("1", "Selected Objects", ""))
	ExportModes.append(("2", "All Objects", ""))
	ExportMode = EnumProperty(name="Export", description="Select which objects to export", items=ExportModes, default="1")
	
	CompressData = BoolProperty(name="Compress Data", description="Zlib Compress data as per .a3d spec", default=True)
	
	#ExportAnim = BoolProperty(name="Animation", description="Animation", default=False)
	ExportUV = BoolProperty(name="Include UVs", description="Normals", default=True)
	ExportNormals = BoolProperty(name="Include Normals", description="Normals", default=True)
	ExportTangents = BoolProperty(name="Include Tangents", description="Tangents", default=True)
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		if not filePath.lower().endswith('.a3d'):
			filePath += '.a3d'
		try:
			print('Output file : %s' %filePath)
			file = open(filePath, 'wb')
			file.close()
			file = open(filePath, 'ab')
			Config = A3DExporterSettings(A3DVersionSystem=self.A3DVersionSystem,ExportMode=self.ExportMode,CompressData=self.CompressData,ExportAnim=False,ExportUV=self.ExportUV,ExportNormals=self.ExportNormals,ExportTangents=self.ExportTangents)
			a3dexport(file,Config)
			
			file.close()
		except Exception as e:
			print(e)
			file.close()
		return {'FINISHED'}
	def invoke (self, context, event):		
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}

def a3dexport(file,Config):
	print('Export to Alternativa3d binary started...\n')
			
	if Config.ExportMode == 1:
		#export selected only
		objs = [obj for obj in bpy.context.selected_objects]
		print('Export selection only...\n')
	else:
		#export whole scene
		objs = [obj for obj in bpy.data.objects]		
		print('Export scene...\n')
	
	objs_mesh = []
	objs_arm = []
	objs_lights = []
	objs_cameras = []
	
	for obj in objs:
		if obj.type == 'MESH':
			objs_mesh.append(obj)
		if obj.type == 'ARMATURE':
			objs_arm.append(obj)
		if obj.type == 'LAMP':
			objs_lights.append(obj)
		if obj.type == 'CAMERA':
			objs_cameras.append(obj)
	
	
	ambientLights = []
	animationClips = []
	animationTracks = []
	boxes = []
	cubeMaps = []
	decals = []
	directionalLights = []
	images = []
	indexBuffers = []
	joints = []
	maps = []
	materials = []
	meshes = []
	surfaces = []
	objects = []
	omniLights = []
	spotLights = []
	sprites = []
	skins = []
	vertexBuffers = []
	layers = []
	cameras = []
	lods = []
	
	
	if len(objs_lights) > 0:
		print("Exporting lights...\n")
		#loop over every light
		for obj in objs_lights:
			light = obj.data
			
			#name
			a3dstr = A3D2String()
			a3dstr.name = cleanupString(light.name)
			
			#create transform/matrix
			a3dtrans = A3D2Transform(Config)
			trns = getObjTransform(obj)
			a3dtrans._matrix.a = trns[0]
			a3dtrans._matrix.b = trns[1]
			a3dtrans._matrix.c = trns[2]
			a3dtrans._matrix.d = trns[3]
			a3dtrans._matrix.e = trns[4]
			a3dtrans._matrix.f = trns[5]
			a3dtrans._matrix.g = trns[6]
			a3dtrans._matrix.h = trns[7]
			a3dtrans._matrix.i = trns[8]
			a3dtrans._matrix.j = trns[9]
			a3dtrans._matrix.k = trns[10]
			a3dtrans._matrix.l = trns[11]
			
			a3dbox = A3D2Box(Config)
			a3dbox._box = getBoundBox(obj)
			a3dbox._id = len(boxes)
			
				
			if light.type == 'HEMI':
				#ambientlight
				print("ambientlight")
				
				boxes.append(a3dbox)
				
				a3damb = A3D2AmbientLight(Config)
				a3damb._boundBoxId = a3dbox._id
				a3damb._color = int(rgb2hex(light.color), 0)
				a3damb._id = len(ambientLights)
				a3damb._intensity = int(light.energy)
				a3damb._name = a3dstr
				#a3damb._parentId = None
				a3damb._transform = a3dtrans
				a3damb._visible = 1
				
				ambientLights.append(a3damb)
			elif light.type == 'POINT':
				#omniLights
				print("omniLight")
				
				boxes.append(a3dbox)
				
				a3domn = A3D2OmniLight(Config)
				a3domn._attenuationBegin = 0
				a3domn._attenuationEnd = 0
				a3domn._boundBoxId = a3dbox._id
				a3domn._color = int(rgb2hex(light.color), 0)
				a3domn._id = len(directionalLights)
				a3domn._intensity = int(light.energy)
				a3domn._name = a3dstr
				#a3domn._parentId = None
				a3domn._transform = a3dtrans
				a3domn._visible = 1
				
				omniLights.append(a3domn)
			elif light.type == 'SPOT':
				print("spotlight")
				#spotLights
				
				boxes.append(a3dbox)
				
				a3dspot = A3D2SpotLight(Config)
				a3dspot._attenuationBegin = 0
				a3dspot._attenuationEnd = 0
				a3dspot._boundBoxId = a3dbox._id
				a3dspot._color = int(rgb2hex(light.color), 0)
				#a3dspot._falloff = None
				#a3dspot._hotspot = None
				a3dspot._id = len(spotLights)
				a3dspot._intensity = int(light.energy)
				a3dspot._name = a3dstr
				#a3dspot._parentId = None
				a3dspot._transform = a3dtrans
				a3dspot._visible = 1
				
				#skip spotlights for now because seems to cause problem
				#spotLights.append(a3dspot)
			elif light.type == 'AREA':
				#directionalLights
				print("directional")
				boxes.append(a3dbox)

				a3ddir = A3D2DirectionalLight(Config)
				a3ddir._boundBoxId = a3dbox._id
				a3ddir._color = int(rgb2hex(light.color), 0)
				a3ddir._id = len(directionalLights)
				a3ddir._intensity = int(light.energy)
				a3ddir._name = a3dstr
				#a3ddir._parentId = None
				a3ddir._transform = a3dtrans
				a3ddir._visible = 1
				
				directionalLights.append(a3ddir)
			else:
				print("light type not supported")
	
	if len(objs_arm) > 0:
		print("Exporting rigging/animations...\n")
		for obj in objs_arm:
			arm = obj.data
			bones = arm.bones
			
			bonedict = {}
			
			#taken from .x exporter
			ParentList = [Bone for Bone in arm.bones if Bone.parent is None]
			PoseBones = obj.pose.bones
			
			for Bone in ParentList:
			
				bonedict[Bone] = len(joints)
			
				a3dstr = A3D2String()
				a3dstr.name = Bone.name
				
				a3djnt = A3D2Joint(Config)
				a3djnt._id = len(joints)
				a3djnt._name = a3dstr
				a3djnt._visible = 1

				PoseBone = PoseBones[Bone.name]
				if Bone.parent:
					jnt._parentId = bonedict[Bone.parent]
					BoneMatrix = PoseBone.parent.matrix.inverted()
				else:
					BoneMatrix = mathutils.Matrix()
				BoneMatrix *= PoseBone.matrix
				
				#a3djnt._transform = [BoneMatrix[0][0],BoneMatrix[0][1],BoneMatrix[0][2],BoneMatrix[1][0],BoneMatrix[1][1],BoneMatrix[1][2],BoneMatrix[2][0],BoneMatrix[2][1],BoneMatrix[2][2],BoneMatrix[3][0],BoneMatrix[3][1],BoneMatrix[3][2]]
				joints.append(a3djnt)
				
				#now do same as above for bone children
				#Bone.children
			
			#print(arm.name)
			#for b in bones:
				
			#	a3dstr = A3D2String()
			#	a3dstr.name = b.name
			
			#	jnt = A3D2Joint(Config)
				#jnt._boundBoxId = a3dbox
			#	jnt._id = len(joints)
			#	jnt._name = a3dstr
				#jnt._parentId = None
				#jnt._transform = getObjTransform(b)
			#	jnt._visible = 1
			#	joints.append(jnt)
				#print(b.name) #name bone
				#print(b.head_local) #vector xyz - head_radius
				#print(b.tail_local) #vector xyz - tail_radius
				#print(b.matrix_local) #matrix

	if len(objs_mesh) > 0:
		print("Exporting meshes...\n")
		#loop over every mesh and populate data
		for obj in objs_mesh:
			#convert to triangles
			ConvertQuadsToTris(obj)
		
			#data
			mesh = obj.data
			
			#get raw geometry data
			vs,uvt,ins,nr,tan,bb,trns = getCommonData(obj)
			#get surface data
			start,end,mts,mats = collectSurfaces(mesh)
					
			#create mesh boundbox
			a3dbox = A3D2Box(Config)
			a3dbox._box = bb
			a3dbox._id = len(boxes)
			boxes.append(a3dbox)
			
			#create indexbuffer
			a3dibuf = A3D2IndexBuffer(Config)
			for x in range(len(ins)):
				a3dibuf._byteBuffer.append(ins[x])
			a3dibuf._id = len(indexBuffers)
			a3dibuf._indexCount = len(a3dibuf._byteBuffer)
			indexBuffers.append(a3dibuf)
			
			#notes to self -taken from obj exporter
			#for mtex in reversed(mat.texture_slots):
			#        if mtex and mtex.texture.type == 'IMAGE':
			#            image = mtex.texture.image
			#            if image:
			# texface overrides others
			#if mtex.use_map_color_diffuse and face_img is None:
			#	image_map["map_Kd"] = image
			#if mtex.use_map_ambient:
			#	image_map["map_Ka"] = image
			#if mtex.use_map_specular:
			#	image_map["map_Ks"] = image
			#if mtex.use_map_alpha:
			#	image_map["map_d"] = image
			#if mtex.use_map_translucency:
			#	image_map["map_Tr"] = image
			#if mtex.use_map_normal:
			#	image_map["map_Bump"] = image
			#if mtex.use_map_hardness:
			#	image_map["map_Ns"] = image
			
			mesh_surfaces = []
			
			# NOTE TO SELF
			# Each Surface has a material/blender material
			# a material can then have the various textures diffuse, spec, norm etc
			
			
			#set surfaces
			if len(mts) > 0:
				for x in range(len(mts)):
					print("mts[x]="+str(mts[x]))
					print("mat="+str(GetMaterialTexture(mats[x])))
					
					matname = GetMaterialTexture(mats[x])
					if matname is not None:
						#create images
						a3dstr = A3D2String()
						a3dstr.name = matname
						a3dimg = A3D2Image(Config)
						a3dimg._id = len(images)
						a3dimg._url = a3dstr
						images.append(a3dimg)
						#create maps
						a3dmap = A3D2Map(Config)
						a3dmap._channel = 0
						a3dmap._id = len(maps)
						a3dmap._imageId = a3dimg._id
						maps.append(a3dmap)
					
					#create material
					a3dmat = A3D2Material(Config)
					if matname is not None:
						a3dmat._diffuseMapId = a3dmap._id
					else:
						a3dmat._diffuseMapId = int("ffffffff",16)
					a3dmat._glossinessMapId = int("ffffffff",16)
					a3dmat._id = len(materials)
					a3dmat._lightMapId = int("ffffffff",16)
					a3dmat._normalMapId = int("ffffffff",16)
					a3dmat._opacityMapId = int("ffffffff",16)
					a3dmat._reflectionCubeMapId = int("ffffffff",16)
					a3dmat._specularMapId = int("ffffffff",16)
					materials.append(a3dmat)
					
					#create surface
					a3dsurf = A3D2Surface(Config)
					a3dsurf._indexBegin = int(start[x])
					#a3dsurf._materialId = int("ffffffff",16)
					a3dsurf._materialId = a3dmat._id
					a3dsurf._numTriangles = int(end[x])
					mesh_surfaces.append(a3dsurf)
			else:
				#surface for all faces
				a3dsurf = A3D2Surface(Config)
				a3dsurf._indexBegin = 0
				#a3dsurf._materialId = int("ffffffff",16)
				#a3dsurf._materialId = 0
				a3dsurf._numTriangles = int(len(ins)/3)
				mesh_surfaces.append(a3dsurf)
			
			#create transform/matrix
			a3dtrans = A3D2Transform(Config)
			a3dtrans._matrix.a = trns[0]
			a3dtrans._matrix.b = trns[1]
			a3dtrans._matrix.c = trns[2]
			a3dtrans._matrix.d = trns[3]
			a3dtrans._matrix.e = trns[4]
			a3dtrans._matrix.f = trns[5]
			a3dtrans._matrix.g = trns[6]
			a3dtrans._matrix.h = trns[7]
			a3dtrans._matrix.i = trns[8]
			a3dtrans._matrix.j = trns[9]
			a3dtrans._matrix.k = trns[10]
			a3dtrans._matrix.l = trns[11]
			
			#name
			a3dstr = A3D2String()
			a3dstr.name = cleanupString(obj.data.name)
			
			#create mesh
			a3dmesh = A3D2Mesh(Config)
			#a3dmesh._boundBoxId = 0
			a3dmesh._id = len(meshes)
			a3dmesh._indexBufferId = a3dibuf._id
			a3dmesh._name = a3dstr
			#a3dmesh._parentId = 0
			a3dmesh._surfaces = mesh_surfaces
			a3dmesh._transform = a3dtrans
			a3dmesh._vertexBuffers = [len(vertexBuffers)] #vertex buffer ids
			a3dmesh._visible = 1
			if obj.hide == True:
				a3dmesh._visible = 0
			else:
				a3dmesh._visible = 1
			meshes.append(a3dmesh)
			
			a3dstr2 = A3D2String()
			a3dstr2.name = ""
			
			a3dobj = A3D2Object(Config)
			a3dobj._boundBoxId = 0
			a3dobj._id = len(objects)
			a3dobj._name = a3dstr2
			a3dobj._parentId = 0
			a3dobj._transform = a3dtrans
			if obj.hide == True:
				a3dobj._visible = 1
			else:
				a3dobj._visible = 0
			#objects.append(a3dobj)
			
			#create vertexbuffer
			a3dvbuf = A3D2VertexBuffer(Config)
			#POSITION = 0, NORMAL = 1, TANGENT4 = 2, JOINT = 3,TEXCOORD = 4
			attar = []
			if len(vs) > 0:
				attar.append(0)
			if (len(uvt) > 0) and (Config.ExportUV == 1):
				attar.append(4)
			if (len(nr) > 0) and (Config.ExportNormals == 1):
				attar.append(1)
			if (len(tan) > 0) and (Config.ExportTangents == 1):
				attar.append(2)
			#if len(jnt) > 0:
			#	attar.append(3)
			
			a3dvbuf._attributes = attar
			j=0
			for v in vs:
				if 0 in attar:
					a3dvbuf._byteBuffer.append(v[0]) #vert1
					a3dvbuf._byteBuffer.append(v[1]) #vert2
					a3dvbuf._byteBuffer.append(v[2]) #vert3
				if 4 in attar and (Config.ExportUV == 1):
					a3dvbuf._byteBuffer.append(uvt[j][0]) #uv
					a3dvbuf._byteBuffer.append(uvt[j][1]) #uv
				if 1 in attar and (Config.ExportNormals == 1):
					a3dvbuf._byteBuffer.append(nr[j][0]) #normal1
					a3dvbuf._byteBuffer.append(nr[j][1]) #normal2
					a3dvbuf._byteBuffer.append(nr[j][2]) #normal3
				if 2 in attar and (Config.ExportTangents == 1):
					a3dvbuf._byteBuffer.append(tan[j][0]) #tan1
					a3dvbuf._byteBuffer.append(tan[j][1]) #tan2
					a3dvbuf._byteBuffer.append(tan[j][2]) #tan3
					a3dvbuf._byteBuffer.append(-1) #tan4 - static input handedness
				j = j +1
			a3dvbuf._id = len(vertexBuffers)
			#a3dvbuf._vertexCount = int(len(ins))
			#a3dvbuf._vertexCount = int(len(vs) * 3) 
			a3dvbuf._vertexCount = int(len(vs)) #this works for cube
			#a3dvbuf._vertexCount = int(len(ins)) 
			#a3dvbuf._vertexCount = 24
			vertexBuffers.append(a3dvbuf)
			print("vs="+str(len(vs)))
		
	if Config.A3DVersionSystem <= 3:
		print("Exporting layers...\n")
			
	if Config.A3DVersionSystem <= 2:
		if len(objs_cameras) > 0:
			print("Exporting cameras...\n")
			for obj in objs_cameras:
				camera = obj.data
				
				#name
				a3dstr = A3D2String()
				a3dstr.name = cleanupString(camera.name)
				
				#create transform/matrix
				a3dtrans = A3D2Transform(Config)
				trns = getObjTransform(obj)
				a3dtrans._matrix.a = trns[0]
				a3dtrans._matrix.b = trns[1]
				a3dtrans._matrix.c = trns[2]
				a3dtrans._matrix.d = trns[3]
				a3dtrans._matrix.e = trns[4]
				a3dtrans._matrix.f = trns[5]
				a3dtrans._matrix.g = trns[6]
				a3dtrans._matrix.h = trns[7]
				a3dtrans._matrix.i = trns[8]
				a3dtrans._matrix.j = trns[9]
				a3dtrans._matrix.k = trns[10]
				a3dtrans._matrix.l = trns[11]
				
				a3dbox = A3D2Box(Config)
				a3dbox._box = getBoundBox(obj)
				a3dbox._id = len(boxes)
				
				camtype = False
				if camera.type == "PERSP":
					camtype = False
				else:
					camtype = True

				a3dcam = A3D2Camera(Config)
				a3dcam._boundBoxId = a3dbox._id
				a3dcam._farClipping = camera.clip_end
				a3dcam._fov = camera.lens
				#a3dcam._fov = math.pi/2
				a3dcam._id = len(cameras)
				a3dcam._name = a3dstr
				a3dcam._nearClipping = camera.clip_start
				a3dcam._orthographic = camtype
				#a3dcam._parentId = None
				a3dcam._transform = a3dtrans
				if obj.hide == True:
					a3dcam._visible = 1
				else:
					a3dcam._visible = 0
				
				cameras.append(a3dcam)
		print("Exporting Lods...\n")
				
	# create a3d2 object from data
	a3d2 = A3D2(ambientLights,animationClips,animationTracks,boxes,cubeMaps,decals,directionalLights,images,indexBuffers,joints,maps,materials,meshes,objects,omniLights,spotLights,sprites,skins,vertexBuffers,layers,cameras,lods,Config)
	
	# save to file
	a3d2.write(file)
	
	print('Export Completed...\n')

#==================================
# A3D IMPORTER
#==================================

#Container for the importer settings
class A3DImporterSettings:
	def __init__(self,FilePath="",ApplyTransforms=True):
		self.FilePath = str(FilePath)
		self.ApplyTransforms = int(ApplyTransforms)
		
class A3DImporter(bpy.types.Operator):
	bl_idname = "ops.a3dimporter"
	bl_label = "Import A3D (Alternativa)"
	bl_description = "Import A3D (Alternativa)"
	
	ApplyTransforms = BoolProperty(name="Apply Transforms", description="Apply transforms to objects", default=True)
	
	filepath= StringProperty(name="File Path", description="Filepath used for importing the A3D file", maxlen=1024, default="")

	def execute(self, context):
		# open a3d file
		file = open(self.filepath,'rb')
		file.seek(0)
		version = ord(file.read(1))
		Config = A3DImporterSettings(FilePath=self.filepath,ApplyTransforms=self.ApplyTransforms)
		if version == 0:
			loadA3d1(file,Config)
		else:
			loadA3d2(file,Config)
		file.close()
		return {'FINISHED'}
	def invoke (self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}	
	
def loadA3d1(file,Config):	
	file.seek(4)
	
	# read null mask
	a3dnull = A3D2Null(Config)
	a3dnull.read(file)
	print(a3dnull._mask)
	print(a3dnull._byte_list)
	
	print('A3D Version %i.%i' %(1,0))
	
	a3d = A3D(file)
	a3d.read(file,a3dnull._mask)
	
	file.close()
	
	a3d2 = a3d.convert1_2()
	
	a3d2.render()
	
	#after render unset data
	a3dnull.reset()
	a3d2.reset()
	
	return {'FINISHED'}

def loadA3d2(file,Config):	
	#rewind
	file.seek(0)
	
	# read package length
	a3dpackage = A3D2Package(Config)
	a3dpackage.read(file)
	
	#set current position
	curpos = file.tell()
	
	if a3dpackage._packed == 1:
		#decompress into variable
		data = file.read(a3dpackage._length)
		data = zlib.decompress(data)
		file.close()
		
		#file = open("C:/Users/David/Desktop/defaultModel_21-11-2011_13-47-51/model/box-extract.bin","wb")
		#file = open("C:/www/a3dtesting/cone-extract.bin","wb")
		#file.write(data)
		#file.close()
		
		#file1 = open("tempextract.bin",'wb')
		#file1.write(data)
		#file1.close()
		
		#file = open("tempextract.bin",'rb')
		#file.seek(curpos)
		file = tempfile.TemporaryFile()
		file.write(data)
		file.seek(0)
		
	# read null mask
	a3dnull = A3D2Null(Config)
	a3dnull.read(file)
	print(a3dnull._mask)
	print(a3dnull._byte_list)
	
	ver = A3DVersion(Config)
	ver.read(file)
	print('A3D Version %i.%i' %(ver.baseversion,ver.pointversion))
	
	#setup config version to match export
	# set default to 2.0
	Config.A3DVersionSystem = "4"
	if ver.baseversion == 1:
		#1.0
		Config.A3DVersionSystem="5"
	elif ver.baseversion == 2:
		if ver.pointversion == 0:
			#2.0
			Config.A3DVersionSystem="4"
		elif ver.pointversion == 4:
			#2.4
			Config.A3DVersionSystem="3"
		elif ver.pointversion == 5:
			#2.5
			Config.A3DVersionSystem="2"
		elif ver.pointversion == 6:
			#2.5
			Config.A3DVersionSystem="1"
	
	#read data
	#a3d2 = A3D2([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],Config)
	a3d2 = A3D2()
	a3d2.setConfig(Config)
	#a3d2 = A3D2(file)
	a3d2.read(file,a3dnull._mask,ver)
	
	file.close()
	
	#render loaded content to blender	
	a3d2.render()
	
	#after render unset data
	a3dpackage.reset()
	a3dnull.reset()
	ver.reset()
	a3d2.reset()
	
	return {'FINISHED'}

#==================================
# A3D SHARED
#==================================

#notes to self
#setting parents
#obj.parent = None # to remove parent
#obj.parent = obj # to set parent
# also obj.children returns all childs (bpy.data.objects['Cone'],)

#==================================
# A3D1
#==================================

class A3DNull:
	def __init__(self,Config):
		self._byte_list = []
		self._mask = ""
		self.Config = Config
		
	def reset(self):
		self._byte_list = []
		self._mask = ""
		
	def read(self,file):
		print("coming soon")
		
class A3D:
	def __init__(self,boxes=[],geometries=[],images=[],maps=[],materials=[],objects=[],Config=None):
		self.boxes = boxes
		self.geometries = geometries
		self.images = images
		self.maps = maps
		self.materials = materials
		self.objects = objects
		self.nullmask = ""
		self.Config = Config
	
	def reset(self):
		self.boxes = []
		self.geometries = []
		self.images = []
		self.maps = []
		self.materials = []
		self.objects = []
		self.nullmask = ""
		#self.Config = None
		
	def convert1_2(self):
		print("convert1_2")		
				
		a3d2boxes = []
		a3d2images = []
		a3d2indexBuffers = []
		a3d2maps = []
		a3d2materials = []
		a3d2meshes = []
		a3d2objects = []
		a3d2vertexBuffers = []
		
		#index geometries
		geoindex = {}
		
		if len(self.geometries) > 0:
			for x in range(len(self.geometries)):
				geoindex[self.geometries[x]._id] = self.geometries[x]
		
		
		if len(self.boxes) > 0:
			for x in range(len(self.boxes)):
				a3dbox = A3D2Box(self.Config)
				a3dbox._box = self.boxes[x]._box
				a3dbox._id = len(a3d2boxes)
				a3d2boxes.append(a3dbox)
				
		if len(self.images) > 0:
			for x in range(len(self.images)):
				a3dimg = A3D2Image(self.Config)
				a3dimg._id = len(a3d2images)
				a3dimg._url = self.images[x]._url
				a3d2images.append(a3dimg)
				
		if len(self.maps) > 0:
			for x in range(len(self.maps)):
				a3dmap = A3D2Map(self.Config)
				a3dmap._channel = self.maps[x]._channel
				a3dmap._id = len(a3d2maps)
				a3dmap._imageId = self.maps[x]._imageId
				a3d2maps.append(a3dmap)
				
		if len(self.materials) > 0:
			for x in range(len(self.materials)):
				a3dmat = A3D2Material(self.Config)
				a3dmat._diffuseMapId = self.materials[x]._diffuseMapId
				a3dmat._glossinessMapId = self.materials[x]._glossinessMapId
				a3dmat._id = len(a3d2materials)
				a3dmat._lightMapId = self.materials[x]._lightMapId
				a3dmat._normalMapId = self.materials[x]._normalMapId
				a3dmat._opacityMapId = self.materials[x]._opacityMapId
				a3dmat._specularMapId = self.materials[x]._specularMapId
				a3d2materials.append(a3dmat)

		if len(self.objects) > 0:
			for x in range(len(self.objects)):
			
				#get geometry
				geom = geoindex[self.objects[x]._geometryId]
				
				#create indexbuffer
				a3dibuf = A3D2IndexBuffer(self.Config)
				for x in range(len(geom._indexBuffer._byteBuffer)):
					a3dibuf._byteBuffer.append(geom._indexBuffer._byteBuffer[x])
				a3dibuf._id = len(a3d2indexBuffers)
				a3dibuf._indexCount = len(a3dibuf._byteBuffer)
				a3d2indexBuffers.append(a3dibuf)
				
				#create vertexbuffers
				vbuffers = []
				for x in range(len(geom._vertexBuffers)):
					a3dvbuf = A3D2VertexBuffer(self.Config)
					attar = []
					for j in range(len(geom._vertexBuffers[x]._attributes)):
						if geom._vertexBuffers[x]._attributes[j] == 0:
							#position
							attar.append(0)
							print("position")
						if geom._vertexBuffers[x]._attributes[j] == 1:
							#normal
							attar.append(1)
							print("normal")
						if geom._vertexBuffers[x]._attributes[j] == 2:
							#tangent
							attar.append(2)
							print("tangent")
						if geom._vertexBuffers[x]._attributes[j] == 3:
							#binormal
							attar.append(1)
							print("binormal")
						if geom._vertexBuffers[x]._attributes[j] == 4:
							#color
							#attar.append(1)
							print("color")
						if geom._vertexBuffers[x]._attributes[j] == 5:
							#texcoords
							attar.append(4)
							print("texcoords")
						if geom._vertexBuffers[x]._attributes[j] == 6:
							#user def
							#attar.append(1)
							print("user def")
					
					c = 0
					for k in range(len(geom._vertexBuffers[x]._byteBuffer)):
						if c >= len(geom._vertexBuffers[x]._byteBuffer):
							break
						if 0 in attar:
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c]) #vert1
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+1]) #vert2
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+2]) #vert3
							c = c+3
						if 1 in attar:
							c = c+3
						if 2 in attar:
							c = c+4
						if 3 in attar:
							c = c+4
						if 4 in attar:
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+1])
							c = c+2
							
					a3dvbuf._attributes = attar
					a3dvbuf._id = len(a3d2vertexBuffers)
					a3dvbuf._vertexCount = geom._vertexBuffers[x]._vertexCount
					a3d2vertexBuffers.append(a3dvbuf)
					vbuffers.append(a3dvbuf._id)
				
				#create mesh from data
				a3dmesh = A3D2Mesh(self.Config)
				a3dmesh._boundBoxId = self.objects[x]._boundBoxId
				a3dmesh._id = len(a3d2meshes)
				a3dmesh._indexBufferId = a3dibuf._id
				a3dmesh._name = self.objects[x]._name
				a3dmesh._parentId = self.objects[x]._parentId
				a3dmesh._surfaces = self.objects[x]._surfaces
				a3dmesh._transform = None
				a3dmesh._vertexBuffers = vbuffers
				a3dmesh._visible = self.objects[x]._visible
				a3d2meshes.append(a3dmesh)
				
		a3d2 = A3D2([],[],[],a3d2boxes,[],[],[],a3d2images,a3d2indexBuffers,[],a3d2maps,a3d2materials,a3d2meshes,a3d2objects,[],[],[],[],a3d2vertexBuffers,[],[],[],self.Config)
				
		return a3d2
	
	def render(self):
		print("render")
	
	def read(self,file,mask):
		print("reada3d")
		
		self.reset()
		
		# define arrays
		arrs = {
			0: self.boxes,
			1: self.geometries,
			2: self.images,
			3: self.maps,
			4: self.materials,
			5: self.objects
		}
		
		# define classes
		funcs = {
			0: A3DBox, 
			1: A3DGeometry,
			2: A3DImage,
			3: A3DMap,
			4: A3DMaterial,
			5: A3DObject
		}
		
		#reverse nullmask
		#mask = mask[::-1]
		#reverse dicts
		#revkeys = sorted(funcs.keys(), reverse=True)
		#nfuncs = {}
		#i=0
		#for k in revkeys:
		#	nfuncs[i] = funcs[k]
		#	i = i +1
		#funcs = nfuncs
		
		#revkeys = sorted(arrs.keys(), reverse=True)
		#narrs = {}
		#i=0
		#for k in revkeys:
		#	narrs[i] = arrs[k]
		#	i = i +1
		#arrs = narrs
		
		#test
		# remove some bits
		mask = mask[16:]
		print(mask)
		print(str(len(mask)))
		
		
		#counter that just deals with the func keys
		findex = 0
		#mask counter that increments with the options of class
		mskindex = 0
		for i in range(len(mask)):
			#exit if we gone past amount
			if i >= len(funcs):
				break
			#print(mask[mskindex])
			if mask[mskindex] == "0":
				#read array of classes
				arr = A3D2Array()
				arr.read(file)
				mskindex = mskindex + 1
				for a in range(arr.length):
					cla = funcs[findex](self.Config)
					cla.read(file,mask,mskindex)
					arrs[findex].append(cla)
					mskindex = mskindex + cla._mskindex
			else:
				mskindex = mskindex + 1
			findex = findex + 1
		
class A3DBox:
	def __init__(self,Config):
		self._box = []
		self._id = 0

		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._box = []
		self._id = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DBox - "+str(mask[mskindex]))
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			self._box.append( struct.unpack(">f",file.read(struct.calcsize(">f")))[0] )
		
		self._id = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		
		print("box="+str(self._box))
		print("id="+str(self._id))
		
	def write(self,file):
		print("write boundbox\n")
		arr = A3D2Array()
		arr.write(file,len(self._box))
		for x in range(len(self._box)):
			file.write(struct.pack('>f',self._box[x]))
		#write id
		file.write(struct.pack('>L',self._id))	

class A3DGeometry:
	def __init__(self,Config):
		self._id = 0
		self._indexBuffer = 0
		self._vertexBuffers = []

		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._indexBuffer = 0
		self._vertexBuffers = []
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DGeometry - "+str(mask[mskindex]))
		
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
		ibuf = A3DIndexBuffer(self.Config)
		self._indexBuffer = ibuf.read(file,mask,mskindex + self._mskindex)
		#self._mskindex = self._mskindex + ibuf._mskindex
		
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			vbuf = A3DVertexBuffer(self.Config)
			self._vertexBuffers.append(vbuf.read(file,mask,mskindex + self._mskindex))
			#self._mskindex = self._mskindex + vbuf._mskindex
			
		print("id="+str(self._id))
					
	def write(self,file):
		print("write A3DGeometry")

class A3DImage:
	def __init__(self,Config):
		self._id = 0
		self._url = 0

		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._url = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DImage - "+str(mask[mskindex]))
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
		a3dstr = A3D2String()
		a3dstr.read(file)
		self._url = a3dstr.name
		
		print("id="+str(self._id))
		print("url="+str(self._url))
		
	def write(self,file):
		print("write A3DImage")
		
class A3DMap:
	def __init__(self,Config):
		self._channel = 0
		self._id = 0
		self._imageId = 0
		self._uOffset = 0
		self._uScale = 0
		self._vOffset = 0
		self._vScale = 0

		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._channel = 0
		self._id = 0
		self._imageId = 0
		self._uOffset = 0
		self._uScale = 0
		self._vOffset = 0
		self._vScale = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DMap - "+str(mask[mskindex]))
		self._channel = struct.unpack(">H", file.read(struct.calcsize(">H")))[0]
			
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
			
		self._imageId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]

		self._uOffset = struct.unpack(">f", file.read(struct.calcsize(">f")))[0]
		
		self._uScale = struct.unpack(">f", file.read(struct.calcsize(">f")))[0]
		
		self._vOffset = struct.unpack(">f", file.read(struct.calcsize(">f")))[0]

		self._vScale = struct.unpack(">f", file.read(struct.calcsize(">f")))[0]
		
		print("channel="+str(self._channel))
		print("id="+str(self._id))
		print("imageId="+str(self._imageId))
		print("uOffset="+str(self._uOffset))
		print("uScale="+str(self._uScale))
		print("vOffset="+str(self._vOffset))
		print("vScale="+str(self._vScale))
		
	def write(self,file):
		print("write A3DMap")
		
class A3DMaterial:
	def __init__(self,Config):
		self._diffuseMapId = None
		self._glossinessMapId = None
		self._id = 0
		self._lightMapId = None
		self._normalMapId = None
		self._opacityMapId = None
		self._specularMapId = None

		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._diffuseMapId = None
		self._glossinessMapId = None
		self._id = 0
		self._lightMapId = None
		self._normalMapId = None
		self._opacityMapId = None
		self._specularMapId = None
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3dMaterial - "+str(mask[mskindex]))
		if mask[mskindex + self._mskindex] == "0":
			self._diffuseMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":	
			self._glossinessMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":	
			self._id = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._lightMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._normalMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._opacityMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._specularMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		print("diffuseMapId="+str(self._diffuseMapId))
		print("glossinessMapId="+str(self._glossinessMapId))
		print("id="+str(self._id))
		print("lightMapId="+str(self._lightMapId))
		print("normalMapId="+str(self._normalMapId))
		print("opacityMapId="+str(self._opacityMapId))
		print("specularMapId="+str(self._specularMapId))
		
	def write(self,file):
		print("write A3dMaterial")

class A3DObject:
	def __init__(self,Config):
		self._boundBoxId = 0
		self._geometryId = 0
		self._id = 0
		self._name = 0
		self._parentId = 0
		self._surfaces = []
		self._transformation = 0
		self._visible = 0

		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = 0
		self._geometryId = 0
		self._id = 0
		self._name = 0
		self._parentId = 0
		self._surfaces = []
		self._transformation = 0
		self._visible = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DObject - "+str(mask[mskindex]))
		self._boundBoxId = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		self._geometryId = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		self._id = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		
		a3dstr = A3D2String()
		a3dstr.read(file)
		self._name = a3dstr.name
		
		self._parentId = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3DSurface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			#self._mskindex = self._mskindex + a3dsurf._mskindex
		
		a3dtran = A3D2Transform(self.Config)
		a3dtran.read(file)
		self._transformation = a3dtran
			
		print("boundBoxId="+str(self._boundBoxId))
		print("geometryId="+str(self._geometryId))
		print("id="+str(self._id))
		print("name="+self._name)
		print("parentId="+str(self._parentId))
		
	def write(self,file):
		print("write A3DObject")

class A3DIndexBuffer:
	def __init__(self,Config):
		self._byteBuffer = []
		self._indexCount = 0
		
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._byteBuffer = []
		self._indexCount = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DIndexBuffer - "+str(mask[mskindex]))
		arr = A3D2Array()
		arr.read(file)
		for a in range(int(arr.length/2)):
			self._byteBuffer.append( struct.unpack("<H",file.read(struct.calcsize("<H")))[0] )

		self._indexCount = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		
		return self
		
	def write(self,file):
		print("write A3DIndexBuffer")
		
class A3DVertexBuffer:
	def __init__(self,Config):
		self._attributes = []
		self._byteBuffer = []
		self._vertexCount = 0
		
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._attributes = []
		self._byteBuffer = []
		self._vertexCount = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DVertexBuffer - "+str(mask[mskindex]))
		
		arr = A3D2Array()
		arr.read(file)
		self._attributes = []
		for a in range(arr.length):
			self._attributes.append(struct.unpack("B",file.read(struct.calcsize("B")))[0])
	
		arr = A3D2Array()
		arr.read(file)
		for a in range(int(arr.length/4)):
			self._byteBuffer.append(struct.unpack("<f",file.read(struct.calcsize("<f")))[0])
		
		self._vertexCount  = struct.unpack(">H",file.read(struct.calcsize(">H")))[0]
		
		return self
		
	def write(self,file):
		print("write A3DVertexBuffer")
		
class A3DSurface:
	def __init__(self,Config):
		self._indexBegin = 0
		self._materialId = None
		self._numTriangles = 0
		
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._indexBegin = 0
		self._materialId = None
		self._numTriangles = 0
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DSurface - "+str(mask[mskindex]))
		self._indexBegin = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		if mask[mskindex + self._mskindex] == "0":
			self._materialId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		self._numTriangles = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		return self
		
	def write(self,file):
		print("write A3DSurface")
		
#==================================
# A3D2
#==================================

class A3D2Package:
	def __init__(self,Config):
		self._packed = 1
		self._length = 0
		self.Config = Config
	
	def reset(self):
		self._packed = 1
		self._length = 0
		
	def read(self,file):
		#read first byte
		temp_data = ord(file.read(1))
		
		#get byte as binary string
		temp_data = bin(temp_data)[2:].rjust(8, '0')
		
		#remaining 6bits
		#print(temp_data[2:7])
		
		#first bit
		if temp_data[0] == '0':
			temp = ord(file.read(1))
			temp = bin(temp)[2:].rjust(8, '0')
			plen = temp_data[2:8] + temp
			print('Package length %i bytes' % int(plen,2))
			self._length = int(plen,2)
			
			#second bit
			if temp_data[1] == '0':
				self._packed = 0
				print('Package not packed')
			elif temp_data[1] == '1':
				self._packed = 1
				print('Package is packed')
			else:
				print('Error reading package Z')
				
		elif temp_data[0] == '1':
			#read 3 bytes
			temp = ord(file.read(1))
			temp = bin(temp)[2:].rjust(8, '0')
			temp1 = ord(file.read(1))
			temp1 = bin(temp1)[2:].rjust(8, '0')
			temp2 = ord(file.read(1))
			temp2 = bin(temp2)[2:].rjust(8, '0')
			plen = temp_data[1:8] + temp + temp1 + temp2
			print('Package length of %i bytes' % int(plen,2))
			
			self._length = int(plen,2)
			
			# if first bit is one then its auto packed
			self._packed = 1
			print('Package is packed')
		else:
			print('Error reading package L')
	
	def write(self,file):
		print(self._length)
		bitnum = self._length.bit_length()
		if self._length <= 16383:
			#6bits + next 1 byte (14bits)
			print("Package 1 byte required\n")
			if self._packed == 1:
				data = 16384 + self._length
			else:
				data = self._length
			file.write(struct.pack(">H", data))
		elif bitnum > 6 and bitnum <= 31:
			#7bits + next 3 bytes (31bits)
			print("Package 3 byte required\n")
			print("length="+str(self._length))
			
			byte1 = int((self._length >> 24) & 255)
			byte1 = byte1 + 128
			byte2 = int((self._length >> 16) & 255)
			byte3 = int((self._length >> 8) & 255)
			byte4 = int(self._length & 255)
			file.write(struct.pack("B",byte1))
			file.write(struct.pack("B",byte2))
			file.write(struct.pack("B",byte3))
			file.write(struct.pack("B",byte4))
		else:
			print("package bytes too long!\n")

class A3D2Null:
	def __init__(self,Config):
		self._byte_list = []
		self._mask = ""
		self.Config = Config
	
	def reset(self):
		self._byte_list = []
		self._mask = ""
		
	def read(self,file):	
		#read first byte
		temp_data = ord(file.read(1))
		
		#get byte as binary string
		temp_data = bin(temp_data)[2:].rjust(8, '0')
		
		#first bit		
		if temp_data[0] == '0':
			#short null
			print('Short null-mask')
			if temp_data[1] == '0':
				if temp_data[2] == '0':
					#00
					nulldata = temp_data[3:8]
					#print('Null mask %s' % str(nulldata))
					print('(LL=00) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					#print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
					self._mask = nulldata
				elif temp_data[2] == '1':
					#01
					temp = ord(file.read(1))
					temp = bin(temp)[2:].rjust(8, '0')
					nulldata = temp_data[3:8] + temp
					#print('Null mask %s' % str(nulldata))
					print('(LL=01) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					#print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
					self._mask = nulldata
				else:
					print('Error reading short Null...')
			elif temp_data[1] == '1':
				if temp_data[2] == '0':
					#10
					temp = ord(file.read(1))
					temp = bin(temp)[2:].rjust(8, '0')
					temp1 = ord(file.read(1))
					temp1 = bin(temp1)[2:].rjust(8, '0')
					nulldata = temp_data[3:8] + temp + temp1
					#print('Null mask %s' % str(nulldata))
					print('(LL=10) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					#print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
					self._mask = nulldata
				elif temp_data[2] == '1':
					#11
					temp = ord(file.read(1))
					temp = bin(temp)[2:].rjust(8, '0')
					temp1 = ord(file.read(1))
					temp1 = bin(temp1)[2:].rjust(8, '0')
					temp2 = ord(file.read(1))
					temp2 = bin(temp2)[2:].rjust(8, '0')
					nulldata = temp_data[3:8] + temp + temp1 + temp2
					print('Null mask %s' % str(nulldata))
					print('(LL=11) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					#print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
					self._mask = nulldata
				else:
					print('Error reading short Null...')
			else:
				print('Error reading short Null..')
		else:
			#long null
			print('Long null-mask')
			#read L
			if temp_data[1] == '0':
				nulldata = temp_data[2:8]
				#print('Null mask %s' % str(nulldata))
				print('(L=0) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
				#print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
				#read bytes
				for x in range(int(nulldata,2)):
					byt = file.read(1)
					self._mask += '{0:08b}'.format(ord(byt))
					self._byte_list.append('%02X' % ord(byt))
			elif temp_data[1] == '1':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				temp1 = ord(file.read(1))
				temp1 = bin(temp1)[2:].rjust(8, '0')
				nulldata = temp_data[2:8] + temp + temp1
				#print('Null mask %s' % str(nulldata))
				print('(L=1) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
				#print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
				#read bytes
				for x in range(int(nulldata,2)):
					byt = file.read(1)
					self._mask += '{0:08b}'.format(ord(byt))
					self._byte_list.append('%02X' % ord(byt))
			else:
				print('Error reading long Null..')
	
	def write(self,file):
		print("nullmask")
		x=int(self._mask,2)
		#bits = x.bit_length()
		#use len because if starts with zero bit_length doesn't work
		bits = len(self._mask)
		print(str(bits)+" bits")
		print(str(x)+" int")
		if bits <= 5:
			print("5bits")
			
		elif bits > 5 and bits <= 13:
			print("5bits + 1 byte")
			
		elif bits > 13 and bits <= 21:
			print("5bits + 2 bytes")
			#mask1 = int("01011111",2) #8bit mask
			mask2 = int("000000001111111100000000",2) #24bit mask
			mask3 = int("000000000000000011111111",2) #24bit mask
			data = x >> 16 #get rid of bits except first 5 by shifting right 2 bytes
			byte1 = int(data + 64) # 64 = 01000000
			byte2 = int((x & mask2) >> 8)
			byte3 = int((x & mask3))
			print("byte1="+str(byte1))
			print("byte2="+str(byte2))
			print("byte3="+str(byte3))
			file.write(struct.pack("B",byte1))
			file.write(struct.pack("B",byte2))
			file.write(struct.pack("B",byte3))
		elif bits > 21 and bits <= 29:
			#if is 24 bits (fits exacty into 3 bytes) then place left to right
			if bits == 24:
				#place bits left to right
				data = x >> (bits - 5) #19 shr
				byte1 = int(data + 96) #96 = 01100000
				byte2 = int( x >> ((bits-5)-8) & 255 )
				byte3 = int( x >> ((bits-5)-16) & 255 )
				byte4 = int( x << 5 & 255 )
			else:
				#place bits right to left
				byte1 = int( (x >> 24) & 255 )
				byte1 = byte1 + 96 #01100000 
				byte2 = int( (x >> 16) & 255 )
				byte3 = int( (x >> 8) & 255 )
				byte4 = int( x & 255 )
			
			print("byte1="+str(byte1))
			print("byte2="+str(byte2))
			print("byte3="+str(byte3))
			print("byte4="+str(byte4))		
			file.write(struct.pack("B",byte1))
			file.write(struct.pack("B",byte2))
			file.write(struct.pack("B",byte3))
			file.write(struct.pack("B",byte4))
			print(struct.pack("B",byte1))
			print(struct.pack("B",byte2))
			print(struct.pack("B",byte3))
			print(struct.pack("B",byte4))
			print(bin(byte1), bin(byte2), bin(byte3), bin(byte4))
		else:
			if bits <= 504:
				print("long")
				
				rem = bits % 8
				if rem == 0:
					#if fits exactly in bytes
					bytenum = int(bits/8)
				else:
					#if doesn't fit exactly round up
					bytenum = int((bits+(8-rem))/8)
								
				#10000000 = 128
				#byte1 = 4 + 128 #4bytes + mask
				#print(byte1)
				#file.write(struct.pack("B",byte1))				
				#file.write(struct.pack(">L",x))
				#file.write(struct.pack(">L",int('1110111101100000000001101111110',2)))				

				tbits = int(bytenum * 8)
				rbits = int(tbits - bits)
				
				lenbyte = int(bytenum + 128)
				file.write(struct.pack("B",lenbyte))

				#if fits exactly
				if bits == bytenum*8:
					for j in range(bytenum):
						byte = int( ( x >> (tbits - (8 * (j+1))) ) & 255 )
						file.write(struct.pack("B",byte))
				else:
					for j in range(bytenum):
						shift = (tbits - (8 * (j+1)))-rbits
						print("shift:"+str(shift))
						#if last byte shift by remainder
						if j == (bytenum-1):
							byte = int( ( x << rbits ) & 255 )
						else:
							byte = int( ( x >> shift ) & 255 )
						file.write(struct.pack("B",byte))
						print(byte)
					#bitstoshift = (8 * (bytenum-(j+1))-rbits)
					#print(bitstoshift)
					#if last byte
					#if j == (bytenum-1):
					#	byte = int( (x << rbits) & 255 )
					#else:
					#	byte = int( (x >> bitstoshift) & (255) )
					#print(byte)
					#file.write(struct.pack("B",byte))
			else:
				if bits <= 33554432:
					print("even longer")
					#3 bytes space for length + nullmask

					rem = bits % 8
					if rem == 0:
						#if fits exactly in bytes
						bytenum = bits/8
					else:
						#if doesn't fit exactly round up
						bytenum = int((bits+(8-rem))/8)
						
					tbits = int(bytenum * 8)
					rbits = int(tbits - bits)
					
					print("bytenum="+str(bytenum))
					lenbyte = int(bytenum + 12582912) #11000000 00000000 00000000
					lenbits = lenbyte.bit_length()
					
					#place bits right to left
					byte1 = int( (lenbyte >> 16) & 255 )
					byte2 = int( (lenbyte >> 8) & 255 )
					byte3 = int( lenbyte & 255 )
					
					print("byte1="+str(byte1))
					print("byte2="+str(byte2))		
					print("byte3="+str(byte3))		
					file.write(struct.pack("B",byte1))
					file.write(struct.pack("B",byte2))
					file.write(struct.pack("B",byte3))
					
					#nullmask write now
					
					#if fits exactly
					if bits == bytenum*8:
						#left to right
						for j in range(bytenum):
							byte = int( ( x >> (tbits - (8 * (j+1))) ) & 255 )
							file.write(struct.pack("B",byte))
					else:
						#right to left
						for j in range(bytenum):
							shift = (tbits - (8 * (j+1)))-rbits
							#print("shift:"+str(shift))
							#if last byte shift by remainder
							if j == (bytenum-1):
								byte = int( ( x << rbits ) & 255 )
							else:
								byte = int( ( x >> shift ) & 255 )
							file.write(struct.pack("B",byte))
				else:
					print("NullMap overflow!")
					
class A3D2:
	def __init__(self,ambientLights=[],animationClips=[],animationTracks=[],boxes=[],cubeMaps=[],decals=[],directionalLights=[],images=[],indexBuffers=[],joints=[],maps=[],materials=[],meshes=[],objects=[],omniLights=[],spotLights=[],sprites=[],skins=[],vertexBuffers=[],layers=[],cameras=[],lods=[],Config=None):
		self.ambientLights = ambientLights
		self.animationClips = animationClips
		self.animationTracks = animationTracks
		self.boxes = boxes
		self.cubeMaps = cubeMaps
		self.decals = decals
		self.directionalLights = directionalLights
		self.images = images
		self.indexBuffers = indexBuffers
		self.joints = joints
		self.maps = maps
		self.materials = materials
		self.meshes = meshes
		self.objects = objects
		self.omniLights = omniLights
		self.spotLights = spotLights
		self.sprites = sprites
		self.skins = skins
		self.vertexBuffers = vertexBuffers
		self.layers = layers
		self.cameras = cameras
		self.lods = lods
		self.nullmask = ""
		self.Config = Config
	
	def	setConfig(self,Config):
		self.Config = Config
		
	def reset(self):
		self.ambientLights = []
		self.animationClips = []
		self.animationTracks = []
		self.boxes = []
		self.cubeMaps = []
		self.decals = []
		self.directionalLights = []
		self.images = []
		self.indexBuffers = []
		self.joints = []
		self.maps = []
		self.materials = []
		self.meshes = []
		self.objects = []
		self.omniLights = []
		self.spotLights = []
		self.sprites = []
		self.skins = []
		self.vertexBuffers = []
		self.layers = []
		self.cameras = []
		self.lods = []
		self.nullmask = ""
		#self.Config = None
		
	def render(self):	
		#create indexes for access
		ibuffers = {}
		for ib in self.indexBuffers:
			ibuffers[ib._id] = ib
			
		vbuffers = {}
		for vb in self.vertexBuffers:
			vbuffers[vb._id] = vb
			
		materials = {}
		for mat in self.materials:
			materials[mat._id] = mat
			
		maps = {}
		for map in self.maps:
			maps[map._id] = map
			
		images = {}
		for img in self.images:
			images[img._id] = img
			
		#render ambientlights
		for light in self.ambientLights:
		
			if light._name is not None:
				nme = light._name
			else:
				nme = "Lamp"
		
			lamp = bpy.data.lamps.new(nme,"HEMI") 
			ob = bpy.data.objects.new(nme, lamp)
			
			lamp.color = light._color
			lamp.energy = light._intensity

			if (light._transform is not None) and (self.Config.ApplyTransforms == True):
				ob.matrix_local = light._transform.getMatrix()
			else:
				# position object at 3d-cursor
				ob.location = bpy.context.scene.cursor_location
			bpy.context.scene.objects.link(ob)
			
			if light._visible == False:
				ob.hide = False
				
		#render directionallights
		for light in self.directionalLights:
		
			if light._name is not None:
				nme = light._name
			else:
				nme = "Lamp"
		
			lamp = bpy.data.lamps.new(nme,"AREA") 
			ob = bpy.data.objects.new(nme, lamp)
			
			lamp.color = light._color
			lamp.energy = light._intensity

			if (light._transform is not None) and (self.Config.ApplyTransforms == True):
				ob.matrix_local = light._transform.getMatrix()
			else:
				# position object at 3d-cursor
				ob.location = bpy.context.scene.cursor_location
			bpy.context.scene.objects.link(ob)
			
			if light._visible == False:
				ob.hide = False
		
		#render meshes
		for mesh in self.meshes:
		
			verts = []
			faces = []
			uvs = []
			norms = []
			tans = []
			joints = []
		
			#index buff
			ibuf = ibuffers[mesh._indexBufferId]
			i=0
			for x in range(int(len(ibuf._byteBuffer)/3)):
				temp = (ibuf._byteBuffer[i],ibuf._byteBuffer[i+1],ibuf._byteBuffer[i+2])
				faces.append(temp)
				i=i+3
			
			#vert buff
			for v in mesh._vertexBuffers:
				vbuf = vbuffers[v]
				print("Attributes:"+str(vbuf._attributes))
				numflts = 0
				for att in vbuf._attributes:
					if att == 0:
						#position
						numflts = numflts + 3
					if att == 1:
						#normal
						numflts = numflts + 3
					if att == 2:
						#tangent
						numflts = numflts + 4
					if att == 3:
						#joint
						numflts = numflts + 4
					if att == 4:
						#uv
						numflts = numflts + 2
				flcount = int(len(vbuf._byteBuffer))
				points = int(flcount/numflts)
				i = 0
				for p in range(points):
					for att in vbuf._attributes:
						if att == 0:
							x = vbuf._byteBuffer[i]
							i = i + 1
							y = vbuf._byteBuffer[i]
							i = i + 1
							z = vbuf._byteBuffer[i]
							i = i + 1
							verts.append((x, y, z))
						if att == 1:
							x = vbuf._byteBuffer[i]
							i = i + 1
							y = vbuf._byteBuffer[i]
							i = i + 1
							z = vbuf._byteBuffer[i]
							i = i + 1
							norms.append((x, y, z))
						if att == 2:
							a = vbuf._byteBuffer[i]
							i = i + 1
							b = vbuf._byteBuffer[i]
							i = i + 1
							c = vbuf._byteBuffer[i]
							i = i + 1
							d = vbuf._byteBuffer[i]
							i = i + 1
							tans.append((a,b,c,d))
						if att == 3:
							i = i + 1
							a = vbuf._byteBuffer[i]
							i = i + 1
							b = vbuf._byteBuffer[i]
							i = i + 1
							c = vbuf._byteBuffer[i]
							i = i + 1
							d = vbuf._byteBuffer[i]
							i = i + 1
							joints.append((a, b, c, d))
						if att == 4:
							uv1 = vbuf._byteBuffer[i]
							i = i + 1
							uv2 = vbuf._byteBuffer[i]
							uv2 = 1.0 - uv2
							i = i + 1
							uvs.append([uv1,uv2])
						
			#print(verts)
			#print(faces)
			#print(uvs)
			#print(mesh._name)
			
			if mesh._name is not None:
				nme = mesh._name
			else:
				nme = "Mesh"
			
			# create a new mesh  
			me = bpy.data.meshes.new(nme) 
			
			# create an object with that mesh
			ob = bpy.data.objects.new(nme, me)  
			
			if (mesh._transform is not None) and (self.Config.ApplyTransforms == True):
				ob.matrix_local = mesh._transform.getMatrix()
			else:
				# position object at 3d-cursor
				ob.location = bpy.context.scene.cursor_location
			
			# Link object to scene
			bpy.context.scene.objects.link(ob)  
			
			# Fill the mesh with verts, edges, faces 
			# from_pydata doesn't work correctly, it swaps vertices in some triangles 
			#me.from_pydata(verts,[],faces)   # edges or faces should be [], or you ask for problems
			
			me.vertices.add(len(verts))
			me.faces.add(len(faces))
			
			for i in range(len(verts)):
				me.vertices[i].co=verts[i]
				
			for i in range(len(faces)):
				me.faces[i].vertices=faces[i]
			
			#select object
			for object in bpy.data.objects:
				object.select = False
			ob.select = True
			bpy.context.scene.objects.active = ob
			
			#me.update(calc_edges=True)    # Update mesh with new data
			
			#add uv layer
			uvname = "UV1"
			uvlayer = me.uv_textures.new(uvname)
			diffuseimg = None
			
			if mesh._visible == False:
				ob.hide = True
			
			for surf in mesh._surfaces:
				#surf._indexBegin
				#surf._materialId
				#surf._numTriangles
				
				if surf._materialId is not None:
					#get material
					mat = materials[surf._materialId]
					
					#new material
					surf_mat = bpy.data.materials.new("Material")
					me.materials.append(surf_mat)
					
					if (mat._diffuseMapId is not None) and (mat._diffuseMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._diffuseMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("diffuse", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
						
						#set diffuse img for uv window
						diffuseimg = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
						mtex.uv_layer = uvname
						
					if (mat._glossinessMapId is not None) and (mat._glossinessMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._glossinessMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("glossiness", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.use_map_raymir = True
						mtex.uv_layer = uvname
						
					if (mat._lightMapId is not None) and (mat._lightMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._lightMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("light", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.use_map_ambient = True
						mtex.uv_layer = uvname
						
					if (mat._normalMapId is not None) and (mat._normalMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._normalMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("normal", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.use_map_normal = True
						mtex.uv_layer = uvname
						
					if (mat._opacityMapId is not None) and (mat._opacityMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._opacityMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("opacity", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.use_map_alpha = True
						mtex.uv_layer = uvname
						
					if (mat._reflectionCubeMapId is not None) and (mat._reflectionCubeMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._reflectionCubeMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("reflectioncube", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.uv_layer = uvname
						
					if (mat._specularMapId is not None) and (mat._specularMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._specularMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("specular", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.use_map_specular = True
						mtex.uv_layer = uvname
			
			#reorder uvs to current face order
			#newuvs = []
			#for i in range(len(me.faces)):
			#	for j in range(len(me.faces[i].vertices)):
			#		ut = [ uvs[me.faces[i].vertices[j]][0] , uvs[me.faces[i].vertices[j]][1] ]
			#		newuvs.append(ut)
			
			#i=0
			#for u in uvlayer.data:
			#	if diffuseimg is not None:
			#		u.image = diffuseimg
			#	u.uv[0][0] = newuvs[i][0]
			#	u.uv[0][1] = newuvs[i][1]
			#	i=i+1	
			
			#x=0
			#each face
			#for i in range(len(me.faces)):
			#	#set image in uv window to diffuseimg
			#	if diffuseimg is not None:
			#		uvlayer.data[i].image = diffuseimg
			#	#for each vert in face set uv vert
			#	for j in range(len(me.faces[i].vertices)):
			#		uvlayer.data[i].uv[j][0] = uvs[i][0]
			#		uvlayer.data[i].uv[j][1] = uvs[i][1]
			#		#uvlayer.data[i].uv[j][1] = 1.0 + uvlayer.data[i].uv[j][1] #flip back
			#		x=x+1
			
			#print(uvs)
			
			#print final uvs
			#for i in range(len(me.faces)):
			#    for j in range(len(me.faces[i].vertices)):
			#        uv = [me.uv_textures.active.data[i].uv[j][0], me.uv_textures.active.data[i].uv[j][1]]
			#        print(me.uv_textures.active.data[i].uv1)
			#        print(me.uv_textures.active.data[i].uv2)
			#        print(me.uv_textures.active.data[i].uv3)

			#set norms
			if len(norms) > 0:
				for i in range(len(norms)):
					me.vertices[i].normal=norms[i]
			
			#set uvs
			#for i in range(len(faces)):
			#	if diffuseimg is not None:
			#		uvlayer.data[i].image = diffuseimg
			#	uvlayer.data[i].uv1=uvs[faces[i][0]]
			#	uvlayer.data[i].uv2=uvs[faces[i][1]]
			#	uvlayer.data[i].uv3=uvs[faces[i][2]]
			#	print(uvlayer.data[i].uv1)
			#	print(uvlayer.data[i].uv2)
			#	print(uvlayer.data[i].uv3)
			
			#loop over all uv layers
			uv_faces = me.uv_textures.active.data[:]
			for fidx, uf in enumerate(uv_faces):
				face = faces[fidx]
				v1, v2, v3 = face
				if diffuseimg is not None:
					uf.image = diffuseimg
				uf.uv1 = uvs[v1]
				uf.uv2 = uvs[v2]
				uf.uv3 = uvs[v3]
			
			#bpy.ops.object.editmode_toggle() 
			#bpy.ops.uv.unwrap() 
			#bpy.ops.object.editmode_toggle() 
			me.validate()
			me.update(calc_edges=True) 		

		#render skins
		for skin in self.skins:		
			verts = []
			faces = []
			uvs = []
			norms = []
			tans = []
			joints = []
			
			ar = bpy.data.armatures.new("armature")
			ob = bpy.data.objects.new("armature", ar)
			bpy.context.scene.objects.link(ob)
			
			#context.scene.objects.active = ar
			#bpy.ops.object.mode_set(mode='EDIT')
			#add bone
			#bo = ar.edit_bones.new("bone")
			#bo.head = head
			#bo.tail = tail
			#bo.parent = parent_bone
		
			#index buff
			ibuf = ibuffers[skin._indexBufferId]
			i=0
			for x in range(int(len(ibuf._byteBuffer)/3)):
				temp = (ibuf._byteBuffer[i],ibuf._byteBuffer[i+1],ibuf._byteBuffer[i+2])
				faces.append(temp)
				i=i+3
			
			#vert buff
			for v in skin._vertexBuffers:
				vbuf = vbuffers[v]
				#print(vbuf._byteBuffer)
				#print(vbuf._id)
				#print(vbuf._attributes)
				numflts = 0
				for att in vbuf._attributes:
					if att == 0:
						#position
						numflts = numflts + 3
					if att == 1:
						#normal
						numflts = numflts + 3
					if att == 2:
						#tangent
						numflts = numflts + 4
					if att == 3:
						#joint
						numflts = numflts + 4
					if att == 4:
						#uv
						numflts = numflts + 2
				flcount = int(len(vbuf._byteBuffer))
				points = int(flcount/numflts)
				i = 0
				for att in vbuf._attributes:
						if att == 0:
							x = vbuf._byteBuffer[i]
							i = i + 1
							y = vbuf._byteBuffer[i]
							i = i + 1
							z = vbuf._byteBuffer[i]
							i = i + 1
							verts.append((x, y, z))
						if att == 1:
							x = vbuf._byteBuffer[i]
							i = i + 1
							y = vbuf._byteBuffer[i]
							i = i + 1
							z = vbuf._byteBuffer[i]
							i = i + 1
							norms.append((x, y, z))
						if att == 2:
							a = vbuf._byteBuffer[i]
							i = i + 1
							b = vbuf._byteBuffer[i]
							i = i + 1
							c = vbuf._byteBuffer[i]
							i = i + 1
							d = vbuf._byteBuffer[i]
							i = i + 1
							tans.append((a,b,c,d))
						if att == 3:
							i = i + 1
							a = vbuf._byteBuffer[i]
							i = i + 1
							b = vbuf._byteBuffer[i]
							i = i + 1
							c = vbuf._byteBuffer[i]
							i = i + 1
							d = vbuf._byteBuffer[i]
							i = i + 1
							joints.append((a, b, c, d))
						if att == 4:
							uv1 = vbuf._byteBuffer[i]
							i = i + 1
							uv2 = vbuf._byteBuffer[i]
							uv2 = 1.0 - uv2
							i = i + 1
							uvs.append([uv1,uv2])
			
			#print(verts)
			#print(faces)
			#print(uvs)
			#print(mesh._name)
			
			if skin._name is not None:
				nme = skin._name
			else:
				nme = "Skin"
			
			# create a new mesh  
			me = bpy.data.meshes.new(nme) 
			
			# create an object with that mesh
			ob = bpy.data.objects.new(nme, me)  
			
			if (skin._transform is not None) and (self.Config.ApplyTransforms == True):
				ob.matrix_local = skin._transform.getMatrix()
			else:
				# position object at 3d-cursor
				ob.location = bpy.context.scene.cursor_location
			
			# Link object to scene
			bpy.context.scene.objects.link(ob)  
			
			# Fill the mesh with verts, edges, faces 
			me.from_pydata(verts,[],faces)   # edges or faces should be [], or you ask for problems
			me.update(calc_edges=True)    # Update mesh with new data
			
			if skin._visible == False:
				ob.hide = True
			
			for surf in skin._surfaces:
				#surf._indexBegin
				#surf._materialId
				#surf._numTriangles
				
				if surf._materialId is not None:
					#get material
					mat = materials[surf._materialId]
					
					#new material
					surf_mat = bpy.data.materials.new("Material")
					me.materials.append(surf_mat)
					
					if (mat._diffuseMapId is not None) and (mat._diffuseMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._diffuseMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("diffuse", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
						
					if (mat._glossinessMapId is not None) and (mat._glossinessMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._glossinessMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("glossiness", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
						
					if (mat._lightMapId is not None) and (mat._lightMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._lightMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("light", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
						
					if (mat._normalMapId is not None) and (mat._normalMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._normalMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("normal", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = False
						mtex.use_map_normal = True
						
					if (mat._opacityMapId is not None) and (mat._opacityMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._opacityMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("opacity", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
						
					if (mat._reflectionCubeMapId is not None) and (mat._reflectionCubeMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._reflectionCubeMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("reflectioncube", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
						
					if (mat._specularMapId is not None) and (mat._specularMapId != int("0xFFFFFFFF",16)):
						#get map
						map = maps[mat._specularMapId]
						#get img
						img = images[map._imageId]
						
						#new image
						texture = bpy.data.textures.new("specular", type='IMAGE')
						DIR = os.path.dirname(self.Config.FilePath)
						image = load_image(img._url, DIR)
						texture.image = image
					
						#new texture
						mtex = surf_mat.texture_slots.add()
						mtex.texture = texture
						mtex.texture_coords = 'UV'
						mtex.use_map_color_diffuse = True
			
			#add uv
			uvlayer = me.uv_textures.new()
		
	def read(self,file,mask,ver):
		print("reada3d2")
		
		self.reset()
		
		# define arrays
		arrs = {
			0: self.ambientLights, 
			1: self.animationClips, 
			2: self.animationTracks,
			3: self.boxes,
			4: self.cubeMaps,
			5: self.decals,
			6: self.directionalLights,
			7: self.images,
			8: self.indexBuffers,
			9: self.joints,
			10: self.maps,
			11: self.materials,
			12: self.meshes,
			13: self.objects,
			14: self.omniLights,
			15: self.skins,
			16: self.spotLights,
			17: self.sprites,
			18: self.vertexBuffers,
			19: self.layers,
			20: self.cameras,
			21: self.lods
		}
		
		# define classes
		funcs = {
			0: A3D2AmbientLight, 
			1: A3D2AnimationClip, 
			2: A3D2Track,
			3: A3D2Box,
			4: A3D2CubeMap,
			5: A3D2Decal,
			6: A3D2DirectionalLight,
			7: A3D2Image,
			8: A3D2IndexBuffer,
			9: A3D2Joint,
			10: A3D2Map,
			11: A3D2Material,
			12: A3D2Mesh,
			13: A3D2Object,
			14: A3D2OmniLight,
			15: A3D2Skin,
			16: A3D2SpotLight,
			17: A3D2Sprite,
			18: A3D2VertexBuffer
		}

		if (ver.baseversion == 2) and (ver.pointversion >= 4):
			funcs.update({19: A3D2Layer})
			
		if (ver.baseversion == 2) and (ver.pointversion >= 5):
			funcs.update({20: A3D2Camera, 21: A3D2LOD})
		
		#counter that just deals with the func keys
		findex = 0
		#mask counter that increments with the options of class
		mskindex = 0
		for i in range(len(mask)):
			#exit if we gone past amount
			if i >= len(funcs):
				break
			#print(mask[mskindex])
			if mask[mskindex] == "0":
				#read array of classes
				arr = A3D2Array()
				arr.read(file)
				mskindex = mskindex + 1
				for a in range(arr.length):
					cla = funcs[findex](self.Config)
					cla.read(file,mask,mskindex)
					arrs[findex].append(cla)
					mskindex = mskindex + cla._mskindex
			else:
				mskindex = mskindex + 1
			findex = findex + 1
		
	def write(self,file):
		print("write a3d2\n")
		
		tfile = tempfile.TemporaryFile(mode ='w+b')
				
		if len(self.ambientLights) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.ambientLights))
			#add class as option
			self.nullmask = self.nullmask + str(0)
			for cla in self.ambientLights:
				cla.write(tfile)
				#add class properties as options
				#self.nullmask = self.nullmask + amd.readOptions()
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.animationClips) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.animationClips))
			#add class as option
			self.nullmask = self.nullmask + str(0)
			for cla in self.animationClips:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.animationTracks) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.animationTracks))
			self.nullmask = self.nullmask + str(0)
			for cla in self.animationTracks:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.boxes) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.boxes))
			self.nullmask = self.nullmask + str(0)
			for cla in self.boxes:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.cubeMaps) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.cubeMaps))
			self.nullmask = self.nullmask + str(0)
			for cla in self.cubeMaps:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.decals) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.decals))
			self.nullmask = self.nullmask + str(0)
			for cla in self.decals:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.directionalLights) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.directionalLights))
			self.nullmask = self.nullmask + str(0)
			for cla in self.directionalLights:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.images) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.images))
			self.nullmask = self.nullmask + str(0)
			for cla in self.images:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.indexBuffers) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.indexBuffers))
			self.nullmask = self.nullmask + str(0)
			for cla in self.indexBuffers:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.joints) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.joints))
			self.nullmask = self.nullmask + str(0)
			for cla in self.joints:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.maps) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.maps))
			self.nullmask = self.nullmask + str(0)
			for cla in self.maps:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.materials) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.materials))
			self.nullmask = self.nullmask + str(0)
			for cla in self.materials:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.meshes) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.meshes))
			self.nullmask = self.nullmask + str(0)
			for cla in self.meshes:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.objects) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.objects))
			self.nullmask = self.nullmask + str(0)
			for cla in self.objects:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.omniLights) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.omniLights))
			self.nullmask = self.nullmask + str(0)
			for cla in self.omniLights:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.spotLights) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.spotLights))
			self.nullmask = self.nullmask + str(0)
			for cla in self.spotLights:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.sprites) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.sprites))
			self.nullmask = self.nullmask + str(0)
			for cla in self.sprites:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.skins) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.skins))
			self.nullmask = self.nullmask + str(0)
			for cla in self.skins:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.vertexBuffers) > 0:
			#write
			arr = A3D2Array()
			arr.write(tfile,len(self.vertexBuffers))
			self.nullmask = self.nullmask + str(0)
			for cla in self.vertexBuffers:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
					
		if self.Config.A3DVersionSystem <= 3:
			if len(self.layers) > 0:
				arr = A3D2Array()
				arr.write(tfile,len(self.layers))
				self.nullmask = self.nullmask + str(0)
				for cla in self.layers:
					cla.write(tfile)
					self.nullmask = self.nullmask + cla._optmask
			else:
				self.nullmask = self.nullmask + str(1)
		
		if self.Config.A3DVersionSystem <= 2:
			if len(self.cameras) > 0:
				arr = A3D2Array()
				arr.write(tfile,len(self.cameras))
				self.nullmask = self.nullmask + str(0)
				for cla in self.cameras:
					cla.write(tfile)
					self.nullmask = self.nullmask + cla._optmask
			else:
				self.nullmask = self.nullmask + str(1)
			
			if len(self.lods) > 0:
				arr = A3D2Array()
				arr.write(tfile,len(self.lods))
				self.nullmask = self.nullmask + str(0)
				for cla in self.lods:
					cla.write(tfile)
					self.nullmask = self.nullmask + cla._optmask
			else:
				self.nullmask = self.nullmask + str(1)
		
		
		tfile2 = tempfile.TemporaryFile(mode ='w+b')
		
		print("nullmask = "+self.nullmask)
		
		#nullmask
		null = A3D2Null(self.Config)
		null._mask = self.nullmask
		null.write(tfile2)
		
		#version
		ver = A3DVersion(self.Config)
		
		if self.Config.A3DVersionSystem == 5:
			major = 1
			minor = 0
		elif self.Config.A3DVersionSystem == 4:
			major = 2
			minor = 0
		elif self.Config.A3DVersionSystem == 3:
			major = 2
			minor = 4
		elif self.Config.A3DVersionSystem == 2:
			major = 2
			minor = 5
		elif self.Config.A3DVersionSystem == 1:
			major = 2
			minor = 6
		
		ver.baseversion = major
		ver.pointversion = minor
		ver.write(tfile2)
		
		#a3d2
		tfile.seek(0)
		data = tfile.read()
		tfile2.write(data)
		tfile.close()
		
		#write package length
		a3dpack = A3D2Package(self.Config)
		if self.Config.CompressData == 1:
			a3dpack._packed = 1
			tfile2.seek(0)
			indata = tfile2.read()
			outdata = zlib.compress(indata)
			a3dpack._length = len(outdata)
		else:
			a3dpack._length = tfile2.tell()
			a3dpack._packed = 0
		a3dpack.write(file)
		
		#compress and write data
		if self.Config.CompressData == 1:
			# compressed
			tfile2.seek(0)
			indata = tfile2.read()
			outdata = zlib.compress(indata)
			file.write(outdata)
		else:
			# uncompressed
			tfile2.seek(0)
			data = tfile2.read()
			file.write(data)
		tfile2.close()
		
class A3D2Array:
	def __init__(self):
		self.length = 0
	
	def read(self,file):
		numelements = 0
		temp_data = ord(file.read(1))
		temp_data = bin(temp_data)[2:].rjust(8, '0')
		if temp_data[0] == '0':
			numelements = temp_data[1:8]
		elif temp_data[0] == '1':
			if temp_data[0:2] == '10':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				numelements = temp_data[2:8] + temp
			elif temp_data[0:2] == '11':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				temp1 = ord(file.read(1))
				temp1 = bin(temp1)[2:].rjust(8, '0')
				numelements = temp_data[2:8] + temp + temp1
			else:
				print('Error reading array')
		else:
			print('Error reading array')
		#print('Array Length %s' % numelements)
		#print('Array Length %i' % int(numelements,2))
		self.length = int(numelements,2)
		
	def write(self,file,bylen):
		#bitnum = NumberOfSetBits(bylen)
		bitnum = bylen.bit_length()
		if bitnum <= 7:
			print("Array 1 byte required\n")
			file.write(struct.pack("B", bylen))
		elif bitnum > 7 and bitnum <= 14:
			print("Array 2 byte required\n")
			print(bitnum) #8
			print(bylen) #192
			#if is 8 bits (fits exacty into 1 byte)
			#if bitnum == 8:
			#	#placed right to left
			#	byte1 = int((bylen >> 8) & 255)
			#	byte1 = byte1 + 128 #add 10000000 bits
			#	byte2 = int(bylen & 255)
			#else:
			#	byte1 = int((bylen >> (bitnum - 6)) & 255)
			#	byte1 = byte1 + 128 #add 10000000 bits
			#	byte2 = int(bylen << (8 - (bitnum - 6)) & 255)
			
			byte1 = int((bylen >> 8) & 255)
			byte1 = byte1 + 128 #add 10000000 bits
			byte2 = int(bylen & 255)
			print(byte1)
			print(byte2)
			file.write(struct.pack("B", byte1))
			file.write(struct.pack("B", byte2))
		elif bitnum > 14 and bitnum <= 22:
			print("Array 3 byte required\n")
			#if bitnum == 16:
				#left to right
			#	print("coming soon..")
			#right to left
			byte1 = int( (bylen >> 16) & 255 )
			byte1 = byte1 + 192 #add 11000000 bits
			byte2 = int( (bylen >> 8) & 255 )
			byte3 = int(bylen & 255)
			print(byte1)
			print(byte2)
			print(byte3)
			file.write(struct.pack("B", byte1))
			file.write(struct.pack("B", byte2))
			file.write(struct.pack("B", byte3))
		else:
			print("Array bytes too long!\n")

class A3D2String:
	def __init__(self):
		self.length = 0
		self.name = ""
	
	def read(self,file):
		numelements = 0
		name = ''
		temp_data = ord(file.read(1))
		temp_data = bin(temp_data)[2:].rjust(8, '0')
		if temp_data[0] == '0':
			numelements = temp_data[1:8]
		elif temp_data[0] == '1':
			if temp_data[0:2] == '10':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				numelements = temp_data[2:8] + temp
			elif temp_data[0:2] == '11':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				temp1 = ord(file.read(1))
				temp1 = bin(temp1)[2:].rjust(8, '0')
				numelements = temp_data[2:8] + temp + temp1
			else:
				print('Error reading string type 1')
		else:
			print('Error reading string')
			
		nlen = int(numelements,2)
		self.length = nlen
		for x in range(nlen):
			name += chr(ord(file.read(1)))
		self.name = name
	
	def write(self,file):
		bylen = len(self.name)
		if bylen > 0:
			#bitnum = NumberOfSetBits(bylen)
			bitnum = bylen.bit_length()
			if bitnum <= 7:
				print("String 1 byte required\n")
				file.write(struct.pack("B", bylen))
				self.writeName(file)
			elif bitnum > 7 and bitnum <= 14:
				print("String 2 byte required\n")
				byte1 = int((bylen >> 8) & 255)
				byte1 = byte1 + 128 #add 10000000 bits
				byte2 = int(bylen & 255)
				file.write(struct.pack("B", byte1))
				file.write(struct.pack("B", byte2))
				self.writeName(file)
			elif bitnum > 14 and bitnum <= 22:
				print("String 3 byte required\n")
				byte1 = int( (bylen >> 16) & 255 )
				byte1 = byte1 + 192 #add 11000000 bits
				byte2 = int( (bylen >> 8) & 255 )
				byte3 = int(bylen & 255)
				file.write(struct.pack("B", byte1))
				file.write(struct.pack("B", byte2))
				file.write(struct.pack("B", byte3))
				self.writeName(file)
			else:
				print("String bytes too long!\n")
	
	def writeName(self,file):
		file.write(struct.pack(str(len(self.name))+"s",self.name.encode("utf-8")))

class A3D2AmbientLight:
	def __init__(self,Config):
		self._boundBoxId = None
		self._color = 0
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._color = 0
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2AmbientLight")
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._color = toRgb(struct.unpack(">L", file.read(struct.calcsize(">L")))[0])
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._intensity = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
		
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack(">L",self._color))
		file.write(struct.pack("Q",self._id))
		file.write(struct.pack(">L",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("B",self._visible))

class A3D2AnimationClip:
	def __init__(self,Config):
		self._id = 0
		self._loop = 0
		self._name = None
		self._objectIDs = None
		self._tracks = []
		
		self._optionals = [self._name,self._objectIDs]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._loop = 0
		self._name = None
		self._objectIDs = None
		self._tracks = []
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2AnimationClip")
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._loop = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			arr = A3D2Array()
			arr.read(file)
			self._objectIDs = []
			for x in range(arr.length):
				self._objectIDs.append(struct.unpack("Q", file.read(struct.calcsize("Q")))[0])
		self._mskindex = self._mskindex + 1
		
		arr = A3D2Array()
		arr.read(file)
		for x in range(arr.length):
			self._tracks.append(struct.unpack(">L", file.read(struct.calcsize(">L")))[0])		
		
	def write(self,file):
		print("write")
		
class A3D2Track:
	def __init__(self,Config):
		self._id = 0
		self._keyframes = []
		self._objectName = ""
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._keyframes = []
		self._objectName = ""
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Track")
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
		arr = A3D2Array()
		arr.read(file)
		print(str(arr.length)+" x keyframes")
		if arr.length > 0:
			for a in range(arr.length):
				a3dkeyf = A3D2Keyframe(self.Config)
				self._keyframes.append(a3dkeyf.read(file,mask,mskindex + self._mskindex))
				self._mskindex = self._mskindex + a3dkeyf._mskindex
		
		a3dstr = A3D2String()
		a3dstr.read(file)
		self._objectName = a3dstr.name
		
		print(self._objectName)
		
	def write(self,file):
		print("write")
	
class A3D2Box:
	def __init__(self,Config):
		self._box = []
		self._id = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._box = []
		self._id = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file,mask,mskindex):
		print("read A3D2Box")
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			self._box.append( struct.unpack(">f",file.read(struct.calcsize(">f")))[0] )
		self._id = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		
	def write(self,file):
		print("write boundbox\n")
		#6 floats minX, minY, minZ, maxX, maxY, maxZ
		#bpy.data.object['cube'].bound_box
		#Vertex 1: bound_box[0][0]    bound_box[0][1]    bound_box[0][2]
		#Vertex 2: bound_box[1][0]    etc
		#Or you could go the long way... bound_box.data.data.vertices[0].co etc
		arr = A3D2Array()
		arr.write(file,len(self._box))
		#file.write(struct.pack('f'*len(self._box),*self._box))
		for x in range(len(self._box)):
			file.write(struct.pack('>f',self._box[x]))
		#write id
		file.write(struct.pack('>L',self._id))		

class A3D2CubeMap:
	def __init__(self,Config):
		self._backId = None
		self._bottomId = None
		self._frontId = None
		self._id = 0
		self._leftId = None
		self._rightId = None
		self._topId = 0
		
		self._optionals = [self._backId,self._bottomId,self._frontId,self._leftId,self._rightId]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._backId = None
		self._bottomId = None
		self._frontId = None
		self._id = 0
		self._leftId = None
		self._rightId = None
		self._topId = 0
		self._mskindex = 0	
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2CubeMap")
		if mask[mskindex + self._mskindex] == "0":
			self._backId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":	
			self._bottomId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._frontId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		#id
		self._id = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._leftId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._rightId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._topId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
	def write(self,file):
		print("write")

class A3D2Decal:
	def __init__(self,Config):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._name = None
		self._offset = None
		self._parentId = None
		self._surfaces = 0
		self._transform = None
		self._vertexBuffers = 0
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._offset,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._name = None
		self._offset = None
		self._parentId = None
		self._surfaces = 0
		self._transform = None
		self._vertexBuffers = 0
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Decal")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._indexBufferId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._offset = struct.unpack(">f", file.read(struct.calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3D2Surface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			self._mskindex = self._mskindex + a3dsurf._mskindex
			
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
		
		arr = A3D2Array()
		arr.read(file)
		self._vertexBuffers = []
		for a in range(arr.length):
			self._vertexBuffers.append(struct.unpack(">L", file.read(struct.calcsize(">L")))[0])
		
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
	def write(self,file):
		print("write")

class A3D2DirectionalLight:
	def __init__(self,Config):
		self._boundBoxId = None
		self._color = 0
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._color = 0
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2DirectionalLight")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._color = toRgb(struct.unpack("I", file.read(struct.calcsize("I")))[0])
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._intensity = struct.unpack(">f", file.read(struct.calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("I",self._color))
		file.write(struct.pack("Q",self._id))
		file.write(struct.pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("B",self._visible))

class A3D2Image:
	def __init__(self,Config):
		self._id = 0
		self._url = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._url = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Image")
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		a3dstr = A3D2String()
		a3dstr.read(file)
		self._url = a3dstr.name
		
	def write(self,file):
		file.write(struct.pack(">L",self._id))
		self._url.write(file)

class A3D2IndexBuffer:
	def __init__(self,Config):
		self._byteBuffer = []
		self._id = 0
		self._indexCount = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._byteBuffer = []
		self._id = 0
		self._indexCount = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file,mask,mskindex):
		print("read A3D2IndexBuffer")
		arr = A3D2Array()
		arr.read(file)
		for a in range(int(arr.length/2)):
			self._byteBuffer.append( struct.unpack("<H",file.read(struct.calcsize("<H")))[0] )
		self._id = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		self._indexCount = struct.unpack('>L',file.read(struct.calcsize(">L")))[0]
		
	def write(self,file):
		
		arr = A3D2Array()
		# multiply by 2 because its length of bytes and we are using 2 bytes
		vbuflen = int(len(self._byteBuffer) * 2)
		#vbuflen = len(self._byteBuffer) 
		#vbuflen = int((len(self._byteBuffer) * 3) * 2)
		arr.write(file,vbuflen) 
		for x in range(len(self._byteBuffer)):
			#each index uses 2 bytes (little-endian)
			file.write(struct.pack('<H',self._byteBuffer[x]))
		#write id
		file.write(struct.pack('>L',self._id))
		#write indexcount
		file.write(struct.pack('>L',self._indexCount))
		print("ibuf_indexCount="+str(self._indexCount))
		print("ibuf_byteBufferlength="+str(vbuflen))

class A3D2Joint:
	def __init__(self,Config):
		self._boundBoxId = None
		self._id = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._id = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Joint")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
		
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("Q",self._id))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("B",self._visible))
		
class A3D2Map:
	def __init__(self,Config):
		self._channel = 0
		self._id = 0
		self._imageId = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._channel = 0
		self._id = 0
		self._imageId = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Map")
		self._channel = struct.unpack(">H", file.read(struct.calcsize(">H")))[0]
		self._id = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._imageId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
	def write(self,file):
		file.write(struct.pack(">H",self._channel))
		file.write(struct.pack(">L",self._id))
		file.write(struct.pack(">L",self._imageId))

class A3D2Material:
	def __init__(self,Config):
		self._diffuseMapId = None
		self._glossinessMapId = None
		self._id = 0
		self._lightMapId = None
		self._normalMapId = None
		self._opacityMapId = None
		self._reflectionCubeMapId = None
		self._specularMapId = None
		
		self._optionals = [self._diffuseMapId,self._glossinessMapId,self._lightMapId,self._normalMapId,self._opacityMapId,self._reflectionCubeMapId,self._specularMapId]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._diffuseMapId = None
		self._glossinessMapId = None
		self._id = 0
		self._lightMapId = None
		self._normalMapId = None
		self._opacityMapId = None
		self._reflectionCubeMapId = None
		self._specularMapId = None
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
	
	def read(self,file,mask,mskindex):
		print("read A3D2Material")
				
		if mask[mskindex + self._mskindex] == "0":
			self._diffuseMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":	
			self._glossinessMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._lightMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._normalMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._opacityMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._reflectionCubeMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._specularMapId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
	
	#def read(self,file,mask,mskindex):
	#	print("read A3D2Material")
	#	x = 0
	#	items = sorted(self._properties.items(), key=lambda x: x[1])
	#	for item in items:
	#		o = item[0]
	#		v = item[1]
	#		if v == 0:
	#			o = struct.unpack(self._structs[x], file.read(struct.calcsize(self._structs[x])))
	#		elif (v == 1) and (mask[mskindex]) == "0":
	#			o = struct.unpack(self._structs[x], file.read(struct.calcsize(self._structs[x])))
	#			self._mskindex = self._mskindex + 1
	#		x=x+1
		
	def write(self,file):
		if self._diffuseMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._diffuseMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._glossinessMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._glossinessMapId))
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(struct.pack(">L",self._id))
		
		if self._lightMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._lightMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._normalMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._normalMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._opacityMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._opacityMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._reflectionCubeMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._reflectionCubeMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._specularMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._specularMapId))
		else:
			self._optmask = self._optmask + str(1)
		
class A3D2Mesh:
	def __init__(self,Config):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._name = None
		self._parentId = None
		self._surfaces = []
		self._transform = None
		self._vertexBuffers = [0]
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._name = None
		self._parentId = None
		self._surfaces = []
		self._transform = None
		self._vertexBuffers = [0]
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file,mask,mskindex):
		print("read A3D2Mesh")
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._indexBufferId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]

		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		#surfaces
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3D2Surface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			self._mskindex = self._mskindex + a3dsurf._mskindex
		
		#transform
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		#buffer
		arr = A3D2Array()
		arr.read(file)
		self._vertexBuffers = []
		for a in range(arr.length):
			self._vertexBuffers.append(struct.unpack(">L", file.read(struct.calcsize(">L")))[0])
		
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
	def write(self,file):
		print("write mesh\n")
		#bbid, id, indexbufid
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(struct.pack("Q",self._id))
		file.write(struct.pack(">L",self._indexBufferId))
		
		#string
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#parentid
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		#surfaces
		arr = A3D2Array()
		arr.write(file,len(self._surfaces))
		for surf in self._surfaces:
			surf.write(file)
			self._optmask = self._optmask + surf._optmask
		#transform
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#vbuffers
		arr = A3D2Array()
		arr.write(file,len(self._vertexBuffers))
		for x in range(len(self._vertexBuffers)):
			file.write(struct.pack(">L",self._vertexBuffers[x]))
		#visible
		file.write(struct.pack("B",self._visible))

class A3D2Object:
	def __init__(self,Config):
		self._boundBoxId = None
		self._id = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._id = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file,mask,mskindex):
		print("read A3D2Object")
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]

		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print(self._name)
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		#transform
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
				
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
	def write(self,file):
		#bbid, id, indexbufid
		if self._boundBoxId is not None:
			file.write(struct.pack(">L",self._boundBoxId))
		file.write(struct.pack("Q",self._id))
		#string
		if self._name is not None:
			self._name.write(file)
		#parentid
		if self._parentId is not None:
			file.write(struct.pack("Q",self._parentId))
		#transform
		if self._transform is not None:
			self._transform.write(file)
		#visible
		file.write(struct.pack("B",self._visible))

class A3D2OmniLight:
	def __init__(self,Config):
		self._attenuationBegin = 0
		self._attenuationEnd = 0
		self._boundBoxId = None
		self._color = 0
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._attenuationBegin = 0
		self._attenuationEnd = 0
		self._boundBoxId = None
		self._color = 0
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2OmniLight")
		self._mskindex = 1
		
	def write(self,file):
		file.write(struct.pack('>f',self._attenuationBegin))
		file.write(struct.pack('>f',self._attenuationEnd))
		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)

		file.write(struct.pack("I",self._color))			
		file.write(struct.pack("Q",self._id))
		file.write(struct.pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("B",self._visible))

class A3D2SpotLight:
	def __init__(self,Config):
		self._attenuationBegin = 0
		self._attenuationEnd = 0
		self._boundBoxId = None
		self._color = 0
		self._falloff = None
		self._hotspot = None
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._falloff,self._hotspot,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._attenuationBegin = 0
		self._attenuationEnd = 0
		self._boundBoxId = None
		self._color = 0
		self._falloff = None
		self._hotspot = None
		self._id = 0
		self._intensity = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2SpotLight")
		self._attenuationBegin = struct.unpack('>f', file.read(struct.calcsize(">f")))[0]
		self._attenuationEnd = struct.unpack('>f', file.read(struct.calcsize(">f")))[0]
		
		print(self._attenuationBegin)
		print(self._attenuationEnd)
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		print(self._boundBoxId)
		
		self._color = struct.unpack("I",file.read(struct.calcsize("I")))[0]
		print(self._color)
		
		if mask[mskindex + self._mskindex] == "0":
			self._falloff = struct.unpack('>f', file.read(struct.calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._hotspot = struct.unpack('>f', file.read(struct.calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack("Q",file.read(struct.calcsize("Q")))[0]
		self._intensity = struct.unpack(">f",file.read(struct.calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print(self._name)
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
		
		file.write(struct.pack("B",self._visible))
		
	def write(self,file):
		file.write(struct.pack('>f',self._attenuationBegin))
		file.write(struct.pack('>f',self._attenuationEnd))
		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)

		file.write(struct.pack("I",self._color))
		
		if self._falloff is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">f",self._falloff))
		else:
			self._optmask = self._optmask + str(1)
			
		if self._hotspot is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">f",self._hotspot))
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(struct.pack("Q",self._id))
		file.write(struct.pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack("B",self._visible))

class A3D2Sprite:
	def __init__(self,Config):
		self._alwaysOnTop = 1
		self._boundBoxId = None
		self._height = 0
		self._id = 0
		self._materialId = 0
		self._name = None
		self._originX = 0
		self._originY = 0
		self._parentId = None
		self._perspectiveScale = 0
		self._rotation = 0
		self._transform = None
		self._visible = 1
		self._width = 0
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._alwaysOnTop = 1
		self._boundBoxId = None
		self._height = 0
		self._id = 0
		self._materialId = 0
		self._name = None
		self._originX = 0
		self._originY = 0
		self._parentId = None
		self._perspectiveScale = 0
		self._rotation = 0
		self._transform = None
		self._visible = 1
		self._width = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Sprite")
		self._mskindex = 1
		
	def write(self,file):
		print("write")

class A3D2Skin:
	def __init__(self,Config):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._jointBindTransforms = []
		self._joints = []
		self._name = None
		self._numJoints = []
		self._parentId = None
		self._surfaces = []
		self._transform = None
		self._vertexBuffers = []
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._jointBindTransforms = 0
		self._joints = []
		self._name = None
		self._numJoints = []
		self._parentId = None
		self._surfaces = []
		self._transform = None
		self._vertexBuffers = []
		self._visible = 1
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2Skin")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._indexBufferId = struct.unpack(">L", file.read(struct.calcsize(">L")))[0]
		
		arr = A3D2Array()
		arr.read(file)
		for x in range(arr.length):
			a3djntbnd = A3D2JointBindTransform(self.Config)
			self._jointBindTransforms.append(a3djntbnd.read(file,mask,mskindex))
			
		arr = A3D2Array()
		arr.read(file)
		for x in range(arr.length):
			self._joints.append(struct.unpack("Q", file.read(struct.calcsize("Q")))[0])
			
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3D2String()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print(self._name)
		
		arr = A3D2Array()
		arr.read(file)
		for x in range(arr.length):
			self._numJoints.append(struct.unpack(">H", file.read(struct.calcsize(">H")))[0])
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		arr = A3D2Array()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3D2Surface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			self._mskindex = self._mskindex + a3dsurf._mskindex
			
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3D2Transform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
		
		arr = A3D2Array()
		arr.read(file)
		self._vertexBuffers = []
		for a in range(arr.length):
			self._vertexBuffers.append(struct.unpack(">L", file.read(struct.calcsize(">L")))[0])
		
		self._visible = struct.unpack("B", file.read(struct.calcsize("B")))[0]
		
	def write(self,file):
		print("write")
		
class A3D2JointBindTransform:
	def __init__(self,Config):
		self._bindPoseTransform = 0
		self._id = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._bindPoseTransform = 0
		self._id = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		print("read A3D2JointBindTransform")
		a3dtran = A3D2Transform(self.Config)
		a3dtran.read(file)
		self._id = struct.unpack("Q", file.read(struct.calcsize("Q")))[0]
		return self
		
	def write(self,file):
		print("write")

class A3D2Keyframe:
	def __init__(self,Config):
		self._time = 0
		self._transform = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._time = 0
		self._transform = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file,mask,mskindex):
		#print("read A3D2Keyframe")
		self._time = struct.unpack(">f",file.read(struct.calcsize(">f")))[0]
		a3dtran = A3D2Transform(self.Config)
		a3dtran.read(file)
		return self
		
	def write(self,file):
		print("write")
		
class A3D2VertexBuffer:
	def __init__(self,Config):
		self._attributes = [0]
		self._byteBuffer = []
		self._id = 0
		self._vertexCount = 0
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._attributes = [0]
		self._byteBuffer = []
		self._id = 0
		self._vertexCount = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file,mask,mskindex):
		print("read A3D2VertexBuffer")
		arr = A3D2Array()
		arr.read(file)
		self._attributes = []
		for a in range(arr.length):
			self._attributes.append(struct.unpack(">L",file.read(struct.calcsize(">L")))[0])
		
		arr = A3D2Array()
		arr.read(file)
		if self.Config.A3DVersionSystem == 1:
			#2.6
			for a in range(int(arr.length/2)):
				self._byteBuffer.append(struct.unpack(">H",file.read(struct.calcsize(">H")))[0])
		else:
			for a in range(int(arr.length/4)):
				self._byteBuffer.append(struct.unpack("<f",file.read(struct.calcsize("<f")))[0])
		self._id  = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._vertexCount  = struct.unpack(">H",file.read(struct.calcsize(">H")))[0]
		
	def write(self,file):
		print("write vertexbuffer")
		#attributes
		arr = A3D2Array()
		arr.write(file,len(self._attributes))
		for x in range(len(self._attributes)):
			file.write(struct.pack(">L",self._attributes[x]))
		#bytebuffer -little endian float
		arr = A3D2Array()
		#bybufsize = int(len(self._byteBuffer))
		bybufsize = int(len(self._byteBuffer)*4) #this worked for cube # times 4 because bytebuffer is length of bytes
		#bybufsize = int(len(self._byteBuffer)*3)
		#bybufsize = int( (self._vertexCount*3)*4 )
		
		print("A3DVersionSystem="+str(self.Config.A3DVersionSystem))
		#if version 2.6 then compressed vertex buffer
		if self.Config.A3DVersionSystem == 1:
			#2.6
			arr.write(file,int(bybufsize/2)) #half it because we storing shorts now
			self.packVertexBuffer(file)
		else:
			arr.write(file,bybufsize) 
			for byte in self._byteBuffer:
				file.write(struct.pack("<f",byte))
		
		#id
		file.write(struct.pack(">L",self._id))
		#vertexcount
		file.write(struct.pack(">H",self._vertexCount))
	
	def packVertexBuffer(self,file):
		basetable,shifttable = {},{}
		for byte in self._byteBuffer:
			f32 = int(byte)
			#h = ((f32>>16)&0x8000)|((((f32&0x7f800000)-0x38000000)>>13)&0x7c00)|((f32>>13)&0x03ff)
			basetable, shifttable = self.generatetables()
			h=basetable[(f32>>23)&0x1ff]+((f32&0x007fffff)>>shifttable[(f32>>23)&0x1ff])
			print("float %f" % byte)
			print(h)
			file.write(struct.pack(">H",h))
	
	def packVertexBuffer_OLD2(self,file):
		#http://gamedev.stackexchange.com/questions/17326/conversion-of-a-number-from-single-precision-floating-point-representation-to-a
		F16_EXPONENT_BITS = 0x1F
		F16_EXPONENT_SHIFT = 10
		F16_EXPONENT_BIAS = 15
		F16_MANTISSA_BITS = 0x3ff
		F16_MANTISSA_SHIFT =  (23 - F16_EXPONENT_SHIFT)
		F16_MAX_EXPONENT =  (F16_EXPONENT_BITS << F16_EXPONENT_SHIFT)

		for byte in self._byteBuffer:
			f32 = int(byte)
			f16 = 0
			sign = (f32 >> 16) & 0x8000
			exponent = ((f32 >> 23) & 0xff) - 127
			mantissa = f32 & 0x007fffff
			
			if exponent == 128:
				f16 = sign | F16_MAX_EXPONENT
				if mantissa:
					f16 |= (mantissa & F16_MANTISSA_BITS)
			elif exponent > 15:
				f16 = sign | F16_MAX_EXPONENT
			elif exponent > -15:
				exponent += F16_EXPONENT_BIAS
				mantissa >>= F16_MANTISSA_SHIFT
				f16 = sign | exponent << F16_EXPONENT_SHIFT | mantissa
			else:
				f16 = sign
			print("float %f" % byte)
			print(f16)
			file.write(struct.pack(">H",f16))
	
	def packVertexBuffer_OLD1(self,file):
		#http://stackoverflow.com/questions/1659440/32-bit-to-16-bit-floating-point-conversion
		shift = 13
		shiftSign = 16
		infN = 0x7F800000
		maxN = 0x477FE000
		minN = 0x38800000
		signN = 0x80000000
		infC = infN >> shift
		nanN = (infC + 1) << shift
		maxC = maxN >> shift
		minC = minN >> shift
		signC = signN >> shiftSign
		mulN = 0x52000000
		mulC = 0x33800000
		subC = 0x003FF
		norC = 0x00400
		maxD = infC - maxC - 1
		minD = minC - subC - 1
		
		for byte in self._byteBuffer:
			v = VBits()
			s = VBits()
			
			v.f = byte
			sign = v.si & signN
			v.si ^= sign
			sign >>= shiftSign # logical shift
			s.si = mulN
			s.si = s.f * v.f # correct subnormals
			v.si ^= (int(s.si) ^ v.si) & -(minN > v.si)
			v.si ^= (infN ^ v.si) & -((infN > v.si) & (v.si > maxN))
			v.si ^= (nanN ^ v.si) & -((nanN > v.si) & (v.si > infN))
			v.ui >>= shift # logical shift
			v.si ^= ((v.si - maxD) ^ v.si) & -(v.si > maxC)
			v.si ^= ((v.si - minD) ^ v.si) & -(v.si > subC)
			data = v.ui | sign
			
			print("float %f" % byte)
			print(data)
			file.write(struct.pack(">H",data))
		
	def packVertexBuffer_OLD(self,file):
		print("packVertexBuffer")
		
		#getting matissa and exponent
		#param = 8.0
		#m, e = math.frexp(param)
		#print(m)
		#print(e)
		#print("%f * 2^%d = %f\n" % (m, e, param))
		
		fl=struct.pack('f',1.1)
		print(FloatToHalf(fl))
		
		#http://www.cplusplus.com/reference/clibrary/cmath/frexp/
		#m, e = frexp(x)
		#mantissa = float
		#e = decimal
		
		#http://hildstrom.com/projects/floatcomposition/index.html
		#loop self._byteBuffer
		n1 = float
		
		#parse float components
		#right-shift by 31 bits, leaving sign bit in bit 0, keep 1 bit
		sign = n1 >> 31 & 0x1 
		#right-shift by 23 bits, leaving exponent in bits 0-8, keep 8 bits
		exp =  n1 >> 23 & 0xFF
		#no shift, mantissa is in bits 0-23, keep 23 bits
		mant = n1 & 0x7FFFFF

		file.write(short)
		
	def unpackVertexBuffer(self,file):
		print("unpackVertexBuffer")
		#epsilon = 2^(E-10)    % For a 16-bit float (half precision)
		# sample (1.0) - see Wikipedia
		FP16='\x00\x3c'

		v = struct.unpack('H', FP16)
		x = HalfToFloat(v[0])

		# hack to coerce int to float
		str = struct.pack('I',x)
		f=struct.unpack('f', str)

		# print the floating point
		print(f[0])
	
	def FloatToHalf(i):
		#Half precision floating point = 1 Sign bit , 5 exponent bits , 10 significand bits = 16 bit
		b=binascii.hexlify(i)
		i = int(b,16)
		s = int((i >> 16) & 0x00008000)
		e = int(((i >> 23) & 0x000000ff) - (127 - 15))
		f = int(i & 0x007fffff)
		if e <= 0:
			if e <= -10:
				if s:
					return 0x8000
				else:
					return 0
			f = (f | 0x00800000) >> (1 - e)
			return s | (f >> 13)
		elif e == 0xff - (127 - 15):
			if f == 0:
				return s | 0x7c00
			else:
				f >>= 13
				return s | 0x7c00 | f | (f == 0)
		else:
			if e > 30:
				return s | 0x7c00
			return s | (e << 10) | (f >> 13)
		
	def HalfToFloat(h):
		#http://forums.devshed.com/python-programming-11/converting-half-precision-floating-point-numbers-from-hexidecimal-to-decimal-576842.html
		s = int((h >> 15) & 0x00000001)    # sign
		e = int((h >> 10) & 0x0000001f)    # exponent
		f = int(h & 0x000003ff)            # fraction

		if e == 0:
			if f == 0:
				return int(s << 31)
			else:
				while not (f & 0x00000400):
					f = f << 1
					e -= 1
				e += 1
				f &= ~0x00000400
				print(s,e,f)
		elif e == 31:
			if f == 0:
				return int((s << 31) | 0x7f800000)
			else:
				return int((s << 31) | 0x7f800000 | (f << 13))

		e = e + (127 -15)
		f = f << 13
		return int((s << 31) | (e << 23) | f)

	def generatetables(self):
		i=0
		e=0
		basetable,shifttable = {},{}
		for i in range(256):
			e=i-127
			#Very small numbers map to zero
			if e<-24:
			  basetable[i|0x000]=0x0000
			  basetable[i|0x100]=0x8000
			  shifttable[i|0x000]=24
			  shifttable[i|0x100]=24
			#Small numbers map to denorms
			elif e<-14:
			  basetable[i|0x000]=(0x0400>>(-e-14))
			  basetable[i|0x100]=(0x0400>>(-e-14)) | 0x8000
			  shifttable[i|0x000]=-e-1
			  shifttable[i|0x100]=-e-1
			# Normal numbers just lose precision
			elif e<=15:
			  basetable[i|0x000]=((e+15)<<10)
			  basetable[i|0x100]=((e+15)<<10) | 0x8000
			  shifttable[i|0x000]=13
			  shifttable[i|0x100]=13
			# Large numbers map to Infinity
			elif e<128:
			  basetable[i|0x000]=0x7C00
			  basetable[i|0x100]=0xFC00
			  shifttable[i|0x000]=24
			  shifttable[i|0x100]=24
			# Infinity and NaN's stay Infinity and NaN's
			else:
			  basetable[i|0x000]=0x7C00
			  basetable[i|0x100]=0xFC00
			  shifttable[i|0x000]=13
			  shifttable[i|0x100]=13
		return basetable,shifttable
	
class VBits:
	def __init__(self):
		self.f = 0
		self.si = 0x00000000
		self.ui = 0x00000000
		
class A3D2Layer:
	def __init__(self,Config):
		self._id = 0
		self._name = ""
		self._objects = []
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._name = ""
		self._objects = []
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Layer")
		self._mskindex = 1
		
	def write(self,file):
		print("write")
		
class A3D2Camera:
	def __init__(self,Config):
		self._boundBoxId = None
		self._farClipping = 0
		self._fov = 0
		self._id = 0
		self._name = None
		self._nearClipping = 0
		self._orthographic = False
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._farClipping = 0
		self._fov = 0
		self._id = 0
		self._name = None
		self._nearClipping = 0
		self._orthographic = False
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Camera")
		self._mskindex = 1
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(struct.pack(">f",self._farClipping))
		file.write(struct.pack(">f",self._fov))
		file.write(struct.pack("Q",self._id))
		
		#string
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(struct.pack(">f",self._nearClipping))
		file.write(struct.pack("Q",self._orthographic))
			
		#parentid
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		#transform
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#visible
		file.write(struct.pack("B",self._visible))

class A3D2LOD:
	def __init__(self,Config):
		self._boundBoxId = None
		self._distances = []
		self._id = 0
		self._name = None
		self._objects = []
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._boundBoxId = None
		self._distances = []
		self._id = 0
		self._name = None
		self._objects = []
		self._parentId = None
		self._transform = None
		self._visible = 1
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2LOD")
		self._mskindex = 1
		
	def write(self,file):
		print("write")
		
class A3D2Surface:
	def __init__(self,Config):
		self._indexBegin = 0
		self._materialId = None
		self._numTriangles = 0
		
		self._optionals = [self._materialId]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._indexBegin = 0
		self._materialId = None
		self._numTriangles = 0
		self._mskindex = 0
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
			
	def read(self,file,mask,mskindex):
		print("read A3D2Surface")
		self._indexBegin = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		if mask[mskindex + self._mskindex] == "0":
			self._materialId = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		self._numTriangles = struct.unpack(">L",file.read(struct.calcsize(">L")))[0]
		return self
		
	def write(self,file):
		file.write(struct.pack(">L",self._indexBegin))
		if self._materialId is not None:
			self._optmask = self._optmask + str(0)
			file.write(struct.pack(">L",self._materialId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(struct.pack(">L",self._numTriangles))
		print("surf_numTriangles="+str(self._numTriangles))

class A3DVersion:
	def __init__(self,Config):
		self.baseversion = 2
		self.pointversion = 0
		self.Config = Config
	def reset(self):
		self.baseversion = 2
		self.pointversion = 0
	def read(self,file):
		temp_data = file.read(struct.calcsize('H'))
		self.baseversion = int(struct.unpack('>H', temp_data)[0]) 
		temp_data = file.read(struct.calcsize('H'))
		self.pointversion = int(struct.unpack('>H', temp_data)[0])
	def write(self,file):
		file.write(struct.pack('>H', self.baseversion))
		file.write(struct.pack('>H', self.pointversion))

class A3D2Transform:
	def __init__(self,Config):
		self._matrix = A3DMatrix()
		self.Config = Config
		self._mskindex = 0
		
	def reset(self):
		self._matrix = A3DMatrix()
		self._mskindex = 0
		self._matrix.reset()
		
	def getMatrix(self):	
		matrx = mathutils.Matrix()
		matrx[0][0], matrx[0][1], matrx[0][2], matrx[0][3] = self._matrix.a, self._matrix.b, self._matrix.c, self._matrix.d
		matrx[1][0], matrx[1][1], matrx[1][2], matrx[1][3] = self._matrix.e, self._matrix.f, self._matrix.g, self._matrix.h
		matrx[2][0], matrx[2][1], matrx[2][2], matrx[2][3] = self._matrix.i, self._matrix.j, self._matrix.k, self._matrix.l
		return matrx
		
	def read(self,file):
		self._matrix.read(file)
		
	def write(self,file):
		self._matrix.write(file)
		
class A3DMatrix:
	def __init__(self):
		self.a = 0
		self.b = 0
		self.c = 0
		self.d = 0
		self.e = 0
		self.f = 0
		self.g = 0
		self.h = 0
		self.i = 0
		self.j = 0
		self.k = 0
		self.l = 0
		self._mskindex = 0
	
	def reset(self):
		self.a = 0
		self.b = 0
		self.c = 0
		self.d = 0
		self.e = 0
		self.f = 0
		self.g = 0
		self.h = 0
		self.i = 0
		self.j = 0
		self.k = 0
		self.l = 0
		self._mskindex = 0
		
	def read(self,file):
		temp = file.read(4)
		self.a = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.b = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.c = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.d = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.e = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.f = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.g = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.h = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.i = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.j = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.k = struct.unpack('>f',temp)[0]
		temp = file.read(4)
		self.l = struct.unpack('>f',temp)[0]
	
	def write(self,file):
		file.write(struct.pack('>f',self.a))
		file.write(struct.pack('>f',self.b))
		file.write(struct.pack('>f',self.c))
		file.write(struct.pack('>f',self.d))
		file.write(struct.pack('>f',self.e))
		file.write(struct.pack('>f',self.f))
		file.write(struct.pack('>f',self.g))
		file.write(struct.pack('>f',self.h))
		file.write(struct.pack('>f',self.i))
		file.write(struct.pack('>f',self.j))
		file.write(struct.pack('>f',self.k))
		file.write(struct.pack('>f',self.l))
		
#==================================
# Custom Meshes
#==================================		
class AddA3DLogo(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_logo"
	bl_label = "Add A3D Logo"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):		
		coords=[(49.6592, -9.7168, -36.695),(68.0484, -9.7168, -30.768),(65.9799, -9.7168, -23.6486),(-57.6792, 8.46341, -13.1369),(-39.1325, 8.46341, -13.9348),(-38.8807, 8.46341, -16.1225),(-8.20569, 6.46341, 53.3047),(-8.20569, -7.7168, 53.3047),(-1.46778, -7.7168, 57.5386),(-1.46778, -7.7168, 57.5386),(-1.46778, 6.46341, 57.5386),(-8.20569, 6.46341, 53.3047),(-1.46778, 6.46341, 57.5386),(-1.46778, -7.7168, 57.5386),(0.0871229, -7.7168, 57.966),(0.0871229, -7.7168, 57.966),(0.0871229, 6.46341, 57.966),(-1.46778, 6.46341, 57.5386),(0.0871229, 6.46341, 57.966),(0.0871229, -7.7168, 57.966),(1.64202, -7.7168, 57.5364),(1.64202, -7.7168, 57.5364),(1.64202, 6.46341, 57.5364),(0.0871229, 6.46341, 57.966),(1.64202, 6.46341, 57.5364),(1.64202, -7.7168, 57.5364),(9.31166, -7.7168, 53.6338),(9.31166, -7.7168, 53.6338),(9.31166, 6.46341, 53.6338),(1.64202, 6.46341, 57.5364),(9.31166, 6.46341, 53.6338),(9.31166, -7.7168, 53.6338),(14.5647, -7.7168, 50.3964),(14.5647, -7.7168, 50.3964),(14.5647, 6.46341, 50.3964),(9.31166, 6.46341, 53.6338),(14.5647, 6.46341, 50.3964),(14.5647, -7.7168, 50.3964),(19.4513, -7.7168, 46.8536),(19.4513, -7.7168, 46.8536),(19.4513, 6.46341, 46.8536),(14.5647, 6.46341, 50.3964),(19.4513, 6.46341, 46.8536),(19.4513, -7.7168, 46.8536),(25.0709, -7.7168, 42.0892),(25.0709, -7.7168, 42.0892),(25.0709, 6.46341, 42.0892),(19.4513, 6.46341, 46.8536),(25.0709, 6.46341, 42.0892),(25.0709, -7.7168, 42.0892),(31.7899, -7.7168, 35.6756),(31.7899, -7.7168, 35.6756),(31.7899, 6.46341, 35.6756),(25.0709, 6.46341, 42.0892),(31.7899, 6.46341, 35.6756),(31.7899, -7.7168, 35.6756),(37.8371, -7.7168, 29.0176),(37.8371, -7.7168, 29.0176),(37.8371, 6.46341, 29.0176),(31.7899, 6.46341, 35.6756),(37.8371, 6.46341, 29.0176),(37.8371, -7.7168, 29.0176),(42.1739, -7.7168, 23.7645),(42.1739, -7.7168, 23.7645),(42.1739, 6.46341, 23.7645),(37.8371, 6.46341, 29.0176),(42.1739, 6.46341, 23.7645),(42.1739, -7.7168, 23.7645),(47.7324, -7.7168, 16.2514),(47.7324, -7.7168, 16.2514),(47.7324, 6.46341, 16.2514),(42.1739, 6.46341, 23.7645),(47.7324, 6.46341, 16.2514),(47.7324, -7.7168, 16.2514),(52.2525, -7.7168, 9.46394),(52.2525, -7.7168, 9.46394),(52.2525, 6.46341, 9.46394),(47.7324, 6.46341, 16.2514),(52.2525, 6.46341, 9.46394),(52.2525, -7.7168, 9.46394),(55.8513, -7.7168, 3.35219),(55.8513, -7.7168, 3.35219),(55.8513, 6.46341, 3.35219),(52.2525, 6.46341, 9.46394),(55.8513, 6.46341, 3.35219),(55.8513, -7.7168, 3.35219),(59.0276, -7.7168, -2.38955),(59.0276, -7.7168, -2.38955),(59.0276, 6.46341, -2.38955),(55.8513, 6.46341, 3.35219),(59.0276, 6.46341, -2.38955),(59.0276, -7.7168, -2.38955),(61.7152, -7.7168, -7.76479),(61.7152, -7.7168, -7.76479),(61.7152, 6.46341, -7.76479),(59.0276, 6.46341, -2.38955),(61.7152, 6.46341, -7.76479),(61.7152, -7.7168, -7.76479),(65.4412, -7.7168, -16.1331),(65.4412, -7.7168, -16.1331),(65.4412, 6.46341, -16.1331),(61.7152, 6.46341, -7.76479),(65.4412, 6.46341, -16.1331),(65.4412, -7.7168, -16.1331),(67.8845, -7.7168, -23.0354),(67.8845, -7.7168, -23.0354),(67.8845, 6.46341, -23.0354),(65.4412, 6.46341, -16.1331),(67.8845, 6.46341, -23.0354),(67.8845, -7.7168, -23.0354),(70.511, -7.7168, -32.0755),(70.511, -7.7168, -32.0755),(70.511, 6.46341, -32.0755),(67.8845, 6.46341, -23.0354),(70.511, 6.46341, -32.0755),(70.511, -7.7168, -32.0755),(48.3382, -7.7168, -39.2222),(48.3382, -7.7168, -39.2222),(48.3382, 6.46341, -39.2222),(70.511, 6.46341, -32.0755),(-15.8074, 6.46341, 47.4306),(-15.8074, -7.7168, 47.4306),(-8.20569, -7.7168, 53.3047),(-8.20569, -7.7168, 53.3047),(-8.20569, 6.46341, 53.3047),(-15.8074, 6.46341, 47.4306),(-24.1866, 6.46341, 39.9153),(-24.1866, -7.7168, 39.9153),(-15.8074, -7.7168, 47.4306),(-15.8074, -7.7168, 47.4306),(-15.8074, 6.46341, 47.4306),(-24.1866, 6.46341, 39.9153),(-30.7518, 6.46341, 33.091),(-30.7518, -7.7168, 33.091),(-24.1866, -7.7168, 39.9153),(-24.1866, -7.7168, 39.9153),(-24.1866, 6.46341, 39.9153),(-30.7518, 6.46341, 33.091),(-36.9714, 6.46341, 25.7484),(-36.9714, -7.7168, 25.7484),(-30.7518, -7.7168, 33.091),(-30.7518, -7.7168, 33.091),(-30.7518, 6.46341, 33.091),(-36.9714, 6.46341, 25.7484),(-42.6727, 6.46341, 18.233),(-42.6727, -7.7168, 18.233),(-36.9714, -7.7168, 25.7484),(-36.9714, -7.7168, 25.7484),(-36.9714, 6.46341, 25.7484),(-42.6727, 6.46341, 18.233),(-48.201, 6.46341, 9.46394),(-48.201, -7.7168, 9.46394),(-42.6727, -7.7168, 18.233),(-42.6727, -7.7168, 18.233),(-42.6727, 6.46341, 18.233),(-48.201, 6.46341, 9.46394),(-52.4338, 6.46341, 2.42471),(-52.4338, -7.7168, 2.42471),(-48.201, -7.7168, 9.46394),(-48.201, -7.7168, 9.46394),(-48.201, 6.46341, 9.46394),(-52.4338, 6.46341, 2.42471),(-55.7163, 6.46341, -4.05405),(-55.7163, -7.7168, -4.05405),(-52.4338, -7.7168, 2.42471),(-52.4338, -7.7168, 2.42471),(-52.4338, 6.46341, 2.42471),(-55.7163, 6.46341, -4.05405),(-59.5172, 6.46341, -12.3469),(-59.5172, -7.7168, -12.3469),(-55.7163, -7.7168, -4.05405),(-55.7163, -7.7168, -4.05405),(-55.7163, 6.46341, -4.05405),(-59.5172, 6.46341, -12.3469),(-63.0589, 6.46341, -21.158),(-63.0589, -7.7168, -21.158),(-59.5172, -7.7168, -12.3469),(-59.5172, -7.7168, -12.3469),(-59.5172, 6.46341, -12.3469),(-63.0589, 6.46341, -21.158),(-65.3913, 6.46341, -27.8095),(-65.3913, -7.7168, -27.8095),(-63.0589, -7.7168, -21.158),(-63.0589, -7.7168, -21.158),(-63.0589, 6.46341, -21.158),(-65.3913, 6.46341, -27.8095),(-65.8232, 6.46341, -30.8329),(-65.8232, -7.7168, -30.8329),(-65.3913, -7.7168, -27.8095),(-65.3913, -7.7168, -27.8095),(-65.3913, 6.46341, -27.8095),(-65.8232, 6.46341, -30.8329),(-64.7866, 6.46341, -33.338),(-64.7866, -7.7168, -33.338),(-65.8232, -7.7168, -30.8329),(-65.8232, -7.7168, -30.8329),(-65.8232, 6.46341, -30.8329),(-64.7866, 6.46341, -33.338),(-63.0589, 6.46341, -34.6338),(-63.0589, -7.7168, -34.6338),(-64.7866, -7.7168, -33.338),(-64.7866, -7.7168, -33.338),(-64.7866, 6.46341, -33.338),(-63.0589, 6.46341, -34.6338),(-60.2947, 6.46341, -35.4112),(-60.2947, -7.7168, -35.4112),(-63.0589, -7.7168, -34.6338),(-63.0589, -7.7168, -34.6338),(-63.0589, 6.46341, -34.6338),(-60.2947, 6.46341, -35.4112),(-49.0648, 6.46341, -36.3615),(-49.0648, -7.7168, -36.3615),(-60.2947, -7.7168, -35.4112),(-60.2947, -7.7168, -35.4112),(-60.2947, 6.46341, -35.4112),(-49.0648, 6.46341, -36.3615),(-39.3035, 6.46341, -36.7934),(-39.3035, -7.7168, -36.7934),(-49.0648, -7.7168, -36.3615),(-49.0648, -7.7168, -36.3615),(-49.0648, 6.46341, -36.3615),(-39.3035, 6.46341, -36.7934),(-31.9609, 6.46341, -36.7934),(-31.9609, -7.7168, -36.7934),(-39.3035, -7.7168, -36.7934),(-39.3035, -7.7168, -36.7934),(-39.3035, 6.46341, -36.7934),(-31.9609, 6.46341, -36.7934),(-22.0268, 6.46341, -36.0159),(-22.0268, -7.7168, -36.0159),(-31.9609, -7.7168, -36.7934),(-31.9609, -7.7168, -36.7934),(-31.9609, 6.46341, -36.7934),(-22.0268, 6.46341, -36.0159),(-11.4016, 6.46341, -34.2019),(-11.4016, -7.7168, -34.2019),(-22.0268, -7.7168, -36.0159),(-22.0268, -7.7168, -36.0159),(-22.0268, 6.46341, -36.0159),(-11.4016, 6.46341, -34.2019),(-1.81306, 6.46341, -31.8695),(-1.81306, -7.7168, -31.8695),(-11.4016, -7.7168, -34.2019),(-11.4016, -7.7168, -34.2019),(-11.4016, 6.46341, -34.2019),(-1.81306, 6.46341, -31.8695),(6.91933, 6.46341, -29.0107),(6.91933, -7.7168, -29.0107),(-1.81306, -7.7168, -31.8695),(-1.81306, -7.7168, -31.8695),(-1.81306, 6.46341, -31.8695),(6.91933, 6.46341, -29.0107),(15.9595, 6.46341, -24.9792),(15.9595, -7.7168, -24.9792),(6.91933, -7.7168, -29.0107),(6.91933, -7.7168, -29.0107),(6.91933, 6.46341, -29.0107),(15.9595, 6.46341, -24.9792),(25.6105, 6.46341, -19.604),(25.6105, -7.7168, -19.604),(15.9595, -7.7168, -24.9792),(15.9595, -7.7168, -24.9792),(15.9595, 6.46341, -24.9792),(25.6105, 6.46341, -19.604),(33.1847, 6.46341, -14.5952),(33.1847, -7.7168, -14.5952),(25.6105, -7.7168, -19.604),(25.6105, -7.7168, -19.604),(25.6105, 6.46341, -19.604),(33.1847, 6.46341, -14.5952),(30.1306, 6.46341, -7.87619),(30.1306, -7.7168, -7.87619),(33.1847, -7.7168, -14.5952),(33.1847, -7.7168, -14.5952),(33.1847, 6.46341, -14.5952),(30.1306, 6.46341, -7.87619),(27.3208, 6.46341, -2.50095),(27.3208, -7.7168, -2.50095),(30.1306, -7.7168, -7.87619),(30.1306, -7.7168, -7.87619),(30.1306, 6.46341, -7.87619),(27.3208, 6.46341, -2.50095),(23.5337, 6.46341, 2.99647),(23.5337, -7.7168, 2.99647),(27.3208, -7.7168, -2.50095),(27.3208, -7.7168, -2.50095),(27.3208, 6.46341, -2.50095),(23.5337, 6.46341, 2.99647),(17.5527, 6.46341, -0.519135),(17.5527, -7.7168, -0.519135),(23.5337, -7.7168, 2.99647),(23.5337, -7.7168, 2.99647),(23.5337, 6.46341, 2.99647),(17.5527, 6.46341, -0.519135),(11.2612, 6.46341, -3.93974),(11.2612, -7.7168, -3.93974),(17.5527, -7.7168, -0.519135),(17.5527, -7.7168, -0.519135),(17.5527, 6.46341, -0.519135),(11.2612, 6.46341, -3.93974),(4.49783, 6.46341, -6.68845),(4.49783, -7.7168, -6.68845),(11.2612, -7.7168, -3.93974),(11.2612, -7.7168, -3.93974),(11.2612, 6.46341, -3.93974),(4.49783, 6.46341, -6.68845),(-1.01632, 6.46341, -8.76525),(-1.01632, -7.7168, -8.76525),(4.49783, -7.7168, -6.68845),(4.49783, -7.7168, -6.68845),(4.49783, 6.46341, -6.68845),(-1.01632, 6.46341, -8.76525),(-8.22404, 6.46341, -11.2085),(-8.22404, -7.7168, -11.2085),(-1.01632, -7.7168, -8.76525),(-1.01632, -7.7168, -8.76525),(-1.01632, 6.46341, -8.76525),(-8.22404, 6.46341, -11.2085),(-16.5312, 6.46341, -13.2853),(-16.5312, -7.7168, -13.2853),(-8.22404, -7.7168, -11.2085),(-8.22404, -7.7168, -11.2085),(-8.22404, 6.46341, -11.2085),(-16.5312, 6.46341, -13.2853),(-23.9222, 6.46341, -14.6291),(-23.9222, -7.7168, -14.6291),(-16.5312, -7.7168, -13.2853),(-16.5312, -7.7168, -13.2853),(-16.5312, 6.46341, -13.2853),(-23.9222, 6.46341, -14.6291),(-30.2137, 6.46341, -15.1789),(-30.2137, -7.7168, -15.1789),(-23.9222, -7.7168, -14.6291),(-23.9222, -7.7168, -14.6291),(-23.9222, 6.46341, -14.6291),(-30.2137, 6.46341, -15.1789),(-36.5662, 6.46341, -15.1178),(-36.5662, -7.7168, -15.1178),(-30.2137, -7.7168, -15.1789),(-30.2137, -7.7168, -15.1789),(-30.2137, 6.46341, -15.1789),(-36.5662, 6.46341, -15.1178),(-36.9998, 6.46341, -14.7524),(-36.9998, -7.7168, -14.7524),(-36.5662, -7.7168, -15.1178),(-36.5662, -7.7168, -15.1178),(-36.5662, 6.46341, -15.1178),(-36.9998, 6.46341, -14.7524),(-36.8716, 6.46341, -14.1405),(-36.8716, -7.7168, -14.1405),(-36.9998, -7.7168, -14.7524),(-36.9998, -7.7168, -14.7524),(-36.9998, 6.46341, -14.7524),(-36.8716, 6.46341, -14.1405),(-33.8786, 6.46341, -7.84901),(-33.8786, -7.7168, -7.84901),(-36.8716, -7.7168, -14.1405),(-36.8716, -7.7168, -14.1405),(-36.8716, 6.46341, -14.1405),(-33.8786, 6.46341, -7.84901),(-31.0077, 6.46341, -2.59593),(-31.0077, -7.7168, -2.59593),(-33.8786, -7.7168, -7.84901),(-33.8786, -7.7168, -7.84901),(-33.8786, 6.46341, -7.84901),(-31.0077, 6.46341, -2.59593),(-27.465, 6.46341, 3.02364),(-27.465, -7.7168, 3.02364),(-31.0077, -7.7168, -2.59593),(-31.0077, -7.7168, -2.59593),(-31.0077, 6.46341, -2.59593),(-27.465, 6.46341, 3.02364),(-22.8986, 6.46341, 9.46394),(-22.8986, -7.7168, 9.46394),(-27.465, -7.7168, 3.02364),(-27.465, -7.7168, 3.02364),(-27.465, 6.46341, 3.02364),(-22.8986, 6.46341, 9.46394),(-16.0574, 6.46341, 17.8011),(-16.0574, -7.7168, 17.8011),(-22.8986, -7.7168, 9.46394),(-22.8986, -7.7168, 9.46394),(-22.8986, 6.46341, 9.46394),(-16.0574, 6.46341, 17.8011),(-9.76589, 6.46341, 24.4591),(-9.76589, -7.7168, 24.4591),(-16.0574, -7.7168, 17.8011),(-16.0574, -7.7168, 17.8011),(-16.0574, 6.46341, 17.8011),(-9.76589, 6.46341, 24.4591),(-3.53549, 6.46341, 30.0176),(-3.53549, -7.7168, 30.0176),(-9.76589, -7.7168, 24.4591),(-9.76589, -7.7168, 24.4591),(-9.76589, 6.46341, 24.4591),(-3.53549, 6.46341, 30.0176),(1.35109, 6.46341, 33.6825),(1.35109, -7.7168, 33.6825),(-3.53549, -7.7168, 30.0176),(-3.53549, -7.7168, 30.0176),(-3.53549, 6.46341, 30.0176),(1.35109, 6.46341, 33.6825),(5.8101, 6.46341, 30.2619),(5.8101, -7.7168, 30.2619),(1.35109, -7.7168, 33.6825),(1.35109, -7.7168, 33.6825),(1.35109, 6.46341, 33.6825),(5.8101, 6.46341, 30.2619),(10.941, 6.46341, 25.5586),(10.941, -7.7168, 25.5586),(5.8101, -7.7168, 30.2619),(5.8101, -7.7168, 30.2619),(5.8101, 6.46341, 30.2619),(10.941, 6.46341, 25.5586),(15.7054, 6.46341, 20.7331),(15.7054, -7.7168, 20.7331),(10.941, -7.7168, 25.5586),(10.941, -7.7168, 25.5586),(10.941, 6.46341, 25.5586),(15.7054, 6.46341, 20.7331),(20.6531, 6.46341, 14.9303),(20.6531, -7.7168, 14.9303),(15.7054, -7.7168, 20.7331),(15.7054, -7.7168, 20.7331),(15.7054, 6.46341, 20.7331),(20.6531, 6.46341, 14.9303),(27.0608, 6.46341, 6.60854),(27.0608, -7.7168, 6.60854),(20.6531, -7.7168, 14.9303),(20.6531, -7.7168, 14.9303),(20.6531, 6.46341, 14.9303),(27.0608, 6.46341, 6.60854),(30.6025, 6.46341, 1.25276),(30.6025, -7.7168, 1.25276),(27.0608, -7.7168, 6.60854),(27.0608, -7.7168, 6.60854),(27.0608, 6.46341, 6.60854),(30.6025, 6.46341, 1.25276),(34.6625, 6.46341, -5.83068),(34.6625, -7.7168, -5.83068),(30.6025, -7.7168, 1.25276),(30.6025, -7.7168, 1.25276),(30.6025, 6.46341, 1.25276),(34.6625, 6.46341, -5.83068),(38.0315, 6.46341, -12.1367),(38.0315, -7.7168, -12.1367),(34.6625, -7.7168, -5.83068),(34.6625, -7.7168, -5.83068),(34.6625, 6.46341, -5.83068),(38.0315, 6.46341, -12.1367),(40.9685, 6.46341, -18.7018),(40.9685, -7.7168, -18.7018),(38.0315, -7.7168, -12.1367),(38.0315, -7.7168, -12.1367),(38.0315, 6.46341, -12.1367),(40.9685, 6.46341, -18.7018),(43.9056, 6.46341, -25.4397),(43.9056, -7.7168, -25.4397),(40.9685, -7.7168, -18.7018),(40.9685, -7.7168, -18.7018),(40.9685, 6.46341, -18.7018),(43.9056, 6.46341, -25.4397),(46.3243, 6.46341, -32.6095),(46.3243, -7.7168, -32.6095),(43.9056, -7.7168, -25.4397),(43.9056, -7.7168, -25.4397),(43.9056, 6.46341, -25.4397),(46.3243, 6.46341, -32.6095),(48.3382, 6.46341, -39.2222),(48.3382, -7.7168, -39.2222),(46.3243, -7.7168, -32.6095),(46.3243, -7.7168, -32.6095),(46.3243, 6.46341, -32.6095),(48.3382, 6.46341, -39.2222),(-0.342632, -9.7168, -10.6487),(-1.01632, -7.7168, -8.76525),(-8.22404, -7.7168, -11.2085),(-8.22404, -7.7168, -11.2085),(-7.65952, -9.7168, -13.129),(-0.342632, -9.7168, -10.6487),(-7.65952, -9.7168, -13.129),(-8.22404, -7.7168, -11.2085),(-16.5312, -7.7168, -13.2853),(-16.5312, -7.7168, -13.2853),(-16.1094, -9.7168, -15.2414),(-7.65952, -9.7168, -13.129),(-16.1094, -9.7168, -15.2414),(-16.5312, -7.7168, -13.2853),(-23.9222, -7.7168, -14.6291),(-23.9222, -7.7168, -14.6291),(-23.6557, -9.7168, -16.6135),(-16.1094, -9.7168, -15.2414),(-23.6557, -9.7168, -16.6135),(-23.9222, -7.7168, -14.6291),(-30.2137, -7.7168, -15.1789),(-30.2137, -7.7168, -15.1789),(-30.1361, -9.7168, -17.1797),(-23.6557, -9.7168, -16.6135),(-30.1361, -9.7168, -17.1797),(-30.2137, -7.7168, -15.1789),(-36.5662, -7.7168, -15.1178),(-36.5662, -7.7168, -15.1178),(-36.7622, -9.7168, -17.0322),(-30.1361, -9.7168, -17.1797),(-36.7622, -9.7168, -17.0322),(-36.5662, -7.7168, -15.1178),(-36.9998, -7.7168, -14.7524),(-36.9998, -7.7168, -14.7524),(-38.8807, -9.7168, -16.1225),(-36.7622, -9.7168, -17.0322),(-38.8807, -9.7168, -16.1225),(-36.9998, -7.7168, -14.7524),(-36.8716, -7.7168, -14.1405),(-36.8716, -7.7168, -14.1405),(-39.1325, -9.7168, -13.9348),(-38.8807, -9.7168, -16.1225),(-39.1325, -9.7168, -13.9348),(-36.8716, -7.7168, -14.1405),(-33.8786, -7.7168, -7.84901),(-33.8786, -7.7168, -7.84901),(-35.6605, -9.7168, -6.93914),(-39.1325, -9.7168, -13.9348),(-35.6605, -9.7168, -6.93914),(-33.8786, -7.7168, -7.84901),(-31.0077, -7.7168, -2.59593),(-31.0077, -7.7168, -2.59593),(-32.7328, -9.7168, -1.58208),(-35.6605, -9.7168, -6.93914),(-32.7328, -9.7168, -1.58208),(-31.0077, -7.7168, -2.59593),(-27.465, -7.7168, 3.02364),(-27.465, -7.7168, 3.02364),(-29.1279, -9.7168, 4.13616),(-32.7328, -9.7168, -1.58208),(-29.1279, -9.7168, 4.13616),(-27.465, -7.7168, 3.02364),(-22.8986, -7.7168, 9.46394),(-22.8986, -7.7168, 9.46394),(-24.4894, -9.7168, 10.6782),(-29.1279, -9.7168, 4.13616),(-24.4894, -9.7168, 10.6782),(-22.8986, -7.7168, 9.46394),(-16.0574, -7.7168, 17.8011),(-16.0574, -7.7168, 17.8011),(-17.5591, -9.7168, 19.1239),(-24.4894, -9.7168, 10.6782),(-17.5591, -9.7168, 19.1239),(-16.0574, -7.7168, 17.8011),(-9.76589, -7.7168, 24.4591),(-9.76589, -7.7168, 24.4591),(-11.161, -9.7168, 25.8947),(-17.5591, -9.7168, 19.1239),(-11.161, -9.7168, 25.8947),(-9.76589, -7.7168, 24.4591),(-3.53549, -7.7168, 30.0176),(-3.53549, -7.7168, 30.0176),(-4.8035, -9.7168, 31.5666),(-11.161, -9.7168, 25.8947),(-4.8035, -9.7168, 31.5666),(-3.53549, -7.7168, 30.0176),(1.35109, -7.7168, 33.6825),(1.35109, -7.7168, 33.6825),(1.36473, -9.7168, 36.1928),(-4.8035, -9.7168, 31.5666),(1.36473, -9.7168, 36.1928),(1.35109, -7.7168, 33.6825),(5.8101, -7.7168, 30.2619),(5.8101, -7.7168, 30.2619),(7.09695, -9.7168, 31.7955),(1.36473, -9.7168, 36.1928),(7.09695, -9.7168, 31.7955),(5.8101, -7.7168, 30.2619),(10.941, -7.7168, 25.5586),(10.941, -7.7168, 25.5586),(12.3292, -9.7168, 26.9992),(7.09695, -9.7168, 31.7955),(12.3292, -9.7168, 26.9992),(10.941, -7.7168, 25.5586),(15.7054, -7.7168, 20.7331),(15.7054, -7.7168, 20.7331),(17.1799, -9.7168, 22.0863),(12.3292, -9.7168, 26.9992),(17.1799, -9.7168, 22.0863),(15.7054, -7.7168, 20.7331),(20.6531, -7.7168, 14.9303),(20.6531, -7.7168, 14.9303),(22.2073, -9.7168, 16.19),(17.1799, -9.7168, 22.0863),(22.2073, -9.7168, 16.19),(20.6531, -7.7168, 14.9303),(27.0608, -7.7168, 6.60854),(27.0608, -7.7168, 6.60854),(28.6893, -9.7168, 7.77172),(22.2073, -9.7168, 16.19),(28.6893, -9.7168, 7.77172),(27.0608, -7.7168, 6.60854),(30.6025, -7.7168, 1.25276),(30.6025, -7.7168, 1.25276),(32.306, -9.7168, 2.3027),(28.6893, -9.7168, 7.77172),(32.306, -9.7168, 2.3027),(30.6025, -7.7168, 1.25276),(34.6625, -7.7168, -5.83068),(34.6625, -7.7168, -5.83068),(36.4125, -9.7168, -4.86197),(32.306, -9.7168, 2.3027),(36.4125, -9.7168, -4.86197),(34.6625, -7.7168, -5.83068),(38.0315, -7.7168, -12.1367),(38.0315, -7.7168, -12.1367),(39.8285, -9.7168, -11.256),(36.4125, -9.7168, -4.86197),(39.8285, -9.7168, -11.256),(38.0315, -7.7168, -12.1367),(40.9685, -7.7168, -18.7018),(40.9685, -7.7168, -18.7018),(42.7981, -9.7168, -17.8939),(39.8285, -9.7168, -11.256),(42.7981, -9.7168, -17.8939),(40.9685, -7.7168, -18.7018),(43.9056, -7.7168, -25.4397),(43.9056, -7.7168, -25.4397),(45.7732, -9.7168, -24.7192),(42.7981, -9.7168, -17.8939),(45.7732, -9.7168, -24.7192),(43.9056, -7.7168, -25.4397),(46.3243, -7.7168, -32.6095),(46.3243, -7.7168, -32.6095),(48.2289, -9.7168, -31.9984),(45.7732, -9.7168, -24.7192),(48.2289, -9.7168, -31.9984),(46.3243, -7.7168, -32.6095),(48.3382, -7.7168, -39.2222),(48.3382, -7.7168, -39.2222),(49.6592, -9.7168, -36.695),(48.2289, -9.7168, -31.9984),(49.6592, -9.7168, -36.695),(48.3382, -7.7168, -39.2222),(70.511, -7.7168, -32.0755),(70.511, -7.7168, -32.0755),(68.0484, -9.7168, -30.768),(49.6592, -9.7168, -36.695),(68.0484, -9.7168, -30.768),(70.511, -7.7168, -32.0755),(67.8845, -7.7168, -23.0354),(67.8845, -7.7168, -23.0354),(65.9799, -9.7168, -23.6486),(68.0484, -9.7168, -30.768),(65.9799, -9.7168, -23.6486),(67.8845, -7.7168, -23.0354),(65.4412, -7.7168, -16.1331),(65.4412, -7.7168, -16.1331),(63.5821, -9.7168, -16.8747),(65.9799, -9.7168, -23.6486),(63.5821, -9.7168, -16.8747),(65.4412, -7.7168, -16.1331),(61.7152, -7.7168, -7.76479),(61.7152, -7.7168, -7.76479),(59.9063, -9.7168, -8.61919),(63.5821, -9.7168, -16.8747),(59.9063, -9.7168, -8.61919),(61.7152, -7.7168, -7.76479),(59.0276, -7.7168, -2.38955),(59.0276, -7.7168, -2.38955),(57.2573, -9.7168, -3.32123),(59.9063, -9.7168, -8.61919),(57.2573, -9.7168, -3.32123),(59.0276, -7.7168, -2.38955),(55.8513, -7.7168, 3.35219),(55.8513, -7.7168, 3.35219),(54.1142, -9.7168, 2.36055),(57.2573, -9.7168, -3.32123),(54.1142, -9.7168, 2.36055),(55.8513, -7.7168, 3.35219),(52.2525, -7.7168, 9.46394),(52.2525, -7.7168, 9.46394),(50.5572, -9.7168, 8.40144),(54.1142, -9.7168, 2.36055),(50.5572, -9.7168, 8.40144),(52.2525, -7.7168, 9.46394),(47.7324, -7.7168, 16.2514),(47.7324, -7.7168, 16.2514),(46.0952, -9.7168, 15.1017),(50.5572, -9.7168, 8.40144),(46.0952, -9.7168, 15.1017),(47.7324, -7.7168, 16.2514),(42.1739, -7.7168, 23.7645),(42.1739, -7.7168, 23.7645),(40.5978, -9.7168, 22.5323),(46.0952, -9.7168, 15.1017),(40.5978, -9.7168, 22.5323),(42.1739, -7.7168, 23.7645),(37.8371, -7.7168, 29.0176),(37.8371, -7.7168, 29.0176),(36.3249, -9.7168, 27.7079),(40.5978, -9.7168, 22.5323),(36.3249, -9.7168, 27.7079),(37.8371, -7.7168, 29.0176),(31.7899, -7.7168, 35.6756),(31.7899, -7.7168, 35.6756),(30.3574, -9.7168, 34.2781),(36.3249, -9.7168, 27.7079),(30.3574, -9.7168, 34.2781),(31.7899, -7.7168, 35.6756),(25.0709, -7.7168, 42.0892),(25.0709, -7.7168, 42.0892),(23.7326, -9.7168, 40.6018),(30.3574, -9.7168, 34.2781),(23.7326, -9.7168, 40.6018),(25.0709, -7.7168, 42.0892),(19.4513, -7.7168, 46.8536),(19.4513, -7.7168, 46.8536),(18.2159, -9.7168, 45.279),(23.7326, -9.7168, 40.6018),(18.2159, -9.7168, 45.279),(19.4513, -7.7168, 46.8536),(14.5647, -7.7168, 50.3964),(14.5647, -7.7168, 50.3964),(13.4516, -9.7168, 48.7331),(18.2159, -9.7168, 45.279),(13.4516, -9.7168, 48.7331),(14.5647, -7.7168, 50.3964),(9.31166, -7.7168, 53.6338),(9.31166, -7.7168, 53.6338),(8.33187, -9.7168, 51.8883),(13.4516, -9.7168, 48.7331),(8.33187, -9.7168, 51.8883),(9.31166, -7.7168, 53.6338),(1.64202, -7.7168, 57.5364),(1.64202, -7.7168, 57.5364),(1.00884, -9.7168, 56.0242),(8.33187, -9.7168, 51.8883),(1.00884, -9.7168, 56.0242),(1.64202, -7.7168, 57.5364),(0.0871229, -7.7168, 57.966),(0.0871229, -7.7168, 57.966),(0.0860662, -9.7168, 56.2969),(1.00884, -9.7168, 56.0242),(0.0860662, -9.7168, 56.2969),(0.0871229, -7.7168, 57.966),(-1.46778, -7.7168, 57.5386),(-1.46778, -7.7168, 57.5386),(-0.768229, -9.7168, 56.0568),(0.0860662, -9.7168, 56.2969),(-0.768229, -9.7168, 56.0568),(-1.46778, -7.7168, 57.5386),(-8.20569, -7.7168, 53.3047),(-8.20569, -7.7168, 53.3047),(-7.0595, -9.7168, 51.6628),(-0.768229, -9.7168, 56.0568),(-7.0595, -9.7168, 51.6628),(-8.20569, -7.7168, 53.3047),(-15.8074, -7.7168, 47.4306),(-15.8074, -7.7168, 47.4306),(-14.5266, -9.7168, 45.8928),(-7.0595, -9.7168, 51.6628),(-14.5266, -9.7168, 45.8928),(-15.8074, -7.7168, 47.4306),(-24.1866, -7.7168, 39.9153),(-24.1866, -7.7168, 39.9153),(-22.7964, -9.7168, 38.4756),(-14.5266, -9.7168, 45.8928),(-22.7964, -9.7168, 38.4756),(-24.1866, -7.7168, 39.9153),(-30.7518, -7.7168, 33.091),(-30.7518, -7.7168, 33.091),(-29.2666, -9.7168, 31.75),(-22.7964, -9.7168, 38.4756),(-29.2666, -9.7168, 31.75),(-30.7518, -7.7168, 33.091),(-36.9714, -7.7168, 25.7484),(-36.9714, -7.7168, 25.7484),(-35.4105, -9.7168, 24.4967),(-29.2666, -9.7168, 31.75),(-35.4105, -9.7168, 24.4967),(-36.9714, -7.7168, 25.7484),(-42.6727, -7.7168, 18.233),(-42.6727, -7.7168, 18.233),(-41.027, -9.7168, 17.0932),(-35.4105, -9.7168, 24.4967),(-41.027, -9.7168, 17.0932),(-42.6727, -7.7168, 18.233),(-48.201, -7.7168, 9.46394),(-48.201, -7.7168, 9.46394),(-46.4979, -9.7168, 8.4152),(-41.027, -9.7168, 17.0932),(-46.4979, -9.7168, 8.4152),(-48.201, -7.7168, 9.46394),(-52.4338, -7.7168, 2.42471),(-52.4338, -7.7168, 2.42471),(-50.6824, -9.7168, 1.45615),(-46.4979, -9.7168, 8.4152),(-50.6824, -9.7168, 1.45615),(-52.4338, -7.7168, 2.42471),(-55.7163, -7.7168, -4.05405),(-55.7163, -7.7168, -4.05405),(-53.9145, -9.7168, -4.923),(-50.6824, -9.7168, 1.45615),(-53.9145, -9.7168, -4.923),(-55.7163, -7.7168, -4.05405),(-59.5172, -7.7168, -12.3469),(-59.5172, -7.7168, -12.3469),(-57.6792, -9.7168, -13.1369),(-53.9145, -9.7168, -4.923),(-57.6792, -9.7168, -13.1369),(-59.5172, -7.7168, -12.3469),(-63.0589, -7.7168, -21.158),(-63.0589, -7.7168, -21.158),(-61.1865, -9.7168, -21.8622),(-57.6792, -9.7168, -13.1369),(-61.1865, -9.7168, -21.8622),(-63.0589, -7.7168, -21.158),(-65.3913, -7.7168, -27.8095),(-65.3913, -7.7168, -27.8095),(-63.4391, -9.7168, -28.2864),(-61.1865, -9.7168, -21.8622),(-63.4391, -9.7168, -28.2864),(-65.3913, -7.7168, -27.8095),(-65.8232, -7.7168, -30.8329),(-65.8232, -7.7168, -30.8329),(-63.7659, -9.7168, -30.5739),(-63.4391, -9.7168, -28.2864),(-63.7659, -9.7168, -30.5739),(-65.8232, -7.7168, -30.8329),(-64.7866, -7.7168, -33.338),(-64.7866, -7.7168, -33.338),(-63.1481, -9.7168, -32.0669),(-63.7659, -9.7168, -30.5739),(-63.1481, -9.7168, -32.0669),(-64.7866, -7.7168, -33.338),(-63.0589, -7.7168, -34.6338),(-63.0589, -7.7168, -34.6338),(-62.1578, -9.7168, -32.8096),(-63.1481, -9.7168, -32.0669),(-62.1578, -9.7168, -32.8096),(-63.0589, -7.7168, -34.6338),(-60.2947, -7.7168, -35.4112),(-60.2947, -7.7168, -35.4112),(-59.9364, -9.7168, -33.4344),(-62.1578, -9.7168, -32.8096),(-59.9364, -9.7168, -33.4344),(-60.2947, -7.7168, -35.4112),(-49.0648, -7.7168, -36.3615),(-49.0648, -7.7168, -36.3615),(-48.9362, -9.7168, -34.3652),(-59.9364, -9.7168, -33.4344),(-48.9362, -9.7168, -34.3652),(-49.0648, -7.7168, -36.3615),(-39.3035, -7.7168, -36.7934),(-39.3035, -7.7168, -36.7934),(-39.2592, -9.7168, -34.7934),(-48.9362, -9.7168, -34.3652),(-39.2592, -9.7168, -34.7934),(-39.3035, -7.7168, -36.7934),(-31.9609, -7.7168, -36.7934),(-31.9609, -7.7168, -36.7934),(-32.039, -9.7168, -34.7934),(-39.2592, -9.7168, -34.7934),(-32.039, -9.7168, -34.7934),(-31.9609, -7.7168, -36.7934),(-22.0268, -7.7168, -36.0159),(-22.0268, -7.7168, -36.0159),(-22.2736, -9.7168, -34.0291),(-32.039, -9.7168, -34.7934),(-22.2736, -9.7168, -34.0291),(-22.0268, -7.7168, -36.0159),(-11.4016, -7.7168, -34.2019),(-11.4016, -7.7168, -34.2019),(-11.8068, -9.7168, -32.2421),(-22.2736, -9.7168, -34.0291),(-11.8068, -9.7168, -32.2421),(-11.4016, -7.7168, -34.2019),(-1.81306, -7.7168, -31.8695),(-1.81306, -7.7168, -31.8695),(-2.36138, -9.7168, -29.9446),(-11.8068, -9.7168, -32.2421),(-2.36138, -9.7168, -29.9446),(-1.81306, -7.7168, -31.8695),(6.91933, -7.7168, -29.0107),(6.91933, -7.7168, -29.0107),(6.199, -9.7168, -27.142),(-2.36138, -9.7168, -29.9446),(6.199, -9.7168, -27.142),(6.91933, -7.7168, -29.0107),(15.9595, -7.7168, -24.9792),(15.9595, -7.7168, -24.9792),(15.0639, -9.7168, -23.1888),(6.199, -9.7168, -27.142),(15.0639, -9.7168, -23.1888),(15.9595, -7.7168, -24.9792),(25.6105, -7.7168, -19.604),(25.6105, -7.7168, -19.604),(24.5708, -9.7168, -17.8938),(15.0639, -9.7168, -23.1888),(24.5708, -9.7168, -17.8938),(25.6105, -7.7168, -19.604),(33.1847, -7.7168, -14.5952),(33.1847, -7.7168, -14.5952),(30.6576, -9.7168, -13.8687),(24.5708, -9.7168, -17.8938),(30.6576, -9.7168, -13.8687),(33.1847, -7.7168, -14.5952),(30.1306, -7.7168, -7.87619),(30.1306, -7.7168, -7.87619),(28.3327, -9.7168, -8.75391),(30.6576, -9.7168, -13.8687),(28.3327, -9.7168, -8.75391),(30.1306, -7.7168, -7.87619),(27.3208, -7.7168, -2.50095),(27.3208, -7.7168, -2.50095),(25.6048, -9.7168, -3.53532),(28.3327, -9.7168, -8.75391),(25.6048, -9.7168, -3.53532),(27.3208, -7.7168, -2.50095),(23.5337, -7.7168, 2.99647),(23.5337, -7.7168, 2.99647),(22.9426, -9.7168, 0.329102),(25.6048, -9.7168, -3.53532),(22.9426, -9.7168, 0.329102),(23.5337, -7.7168, 2.99647),(17.5527, -7.7168, -0.519135),(17.5527, -7.7168, -0.519135),(18.5374, -9.7168, -2.26027),(22.9426, -9.7168, 0.329102),(18.5374, -9.7168, -2.26027),(17.5527, -7.7168, -0.519135),(11.2612, -7.7168, -3.93974),(11.2612, -7.7168, -3.93974),(12.1181, -9.7168, -5.75037),(18.5374, -9.7168, -2.26027),(12.1181, -9.7168, -5.75037),(11.2612, -7.7168, -3.93974),(4.49783, -7.7168, -6.68845),(4.49783, -7.7168, -6.68845),(5.22691, -9.7168, -8.55099),(12.1181, -9.7168, -5.75037),(5.22691, -9.7168, -8.55099),(4.49783, -7.7168, -6.68845),(-1.01632, -7.7168, -8.76525),(-1.01632, -7.7168, -8.76525),(-0.342632, -9.7168, -10.6487),(5.22691, -9.7168, -8.55099),(0.0860662, -9.7168, 56.2969),(-0.768229, -9.7168, 56.0568),(1.36473, -9.7168, 36.1928),(-0.768229, -9.7168, 56.0568),(-7.0595, -9.7168, 51.6628),(1.36473, -9.7168, 36.1928),(1.00884, -9.7168, 56.0242),(0.0860662, -9.7168, 56.2969),(1.36473, -9.7168, 36.1928),(0.0860662, 8.46341, 56.2968),(1.00884, 8.46341, 56.0242),(1.36473, 8.46341, 36.1928),(1.00884, 8.46341, 56.0242),(8.33187, 8.46341, 51.8883),(1.36473, 8.46341, 36.1928),(-0.768229, 8.46341, 56.0568),(0.0860662, 8.46341, 56.2968),(1.36473, 8.46341, 36.1928),(-36.7622, 8.46341, -17.0322),(-38.8807, 8.46341, -16.1225),(-36.9998, 6.46341, -14.7524),(-36.9998, 6.46341, -14.7524),(-36.5662, 6.46341, -15.1178),(-36.7622, 8.46341, -17.0322),(-38.8807, 8.46341, -16.1225),(-39.1325, 8.46341, -13.9348),(-36.8716, 6.46341, -14.1405),(-36.8716, 6.46341, -14.1405),(-36.9998, 6.46341, -14.7524),(-38.8807, 8.46341, -16.1225),(-0.342632, 8.46341, -10.6487),(-7.65952, 8.46341, -13.129),(-8.22404, 6.46341, -11.2085),(-8.22404, 6.46341, -11.2085),(-1.01632, 6.46341, -8.76525),(-0.342632, 8.46341, -10.6487),(-7.65952, 8.46341, -13.129),(-16.1094, 8.46341, -15.2414),(-16.5312, 6.46341, -13.2853),(-16.5312, 6.46341, -13.2853),(-8.22404, 6.46341, -11.2085),(-7.65952, 8.46341, -13.129),(-16.1094, 8.46341, -15.2414),(-23.6557, 8.46341, -16.6135),(-23.9222, 6.46341, -14.6291),(-23.9222, 6.46341, -14.6291),(-16.5312, 6.46341, -13.2853),(-16.1094, 8.46341, -15.2414),(-23.6557, 8.46341, -16.6135),(-30.1361, 8.46341, -17.1797),(-30.2137, 6.46341, -15.1789),(-30.2137, 6.46341, -15.1789),(-23.9222, 6.46341, -14.6291),(-23.6557, 8.46341, -16.6135),(-30.1361, 8.46341, -17.1797),(-36.7622, 8.46341, -17.0322),(-36.5662, 6.46341, -15.1178),(-36.5662, 6.46341, -15.1178),(-30.2137, 6.46341, -15.1789),(-30.1361, 8.46341, -17.1797),(-39.1325, 8.46341, -13.9348),(-35.6605, 8.46341, -6.93914),(-33.8786, 6.46341, -7.84901),(-33.8786, 6.46341, -7.84901),(-36.8716, 6.46341, -14.1405),(-39.1325, 8.46341, -13.9348),(-35.6605, 8.46341, -6.93914),(-32.7328, 8.46341, -1.58208),(-31.0077, 6.46341, -2.59593),(-31.0077, 6.46341, -2.59593),(-33.8786, 6.46341, -7.84901),(-35.6605, 8.46341, -6.93914),(-32.7328, 8.46341, -1.58208),(-29.1279, 8.46341, 4.13616),(-27.465, 6.46341, 3.02364),(-27.465, 6.46341, 3.02364),(-31.0077, 6.46341, -2.59593),(-32.7328, 8.46341, -1.58208),(-29.1279, 8.46341, 4.13616),(-24.4894, 8.46341, 10.6782),(-22.8986, 6.46341, 9.46394),(-22.8986, 6.46341, 9.46394),(-27.465, 6.46341, 3.02364),(-29.1279, 8.46341, 4.13616),(-24.4894, 8.46341, 10.6782),(-17.5591, 8.46341, 19.1239),(-16.0574, 6.46341, 17.8011),(-16.0574, 6.46341, 17.8011),(-22.8986, 6.46341, 9.46394),(-24.4894, 8.46341, 10.6782),(-17.5591, 8.46341, 19.1239),(-11.161, 8.46341, 25.8947),(-9.76589, 6.46341, 24.4591),(-9.76589, 6.46341, 24.4591),(-16.0574, 6.46341, 17.8011),(-17.5591, 8.46341, 19.1239),(-11.161, 8.46341, 25.8947),(-4.8035, 8.46341, 31.5666),(-3.53549, 6.46341, 30.0176),(-3.53549, 6.46341, 30.0176),(-9.76589, 6.46341, 24.4591),(-11.161, 8.46341, 25.8947),(-4.8035, 8.46341, 31.5666),(1.36473, 8.46341, 36.1928),(1.35109, 6.46341, 33.6825),(1.35109, 6.46341, 33.6825),(-3.53549, 6.46341, 30.0176),(-4.8035, 8.46341, 31.5666),(1.36473, 8.46341, 36.1928),(7.09695, 8.46341, 31.7955),(5.8101, 6.46341, 30.2619),(5.8101, 6.46341, 30.2619),(1.35109, 6.46341, 33.6825),(1.36473, 8.46341, 36.1928),(7.09695, 8.46341, 31.7955),(12.3292, 8.46341, 26.9992),(10.941, 6.46341, 25.5586),(10.941, 6.46341, 25.5586),(5.8101, 6.46341, 30.2619),(7.09695, 8.46341, 31.7955),(12.3292, 8.46341, 26.9992),(17.1799, 8.46341, 22.0863),(15.7054, 6.46341, 20.7331),(15.7054, 6.46341, 20.7331),(10.941, 6.46341, 25.5586),(12.3292, 8.46341, 26.9992),(17.1799, 8.46341, 22.0863),(22.2073, 8.46341, 16.19),(20.6531, 6.46341, 14.9303),(20.6531, 6.46341, 14.9303),(15.7054, 6.46341, 20.7331),(17.1799, 8.46341, 22.0863),(22.2073, 8.46341, 16.19),(28.6893, 8.46341, 7.77172),(27.0608, 6.46341, 6.60854),(27.0608, 6.46341, 6.60854),(20.6531, 6.46341, 14.9303),(22.2073, 8.46341, 16.19),(28.6893, 8.46341, 7.77172),(32.306, 8.46341, 2.3027),(30.6025, 6.46341, 1.25276),(30.6025, 6.46341, 1.25276),(27.0608, 6.46341, 6.60854),(28.6893, 8.46341, 7.77172),(32.306, 8.46341, 2.3027),(36.4125, 8.46341, -4.86197),(34.6625, 6.46341, -5.83068),(34.6625, 6.46341, -5.83068),(30.6025, 6.46341, 1.25276),(32.306, 8.46341, 2.3027),(36.4125, 8.46341, -4.86197),(39.8285, 8.46341, -11.256),(38.0315, 6.46341, -12.1367),(38.0315, 6.46341, -12.1367),(34.6625, 6.46341, -5.83068),(36.4125, 8.46341, -4.86197),(39.8285, 8.46341, -11.256),(42.7981, 8.46341, -17.8939),(40.9685, 6.46341, -18.7018),(40.9685, 6.46341, -18.7018),(38.0315, 6.46341, -12.1367),(39.8285, 8.46341, -11.256),(42.7981, 8.46341, -17.8939),(45.7732, 8.46341, -24.7192),(43.9056, 6.46341, -25.4397),(43.9056, 6.46341, -25.4397),(40.9685, 6.46341, -18.7018),(42.7981, 8.46341, -17.8939),(45.7732, 8.46341, -24.7192),(48.2289, 8.46341, -31.9984),(46.3243, 6.46341, -32.6095),(46.3243, 6.46341, -32.6095),(43.9056, 6.46341, -25.4397),(45.7732, 8.46341, -24.7192),(48.2289, 8.46341, -31.9984),(49.6592, 8.46341, -36.695),(48.3382, 6.46341, -39.2222),(48.3382, 6.46341, -39.2222),(46.3243, 6.46341, -32.6095),(48.2289, 8.46341, -31.9984),(49.6592, 8.46341, -36.695),(68.0484, 8.46341, -30.768),(70.511, 6.46341, -32.0755),(70.511, 6.46341, -32.0755),(48.3382, 6.46341, -39.2222),(49.6592, 8.46341, -36.695),(68.0484, 8.46341, -30.768),(65.9799, 8.46341, -23.6486),(67.8845, 6.46341, -23.0354),(67.8845, 6.46341, -23.0354),(70.511, 6.46341, -32.0755),(68.0484, 8.46341, -30.768),(65.9799, 8.46341, -23.6486),(63.5821, 8.46341, -16.8747),(65.4412, 6.46341, -16.1331),(65.4412, 6.46341, -16.1331),(67.8845, 6.46341, -23.0354),(65.9799, 8.46341, -23.6486),(63.5821, 8.46341, -16.8747),(59.9063, 8.46341, -8.61919),(61.7152, 6.46341, -7.76479),(61.7152, 6.46341, -7.76479),(65.4412, 6.46341, -16.1331),(63.5821, 8.46341, -16.8747),(59.9063, 8.46341, -8.61919),(57.2573, 8.46341, -3.32123),(59.0276, 6.46341, -2.38955),(59.0276, 6.46341, -2.38955),(61.7152, 6.46341, -7.76479),(59.9063, 8.46341, -8.61919),(57.2573, 8.46341, -3.32123),(54.1142, 8.46341, 2.36055),(55.8513, 6.46341, 3.35219),(55.8513, 6.46341, 3.35219),(59.0276, 6.46341, -2.38955),(57.2573, 8.46341, -3.32123),(54.1142, 8.46341, 2.36055),(50.5572, 8.46341, 8.40144),(52.2525, 6.46341, 9.46394),(52.2525, 6.46341, 9.46394),(55.8513, 6.46341, 3.35219),(54.1142, 8.46341, 2.36055),(50.5572, 8.46341, 8.40144),(46.0952, 8.46341, 15.1017),(47.7324, 6.46341, 16.2514),(47.7324, 6.46341, 16.2514),(52.2525, 6.46341, 9.46394),(50.5572, 8.46341, 8.40144),(46.0952, 8.46341, 15.1017),(40.5978, 8.46341, 22.5323),(42.1739, 6.46341, 23.7645),(42.1739, 6.46341, 23.7645),(47.7324, 6.46341, 16.2514),(46.0952, 8.46341, 15.1017),(40.5978, 8.46341, 22.5323),(36.3249, 8.46341, 27.7079),(37.8371, 6.46341, 29.0176),(37.8371, 6.46341, 29.0176),(42.1739, 6.46341, 23.7645),(40.5978, 8.46341, 22.5323),(36.3249, 8.46341, 27.7079),(30.3574, 8.46341, 34.2781),(31.7899, 6.46341, 35.6756),(31.7899, 6.46341, 35.6756),(37.8371, 6.46341, 29.0176),(36.3249, 8.46341, 27.7079),(30.3574, 8.46341, 34.2781),(23.7326, 8.46341, 40.6018),(25.0709, 6.46341, 42.0892),(25.0709, 6.46341, 42.0892),(31.7899, 6.46341, 35.6756),(30.3574, 8.46341, 34.2781),(23.7326, 8.46341, 40.6018),(18.2159, 8.46341, 45.279),(19.4513, 6.46341, 46.8536),(19.4513, 6.46341, 46.8536),(25.0709, 6.46341, 42.0892),(23.7326, 8.46341, 40.6018),(18.2159, 8.46341, 45.279),(13.4516, 8.46341, 48.7331),(14.5647, 6.46341, 50.3964),(14.5647, 6.46341, 50.3964),(19.4513, 6.46341, 46.8536),(18.2159, 8.46341, 45.279),(13.4516, 8.46341, 48.7331),(8.33187, 8.46341, 51.8883),(9.31166, 6.46341, 53.6338),(9.31166, 6.46341, 53.6338),(14.5647, 6.46341, 50.3964),(13.4516, 8.46341, 48.7331),(8.33187, 8.46341, 51.8883),(1.00884, 8.46341, 56.0242),(1.64202, 6.46341, 57.5364),(1.64202, 6.46341, 57.5364),(9.31166, 6.46341, 53.6338),(8.33187, 8.46341, 51.8883),(1.00884, 8.46341, 56.0242),(0.0860662, 8.46341, 56.2968),(0.0871229, 6.46341, 57.966),(0.0871229, 6.46341, 57.966),(1.64202, 6.46341, 57.5364),(1.00884, 8.46341, 56.0242),(0.0860662, 8.46341, 56.2968),(-0.768229, 8.46341, 56.0568),(-1.46778, 6.46341, 57.5386),(-1.46778, 6.46341, 57.5386),(0.0871229, 6.46341, 57.966),(0.0860662, 8.46341, 56.2968),(-0.768229, 8.46341, 56.0568),(-7.0595, 8.46341, 51.6628),(-8.20569, 6.46341, 53.3047),(-8.20569, 6.46341, 53.3047),(-1.46778, 6.46341, 57.5386),(-0.768229, 8.46341, 56.0568),(-7.0595, 8.46341, 51.6628),(-14.5266, 8.46341, 45.8928),(-15.8074, 6.46341, 47.4306),(-15.8074, 6.46341, 47.4306),(-8.20569, 6.46341, 53.3047),(-7.0595, 8.46341, 51.6628),(-14.5266, 8.46341, 45.8928),(-22.7964, 8.46341, 38.4756),(-24.1866, 6.46341, 39.9153),(-24.1866, 6.46341, 39.9153),(-15.8074, 6.46341, 47.4306),(-14.5266, 8.46341, 45.8928),(-22.7964, 8.46341, 38.4756),(-29.2666, 8.46341, 31.75),(-30.7518, 6.46341, 33.091),(-30.7518, 6.46341, 33.091),(-24.1866, 6.46341, 39.9153),(-22.7964, 8.46341, 38.4756),(-29.2666, 8.46341, 31.75),(-35.4105, 8.46341, 24.4967),(-36.9714, 6.46341, 25.7484),(-36.9714, 6.46341, 25.7484),(-30.7518, 6.46341, 33.091),(-29.2666, 8.46341, 31.75),(-35.4105, 8.46341, 24.4967),(-41.027, 8.46341, 17.0932),(-42.6727, 6.46341, 18.233),(-42.6727, 6.46341, 18.233),(-36.9714, 6.46341, 25.7484),(-35.4105, 8.46341, 24.4967),(-41.027, 8.46341, 17.0932),(-46.4979, 8.46341, 8.4152),(-48.201, 6.46341, 9.46394),(-48.201, 6.46341, 9.46394),(-42.6727, 6.46341, 18.233),(-41.027, 8.46341, 17.0932),(-46.4979, 8.46341, 8.4152),(-50.6824, 8.46341, 1.45615),(-52.4338, 6.46341, 2.42471),(-52.4338, 6.46341, 2.42471),(-48.201, 6.46341, 9.46394),(-46.4979, 8.46341, 8.4152),(-50.6824, 8.46341, 1.45615),(-53.9145, 8.46341, -4.92301),(-55.7163, 6.46341, -4.05405),(-55.7163, 6.46341, -4.05405),(-52.4338, 6.46341, 2.42471),(-50.6824, 8.46341, 1.45615),(-53.9145, 8.46341, -4.92301),(-57.6792, 8.46341, -13.1369),(-59.5172, 6.46341, -12.3469),(-59.5172, 6.46341, -12.3469),(-55.7163, 6.46341, -4.05405),(-53.9145, 8.46341, -4.92301),(-57.6792, 8.46341, -13.1369),(-61.1865, 8.46341, -21.8622),(-63.0589, 6.46341, -21.158),(-63.0589, 6.46341, -21.158),(-59.5172, 6.46341, -12.3469),(-57.6792, 8.46341, -13.1369),(-61.1865, 8.46341, -21.8622),(-63.4391, 8.46341, -28.2864),(-65.3913, 6.46341, -27.8095),(-65.3913, 6.46341, -27.8095),(-63.0589, 6.46341, -21.158),(-61.1865, 8.46341, -21.8622),(-63.4391, 8.46341, -28.2864),(-63.7659, 8.46341, -30.5739),(-65.8232, 6.46341, -30.8329),(-65.8232, 6.46341, -30.8329),(-65.3913, 6.46341, -27.8095),(-63.4391, 8.46341, -28.2864),(-63.7659, 8.46341, -30.5739),(-63.1481, 8.46341, -32.0669),(-64.7866, 6.46341, -33.338),(-64.7866, 6.46341, -33.338),(-65.8232, 6.46341, -30.8329),(-63.7659, 8.46341, -30.5739),(-63.1481, 8.46341, -32.0669),(-62.1578, 8.46341, -32.8096),(-63.0589, 6.46341, -34.6338),(-63.0589, 6.46341, -34.6338),(-64.7866, 6.46341, -33.338),(-63.1481, 8.46341, -32.0669),(-62.1578, 8.46341, -32.8096),(-59.9364, 8.46341, -33.4344),(-60.2947, 6.46341, -35.4112),(-60.2947, 6.46341, -35.4112),(-63.0589, 6.46341, -34.6338),(-62.1578, 8.46341, -32.8096),(-59.9364, 8.46341, -33.4344),(-48.9362, 8.46341, -34.3652),(-49.0648, 6.46341, -36.3615),(-49.0648, 6.46341, -36.3615),(-60.2947, 6.46341, -35.4112),(-59.9364, 8.46341, -33.4344),(-48.9362, 8.46341, -34.3652),(-39.2592, 8.46341, -34.7934),(-39.3035, 6.46341, -36.7934),(-39.3035, 6.46341, -36.7934),(-49.0648, 6.46341, -36.3615),(-48.9362, 8.46341, -34.3652),(-39.2592, 8.46341, -34.7934),(-32.039, 8.46341, -34.7934),(-31.9609, 6.46341, -36.7934),(-31.9609, 6.46341, -36.7934),(-39.3035, 6.46341, -36.7934),(-39.2592, 8.46341, -34.7934),(-32.039, 8.46341, -34.7934),(-22.2736, 8.46341, -34.0291),(-22.0268, 6.46341, -36.0159),(-22.0268, 6.46341, -36.0159),(-31.9609, 6.46341, -36.7934),(-32.039, 8.46341, -34.7934),(-22.2736, 8.46341, -34.0291),(-11.8068, 8.46341, -32.2421),(-11.4016, 6.46341, -34.2019),(-11.4016, 6.46341, -34.2019),(-22.0268, 6.46341, -36.0159),(-22.2736, 8.46341, -34.0291),(-11.8068, 8.46341, -32.2421),(-2.36138, 8.46341, -29.9446),(-1.81306, 6.46341, -31.8695),(-1.81306, 6.46341, -31.8695),(-11.4016, 6.46341, -34.2019),(-11.8068, 8.46341, -32.2421),(-2.36138, 8.46341, -29.9446),(6.199, 8.46341, -27.142),(6.91933, 6.46341, -29.0107),(6.91933, 6.46341, -29.0107),(-1.81306, 6.46341, -31.8695),(-2.36138, 8.46341, -29.9446),(6.199, 8.46341, -27.142),(15.0639, 8.46341, -23.1888),(15.9595, 6.46341, -24.9792),(15.9595, 6.46341, -24.9792),(6.91933, 6.46341, -29.0107),(6.199, 8.46341, -27.142),(15.0639, 8.46341, -23.1888),(24.5708, 8.46341, -17.8938),(25.6105, 6.46341, -19.604),(25.6105, 6.46341, -19.604),(15.9595, 6.46341, -24.9792),(15.0639, 8.46341, -23.1888),(24.5708, 8.46341, -17.8938),(30.6576, 8.46341, -13.8687),(33.1847, 6.46341, -14.5952),(33.1847, 6.46341, -14.5952),(25.6105, 6.46341, -19.604),(24.5708, 8.46341, -17.8938),(30.6576, 8.46341, -13.8687),(28.3327, 8.46341, -8.75391),(30.1306, 6.46341, -7.87619),(30.1306, 6.46341, -7.87619),(33.1847, 6.46341, -14.5952),(30.6576, 8.46341, -13.8687),(28.3327, 8.46341, -8.75391),(25.6048, 8.46341, -3.53532),(27.3208, 6.46341, -2.50095),(27.3208, 6.46341, -2.50095),(30.1306, 6.46341, -7.87619),(28.3327, 8.46341, -8.75391),(25.6048, 8.46341, -3.53532),(22.9426, 8.46341, 0.329102),(23.5337, 6.46341, 2.99647),(23.5337, 6.46341, 2.99647),(27.3208, 6.46341, -2.50095),(25.6048, 8.46341, -3.53532),(22.9426, 8.46341, 0.329102),(18.5374, 8.46341, -2.26027),(17.5527, 6.46341, -0.519135),(17.5527, 6.46341, -0.519135),(23.5337, 6.46341, 2.99647),(22.9426, 8.46341, 0.329102),(18.5374, 8.46341, -2.26027),(12.1181, 8.46341, -5.75037),(11.2612, 6.46341, -3.93974),(11.2612, 6.46341, -3.93974),(17.5527, 6.46341, -0.519135),(18.5374, 8.46341, -2.26027),(12.1181, 8.46341, -5.75037),(5.22691, 8.46341, -8.55099),(4.49783, 6.46341, -6.68845),(4.49783, 6.46341, -6.68845),(11.2612, 6.46341, -3.93974),(12.1181, 8.46341, -5.75037),(5.22691, 8.46341, -8.55099),(-0.342632, 8.46341, -10.6487),(-1.01632, 6.46341, -8.76525),(-1.01632, 6.46341, -8.76525),(4.49783, 6.46341, -6.68845),(5.22691, 8.46341, -8.55099),(-14.5266, -9.7168, 45.8928),(-4.8035, -9.7168, 31.5666),(1.36473, -9.7168, 36.1928),(1.36473, -9.7168, 36.1928),(-7.0595, -9.7168, 51.6628),(-14.5266, -9.7168, 45.8928),(-22.7964, -9.7168, 38.4756),(-11.161, -9.7168, 25.8947),(-4.8035, -9.7168, 31.5666),(-4.8035, -9.7168, 31.5666),(-14.5266, -9.7168, 45.8928),(-22.7964, -9.7168, 38.4756),(-29.2666, -9.7168, 31.75),(-17.5591, -9.7168, 19.1239),(-11.161, -9.7168, 25.8947),(-11.161, -9.7168, 25.8947),(-22.7964, -9.7168, 38.4756),(-29.2666, -9.7168, 31.75),(8.33187, -9.7168, 51.8883),(1.00884, -9.7168, 56.0242),(1.36473, -9.7168, 36.1928),(13.4516, -9.7168, 48.7331),(8.33187, -9.7168, 51.8883),(1.36473, -9.7168, 36.1928),(1.36473, -9.7168, 36.1928),(7.09695, -9.7168, 31.7955),(13.4516, -9.7168, 48.7331),(7.09695, -9.7168, 31.7955),(12.3292, -9.7168, 26.9992),(18.2159, -9.7168, 45.279),(18.2159, -9.7168, 45.279),(13.4516, -9.7168, 48.7331),(7.09695, -9.7168, 31.7955),(23.7326, -9.7168, 40.6018),(18.2159, -9.7168, 45.279),(12.3292, -9.7168, 26.9992),(12.3292, -9.7168, 26.9992),(17.1799, -9.7168, 22.0863),(23.7326, -9.7168, 40.6018),(17.1799, -9.7168, 22.0863),(22.2073, -9.7168, 16.19),(30.3574, -9.7168, 34.2781),(30.3574, -9.7168, 34.2781),(23.7326, -9.7168, 40.6018),(17.1799, -9.7168, 22.0863),(36.3249, -9.7168, 27.7079),(30.3574, -9.7168, 34.2781),(22.2073, -9.7168, 16.19),(22.2073, -9.7168, 16.19),(28.6893, -9.7168, 7.77172),(36.3249, -9.7168, 27.7079),(28.6893, -9.7168, 7.77172),(32.306, -9.7168, 2.3027),(40.5978, -9.7168, 22.5323),(40.5978, -9.7168, 22.5323),(36.3249, -9.7168, 27.7079),(28.6893, -9.7168, 7.77172),(46.0952, -9.7168, 15.1017),(40.5978, -9.7168, 22.5323),(32.306, -9.7168, 2.3027),(32.306, -9.7168, 2.3027),(36.4125, -9.7168, -4.86197),(46.0952, -9.7168, 15.1017),(36.4125, -9.7168, -4.86197),(39.8285, -9.7168, -11.256),(50.5572, -9.7168, 8.40144),(50.5572, -9.7168, 8.40144),(46.0952, -9.7168, 15.1017),(36.4125, -9.7168, -4.86197),(54.1142, -9.7168, 2.36055),(50.5572, -9.7168, 8.40144),(39.8285, -9.7168, -11.256),(39.8285, -9.7168, -11.256),(42.7981, -9.7168, -17.8939),(54.1142, -9.7168, 2.36055),(42.7981, -9.7168, -17.8939),(45.7732, -9.7168, -24.7192),(57.2573, -9.7168, -3.32123),(57.2573, -9.7168, -3.32123),(54.1142, -9.7168, 2.36055),(42.7981, -9.7168, -17.8939),(59.9063, -9.7168, -8.61919),(57.2573, -9.7168, -3.32123),(45.7732, -9.7168, -24.7192),(45.7732, -9.7168, -24.7192),(48.2289, -9.7168, -31.9984),(59.9063, -9.7168, -8.61919),(63.5821, -9.7168, -16.8747),(59.9063, -9.7168, -8.61919),(48.2289, -9.7168, -31.9984),(48.2289, -9.7168, -31.9984),(49.6592, -9.7168, -36.695),(63.5821, -9.7168, -16.8747),(65.9799, -9.7168, -23.6486),(63.5821, -9.7168, -16.8747),(49.6592, -9.7168, -36.695),(-35.4105, -9.7168, 24.4967),(-24.4894, -9.7168, 10.6782),(-17.5591, -9.7168, 19.1239),(-17.5591, -9.7168, 19.1239),(-29.2666, -9.7168, 31.75),(-35.4105, -9.7168, 24.4967),(-41.027, -9.7168, 17.0932),(-29.1279, -9.7168, 4.13616),(-24.4894, -9.7168, 10.6782),(-24.4894, -9.7168, 10.6782),(-35.4105, -9.7168, 24.4967),(-41.027, -9.7168, 17.0932),(-46.4979, -9.7168, 8.4152),(-32.7328, -9.7168, -1.58208),(-29.1279, -9.7168, 4.13616),(-29.1279, -9.7168, 4.13616),(-41.027, -9.7168, 17.0932),(-46.4979, -9.7168, 8.4152),(-50.6824, -9.7168, 1.45615),(-35.6605, -9.7168, -6.93914),(-32.7328, -9.7168, -1.58208),(-32.7328, -9.7168, -1.58208),(-46.4979, -9.7168, 8.4152),(-50.6824, -9.7168, 1.45615),(-53.9145, -9.7168, -4.923),(-39.1325, -9.7168, -13.9348),(-35.6605, -9.7168, -6.93914),(-35.6605, -9.7168, -6.93914),(-50.6824, -9.7168, 1.45615),(-53.9145, -9.7168, -4.923),(-53.9145, -9.7168, -4.923),(-57.6792, -9.7168, -13.1369),(-39.1325, -9.7168, -13.9348),(-57.6792, -9.7168, -13.1369),(-38.8807, -9.7168, -16.1225),(-39.1325, -9.7168, -13.9348),(25.6048, -9.7168, -3.53532),(22.9426, -9.7168, 0.329102),(18.5374, -9.7168, -2.26027),(-38.8807, -9.7168, -16.1225),(-57.6792, -9.7168, -13.1369),(-61.1865, -9.7168, -21.8622),(-38.8807, -9.7168, -16.1225),(-61.1865, -9.7168, -21.8622),(-63.4391, -9.7168, -28.2864),(-38.8807, -9.7168, -16.1225),(-63.4391, -9.7168, -28.2864),(-63.7659, -9.7168, -30.5739),(-38.8807, -9.7168, -16.1225),(-63.7659, -9.7168, -30.5739),(-63.1481, -9.7168, -32.0669),(-38.8807, -9.7168, -16.1225),(-63.1481, -9.7168, -32.0669),(-62.1578, -9.7168, -32.8096),(-38.8807, -9.7168, -16.1225),(-62.1578, -9.7168, -32.8096),(-59.9364, -9.7168, -33.4344),(-59.9364, -9.7168, -33.4344),(-36.7622, -9.7168, -17.0322),(-38.8807, -9.7168, -16.1225),(-36.7622, -9.7168, -17.0322),(-59.9364, -9.7168, -33.4344),(-48.9362, -9.7168, -34.3652),(-36.7622, -9.7168, -17.0322),(-48.9362, -9.7168, -34.3652),(-39.2592, -9.7168, -34.7934),(-39.2592, -9.7168, -34.7934),(-30.1361, -9.7168, -17.1797),(-36.7622, -9.7168, -17.0322),(-30.1361, -9.7168, -17.1797),(-39.2592, -9.7168, -34.7934),(-32.039, -9.7168, -34.7934),(-32.039, -9.7168, -34.7934),(-23.6557, -9.7168, -16.6135),(-30.1361, -9.7168, -17.1797),(-23.6557, -9.7168, -16.6135),(-32.039, -9.7168, -34.7934),(-22.2736, -9.7168, -34.0291),(-22.2736, -9.7168, -34.0291),(-16.1094, -9.7168, -15.2414),(-23.6557, -9.7168, -16.6135),(-16.1094, -9.7168, -15.2414),(-22.2736, -9.7168, -34.0291),(-11.8068, -9.7168, -32.2421),(-11.8068, -9.7168, -32.2421),(-7.65952, -9.7168, -13.129),(-16.1094, -9.7168, -15.2414),(-7.65952, -9.7168, -13.129),(-11.8068, -9.7168, -32.2421),(-2.36138, -9.7168, -29.9446),(-2.36138, -9.7168, -29.9446),(-0.342632, -9.7168, -10.6487),(-7.65952, -9.7168, -13.129),(-0.342632, -9.7168, -10.6487),(-2.36138, -9.7168, -29.9446),(6.199, -9.7168, -27.142),(6.199, -9.7168, -27.142),(5.22691, -9.7168, -8.55099),(-0.342632, -9.7168, -10.6487),(5.22691, -9.7168, -8.55099),(6.199, -9.7168, -27.142),(15.0639, -9.7168, -23.1888),(15.0639, -9.7168, -23.1888),(12.1181, -9.7168, -5.75037),(5.22691, -9.7168, -8.55099),(12.1181, -9.7168, -5.75037),(15.0639, -9.7168, -23.1888),(24.5708, -9.7168, -17.8938),(24.5708, -9.7168, -17.8938),(18.5374, -9.7168, -2.26027),(12.1181, -9.7168, -5.75037),(24.5708, -9.7168, -17.8938),(30.6576, -9.7168, -13.8687),(28.3327, -9.7168, -8.75391),(28.3327, -9.7168, -8.75391),(25.6048, -9.7168, -3.53532),(18.5374, -9.7168, -2.26027),(18.5374, -9.7168, -2.26027),(24.5708, -9.7168, -17.8938),(28.3327, -9.7168, -8.75391),(-7.0595, 8.46341, 51.6628),(-0.768229, 8.46341, 56.0568),(1.36473, 8.46341, 36.1928),(-14.5266, 8.46341, 45.8928),(-7.0595, 8.46341, 51.6628),(1.36473, 8.46341, 36.1928),(1.36473, 8.46341, 36.1928),(-4.8035, 8.46341, 31.5666),(-14.5266, 8.46341, 45.8928),(-22.7964, 8.46341, 38.4756),(-14.5266, 8.46341, 45.8928),(-4.8035, 8.46341, 31.5666),(-4.8035, 8.46341, 31.5666),(-11.161, 8.46341, 25.8947),(-22.7964, 8.46341, 38.4756),(-29.2666, 8.46341, 31.75),(-22.7964, 8.46341, 38.4756),(-11.161, 8.46341, 25.8947),(-11.161, 8.46341, 25.8947),(-17.5591, 8.46341, 19.1239),(-29.2666, 8.46341, 31.75),(-35.4105, 8.46341, 24.4967),(-29.2666, 8.46341, 31.75),(-17.5591, 8.46341, 19.1239),(-17.5591, 8.46341, 19.1239),(-24.4894, 8.46341, 10.6782),(-35.4105, 8.46341, 24.4967),(-41.027, 8.46341, 17.0932),(-35.4105, 8.46341, 24.4967),(-24.4894, 8.46341, 10.6782),(-24.4894, 8.46341, 10.6782),(-29.1279, 8.46341, 4.13616),(-41.027, 8.46341, 17.0932),(-46.4979, 8.46341, 8.4152),(-41.027, 8.46341, 17.0932),(-29.1279, 8.46341, 4.13616),(-29.1279, 8.46341, 4.13616),(-32.7328, 8.46341, -1.58208),(-46.4979, 8.46341, 8.4152),(-50.6824, 8.46341, 1.45615),(-46.4979, 8.46341, 8.4152),(-32.7328, 8.46341, -1.58208),(-32.7328, 8.46341, -1.58208),(-35.6605, 8.46341, -6.93914),(-50.6824, 8.46341, 1.45615),(-53.9145, 8.46341, -4.92301),(-50.6824, 8.46341, 1.45615),(-35.6605, 8.46341, -6.93914),(-35.6605, 8.46341, -6.93914),(-39.1325, 8.46341, -13.9348),(-53.9145, 8.46341, -4.92301),(-57.6792, 8.46341, -13.1369),(-53.9145, 8.46341, -4.92301),(-39.1325, 8.46341, -13.9348),(-38.8807, 8.46341, -16.1225),(-61.1865, 8.46341, -21.8622),(-57.6792, 8.46341, -13.1369),(-38.8807, 8.46341, -16.1225),(-63.4391, 8.46341, -28.2864),(-61.1865, 8.46341, -21.8622),(-38.8807, 8.46341, -16.1225),(-63.7659, 8.46341, -30.5739),(-63.4391, 8.46341, -28.2864),(-38.8807, 8.46341, -16.1225),(-36.7622, 8.46341, -17.0322),(-59.9364, 8.46341, -33.4344),(-59.9364, 8.46341, -33.4344),(-62.1578, 8.46341, -32.8096),(-38.8807, 8.46341, -16.1225),(-63.1481, 8.46341, -32.0669),(-63.7659, 8.46341, -30.5739),(-38.8807, 8.46341, -16.1225),(-62.1578, 8.46341, -32.8096),(-63.1481, 8.46341, -32.0669),(-38.8807, 8.46341, -16.1225),(-36.7622, 8.46341, -17.0322),(-48.9362, 8.46341, -34.3652),(-59.9364, 8.46341, -33.4344),(-36.7622, 8.46341, -17.0322),(-30.1361, 8.46341, -17.1797),(-39.2592, 8.46341, -34.7934),(-39.2592, 8.46341, -34.7934),(-48.9362, 8.46341, -34.3652),(-36.7622, 8.46341, -17.0322),(-30.1361, 8.46341, -17.1797),(-23.6557, 8.46341, -16.6135),(-32.039, 8.46341, -34.7934),(-32.039, 8.46341, -34.7934),(-39.2592, 8.46341, -34.7934),(-30.1361, 8.46341, -17.1797),(-23.6557, 8.46341, -16.6135),(-16.1094, 8.46341, -15.2414),(-22.2736, 8.46341, -34.0291),(-22.2736, 8.46341, -34.0291),(-32.039, 8.46341, -34.7934),(-23.6557, 8.46341, -16.6135),(-16.1094, 8.46341, -15.2414),(-7.65952, 8.46341, -13.129),(-11.8068, 8.46341, -32.2421),(-11.8068, 8.46341, -32.2421),(-22.2736, 8.46341, -34.0291),(-16.1094, 8.46341, -15.2414),(-7.65952, 8.46341, -13.129),(-0.342632, 8.46341, -10.6487),(-2.36138, 8.46341, -29.9446),(-2.36138, 8.46341, -29.9446),(-11.8068, 8.46341, -32.2421),(-7.65952, 8.46341, -13.129),(-0.342632, 8.46341, -10.6487),(5.22691, 8.46341, -8.55099),(6.199, 8.46341, -27.142),(6.199, 8.46341, -27.142),(-2.36138, 8.46341, -29.9446),(-0.342632, 8.46341, -10.6487),(5.22691, 8.46341, -8.55099),(12.1181, 8.46341, -5.75037),(15.0639, 8.46341, -23.1888),(15.0639, 8.46341, -23.1888),(6.199, 8.46341, -27.142),(5.22691, 8.46341, -8.55099),(12.1181, 8.46341, -5.75037),(18.5374, 8.46341, -2.26027),(24.5708, 8.46341, -17.8938),(24.5708, 8.46341, -17.8938),(15.0639, 8.46341, -23.1888),(12.1181, 8.46341, -5.75037),(25.6048, 8.46341, -3.53532),(28.3327, 8.46341, -8.75391),(24.5708, 8.46341, -17.8938),(24.5708, 8.46341, -17.8938),(18.5374, 8.46341, -2.26027),(25.6048, 8.46341, -3.53532),(18.5374, 8.46341, -2.26027),(22.9426, 8.46341, 0.329102),(25.6048, 8.46341, -3.53532),(28.3327, 8.46341, -8.75391),(30.6576, 8.46341, -13.8687),(24.5708, 8.46341, -17.8938),(13.4516, 8.46341, 48.7331),(7.09695, 8.46341, 31.7955),(1.36473, 8.46341, 36.1928),(1.36473, 8.46341, 36.1928),(8.33187, 8.46341, 51.8883),(13.4516, 8.46341, 48.7331),(18.2159, 8.46341, 45.279),(12.3292, 8.46341, 26.9992),(7.09695, 8.46341, 31.7955),(7.09695, 8.46341, 31.7955),(13.4516, 8.46341, 48.7331),(18.2159, 8.46341, 45.279),(23.7326, 8.46341, 40.6018),(17.1799, 8.46341, 22.0863),(12.3292, 8.46341, 26.9992),(12.3292, 8.46341, 26.9992),(18.2159, 8.46341, 45.279),(23.7326, 8.46341, 40.6018),(30.3574, 8.46341, 34.2781),(22.2073, 8.46341, 16.19),(17.1799, 8.46341, 22.0863),(17.1799, 8.46341, 22.0863),(23.7326, 8.46341, 40.6018),(30.3574, 8.46341, 34.2781),(36.3249, 8.46341, 27.7079),(28.6893, 8.46341, 7.77172),(22.2073, 8.46341, 16.19),(22.2073, 8.46341, 16.19),(30.3574, 8.46341, 34.2781),(36.3249, 8.46341, 27.7079),(40.5978, 8.46341, 22.5323),(32.306, 8.46341, 2.3027),(28.6893, 8.46341, 7.77172),(28.6893, 8.46341, 7.77172),(36.3249, 8.46341, 27.7079),(40.5978, 8.46341, 22.5323),(46.0952, 8.46341, 15.1017),(36.4125, 8.46341, -4.86197),(32.306, 8.46341, 2.3027),(32.306, 8.46341, 2.3027),(40.5978, 8.46341, 22.5323),(46.0952, 8.46341, 15.1017),(50.5572, 8.46341, 8.40144),(39.8285, 8.46341, -11.256),(36.4125, 8.46341, -4.86197),(36.4125, 8.46341, -4.86197),(46.0952, 8.46341, 15.1017),(50.5572, 8.46341, 8.40144),(54.1142, 8.46341, 2.36055),(42.7981, 8.46341, -17.8939),(39.8285, 8.46341, -11.256),(39.8285, 8.46341, -11.256),(50.5572, 8.46341, 8.40144),(54.1142, 8.46341, 2.36055),(57.2573, 8.46341, -3.32123),(45.7732, 8.46341, -24.7192),(42.7981, 8.46341, -17.8939),(42.7981, 8.46341, -17.8939),(54.1142, 8.46341, 2.36055),(57.2573, 8.46341, -3.32123),(59.9063, 8.46341, -8.61919),(48.2289, 8.46341, -31.9984),(45.7732, 8.46341, -24.7192),(45.7732, 8.46341, -24.7192),(57.2573, 8.46341, -3.32123),(59.9063, 8.46341, -8.61919),(63.5821, 8.46341, -16.8747),(49.6592, 8.46341, -36.695),(48.2289, 8.46341, -31.9984),(48.2289, 8.46341, -31.9984),(59.9063, 8.46341, -8.61919),(63.5821, 8.46341, -16.8747),(63.5821, 8.46341, -16.8747),(65.9799, 8.46341, -23.6486),(49.6592, 8.46341, -36.695),(65.9799, 8.46341, -23.6486),(68.0484, 8.46341, -30.768),(49.6592, 8.46341, -36.695)]
		
		faces=[(0,1,2),(3,4,5),(6,7,8),(9,10,11),(12,13,14),(15,16,17),(18,19,20),(21,22,23),(24,25,26),(27,28,29),(30,31,32),(33,34,35),(36,37,38),(39,40,41),(42,43,44),(45,46,47),(48,49,50),(51,52,53),(54,55,56),(57,58,59),(60,61,62),(63,64,65),(66,67,68),(69,70,71),(72,73,74),(75,76,77),(78,79,80),(81,82,83),(84,85,86),(87,88,89),(90,91,92),(93,94,95),(96,97,98),(99,100,101),(102,103,104),(105,106,107),(108,109,110),(111,112,113),(114,115,116),(117,118,119),(120,121,122),(123,124,125),(126,127,128),(129,130,131),(132,133,134),(135,136,137),(138,139,140),(141,142,143),(144,145,146),(147,148,149),(150,151,152),(153,154,155),(156,157,158),(159,160,161),(162,163,164),(165,166,167),(168,169,170),(171,172,173),(174,175,176),(177,178,179),(180,181,182),(183,184,185),(186,187,188),(189,190,191),(192,193,194),(195,196,197),(198,199,200),(201,202,203),(204,205,206),(207,208,209),(210,211,212),(213,214,215),(216,217,218),(219,220,221),(222,223,224),(225,226,227),(228,229,230),(231,232,233),(234,235,236),(237,238,239),(240,241,242),(243,244,245),(246,247,248),(249,250,251),(252,253,254),(255,256,257),(258,259,260),(261,262,263),(264,265,266),(267,268,269),(270,271,272),(273,274,275),(276,277,278),(279,280,281),(282,283,284),(285,286,287),(288,289,290),(291,292,293),(294,295,296),(297,298,299),(300,301,302),(303,304,305),(306,307,308),(309,310,311),(312,313,314),(315,316,317),(318,319,320),(321,322,323),(324,325,326),(327,328,329),(330,331,332),(333,334,335),(336,337,338),(339,340,341),(342,343,344),(345,346,347),(348,349,350),(351,352,353),(354,355,356),(357,358,359),(360,361,362),(363,364,365),(366,367,368),(369,370,371),(372,373,374),(375,376,377),(378,379,380),(381,382,383),(384,385,386),(387,388,389),(390,391,392),(393,394,395),(396,397,398),(399,400,401),(402,403,404),(405,406,407),(408,409,410),(411,412,413),(414,415,416),(417,418,419),(420,421,422),(423,424,425),(426,427,428),(429,430,431),(432,433,434),(435,436,437),(438,439,440),(441,442,443),(444,445,446),(447,448,449),(450,451,452),(453,454,455),(456,457,458),(459,460,461),(462,463,464),(465,466,467),(468,469,470),(471,472,473),(474,475,476),(477,478,479),(480,481,482),(483,484,485),(486,487,488),(489,490,491),(492,493,494),(495,496,497),(498,499,500),(501,502,503),(504,505,506),(507,508,509),(510,511,512),(513,514,515),(516,517,518),(519,520,521),(522,523,524),(525,526,527),(528,529,530),(531,532,533),(534,535,536),(537,538,539),(540,541,542),(543,544,545),(546,547,548),(549,550,551),(552,553,554),(555,556,557),(558,559,560),(561,562,563),(564,565,566),(567,568,569),(570,571,572),(573,574,575),(576,577,578),(579,580,581),(582,583,584),(585,586,587),(588,589,590),(591,592,593),(594,595,596),(597,598,599),(600,601,602),(603,604,605),(606,607,608),(609,610,611),(612,613,614),(615,616,617),(618,619,620),(621,622,623),(624,625,626),(627,628,629),(630,631,632),(633,634,635),(636,637,638),(639,640,641),(642,643,644),(645,646,647),(648,649,650),(651,652,653),(654,655,656),(657,658,659),(660,661,662),(663,664,665),(666,667,668),(669,670,671),(672,673,674),(675,676,677),(678,679,680),(681,682,683),(684,685,686),(687,688,689),(690,691,692),(693,694,695),(696,697,698),(699,700,701),(702,703,704),(705,706,707),(708,709,710),(711,712,713),(714,715,716),(717,718,719),(720,721,722),(723,724,725),(726,727,728),(729,730,731),(732,733,734),(735,736,737),(738,739,740),(741,742,743),(744,745,746),(747,748,749),(750,751,752),(753,754,755),(756,757,758),(759,760,761),(762,763,764),(765,766,767),(768,769,770),(771,772,773),(774,775,776),(777,778,779),(780,781,782),(783,784,785),(786,787,788),(789,790,791),(792,793,794),(795,796,797),(798,799,800),(801,802,803),(804,805,806),(807,808,809),(810,811,812),(813,814,815),(816,817,818),(819,820,821),(822,823,824),(825,826,827),(828,829,830),(831,832,833),(834,835,836),(837,838,839),(840,841,842),(843,844,845),(846,847,848),(849,850,851),(852,853,854),(855,856,857),(858,859,860),(861,862,863),(864,865,866),(867,868,869),(870,871,872),(873,874,875),(876,877,878),(879,880,881),(882,883,884),(885,886,887),(888,889,890),(891,892,893),(894,895,896),(897,898,899),(900,901,902),(903,904,905),(906,907,908),(909,910,911),(912,913,914),(915,916,917),(918,919,920),(921,922,923),(924,925,926),(927,928,929),(930,931,932),(933,934,935),(936,937,938),(939,940,941),(942,943,944),(945,946,947),(948,949,950),(951,952,953),(954,955,956),(957,958,959),(960,961,962),(963,964,965),(966,967,968),(969,970,971),(972,973,974),(975,976,977),(978,979,980),(981,982,983),(984,985,986),(987,988,989),(990,991,992),(993,994,995),(996,997,998),(999,1000,1001),(1002,1003,1004),(1005,1006,1007),(1008,1009,1010),(1011,1012,1013),(1014,1015,1016),(1017,1018,1019),(1020,1021,1022),(1023,1024,1025),(1026,1027,1028),(1029,1030,1031),(1032,1033,1034),(1035,1036,1037),(1038,1039,1040),(1041,1042,1043),(1044,1045,1046),(1047,1048,1049),(1050,1051,1052),(1053,1054,1055),(1056,1057,1058),(1059,1060,1061),(1062,1063,1064),(1065,1066,1067),(1068,1069,1070),(1071,1072,1073),(1074,1075,1076),(1077,1078,1079),(1080,1081,1082),(1083,1084,1085),(1086,1087,1088),(1089,1090,1091),(1092,1093,1094),(1095,1096,1097),(1098,1099,1100),(1101,1102,1103),(1104,1105,1106),(1107,1108,1109),(1110,1111,1112),(1113,1114,1115),(1116,1117,1118),(1119,1120,1121),(1122,1123,1124),(1125,1126,1127),(1128,1129,1130),(1131,1132,1133),(1134,1135,1136),(1137,1138,1139),(1140,1141,1142),(1143,1144,1145),(1146,1147,1148),(1149,1150,1151),(1152,1153,1154),(1155,1156,1157),(1158,1159,1160),(1161,1162,1163),(1164,1165,1166),(1167,1168,1169),(1170,1171,1172),(1173,1174,1175),(1176,1177,1178),(1179,1180,1181),(1182,1183,1184),(1185,1186,1187),(1188,1189,1190),(1191,1192,1193),(1194,1195,1196),(1197,1198,1199),(1200,1201,1202),(1203,1204,1205),(1206,1207,1208),(1209,1210,1211),(1212,1213,1214),(1215,1216,1217),(1218,1219,1220),(1221,1222,1223),(1224,1225,1226),(1227,1228,1229),(1230,1231,1232),(1233,1234,1235),(1236,1237,1238),(1239,1240,1241),(1242,1243,1244),(1245,1246,1247),(1248,1249,1250),(1251,1252,1253),(1254,1255,1256),(1257,1258,1259),(1260,1261,1262),(1263,1264,1265),(1266,1267,1268),(1269,1270,1271),(1272,1273,1274),(1275,1276,1277),(1278,1279,1280),(1281,1282,1283),(1284,1285,1286),(1287,1288,1289),(1290,1291,1292),(1293,1294,1295),(1296,1297,1298),(1299,1300,1301),(1302,1303,1304),(1305,1306,1307),(1308,1309,1310),(1311,1312,1313),(1314,1315,1316),(1317,1318,1319),(1320,1321,1322),(1323,1324,1325),(1326,1327,1328),(1329,1330,1331),(1332,1333,1334),(1335,1336,1337),(1338,1339,1340),(1341,1342,1343),(1344,1345,1346),(1347,1348,1349),(1350,1351,1352),(1353,1354,1355),(1356,1357,1358),(1359,1360,1361),(1362,1363,1364),(1365,1366,1367),(1368,1369,1370),(1371,1372,1373),(1374,1375,1376),(1377,1378,1379),(1380,1381,1382),(1383,1384,1385),(1386,1387,1388),(1389,1390,1391),(1392,1393,1394),(1395,1396,1397),(1398,1399,1400),(1401,1402,1403),(1404,1405,1406),(1407,1408,1409),(1410,1411,1412),(1413,1414,1415),(1416,1417,1418),(1419,1420,1421),(1422,1423,1424),(1425,1426,1427),(1428,1429,1430),(1431,1432,1433),(1434,1435,1436),(1437,1438,1439),(1440,1441,1442),(1443,1444,1445),(1446,1447,1448),(1449,1450,1451),(1452,1453,1454),(1455,1456,1457),(1458,1459,1460),(1461,1462,1463),(1464,1465,1466),(1467,1468,1469),(1470,1471,1472),(1473,1474,1475),(1476,1477,1478),(1479,1480,1481),(1482,1483,1484),(1485,1486,1487),(1488,1489,1490),(1491,1492,1493),(1494,1495,1496),(1497,1498,1499),(1500,1501,1502),(1503,1504,1505),(1506,1507,1508),(1509,1510,1511),(1512,1513,1514),(1515,1516,1517),(1518,1519,1520),(1521,1522,1523),(1524,1525,1526),(1527,1528,1529),(1530,1531,1532),(1533,1534,1535),(1536,1537,1538),(1539,1540,1541),(1542,1543,1544),(1545,1546,1547),(1548,1549,1550),(1551,1552,1553),(1554,1555,1556),(1557,1558,1559),(1560,1561,1562),(1563,1564,1565),(1566,1567,1568),(1569,1570,1571),(1572,1573,1574),(1575,1576,1577),(1578,1579,1580),(1581,1582,1583),(1584,1585,1586),(1587,1588,1589),(1590,1591,1592),(1593,1594,1595),(1596,1597,1598),(1599,1600,1601),(1602,1603,1604),(1605,1606,1607),(1608,1609,1610),(1611,1612,1613),(1614,1615,1616),(1617,1618,1619),(1620,1621,1622),(1623,1624,1625),(1626,1627,1628),(1629,1630,1631),(1632,1633,1634),(1635,1636,1637),(1638,1639,1640),(1641,1642,1643),(1644,1645,1646),(1647,1648,1649),(1650,1651,1652),(1653,1654,1655),(1656,1657,1658),(1659,1660,1661),(1662,1663,1664),(1665,1666,1667),(1668,1669,1670),(1671,1672,1673),(1674,1675,1676),(1677,1678,1679),(1680,1681,1682),(1683,1684,1685),(1686,1687,1688),(1689,1690,1691),(1692,1693,1694),(1695,1696,1697),(1698,1699,1700),(1701,1702,1703),(1704,1705,1706),(1707,1708,1709),(1710,1711,1712),(1713,1714,1715),(1716,1717,1718),(1719,1720,1721),(1722,1723,1724),(1725,1726,1727),(1728,1729,1730),(1731,1732,1733),(1734,1735,1736),(1737,1738,1739),(1740,1741,1742),(1743,1744,1745),(1746,1747,1748),(1749,1750,1751),(1752,1753,1754),(1755,1756,1757),(1758,1759,1760),(1761,1762,1763),(1764,1765,1766),(1767,1768,1769),(1770,1771,1772),(1773,1774,1775),(1776,1777,1778),(1779,1780,1781),(1782,1783,1784),(1785,1786,1787),(1788,1789,1790),(1791,1792,1793),(1794,1795,1796),(1797,1798,1799),(1800,1801,1802),(1803,1804,1805),(1806,1807,1808),(1809,1810,1811),(1812,1813,1814),(1815,1816,1817),(1818,1819,1820),(1821,1822,1823),(1824,1825,1826),(1827,1828,1829),(1830,1831,1832),(1833,1834,1835),(1836,1837,1838),(1839,1840,1841),(1842,1843,1844),(1845,1846,1847),(1848,1849,1850),(1851,1852,1853),(1854,1855,1856),(1857,1858,1859)]	
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DLogo") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DLogo", me)   
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}
		
class AddOccluder(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_occluder"
	bl_label = "Add Occluder"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, -1), (1, -1, -1), (-1, -0.9999998, -1), (-0.9999997, 1, -1), (1, 0.9999995, 1), (0.9999994, -1.000001, 1), (-1, -0.9999997, 1), (-1, 1, 1) ]
		faces=[ (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DOccluder") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DOccluder", me)  		
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "A3DOccluder"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}
		
class AddSprite3D(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_sprite3d"
	bl_label = "Add Sprite3D"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, 0), (1, -1, 0), (-1, -0.9999998, 0), (-0.9999997, 1, 0) ]
		faces=[ (0, 3, 2, 1) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DSprite3D") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DSprite3D", me)  
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		#rotate 90 degrees so plane is upright
		ob.rotation_euler = (1.57079633,0,1) 
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "A3DSprite3D"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}
				
class AddSkybox(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_skybox"
	bl_label = "Add Skybox"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, -1), (1, -1, -1), (-1, -0.9999998, -1), (-0.9999997, 1, -1), (1, 0.9999995, 1), (0.9999994, -1.000001, 1), (-1, -0.9999997, 1), (-1, 1, 1) ]
		faces=[ (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DSkybox") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DSkybox", me)  
				
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob) 

		# give custom property type
		ob["a3dtype"] = "A3DSkybox"		
		
		# set the skybox to active
		bpy.context.scene.objects.active = ob
		
		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		
		# flip the normals as we want it inside the cube not outside
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.mesh.flip_normals()
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		bpy.ops.object.select_all(action='DESELECT')
		
		return {'FINISHED'}

class AddAmbientLight(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_ambientlight"
	bl_label = "Add AmbientLight"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		lamp = bpy.data.lamps.new("A3DAmbientLight","HEMI") 
		ob = bpy.data.objects.new("A3DAmbientLight", lamp)

		ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
	
		# give custom property type
		ob["a3dtype"] = "A3DAmbientLight"		
		
		# set the skybox to active
		bpy.context.scene.objects.active = ob
		
		return {'FINISHED'}
		
class AddDirectionalLight(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_directionallight"
	bl_label = "Add DirectionalLight"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		lamp = bpy.data.lamps.new("A3DDirectionalLight","AREA") 
		ob = bpy.data.objects.new("A3DDirectionalLight", lamp)

		ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
	
		# give custom property type
		ob["a3dtype"] = "A3DDirectionalLight"		
		
		# set the skybox to active
		bpy.context.scene.objects.active = ob
		
		return {'FINISHED'}

class AddOmniLight(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_omnilight"
	bl_label = "Add OmniLight"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		lamp = bpy.data.lamps.new("A3DOmniLight","POINT") 
		ob = bpy.data.objects.new("A3DOmniLight", lamp)

		ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
	
		# give custom property type
		ob["a3dtype"] = "A3DOmniLight"		
		
		# set the skybox to active
		bpy.context.scene.objects.active = ob
		
		return {'FINISHED'}

class AddSpotLight(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_spotlight"
	bl_label = "Add SpotLight"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		lamp = bpy.data.lamps.new("A3DSpotLight","SPOT") 
		ob = bpy.data.objects.new("A3DSpotLight", lamp)

		ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
	
		# give custom property type
		ob["a3dtype"] = "A3DSpotLight"		
		
		# set the skybox to active
		bpy.context.scene.objects.active = ob
		
		return {'FINISHED'}

class AddPlane(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_plane"
	bl_label = "Add Plane"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, 0), (1, -1, 0), (-1, -0.9999998, 0), (-0.9999997, 1, 0) ]
		faces=[ (0, 3, 2, 1) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DPlane") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DPlane", me)  
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		#rotate 90 degrees so plane is upright
		ob.rotation_euler = (1.57079633,0,1) 
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "A3DPlane"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}		
		
class AddLOD(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_lod"
	bl_label = "Add LOD"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, 0), (1, -1, 0), (-1, -0.9999998, 0), (-0.9999997, 1, 0) ]
		faces=[ (0, 3, 2, 1) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DLod") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DLod", me)  
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		#rotate 90 degrees so plane is upright
		ob.rotation_euler = (1.57079633,0,1) 
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "A3DLod"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}		
		
class AddBox(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_box"
	bl_label = "Add Box"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, -1), (1, -1, -1), (-1, -0.9999998, -1), (-0.9999997, 1, -1), (1, 0.9999995, 1), (0.9999994, -1.000001, 1), (-1, -0.9999997, 1), (-1, 1, 1) ]
		faces=[ (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("A3DBox") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("A3DBox", me)  
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		#rotate 90 degrees so plane is upright
		ob.rotation_euler = (1.57079633,0,1) 
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "A3DBox"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}		
		
# note to self
# blender info on custom properties
# http://wiki.blender.org/index.php/Doc:2.5/Manual/Extensions/Python/Properties

class A3d_submenu(bpy.types.Menu):
	bl_idname = "A3d_submenu"
	bl_label = "Alternativa3D"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator("a3dobj.a3d_logo", text="A3D Logo", icon='MESH_TORUS')
		layout.operator("a3dobj.a3d_plane", text="Plane", icon='MESH_PLANE')
		layout.operator("a3dobj.a3d_box", text="Box", icon='MESH_CUBE')
		layout.operator("a3dobj.a3d_sprite3d", text="Sprite3D", icon='MESH_PLANE')
		layout.operator("a3dobj.a3d_skybox", text="Skybox", icon='MESH_CUBE')
		layout.operator("a3dobj.a3d_occluder", text="Occluder", icon='MESH_CUBE')
		layout.operator("a3dobj.a3d_lod", text="LOD", icon='MESH_CUBE')
		layout.separator()
		layout.operator("a3dobj.a3d_ambientlight", text="AmbientLight", icon='OUTLINER_OB_LAMP')
		layout.operator("a3dobj.a3d_directionallight", text="DirectionalLight", icon='OUTLINER_OB_LAMP')
		layout.operator("a3dobj.a3d_omnilight", text="OmniLight", icon='OUTLINER_OB_LAMP')
		layout.operator("a3dobj.a3d_spotlight", text="SpotLight", icon='OUTLINER_OB_LAMP')
		
#==================================
# REGISTRATION
#==================================

def menu_func(self, context):
	self.layout.menu("A3d_submenu", icon="PLUGIN")
	
def menu_func_import(self, context):
	self.layout.operator(A3DImporter.bl_idname, text='Alternativa3D Binary (.a3d)')

def menu_func_export(self, context):
	as_path = bpy.data.filepath.replace('.blend', '.as')
	a3d_path = bpy.data.filepath.replace('.blend', '.a3d')
	self.layout.operator(ASExporter.bl_idname, text='Alternativa3D Class (.as)').filepath = as_path
	self.layout.operator(A3DExporter.bl_idname, text='Alternativa3D Binary (.a3d)').filepath = a3d_path
	
def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_file_import.append(menu_func_import)
	bpy.types.INFO_MT_file_export.append(menu_func_export)
	bpy.types.INFO_MT_mesh_add.append(menu_func)
	
def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_file_import.remove(menu_func_import)
	bpy.types.INFO_MT_file_export.remove(menu_func_export)
	bpy.types.INFO_MT_mesh_add.remove(menu_func)

	
if __name__ == '__main__':
	register()