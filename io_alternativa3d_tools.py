bl_info = {
	'name': 'Export: Alternativa3d Tools',
	'author': 'David E Jones, http://davidejones.com',
	'version': (1, 1, 5),
	'blender': (2, 5, 7),
	'location': 'File > Import/Export;',
	'description': 'Importer and exporter for Alternativa3D engine. Supports A3D and Actionscript"',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://davidejones.com',
	'category': 'Import-Export'}

import math, os, time, bpy, random, mathutils, re, ctypes, struct, binascii, zlib, tempfile, re, operator
import bpy_extras.io_utils
from bpy import ops
from bpy.props import *

#==================================
# Common Functions in File
#==================================
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
		WriteDocuClass(file,aobjs,Config)
	
	print('Export Completed...\n')

def GetMeshVertexCount(Mesh):
    VertexCount = 0
    for Face in Mesh.faces:
        VertexCount += len(Face.vertices)
    return VertexCount
	
def WritePackageHeader(file,Config):
	file.write("//Alternativa3D Class Export For Blender 2.57 and above\n")
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
	print("transform="+str(trns))
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

def WriteDocuClass(file,aobjs,Config):
	WritePackageHeader(file,Config)
	file.write("\tpublic class main extends Sprite {\n\n")
	file.write("\t\tpublic function main() {\n\n")
	
	for obj in aobjs:
		#print(obj["a3dtype"])
		if obj["a3dtype"] == "skybox":
			WriteSkyBox(file,obj,Config)
		if obj["a3dtype"] == "occluder":
			WriteOccluder(file,obj,Config)
		if obj["a3dtype"] == "sprite3d":
			WriteSprite3d(file,obj,Config)
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	WritePackageEnd(file)

#==================================
# A3D EXPORTER
#==================================

