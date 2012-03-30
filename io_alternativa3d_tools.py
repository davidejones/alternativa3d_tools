bl_info = {
	'name': 'Export: Alternativa3d Tools',
	'author': 'David E Jones, http://davidejones.com',
	'version': (1, 1, 2),
	'blender': (2, 5, 7),
	'location': 'File > Import/Export;',
	'description': 'Importer and exporter for Alternativa3D engine. Supports A3D and Actionscript"',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://davidejones.com',
	'category': 'Import-Export'}

import math, os, time, bpy, random, mathutils, re, ctypes, struct, binascii, zlib, tempfile, re
import bpy_extras.io_utils
from bpy import ops
from bpy.props import *

#==================================
# Common Functions
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
	def __init__(self,A3DVersionSystem=1,CompilerOption=1,ExportMode=1,DocClass=False,CopyImgs=True,ByClass=False):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.CompilerOption = int(CompilerOption)
		self.ExportMode = int(ExportMode)
		self.DocClass = bool(DocClass)
		self.CopyImgs = bool(CopyImgs)
		self.ByClass = bool(ByClass)

# Exporter (.as) class thats called from menu
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
	A3DVersions.append(("5", "7.8.0", ""))
	A3DVersions.append(("6", "8.5.0", ""))
	A3DVersions.append(("7", "8.8.0", ""))
	A3DVersions.append(("8", "8.12.0", ""))
	A3DVersions.append(("9", "8.17.0", ""))
	A3DVersions.append(("10", "8.27.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D to export to", items=A3DVersions, default="10")
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
			Config = ASExporterSettings(A3DVersionSystem=self.A3DVersionSystem,CompilerOption=self.CompilerOption,ExportMode=self.ExportMode, DocClass=self.DocClass,CopyImgs=self.CopyImgs,ByClass=self.ByClass)
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
	
		#convert quads to triangles
		bpy.ops.object.mode_set(mode="OBJECT", toggle = False)
		bpy.ops.object.mode_set(mode="EDIT", toggle = True)
		mesh = obj.data
		for f in mesh.faces:
			f.select = True	
		bpy.ops.mesh.quads_convert_to_tris()
		#Return to object mode
		bpy.ops.object.mode_set(mode="EDIT", toggle = False)
		bpy.ops.object.mode_set(mode="OBJECT", toggle = True)
		

		if "a3dtype" in obj:
			aobjs.append(obj)
		else:
			if Config.A3DVersionSystem == 10:
				WriteClass8270(file,obj,Config)
			elif (Config.A3DVersionSystem == 6) or (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 8):
				WriteClass85(file,obj,Config)
			elif Config.A3DVersionSystem == 5:
				WriteClass77(file,obj,Config)
			elif Config.A3DVersionSystem == 4:
				WriteClass77(file,obj,Config)
			elif Config.A3DVersionSystem == 3:
				WriteClass76(file,obj,Config)
			elif Config.A3DVersionSystem == 2:
				WriteClass75(file,obj,Config)
			elif Config.A3DVersionSystem == 1:
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
		file.write("\timport alternativa.engine3d.materials.Texture;\n")
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
	elif (Config.A3DVersionSystem == 3) or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5):
		# version 7.6.0, 7.7.0, 7.8.0
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif (Config.A3DVersionSystem == 6) or (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10):
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
			# if version 5
			if Config.A3DVersionSystem == 1:
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(nme)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':Texture = new Texture(new bmp'+str(nme)+'().bitmapData, "'+str(Material.name)+'");\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(Material.name)+":Bitmap = new Bitmap(new bd"+str(nme)+"(0,0));\n")
					file.write('\t\tprivate var '+str(id)+':Texture = new Texture(bmp'+str(nme)+'.bitmapData, "'+str(nme)+'");\n\n')
			#if version 7's
			elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3) or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5):
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(nme)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':TextureMaterial = new TextureMaterial(new bmp'+str(nme)+'().bitmapData, true, true);\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(nme)+":Bitmap = new Bitmap(new bd"+str(nme)+"(0,0));\n")
					file.write("\t\tprivate var "+str(id)+":TextureMaterial = new TextureMaterial(bmp"+str(nme)+".bitmapData, true, true);\n\n")
			#if version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
			elif (Config.A3DVersionSystem == 6) or (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10):
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