#Container for the exporter settings
class A3DExporterSettings:
	def __init__(self,A3DVersionSystem=1,ExportMode=1,CompressData=1,ExportAnim=0,ExportUV=1,ExportNormals=1,ExportTangents=1):
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
	A3DVersions.append(("1", "2.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D .A3D to export to", items=A3DVersions, default="1")
	
	ExportModes = []
	ExportModes.append(("1", "Selected Objects", ""))
	ExportModes.append(("2", "All Objects", ""))
	ExportMode = EnumProperty(name="Export", description="Select which objects to export", items=ExportModes, default="1")
	
	CompressData = BoolProperty(name="Compress Data", description="Zlib Compress data as per .a3d spec", default=True)
	
	ExportAnim = BoolProperty(name="Animation", description="Animation", default=False)
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
			Config = A3DExporterSettings(A3DVersionSystem=self.A3DVersionSystem,ExportMode=self.ExportMode,CompressData=self.CompressData,ExportAnim=self.ExportAnim,ExportUV=self.ExportUV,ExportNormals=self.ExportNormals,ExportTangents=self.ExportTangents)
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
	
	print("exporting lights...\n")
	#loop over every light
	for obj in objs_lights:
		light = obj.data
		if light.type == 'POINT':
			#omniLights/ambientlight
			#name
			a3dstr = A3D2String()
			a3dstr.name = cleanupString(light.name)
			
			#create transform/matrix
			a3dtrans = A3D2Transform()
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
			
			a3damb = A3D2AmbientLight()
			#a3damb._boundBoxId = None
			a3damb._color = int(rgb2hex(light.color), 0)
			a3damb._id = len(ambientLights)
			a3damb._intensity = int(light.energy)
			a3damb._name = a3dstr
			#a3damb._parentId = None
			a3damb._transform = a3dtrans
			a3damb._visible = 1
			ambientLights.append(a3damb)
		elif light.type == 'SPOT':
			print("spotlight")
			#spotLights
			#spotLights.append()
		elif light.type == 'AREA':
			print("arealight")
			#directionalLights
			#directionalLights.append()
		else:
			print("light type not supported")
	
	print("exporting meshes...\n")
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
		a3dbox = A3D2Box()
		a3dbox._box = bb
		a3dbox._id = len(boxes)
		boxes.append(a3dbox)
		
		#create indexbuffer
		a3dibuf = A3D2IndexBuffer()
		for x in range(len(ins)):
			a3dibuf._byteBuffer.append(ins[x])
		a3dibuf._id = len(indexBuffers)
		a3dibuf._indexCount = len(a3dibuf._byteBuffer)
		indexBuffers.append(a3dibuf)
		
		#create material
		a3dmat = A3D2Material()
		a3dmat._diffuseMapId = int("ffffffff",16)
		a3dmat._glossinessMapId = int("ffffffff",16)
		a3dmat._id = 0
		a3dmat._lightMapId = int("ffffffff",16)
		a3dmat._normalMapId = int("ffffffff",16)
		a3dmat._opacityMapId = int("ffffffff",16)
		a3dmat._reflectionCubeMapId = int("ffffffff",16)
		a3dmat._specularMapId = int("ffffffff",16)
		#materials.append(a3dmat)
		
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
					a3dimg = A3D2Image()
					a3dimg._id = len(images)
					a3dimg._url = a3dstr
					images.append(a3dimg)
					#create maps
					a3dmap = A3D2Map()
					a3dmap._channel = 0
					a3dmap._id = len(maps)
					a3dmap._imageId = a3dimg._id
					maps.append(a3dmap)
				
				#create material
				a3dmat = A3D2Material()
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
				a3dsurf = A3D2Surface()
				a3dsurf._indexBegin = int(start[x])
				#a3dsurf._materialId = int("ffffffff",16)
				a3dsurf._materialId = a3dmat._id
				a3dsurf._numTriangles = int(end[x])
				mesh_surfaces.append(a3dsurf)
		else:
			#surface for all faces
			a3dsurf = A3D2Surface()
			a3dsurf._indexBegin = 0
			#a3dsurf._materialId = int("ffffffff",16)
			#a3dsurf._materialId = 0
			a3dsurf._numTriangles = int(len(ins)/3)
			mesh_surfaces.append(a3dsurf)
		
		#create transform/matrix
		a3dtrans = A3D2Transform()
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
		a3dmesh = A3D2Mesh()
		#a3dmesh._boundBoxId = 0
		a3dmesh._id = len(meshes)
		a3dmesh._indexBufferId = a3dibuf._id
		a3dmesh._name = a3dstr
		#a3dmesh._parentId = 0
		a3dmesh._surfaces = mesh_surfaces
		a3dmesh._transform = a3dtrans
		a3dmesh._vertexBuffers = [len(vertexBuffers)] #vertex buffer ids
		a3dmesh._visible = 1
		meshes.append(a3dmesh)
		
		a3dstr2 = A3D2String()
		a3dstr2.name = ""
		
		a3dobj = A3D2Object()
		a3dobj._boundBoxId = 0
		a3dobj._id = len(objects)
		a3dobj._name = a3dstr2
		a3dobj._parentId = 0
		a3dobj._transform = a3dtrans
		a3dobj._visible = 1
		#objects.append(a3dobj)
		
		#create vertexbuffer
		a3dvbuf = A3D2VertexBuffer()
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
	
	
	# create a3d2 object from data
	a3d2 = A3D2(ambientLights,animationClips,animationTracks,boxes,cubeMaps,decals,directionalLights,images,indexBuffers,joints,maps,materials,meshes,objects,omniLights,spotLights,sprites,skins,vertexBuffers,Config)
	
	# save to file
	a3d2.write(file)
	
	print('Export Completed...\n')

#==================================
# A3D IMPORTER
#==================================

class A3DImporter(bpy.types.Operator):
	bl_idname = "ops.a3dimporter"
	bl_label = "Import A3D (Alternativa)"
	bl_description = "Import A3D (Alternativa)"
	
	filepath= StringProperty(name="File Path", description="Filepath used for importing the A3D file", maxlen=1024, default="")

	def execute(self, context):
		# open a3d file
		file = open(self.filepath,'rb')
		file.seek(0)
		version = ord(file.read(1))
		if version == 0:
			loadA3d1(file)
		else:
			loadA3d2(file)
		file.close()
		return {'FINISHED'}
	def invoke (self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}	

def loadA3d1(file):
	print("coming soon...")
	file.close()	
	return {'FINISHED'}

def loadA3d2(file):	
	#rewind
	file.seek(0)
	
	# read package length
	a3dpackage = A3DPackage()
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
	a3dnull = A3DNull()
	a3dnull.read(file)
	print(a3dnull._mask)
	print(a3dnull._byte_list)
	
	ver = A3DVersion()
	ver.read(file)
	print('A3D Version %i.%i' %(ver.baseversion,ver.pointversion))
			
	#read data
	a3d2 = A3D2(file)
	a3d2.read(file,a3dnull._mask)
	
	file.close()
	
	return {'FINISHED'}

#==================================
# A3D SHARED
#==================================

class A3DPackage:
	def __init__(self):
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

class A3DNull:
	def __init__(self):
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
					print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
					self._mask = nulldata
				elif temp_data[2] == '1':
					#01
					temp = ord(file.read(1))
					temp = bin(temp)[2:].rjust(8, '0')
					nulldata = temp_data[3:8] + temp
					#print('Null mask %s' % str(nulldata))
					print('(LL=01) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
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
					print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
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
					#print('Null mask %s' % str(nulldata))
					print('(LL=11) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
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
				print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
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
				print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
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
		bits = x.bit_length()
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
					bytenum = bits/8
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
					#left to right
					for j in range(bytenum):
						byte = int( ( x >> (tbits - (8 * (j+1))) ) & 255 )
						file.write(struct.pack("B",byte))
				else:
					#right to left
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
	def __init__(self,ambientLights=[],animationClips=[],animationTracks=[],boxes=[],cubeMaps=[],decals=[],directionalLights=[],images=[],indexBuffers=[],joints=[],maps=[],materials=[],meshes=[],objects=[],omniLights=[],spotLights=[],sprites=[],skins=[],vertexBuffers=[],Config=None):
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
		self.nullmask = ""
		self.Config = Config
	
	def read(self,file,mask):
		print("reada3d2")
		
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
			temp = ""
			arr = A3D2Array()
			arr.write(tfile,len(self.meshes))
			self.nullmask = self.nullmask + str(0)
			temp = temp + str(0)
			for cla in self.meshes:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
				temp = temp + cla._optmask
			print("mesh:"+str(temp))
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
		
		
		tfile2 = tempfile.TemporaryFile(mode ='w+b')
		
		print("nullmask = "+self.nullmask)
		
		#nullmask
		null = A3DNull()
		null._mask = self.nullmask
		null.write(tfile2)
		
		#version
		ver = A3DVersion()
		ver.baseversion = 2
		ver.pointversion = 0
		ver.write(tfile2)
		
		#a3d2
		tfile.seek(0)
		data = tfile.read()
		tfile2.write(data)
		tfile.close()
		
		#write package length
		a3dpack = A3DPackage()
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
			print("1 byte required\n")
			file.write(struct.pack("B", bylen))
		elif bitnum > 7 and bitnum <= 14:
			print("2 byte required\n")
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
			print("3 byte required\n")
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
				print("1 byte required\n")
				file.write(struct.pack("B", bylen))
				self.writeName(file)
			elif bitnum > 7 and bitnum <= 14:
				print("2 byte required\n")
				byte1 = int((bylen >> 8) & 255)
				byte1 = byte1 + 128 #add 10000000 bits
				byte2 = int(bylen & 255)
				file.write(struct.pack("B", byte1))
				file.write(struct.pack("B", byte2))
				self.writeName(file)
			elif bitnum > 14 and bitnum <= 22:
				print("3 byte required\n")
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
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
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
	def __init__(self):
		self._id = 0
		self._loop = 0
		self._name = None
		self._objectIDs = None
		self._tracks = 0
		
		self._optionals = [self._name,self._objectIDs]
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")
		
class A3D2Track:
	def __init__(self):
		self._id = 0
		self._keyframes = 0
		self._objectName = 0
		
		self._optionals = []
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")
	
class A3D2Box:
	def __init__(self):
		self._box = []
		self._id = 0
		
		self._optionals = []
		self._optmask = ""
	
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file):
		print("read")
		
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
	def __init__(self):
		self._backId = None
		self._bottomId = None
		self._frontId = None
		self._id = 0
		self._leftId = None
		self._rightId = None
		self._topId = 0
		
		self._optionals = [self._backId,self._bottomId,self._frontId,self._leftId,self._rightId]
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2Decal:
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2DirectionalLight:
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2Image:
	def __init__(self):
		self._id = 0
		self._url = 0
		
		self._optionals = []
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		file.write(struct.pack(">L",self._id))
		self._url.write(file)

class A3D2IndexBuffer:
	def __init__(self):
		self._byteBuffer = []
		self._id = 0
		self._indexCount = 0
		
		self._optionals = []
		self._optmask = ""
	
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file):
		print("read")
		
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
	def __init__(self):
		self._boundBoxId = None
		self._id = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")
		
class A3D2Map:
	def __init__(self):
		self._channel = 0
		self._id = 0
		self._imageId = 0
		
		self._optionals = []
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		file.write(struct.pack(">H",self._channel))
		file.write(struct.pack(">L",self._id))
		file.write(struct.pack(">L",self._imageId))

class A3D2Material:
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
			
	def read(self,file):
		print("read")
		
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
	def __init__(self):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._name = None
		self._parentId = None
		self._surfaces = 0
		self._transform = None
		self._vertexBuffers = [0]
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
	
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file):
		print("read")
		
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
	def __init__(self):
		self._boundBoxId = None
		self._id = 0
		self._name = None
		self._parentId = None
		self._transform = None
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
	
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file):
		print("read")
		
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
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2SpotLight:
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2Sprite:
	def __init__(self):
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
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2Skin:
	def __init__(self):
		self._boundBoxId = None
		self._id = 0
		self._indexBufferId = 0
		self._jointBindTransforms = 0
		self._joints = 0
		self._name = None
		self._numJoints = 0
		self._parentId = None
		self._surfaces = 0
		self._transform = None
		self._vertexBuffers = 0
		self._visible = 1
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")
		