def exportDataFile(verts,uvt,indices):
	print("writing file")
	realfile = open("C:/Users/David/Desktop/New folder (4)/test.bin","wb")
	file = tempfile.TemporaryFile(mode ='w+b')
	
	#version file
	#compression on/off
	
	#length of verts -short
	print("verts="+str(len(verts)*3))
	file.write(struct.pack("<H", len(verts)*3))
	for v in verts:
		file.write(struct.pack("<f", v[0]))
		file.write(struct.pack("<f", v[1]))
		file.write(struct.pack("<f", v[2]))
	
	#length of uvts -short
	print("uvt="+str(len(uvt)*2))
	file.write(struct.pack("<H", len(uvt)*2))
	for uv in uvt:
		file.write(struct.pack("<f", uv[0]))
		file.write(struct.pack("<f", uv[1]))
	
	#length of indices -short
	print("indices="+str(len(indices)))
	file.write(struct.pack("<H", len(indices)))
	for i in indices:
		file.write(struct.pack("<I", i))
		
	#materials
	# -name
	# -
		
	
	#rewind
	file.seek(0)
	
	#write compressed version
	realfile.write(zlib.compress(file.read()))
	
	#write regular version
	#realfile.write(file.read())
	
	file.close()
	realfile.close()

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

def WriteClass8270(file,obj,Config):
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	hasFaceUV = len(mesh.uv_textures) > 0
	vs = []
	uvt = []
	ins = []
	nr = []
	
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
	
	vertices_list = []
	vertices_co_list = []
	vertices_index_list = []
	normals_list = []
	uv_coord_list = []
	new_index = 0
	uvtex = mesh.uv_textures.active
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
				nr.append([normals_list[-1][0],normals_list[-1][1],normals_list[-1][2]])
				ins.append(vertices_index_list[-1])
				uv = [uv_coord_list[-1][0], 1.0 - uv_coord_list[-1][1]]
				uvt.append(uv)
	else:
		# if there are no image textures, output the old way
		for face in mesh.faces:
			if len(face.vertices) > 0:
				ins.append(face.vertices[0])
				ins.append(face.vertices[1])
				ins.append(face.vertices[2])
				for i in range(len(face.vertices)):
					hasFaceUV = len(mesh.uv_textures) > 0
					if hasFaceUV:
						uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
						uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
						uvt.append(uv)
		for v in mesh.vertices:
			vs.append([v.co[0],v.co[1],v.co[2]])
			nr.append([v.normal[0],v.normal[1],v.normal[2]])
			
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
		if len(uvt) > 0:
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
		if len(nr) > 0:
			file.write("\t\t\tvar normals:Array = [\n")
			for n in nr:
				#file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % (n[0],n[1],n[2]))
				file.write("\t\t\t\t%.6g, %.6g, %.6g,\n" % (n[0],n[1],n[2]))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar normals:Array = new Array();\n")
			
		#write tangents
		file.write("\t\t\tvar tangent:Array = new Array();\n\n")
		
		#set attributes
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
		if len(uvt) > 0:
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")	
			
		if len(nr) > 0:
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
		file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
		
		#set geometry
		file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
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

	
	#collect surface data, indexbegin/numtriangles etc
	c=0
	triangles = -1
	lastmat = None
	start,end,items,mts = [],[],[],[]
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
			else:
				if srcmat != lastmat:
					start.append(face.index * 3)
					if c != 0:
						end.append(triangles)
						triangles = 0
					mts.append(cleanupString(str(srcmat.name)))
			lastmat = srcmat
			items.append(srcmat)
			c = c+1
	end.append(triangles+1)
	
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
	