class A3D2JointBindTransform:
	def __init__(self):
		self._bindPoseTransform = 0
		self._id = 0
		
		self._optionals = []
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")

class A3D2Keyframe:
	def __init__(self):
		self._time = 0
		self._transform = 0
		
		self._optionals = []
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
		
	def read(self,file):
		print("read")
		
	def write(self,file):
		print("write")
		
class A3D2VertexBuffer:
	def __init__(self):
		self._attributes = [0]
		self._byteBuffer = []
		self._id = 0
		self._vertexCount = 0
		
		self._optionals = []
		self._optmask = ""
	
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
				
	def read(self,file):
		print("read")
		
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
		bybufsize = int(len(self._byteBuffer)*4) #this worked for cube
		#bybufsize = int(len(self._byteBuffer)*3)
		#bybufsize = int( (self._vertexCount*3)*4 )
		arr.write(file,bybufsize) # times 4 because bytebuffer is length of bytes
		for byte in self._byteBuffer:
			file.write(struct.pack("<f",byte))
		#id
		file.write(struct.pack(">L",self._id))
		#vertexcount
		file.write(struct.pack(">H",self._vertexCount))
		print("vbuf_vertexCount="+str(self._vertexCount))
		print("vbuf_byteBufferlength="+str(bybufsize))
		print("vbuf_attributes="+str(self._attributes))
	
	def packVertexBuffer(self,file):
		print("unpackVertexBuffer")
		#versionMinor >= 6 then compressed
		
		#data = read readUnsignedShort
		#vi &= 0x7FFF;
		#vi ^= (vi + 0x1c000) ^ vi;
		#vi = vi << 13;
		#tempBuffer.writeUnsignedInt(data > 0x8000 ? vi | 0x80000000 : vi);
		
	def unpackVertexBuffer(self,file):
		print("unpackVertexBuffer")
		#data = read readUnsignedShort
		#vi &= 0x7FFF;
		#vi ^= (vi + 0x1c000) ^ vi;
		#vi = vi << 13;
		#tempBuffer.writeUnsignedInt(data > 0x8000 ? vi | 0x80000000 : vi);