def WriteClass85(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	# check if we have an a3dtype
	# obj.has_key("a3dtype")
	if "a3dtype" in obj:
		print(obj["a3dtype"])
	else:
		print("nope")
	
	
	mesh = obj.data
	verts = mesh.vertices
	faces = []
	uvt = []
	ind = []
	normals = []
	surfaces = []
	hasFaceUV = len(mesh.uv_textures) > 0
	numVertices = len(mesh.vertices)
	Materials = mesh.materials
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
		
	file.write("\t\tprivate var attributes:Array;\n\n")
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tattributes = new Array();\n")
	file.write("\t\t\tattributes[0] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[1] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[2] = VertexAttributes.POSITION;\n")
	file.write("\t\t\tattributes[3] = VertexAttributes.TEXCOORDS[0];\n")
	file.write("\t\t\tattributes[4] = VertexAttributes.TEXCOORDS[0];\n")
	file.write("\t\t\tattributes[5] = VertexAttributes.NORMAL;\n")
	file.write("\t\t\tattributes[6] = VertexAttributes.NORMAL;\n")
	file.write("\t\t\tattributes[7] = VertexAttributes.NORMAL;\n")
	file.write("\t\t\tattributes[8] = VertexAttributes.TANGENT4;\n")
	file.write("\t\t\tattributes[9] = VertexAttributes.TANGENT4;\n")
	file.write("\t\t\tattributes[10] = VertexAttributes.TANGENT4;\n")
	file.write("\t\t\tattributes[11] = VertexAttributes.TANGENT4;\n\n")
	
	file.write("\t\t\tvar g:Geometry = new Geometry();\n")
	file.write("\t\t\tg.addVertexStream(attributes);\n")
	#file.write("\t\t\tg.numVertices = "+str(numVertices)+";\n\n")
	
	vs = []
	ins = []
	nr = []
	
	#test
	vertices_list = []
	vertices_co_list = []
	vertices_index_list = []
	normals_list = []
	uv_coord_list = []
	new_index = 0
	uvtex = mesh.uv_textures.active
	hasFaceUV = len(mesh.uv_textures) > 0
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
				# ^ We use our own indexing instead of Blender because
				# Warcraft needs UV per vertex, Blender gives per face
				# ^ For tris index is from 0 to 2, for quads 0 to 3
				# (4 vertices make a quad)
				uv_coord_list.append(uvs[vertex_index])
				# uvs is a float array
				# Lets see what we have stored:
				#print("index " + str(vertices_list[-1]))
				# ^ vertices_list
				#print("v " + str(vertices_co_list[-1][0]) + " " + str(vertices_co_list[-1][1]) + " " +  str(vertices_co_list[-1][2]))
				vs.append([vertices_co_list[-1][0],vertices_co_list[-1][1],vertices_co_list[-1][2]])
				# ^ vertices_co_list
				#print("n " + str(normals_list[-1][0]) + " " + str(normals_list[-1][1]) + " " +  str(normals_list[-1][2]))
				nr.append([normals_list[-1][0],normals_list[-1][1],normals_list[-1][2]])
				# ^ normals_list
				#print("f " + str(vertices_index_list[-1]))
				ins.append(vertices_index_list[-1])
				# ^ vertices_index_list
				#print("uv " + str(uv_coord_list[-1][0]) + " " + str(uv_coord_list[-1][1]) + "\n")
				uv = [uv_coord_list[-1][0], 1.0 - uv_coord_list[-1][1]]
				uvt.append(uv)
				# ^ uv_coord_list
	else:
		#no textures
		for face in mesh.faces:
			if len(face.vertices) > 0:
				ins.append(face.vertices[0])
				ins.append(face.vertices[1])
				ins.append(face.vertices[2])
				for i in range(len(face.vertices)):
					hasFaceUV = len(mesh.uv_textures) > 0
					if hasFaceUV:
						uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
						uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
						uvt.append(uv)
		for v in mesh.vertices:
			vs.append([v.co[0],v.co[1],v.co[2]])
			nr.append([v.normal[0],v.normal[1],v.normal[2]])
	#test
	
	if Config.ByClass == 1:
		exportDataFile(vs,uvt,ins)

	file.write("\t\t\tg.numVertices = "+str(len(vs))+";\n\n")
	
	file.write("\t\t\tvar vertices:Array = [\n")
	for v in vs:
		file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % (v[0],v[1],v[2]))
	file.write("\t\t\t];\n")
	
	# verts
	#file.write("\t\t\tvar vertices:Array = [\n")
	#vl =0
	#for face in mesh.faces:
	#	if len(face.vertices) > 0:
	#		v = mesh.vertices[face.index]
	#		normals.append(v.normal)
	#		if vl != len(mesh.vertices)-1:
	#			file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % v.co[:])
	#		else:
	#			file.write("\t\t\t\t%.6f, %.6f, %.6f\n" % v.co[:])
	#		vl += 1
	#file.write("\t\t\t];\n")
	
	#file.write("\t\t\tvar vertices:Array = [\n")
	#vl =0
	#for v in mesh.vertices:
	#	normals.append(v.normal)
	#	if vl != len(mesh.vertices)-1:
	#		file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % v.co[:])
	#	else:
	#		file.write("\t\t\t\t%.6f, %.6f, %.6f\n" % v.co[:])
	#	vl += 1
	#file.write("\t\t\t];\n")
	
	#file.write("\t\t\tvar vertices:Array = [\n")
	#for face in mesh.faces:
	#	if len(face.vertices) > 0:
	#		#v = mesh.vertices[face.index]
	#		#vertex indecies
	#		#print(face.vertices[:])
	#		for vi in face.vertices:
	#			v = mesh.vertices[vi]
	#			normals.append(v.normal)
	#			file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % v.co[:])
	#file.write("\t\t\t];\n")
	
	
	triangles = -1
	start = []
	end = []
	items = []
	c=0
	endcount=-1
	laststart=0
	lastmat = None
	mts = []
	for face in mesh.faces:
		triangles = triangles + 1
		#print(Materials[face.material_index].name+"\n")
		if face.material_index <= len(Materials)-1:
			srcmat = Materials[face.material_index]
			if srcmat not in items:
				#print(srcmat.name+"\n")
				#if c == 0:
				#	start.append(c)
				#	laststart = 0
				#else:
				#temp = (end[endcount] * 3) + laststart
				start.append(face.index * 3)
				#laststart = temp
				if c != 0:
					end.append(triangles)
					#endcount = endcount+1
					triangles = 0
				mts.append(cleanupString(str(srcmat.name)))
			else:
				if srcmat != lastmat:
					#print("last material doesn't match this one.."+lastmat.name+"-"+srcmat.name)
					start.append(face.index * 3)
					if c != 0:
						end.append(triangles)
						triangles = 0
					mts.append(cleanupString(str(srcmat.name)))
			lastmat = srcmat
			items.append(srcmat)
			c = c+1
	end.append(triangles+1)
	
	
	i = len(face.vertices)
	
	#for face in mesh.faces:
	#	if len(face.vertices) > 0:
	#		for i in range(len(face.vertices)):
	#			hasFaceUV = len(mesh.uv_textures) > 0
	#			if hasFaceUV:
	#				uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
	#				uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
					#uv_layer = mesh.uv_textures.active.data 
					#u1 = uv_layer[face.index].uv1[0]
					#v1 = 1.0 - uv_layer[face.index].uv1[1]
					#u2 = uv_layer[face.index].uv2[0] 
					#v2 = 1.0 - uv_layer[face.index].uv2[1] 
					#u3 = uv_layer[face.index].uv3[0] 
					#v3 = 1.0 - uv_layer[face.index].uv3[1] 
					#uv = [u1,v1,u2,v2,u3,v3]
	#				uvt.append(uv)
					
	if len(uvt) > 0:
		x=1
		file.write("\t\t\tvar uvt:Array = [\n")
		for u in uvt:
			#if x <= numVertices:
			file.write("\t\t\t\t"+str(u[0])+","+str(u[1]))
			if i != len(uvt)-1:
				file.write(",\n")
			else:
				file.write("\n")
			x = x+1
		file.write("\t\t\t];\n")
	else:
		file.write("\t\t\tvar uvt:Array = new Array();\n")
	
	#write out indices
	#mesh_faces = mesh.faces[:]
	#ind = 0
	#if len(mesh_faces) > 0:
	#	file.write("\t\t\tvar ind:Array = [\n")
	#	for i in range(len(mesh_faces)):
	#		fv = mesh_faces[i].vertices[:]
	#		if len(fv) == 3:
	#			file.write("\t\t\t\t%i, %i, %i" % fv)
	#			print("%i %i %i -1, " % fv)
	#			if i != len(mesh_faces)-1:
	#				file.write(",\n")
	#			else:
	#				file.write("\n")
	#			ind += 1
	#		else:
	#			file.write("\t\t\t\t%i, %i, %i,\n" % (fv[0], fv[1], fv[2]))
	#			file.write("\t\t\t\t%i, %i, %i" % (fv[0], fv[2], fv[3]))
	#			#print("%i %i %i -1, " % (fv[0], fv[1], fv[2]))
	#			#print("%i %i %i -1, " % (fv[0], fv[2], fv[3]))
	#			if i != len(mesh_faces)-1:
	#				file.write(",\n")
	#			else:
	#				file.write("\n")
	#			ind += 2
	#	file.write("\t\t\t];\n")
	#else:
	#	file.write("\t\t\tvar ind:Array = new Array();\n")
	
	#file.write("\t\t\tvar ind:Array = [\n")
	#for face in mesh.faces:
	#	if len(face.vertices) > 0:
	#		file.write("\t\t\t\t%i, %i, %i,\n" % (face.vertices[:]))
	#file.write("\t\t\t];\n")
	
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
	
	#write normals
	#if len(normals) > 0:
	#	file.write("\t\t\tvar normals:Array = [\n")
	#	for i in range(len(normals)):
	#		#file.write("\t\t\t\t%i, %i, %i" % (normals[i][0],normals[i][1],normals[i][2]))
	#		file.write("\t\t\t\t%.6f, %.6f, %.6f" % normals[i][:])
	#		if i != len(normals)-1:
	#			file.write(",\n")
	#		else:
	#			file.write("\n")
	#	file.write("\t\t\t];\n")
	#else:
	#	file.write("\t\t\tvar normals:Array = new Array();\n")
	
	
	file.write("\t\t\tvar normals:Array = [\n")
	for n in nr:
		file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % (n[0],n[1],n[2]))
	file.write("\t\t\t];\n")
	normals = nr
	
	#write tangents
	file.write("\t\t\tvar tangent:Array = new Array();\n\n")	
	
	file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
	
	if len(uvt) > 0:
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")
	else:
		file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")	
		
	if len(normals) > 0:
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
	else:
		file.write("\t\t\t//g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
	
	file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
	file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
	
	# if version 8.27.0
	if Config.A3DVersionSystem == 10:
		file.write("\t\t\t//g.calculateNormals();\n")
		file.write("\t\t\t//g.calculateTangents(0);\n")
		
	file.write("\t\t\tthis.geometry = g;\n")
	
	#file.write("\t\t\t//this.addSurface(new FillMaterial(0xFF0000), 0, "+str(ind)+");\n")
	
	for x in range(len(mts)):
		#material:Material, indexBegin:uint, numTriangles:uint
		#file.write("\t\t\tthis.addSurface("+mati[x]+", 0, "+str(ind)+");\n")
		file.write("\t\t\tthis.addSurface("+mts[x]+", "+str(start[x])+", "+str(end[x])+");\n")
	
	file.write("\t\t\tthis.calculateBoundBox();\n")
	
	# write mesh rotation, location and scale
	#WriteObjPosRot(file,obj)
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass77(file,obj,Config):
	#base=os.path.basename(file.name)
	#basename, extension = os.path.splitext(base)
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data
	#mesh = Mesh(obj.name)
	#mesh = bpy.data.meshes[obj.name]
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
				if hasFaceUV:
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
	file.write("\t\t\tcalculateFacesNormals();\n")
	file.write("\t\t\tcalculateVerticesNormals();\n")
	file.write("\t\t\tcalculateBounds();\n")
	
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
				if hasFaceUV:
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
	file.write("\t\tcalculateNormals();\n")
	file.write("\t\tcalculateBounds();\n")
	
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass75(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	mesh = obj.data
	verts = mesh.vertices
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tvar g:Geometry = new Geometry();\n\n")
	
	for face in mesh.faces:
		file.write('\t\t\t\tg.addFace(Vector.<Vertex>([\n')
		for i in range(len(face.vertices)):
			hasFaceUV = len(mesh.uv_textures) > 0
			if hasFaceUV:
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
	
	#setup materials
	mati = setupMaterials(file,obj,Config)
	
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	
	count=0
	for vert in mesh.vertices:
		file.write('\t\t\tcreateVertex(%f, %f, %f, %i);\n' % (vert.co.x, vert.co.y, vert.co.z, count))
		count += 1
	file.write('\n')
	
	x=0
	for meshface in mesh.faces:
		file.write('\t\t\tcreateFace([')
		k=0
		for vert in meshface.vertices:
			file.write('%i ' % (vert) )
			if k != len(meshface.vertices)-1:
				file.write(",")
			k += 1
		file.write('], '+str(x)+');\n')
		file.write('\t\t\tsetUVsToFace(new Point(%f,%f), new Point(%f,%f), new Point(%f,%f), %i);\n' % (x,x,x,x,x,x,x))
		x += 1
	
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
	def __init__(self,A3DVersionSystem=1,ExportMode=1):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.ExportMode = int(ExportMode)
		
class A3DExporter(bpy.types.Operator):
	bl_idname = "ops.a3dexporter"
	bl_label = "Export to A3D (Alternativa)"
	bl_description = "Export to A3D (Alternativa)"
	
	A3DVersions = []
	A3DVersions.append(("1.0", "2.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D .A3D to export to", items=A3DVersions, default="1")
	
	ExportModes = []
	ExportModes.append(("1", "Selected Objects", ""))
	ExportModes.append(("2", "All Objects", ""))
	ExportMode = EnumProperty(name="Export", description="Select which objects to export", items=ExportModes, default="1")
	
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		if not filePath.lower().endswith('.a3d'):
			filePath += '.a3d'
		try:
			print('Output file : %s' %filePath)
			file = open(filePath, 'wb')
			Config = A3DExporterSettings(A3DVersionSystem=self.A3DVersionSystem,ExportMode=self.ExportMode)
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
		print('Export all meshes...\n')
	
	objs_mesh = []
	objs_arm = []
	objs_lights = []
	objs_cameras = []
	
	for obj in objs_mesh:
		if obj.type == 'MESH':
			objs_mesh.append(obj)
		if obj.type == 'ARMATURE':
			objs_arm.append(obj)
		if obj.type == 'LAMP':
			objs_lights.append(obj)
		if obj.type == 'CAMERA':
			objs_cameras.append(obj)
	
	#writepackage	
	#write null mask
	#write message data
	
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
		loadA3d(self.filepath)
		return {'FINISHED'}
	def invoke (self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}	

def loadA3d(filename):	
	# open a3d file
	file = open(filename,'rb')
			
	# read package length
	a3dpackage = A3DPackage(file)
	
	#set current position
	curpos = file.tell()
	
	if a3dpackage.packed == 1:
		#decompress into variable
		data = file.read(a3dpackage.length)
		data = zlib.decompress(data)
		file.close()
		
		#file = open("C:/Users/David/Desktop/defaultModel_21-11-2011_13-47-51/model/box-extract.bin","wb")
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
	a3dnull = A3DNull(file)
	#print(a3dnull.mask)
	#print(a3dnull.byte_list)
	
	ver = A3DVersion(file)
	print('A3D Version %i.%i' %(ver.baseversion,ver.pointversion))
		
	#read data
	a3d2 = A3D2(file,a3dnull.mask)
	
	file.close()
	
	return {'FINISHED'}

#==================================
# A3D SHARED
#==================================

class A3DPackage:
	def __init__(self, file):
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
			self.length = int(plen,2)
			
			#second bit
			if temp_data[1] == '0':
				self.packed = 0
				print('Package not packed')
			elif temp_data[1] == '1':
				self.packed = 1
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
			
			self.length = int(plen,2)
			
			# if first bit is one then its auto packed
			self.packed = 1
			print('Package is packed')
		else:
			print('Error reading package L')

class A3DNull:
	def __init__(self, file):
		#setup byte list/mask
		self.byte_list = []
		self.mask = ""
		
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
				elif temp_data[2] == '1':
					#01
					temp = ord(file.read(1))
					temp = bin(temp)[2:].rjust(8, '0')
					nulldata = temp_data[3:8] + temp
					#print('Null mask %s' % str(nulldata))
					print('(LL=01) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					print('19 known classes meaning %i optional fields' % ( (int(nulldata,2)*8) - 19 ) )
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
					self.mask += '{0:08b}'.format(ord(byt))
					self.byte_list.append('%02X' % ord(byt))
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
					self.mask += '{0:08b}'.format(ord(byt))
					self.byte_list.append('%02X' % ord(byt))
			else:
				print('Error reading long Null..')
				
class A3DMessageData:
	def __init__(self, file):
		#read byte
		temp_data = ord(file.read(1))
		
		#get bits of byte
		temp_data = bin(temp_data)[2:].rjust(8, '0')
		
		print(temp_data)
		
		if temp_data[0] == '0':
			numelements = temp_data[1:7]
		elif temp_data[0] == '1':
			if temp_data[0:2] == '10':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				numelements = temp_data[2:7] + temp
			elif temp_data[0:2] == '11':
				temp = ord(file.read(1))
				temp = bin(temp)[2:].rjust(8, '0')
				temp1 = ord(file.read(1))
				temp1 = bin(temp1)[2:].rjust(8, '0')
				numelements = temp_data[2:7] + temp + temp1
			else:
				print('Error reading message data')
		else:
			print('Error reading message data')
		
		#print("Numelements:"+numelements)
		print('Number of elements in message data %i' % int(numelements,2))
		
		ver = A3DVersion(file)
		print('A3D Version %i.%i' %(ver.baseversion,ver.pointversion))
		
class A3D2:
	def __init__(self, file, mask):
	
		# define 19 classes
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
		
		#for key, val in funcs.items():
		#	key()
	
		i = 0
		j = 0
		for x in range(len(mask)):
			#print('i is %i' % i)
			#print('j is %i' % j)
			#print('mask is %s' % mask[j])
			
			#exit if we gone past amount
			if i > 18:
				break
			
			if mask[j] == '0':
				t = funcs[i](file,mask,j+1)
				j = t.ind
			elif mask[j] == '1':
				j += 1
			i += 1	

class readArray:
	def __init__(self, file):
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
		
class readString:
	def __init__(self, file):
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
		for x in range(nlen):
			name += chr(ord(file.read(1)))
		self.name = name
		
class A3D2AmbientLight:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("AmbientLight (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			
			if mask[self.ind] == '0':
				#boundBoxId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("boundBoxId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			#color
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			RGBint = temp_data[0]
			Blue =  RGBint & 255
			Green = (RGBint >> 8) & 255
			Red =   (RGBint >> 16) & 255		
			print("color: %s" % rgbtohtmlcolor((Red, Green, Blue)))
			
			#id
			temp = file.read(8)
			#print("id: %i" % int(temp))
			
			#intensity
			temp = file.read(4)
			s = struct.unpack('>f',temp)
			print("intensity: %f" %s[0])
			
			if mask[self.ind] == '0':
				#name
				string = readString(file)
				print(string.name)
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#parentId
				temp = file.read(8)
				#print("parentId: %i" % int(temp))
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#transform
				transform = A3D2Transform(file)
				self.ind += 1
			else:
				self.ind += 1
				
			#visible
			visible = ord(file.read(1))
			print("visible: %i" % visible)

class A3D2Transform:
	def __init__(self, file):		
		self.matrix = A3DMatrix(file)
		
class A3DMatrix:
	def __init__(self, file):
		
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
		
class A3D2AnimationClip:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("AnimationClip (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			#id
			temp = file.read(4)
			print(temp)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			#loop
			loop = ord(file.read(1))
			print("loop: %i" % loop)
			#name
			string = readString(file)
			print(string.name)
			#objectIDs array of int64
			#tracks array of int 4
	
class A3D2Track:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Track (%i)" % array.length)
		print("===================")

class A3D2Box:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Box (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			arrayfl = readArray(file)
			print("box floats: (%i)" % arrayfl.length)
			for x in range(arrayfl.length):
				temp = file.read(4)
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			print("id: %i" % temp_data[0])
		
class A3D2CubeMap:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("CubeMap (%i)" % array.length)
		print("===================")
	
class A3D2Decal:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Decal (%i)" % array.length)
		print("===================")
	
class A3D2DirectionalLight:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("DirectionalLight (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			if mask[self.ind] == '0':
				#boundBoxId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("boundBoxId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
			
			#color
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			RGBint = temp_data[0]
			Blue =  RGBint & 255
			Green = (RGBint >> 8) & 255
			Red =   (RGBint >> 16) & 255		
			print("color: %s" % rgbtohtmlcolor((Red, Green, Blue)))
			
			#id
			temp = file.read(8)
			#print("id: %i" % int(temp))
			
			#intensity
			temp = file.read(4)
			s = struct.unpack('>f',temp)
			print("intensity: %f" %s[0])
			
			if mask[self.ind] == '0':
				#name
				string = readString(file)
				print(string.name)
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#parentId
				temp = file.read(8)
				#print("parentId: %i" % int(temp))
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#transform
				transform = A3D2Transform(file)
				self.ind += 1
			else:
				self.ind += 1
				
			#visible
			visible = ord(file.read(1))
			print("visible: %i" % visible)
	
class A3D2Image:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Image (%i)" % array.length)
		print("===================")
	
class A3D2IndexBuffer:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		self.indices = []
		
		print("===================")
		print("IndexBuffer (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			byarray = readArray(file)
			print('bytearray(%i)' % byarray.length)
			for x in range(int(byarray.length/2)):
				byte = file.read(struct.calcsize('H'))
				self.indices.append(int(struct.unpack('<H', byte)[0]))
			print(self.indices)			
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			print("id: %i" % temp_data[0])
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			print("indexcount: %i" % temp_data[0])

class A3D2Joint:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Joint (%i)" % array.length)
		print("===================")
	
class A3D2Map:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Map (%i)" % array.length)
		print("===================")
	
class A3D2Material:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Material (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			if mask[self.ind] == '0':
				#diffuseMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("diffuseMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#glossinessMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("glossinessMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			#id
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			print("id: %i" % temp_data[0])
			
			if mask[self.ind] == '0':
				#lightMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("lightMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#normalMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("normalMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#opacityMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("opacityMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#reflectionCubeMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("reflectionCubeMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#specularMapId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("specularMapId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
	
class A3D2Mesh:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Mesh (%i)" % array.length)
		print("===================")
		
		for i in range(array.length):
			if mask[self.ind] == '0':
				#boundBoxId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("boundBoxId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
				
			#id
			temp = file.read(8)
			print('id:')
			
			#indexBufferId
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			print("indexBufferId: %i" % temp_data[0])
			
			if mask[self.ind] == '0':
				#name
				string = readString(file)
				print(string.name)
				self.ind += 1
			else:
				self.ind += 1
				
			if mask[self.ind] == '0':
				#parentid
				temp = file.read(8)
				print('parentid:')
				self.ind += 1
			else:
				self.ind += 1
				
			surfarray = readArray(file)
			for j in range(surfarray.length):
				s = A3D2Surface(file, mask, self.ind)
				self.ind = s.ind
			
			if mask[self.ind] == '0':
				#transform
				transform = A3D2Transform(file)
				print('transform:')
				self.ind += 1
			else:
				self.ind += 1
				
			#vertexbuffers
			vbufarray = readArray(file)
			print('vertexbuffers (%i)' % vbufarray.length)
			for a in range(vbufarray.length):
				temp = file.read(4)
				
			#visible
			visible = ord(file.read(1))
			print("visible: %i" % visible)
				
class A3D2Surface:
	def __init__(self, file, mask, ind):		
		self.ind = ind
		
		#indexBufferId
		temp = file.read(4)
		temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
		print("indexBegin: %i" % temp_data[0])
		
		if mask[self.ind] == '0':
			#materialId
			temp = file.read(4)
			temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
			print("materialId: %i" % temp_data[0])
			self.ind += 1
		else:
			self.ind += 1
		
		#numTriangles
		temp = file.read(4)
		temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
		print("numTriangles: %i" % temp_data[0])
	
class A3D2Object:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
				
		print("===================")
		print("Object (%i)" % array.length)
		print("===================")
		
		for x in range(array.length):		
			if mask[self.ind] == '0':
				#boundBoxId
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
				print("boundBoxId: %i" % temp_data[0])
				self.ind += 1
			else:
				self.ind += 1
			
			#id
			temp = file.read(8)
			print('id:')
			
			if mask[self.ind] == '0':
				#name
				string = readString(file)
				print(string.name)
				self.ind += 1
			else:
				self.ind += 1
			
			if mask[self.ind] == '0':
				#parentid
				temp = file.read(8)
				print('parentid:')
				self.ind += 1
			else:
				self.ind += 1
						
			if mask[self.ind] == '0':
				#transform
				transform = A3D2Transform(file)
				print('transform:')
				self.ind += 1
			else:
				self.ind += 1
			
			#visible
			visible = ord(file.read(1))
			print("visible: %i" % visible)
	
class A3D2OmniLight:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("OmniLight (%i)" % array.length)
		print("===================")
	
class A3D2SpotLight:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("SpotLight (%i)" % array.length)
		print("===================")
			
class A3D2Sprite:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Sprite (%i)" % array.length)
		print("===================")
	
class A3D2Skin:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("Skin (%i)" % array.length)
		print("===================")
	
class A3D2VertexBuffer:
	def __init__(self, file, mask, ind):
		array = readArray(file)
		
		self.ind = ind
		
		print("===================")
		print("VertexBuffer (%i)" % array.length)
		print("===================")
		
		self.atts = []
		self.ByteBuffer = ''
		
		for x in range(array.length):
			#attributes
			atarray = readArray(file)
			for i in range(atarray.length):
				temp = file.read(4)
				temp_data = struct.unpack('>L', temp)
				self.atts.append(temp_data[0])
			print(self.atts)
			#byteBuffer
			bufarray = readArray(file)
			print('bufarray size (%i)' % bufarray.length)
			#self.ByteBuffer = file.read(bufarray.length)
			#for j in range(bufarray.length):
				#temp = file.read(1)
				#buff.append(temp)
				#temp = file.read(struct.calcsize('f'))
				#dat = int(struct.unpack('<f',temp)[0])
				#buff.append(dat)
			
		
		
		coords = []
		norms = []
		tangents = []
		joints = []
		texcoords = []
		faces = []
		flcount = 0
		flts = int(bufarray.length/4)
		
		for a in range(len(self.atts)):
			if self.atts[a] == 0:
				#POSITION
				flcount += 3
			elif self.atts[a] == 1:
				#NORMAL
				flcount += 3	
			elif self.atts[a] == 2:
				#TANGENT4
				flcount += 4
			elif self.atts[a] == 3:
				#JOINT
				flcount += 4
			elif self.atts[a] == 4:
				#TEXCOORD
				flcount += 2		
			else:
				print('Cannot understand attribute')
		
		points = int(flts/flcount)
				
		for i in range(points):
			if 0 in self.atts:
				#POSITION
				temp_data = file.read(struct.calcsize('3f'))
				x, y, z = struct.unpack('<3f', temp_data)
				#print('pos: %f, %f, %f' % (x, y, z))
				coords.append((x, y, z))
			if 1 in self.atts:
				#NORMAL
				temp_data = file.read(struct.calcsize('3f'))
				uva, uvb, uvc = struct.unpack('<3f', temp_data)
				#print('norm: %f, %f, %f' % (uva, uvb, uvc))
				norms.append((uva, uvb, uvc))
			if 2 in self.atts:
				#TANGENT4
				temp_data = file.read(struct.calcsize('4f'))
				x, y, z, binormalDirection = struct.unpack('<4f', temp_data)
				tangents.append((x,y,z,binormalDirection))
			if 3 in self.atts:
				#JOINT
				temp_data = file.read(struct.calcsize('4f'))
				Aindex, Aweight, Bindex, Bweight = struct.unpack('<4f', temp_data)
				joints.append((Aindex,Aweight,Bindex,Bweight))
			if 4 in self.atts:
				#TEXCOORD
				temp_data = file.read(struct.calcsize('2f'))
				s, t = struct.unpack('<2f', temp_data)
				texcoords.append((s,t))
				
		#id
		temp = file.read(4)
		temp_data = struct.unpack('>L', temp) # > for big endian, < for little endian
		print("id: %i" % temp_data[0])
		#vertexCount
		temp_data = file.read(struct.calcsize('H'))
		print("vertexCount: %i" % int(struct.unpack('>H', temp_data)[0]))
		
		# create a new mesh  
		me = bpy.data.meshes.new("temp") 
		
		# create an object with that mesh
		ob = bpy.data.objects.new("temp", me)   
		
		# position object at 3d-cursor
		ob.location = bpy.context.scene.cursor_location   
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  

		# Fill the mesh with verts, edges, faces 
		me.from_pydata(coords,[],faces)   # edges or faces should be [], or you ask for problems
		me.update(calc_edges=True)    # Update mesh with new data

class A3DVersion:
	def __init__(self, file):
		temp_data = file.read(struct.calcsize('H'))
		self.baseversion = int(struct.unpack('>H', temp_data)[0]) 
		temp_data = file.read(struct.calcsize('H'))
		self.pointversion = int(struct.unpack('>H', temp_data)[0])
		
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