class A3D2Surface:
	def __init__(self):
		self._indexBegin = 0
		self._materialId = None
		self._numTriangles = 0
		
		self._optionals = [self._materialId]
		self._optmask = ""
		
	def readOptions(self):
		if len(self._optionals) > 0:
			for o in self._optionals:
				if o is not None:
					self._optmask = self._optmask + str(0)
				else:
					self._optmask = self._optmask + str(1)
		return self._optmask
			
	def read(self,file):
		print("read")
		
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
	def __init__(self):
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
	def __init__(self):		
		self._matrix = A3DMatrix()
		
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
		
	def read(self,file):
		temp = file.read(4)
		self.a = struct.unpack('>f',temp)
		temp = file.read(4)
		self.b = struct.unpack('>f',temp)
		temp = file.read(4)
		self.c = struct.unpack('>f',temp)
		temp = file.read(4)
		self.d = struct.unpack('>f',temp)
		temp = file.read(4)
		self.e = struct.unpack('>f',temp)
		temp = file.read(4)
		self.f = struct.unpack('>f',temp)
		temp = file.read(4)
		self.g = struct.unpack('>f',temp)
		temp = file.read(4)
		self.h = struct.unpack('>f',temp)
		temp = file.read(4)
		self.i = struct.unpack('>f',temp)
		temp = file.read(4)
		self.j = struct.unpack('>f',temp)
		temp = file.read(4)
		self.k = struct.unpack('>f',temp)
		temp = file.read(4)
		self.l = struct.unpack('>f',temp)
	
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
	bl_idname = "mesh.a3d_logo"
	bl_label = "Add A3D Logo"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[(0.872773, -0.617606, 0.000000), (1.018175, -1.009088, 0.000000), (-0.163934, -1.463471, 0.000000), (-0.691019, -0.326800, 0.000000), (0.518353, 0.145759, 0.000000), (0.518353, 0.145759, 0.000000), (-1.050736, 0.329527, 0.000000), (0.158636, 0.802085, 0.000000), (-0.477481, 1.692649, 0.000000), (-1.686853, 1.220090, 0.000000), (-0.969712, 2.306044, 0.000000), (-2.194230, 1.788049, 0.000000), (-2.981800, 2.484746, 0.000000), (-1.757283, 3.002741, 0.000000), (-2.204077, 3.335943, 0.000000), (-3.436167, 2.764939, 0.000000), (-3.385423, 4.138652, 0.000000), (-3.945794, 3.838778, 0.000000), (-4.170708, 2.181850, 0.000000), (-4.460729, 3.478323, 0.000000), (-4.837094, 1.462456, 0.000000), (-5.289167, 2.801334, 0.000000), (-6.397775, 1.447379, 0.000000), (-5.954789, -0.200456, 0.000000), (-7.117453, 0.171587, 0.000000), (-6.325532, -1.410823, 0.000000), (-7.531813, -0.864313, 0.000000), (-7.499100, -1.126014, 0.000000), (-7.400962, -1.213248, 0.000000), (-7.128357, -1.322290, 0.000000), (-6.310541, -1.409523, 0.000000), (-4.809847, -1.410823, 0.000000), (-4.809847, -0.135031, 0.000000), (-3.861181, 0.072149, 0.000000), (-3.664905, -1.105505, 0.000000), (-2.596293, -0.669337, 0.000000), (-2.814377, 0.551934, 0.000000), (-1.320501, 0.126670, 0.000000), (-2.072891, 1.053528, 0.000000), (-2.814377, 0.551934, 1.000000), (-2.072891, 1.053528, 1.000000), (-1.320501, 0.126670, 1.000000), (-2.596293, -0.669337, 1.000000), (-3.861181, 0.072149, 1.000000), (-3.664905, -1.105505, 1.000000), (-4.809847, -1.410823, 1.000000), (-4.809847, -0.135031, 1.000000), (-5.954789, -0.200456, 1.000000), (-6.325532, -1.410823, 1.000000), (-6.310541, -1.409523, 1.000000), (-7.128357, -1.322290, 1.000000), (-7.400962, -1.213248, 1.000000), (-7.499100, -1.126014, 1.000000), (-7.531813, -0.864313, 1.000000), (-7.117453, 0.171587, 1.000000), (-6.397775, 1.447379, 1.000000), (-4.837094, 1.462456, 1.000000), (-5.289167, 2.801334, 1.000000), (-4.170708, 2.181850, 1.000000), (-4.460729, 3.478323, 1.000000), (-3.945794, 3.838778, 1.000000), (-3.436167, 2.764939, 1.000000), (-3.385423, 4.138652, 1.000000), (-2.204077, 3.335943, 1.000000), (-2.981800, 2.484746, 1.000000), (-1.757283, 3.002741, 1.000000), (-2.194230, 1.788049, 1.000000), (-0.969712, 2.306044, 1.000000), (-1.686853, 1.220090, 1.000000), (-0.477481, 1.692649, 1.000000), (-1.050736, 0.329527, 1.000000), (0.158636, 0.802085, 1.000000), (-0.691019, -0.326800, 1.000000), (0.518353, 0.145759, 1.000000), (0.872773, -0.617606, 1.000000), (-0.163934, -1.463471, 1.000000), (1.018175, -1.009088, 1.000000)]
		faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (3, 6, 7), (3, 7, 4), (6, 9, 8), (6, 8, 7), (9, 11, 10), (9, 10, 8), (11, 12, 13), (11, 13, 10), (12, 15, 14), (12, 14, 13), (14, 15, 16), (15, 18, 17), (15, 17, 16), (17, 18, 19), (18, 20, 21), (18, 21, 19), (20, 23, 22), (20, 22, 21), (22, 23, 24), (23, 25, 26), (23, 26, 24), (25, 30, 29), (25, 29, 26), (26, 29, 28), (26, 28, 27), (23, 32, 31), (23, 31, 25), (31, 32, 33), (31, 33, 34), (33, 36, 35), (33, 35, 34), (36, 38, 37), (36, 37, 35), (36, 39, 40), (36, 40, 38), (38, 40, 41), (38, 41, 37), (37, 41, 42), (37, 42, 35), (33, 43, 39), (33, 39, 36), (35, 42, 44), (35, 44, 34), (34, 44, 45), (34, 45, 31), (32, 46, 43), (32, 43, 33), (23, 47, 46), (23, 46, 32), (31, 45, 48), (31, 48, 25), (25, 48, 49), (25, 49, 30), (30, 49, 50), (30, 50, 29), (29, 50, 51), (29, 51, 28), (28, 51, 52), (28, 52, 27), (27, 52, 53), (27, 53, 26), (26, 53, 54), (26, 54, 24), (24, 54, 55), (24, 55, 22), (20, 56, 47), (20, 47, 23), (22, 55, 57), (22, 57, 21), (18, 58, 56), (18, 56, 20), (21, 57, 59), (21, 59, 19), (19, 59, 60), (19, 60, 17), (15, 61, 58), (15, 58, 18), (17, 60, 62), (17, 62, 16), (16, 62, 63), (16, 63, 14), (12, 64, 61), (12, 61, 15), (14, 63, 65), (14, 65, 13), (11, 66, 64), (11, 64, 12), (13, 65, 67), (13, 67, 10), (9, 68, 66), (9, 66, 11), (10, 67, 69), (10, 69, 8), (6, 70, 68), (6, 68, 9), (8, 69, 71), (8, 71, 7), (3, 72, 70), (3, 70, 6), (7, 71, 73), (7, 73, 4), (74, 0, 4), (74, 4, 73), (2, 75, 72), (2, 72, 3), (0, 74, 76), (0, 76, 1), (1, 76, 75), (1, 75, 2), (39, 42, 41), (39, 41, 40), (43, 44, 42), (43, 42, 39), (45, 44, 43), (45, 43, 46), (47, 48, 45), (47, 45, 46), (53, 52, 51), (53, 51, 50), (48, 53, 50), (48, 50, 49), (47, 54, 53), (47, 53, 48), (55, 54, 47), (56, 57, 55), (56, 55, 47), (58, 59, 57), (58, 57, 56), (60, 59, 58), (61, 62, 60), (61, 60, 58), (63, 62, 61), (64, 65, 63), (64, 63, 61), (66, 67, 65), (66, 65, 64), (68, 69, 67), (68, 67, 66), (70, 71, 69), (70, 69, 68), (72, 73, 71), (72, 71, 70), (74, 73, 72), (74, 72, 75), (74, 75, 76) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("a3dlogo") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("a3dlogo", me)   
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}
		
class AddOccluder(bpy.types.Operator):
	bl_idname = "mesh.a3d_occluder"
	bl_label = "Add Occluder"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, -1), (1, -1, -1), (-1, -0.9999998, -1), (-0.9999997, 1, -1), (1, 0.9999995, 1), (0.9999994, -1.000001, 1), (-1, -0.9999997, 1), (-1, 1, 1) ]
		faces=[ (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("Occluder") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("Occluder", me)  		
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "occluder"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}
		
class AddSprite3D(bpy.types.Operator):
	bl_idname = "mesh.a3d_sprite3d"
	bl_label = "Add Sprite3D"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, 0), (1, -1, 0), (-1, -0.9999998, 0), (-0.9999997, 1, 0) ]
		faces=[ (0, 3, 2, 1) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("Sprite3D") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("Sprite3D", me)  
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		#rotate 90 degrees so plane is upright
		ob.rotation_euler = (1.57079633,0,1) 
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# give custom property type
		ob["a3dtype"] = "sprite3d"

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data	
		return {'FINISHED'}
				
class AddSkybox(bpy.types.Operator):
	bl_idname = "mesh.a3d_skybox"
	bl_label = "Add Skybox"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[ (1, 1, -1), (1, -1, -1), (-1, -0.9999998, -1), (-0.9999997, 1, -1), (1, 0.9999995, 1), (0.9999994, -1.000001, 1), (-1, -0.9999997, 1), (-1, 1, 1) ]
		faces=[ (0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (4, 0, 3, 7) ]
		
		# create a new mesh  
		me = bpy.data.meshes.new("Skybox") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("Skybox", me)  
				
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob) 

		# give custom property type
		ob["a3dtype"] = "skybox"		
		
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
		
# note to self
# blender info on custom properties
# http://wiki.blender.org/index.php/Doc:2.5/Manual/Extensions/Python/Properties

class A3d_submenu(bpy.types.Menu):
    bl_idname = "A3d_submenu"
    bl_label = "Alternativa3D"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("mesh.a3d_skybox", text="Skybox", icon='MESH_CUBE')
        layout.operator("mesh.a3d_sprite3d", text="Sprite3D", icon='MESH_PLANE')
        layout.operator("mesh.a3d_occluder", text="Occluder", icon='MESH_CUBE')
        layout.operator("mesh.a3d_logo", text="A3D Logo", icon='MESH_TORUS')
		
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