bl_info = {
	'name': 'Export: Alternativa3d Tools',
	'author': 'David E Jones, http://davidejones.com',
	'version': (1, 1, 7),
	'blender': (2, 6, 3),
	'location': 'File > Import/Export;',
	'description': 'Importer and exporter for Alternativa3D engine. Supports A3D and Actionscript"',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://davidejones.com',
	'category': 'Import-Export'}

import bpy, os, time, zlib, tempfile, re, shutil
from binascii import hexlify
from struct import unpack, pack, calcsize
from math import atan, atan2
from mathutils import Vector, Matrix, Quaternion
from bpy_extras.io_utils import path_reference_copy
from bpy_extras.image_utils import load_image
from bpy.props import *

#==================================
# Common Functions 
#==================================

def checkBMesh():
	a,b,c = bpy.app.version
	return (int(b) >= 63)

def rshift(val, n): return (val % 0x100000000) >> n

def toRgb(RGBint):
	Blue =  RGBint & 255
	Green = (RGBint >> 8) & 255
	Red =   (RGBint >> 16) & 255
	return [Red,Green,Blue]

def fromRgb(Red,Green,Blue):
	RGBint = int(Red)
	RGBint = (RGBint << 8) + int(Green)
	RGBint = (RGBint << 8) + int(Blue)
	return RGBint
	
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
	if checkBMesh() == True:
		mefdata = mesh.polygons
	else:
		mefdata = mesh.faces
	for f in mefdata:
		f.select = True	
	bpy.ops.mesh.quads_convert_to_tris()
	#Return to object mode
	bpy.ops.object.mode_set(mode="EDIT", toggle = False)
	bpy.ops.object.mode_set(mode="OBJECT", toggle = True)
	
#==================================
# AS EXPORTER
#==================================

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

class ASExporter(bpy.types.Operator):
	bl_idname = "ops.asexporter"
	bl_label = "Export to AS (Alternativa)"
	bl_description = "Export to AS (Alternativa)"
	
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

	Compilers = []
	Compilers.append(("1", "Flex", ""))
	Compilers.append(("2", "Flash", ""))
	CompilerOption = EnumProperty(name="Use With", description="Select the compiler you will be using", items=Compilers, default="1")

	ExportModes = []
	ExportModes.append(("1", "Selected Objects", ""))
	ExportModes.append(("2", "All Objects", ""))
	ExportMode = EnumProperty(name="Export", description="Select which objects to export", items=ExportModes, default="1")

	DocClass = BoolProperty(name="Create Document Class", description="Create document class that makes use of exported data", default=False)
	CopyImgs = BoolProperty(name="Copy Images", description="Copy images to destination folder of export", default=True)
	ByClass = BoolProperty(name="Use ByteArray Data (v8.27+)", description="Exports mesh data to compressed bytearray in as3", default=False)
	
	#ExportAnim = BoolProperty(name="Animation", description="Animation", default=False)
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
			time1 = time.clock()
			print('Output file : %s' %filePath)
			file = open(filePath, 'w')
			Config = ASExporterSettings(A3DVersionSystem=self.A3DVersionSystem,CompilerOption=self.CompilerOption,ExportMode=self.ExportMode, DocClass=self.DocClass,CopyImgs=self.CopyImgs,ByClass=self.ByClass,ExportAnim=False,ExportUV=self.ExportUV,ExportNormals=self.ExportNormals,ExportTangents=self.ExportTangents)
			ASExport(file,Config,fp)
			
			file.close()
			print(".as export time: %.2f" % (time.clock() - time1))
		except Exception as e:
			print(e)
			file.close()
		return {'FINISHED'}
	def invoke (self, context, event):		
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}
		
def ASExport(file,Config,fp):
	print('Export to Alternativa3d Class started...\n')
	
	WritePackageHeader(file,Config)
		
	if Config.ExportMode == 1:
		#get selected objects that are mesh
		objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
		print('Export selection only...\n')
	else:
		#get all objects that are mesh
		objs = [obj for obj in bpy.data.objects if obj.type == 'MESH']
		print('Export all meshes...\n')
	
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
		
		if Config.CopyImgs:
			print("copy images...\n")
			copyImages(obj,fp)

	WritePackageEnd(file)
	
	if Config.DocClass:
		WriteDocuClass(file,objs,aobjs,Config,fp)
	
	print('Export Completed...\n')
	
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
		file.write("\timport alternativa.types.Matrix3D;\n")
		file.write("\timport alternativa.types.Point3D;\n")
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
		file.write("\timport alternativa.engine3d.core.BoundBox;\n")
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
		file.write("\timport alternativa.engine3d.controllers.CameraController;\n")
		file.write("\timport alternativa.engine3d.core.Scene3D;\n")
		file.write("\timport alternativa.engine3d.core.Object3D;\n")
		file.write("\timport alternativa.engine3d.core.Camera3D;\n")
		file.write("\timport alternativa.engine3d.display.View;\n")
		file.write("\timport alternativa.utils.MathUtils;\n")
		file.write("\timport alternativa.utils.FPS;\n")
		file.write("\timport alternativa.types.Point3D;\n")
		file.write("\timport flash.display.Sprite;\n")
		file.write("\timport flash.display.StageAlign;\n")
		file.write("\timport flash.display.StageScaleMode;\n")
		file.write("\timport flash.events.Event;\n")
	elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3)  or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
		# version 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0
		file.write("\timport alternativa.engine3d.core.Camera3D;\n")
		file.write("\timport alternativa.engine3d.core.Object3DContainer;\n")
		file.write("\timport alternativa.engine3d.core.View;\n")
		file.write("\timport alternativa.engine3d.controllers.SimpleObjectController;\n")
		file.write("\timport flash.display.Sprite;\n")
		file.write("\timport flash.display.StageAlign;\n")
		file.write("\timport flash.display.StageScaleMode;\n")
		file.write("\timport flash.events.Event;\n")
		file.write("\timport flash.geom.Vector3D;\n")
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
		# version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
		file.write("\timport alternativa.engine3d.core.Camera3D;\n")
		file.write("\timport alternativa.engine3d.core.Object3D;\n")
		file.write("\timport alternativa.engine3d.core.Resource;\n")
		file.write("\timport alternativa.engine3d.core.View;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.controllers.SimpleObjectController;\n")
		file.write("\timport flash.display.Sprite;\n")
		file.write("\timport flash.display.Stage3D;\n")
		file.write("\timport flash.display.StageAlign;\n")
		file.write("\timport flash.display.StageScaleMode;\n")
		file.write("\timport flash.events.Event;\n")
		file.write("\timport flash.geom.Vector3D;\n")
	else:
		print("version not found")
		
	file.write('\n\t[SWF(backgroundColor="#000000", frameRate="100", width="800", height="600")]\n\n')
		
def WritePackageEnd(file):
	file.write("}")
	
def setupMaterials(file,obj,Config):
	mesh = obj.data
	verts = mesh.vertices
	mati = {}

	Materials = mesh.materials
	if Materials.keys():
		MaterialIndexes = {}
		if checkBMesh() == True:
			for Face in mesh.polygons:
				if Materials[Face.material_index] not in MaterialIndexes:
					MaterialIndexes[Materials[Face.material_index]] = len(MaterialIndexes)
		else:
			for Face in mesh.faces:
				if Materials[Face.material_index] not in MaterialIndexes:
					MaterialIndexes[Materials[Face.material_index]] = len(MaterialIndexes)

		Materials = [Item[::-1] for Item in MaterialIndexes.items()]
		Materials.sort()
		x=0
		for Material in Materials:
			mati[x] = cleanupString(str(Material[1].name))
			WriteMaterial(file,mati[x],Config, Material[1])
			x += 1
	return mati
			
def WriteMaterial(file,id,Config,Material=None):
	if Material:
		nme = cleanupString(str(Material.name))
		
		Texture = GetMaterialTexture(Material)
		if Texture:
			# if version 5.6.0
			if Config.A3DVersionSystem == 1:
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(nme)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':TextureMaterial = new TextureMaterial(new Texture(new bmp'+str(nme)+'().bitmapData, "'+str(nme)+'"));\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(nme)+":Bitmap = new Bitmap(new bd"+str(nme)+"(0,0));\n")
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
	path_reference_copy(copy_set)

def writeByteArrayValues(file,verts,uvlayers,indices):
	file.write("\t\t\tvalues= new <uint>[")

	tfile = tempfile.TemporaryFile(mode ='w+b')
	#length of verts -short
	tfile.write(pack("<H", len(verts)*3))
	for v in verts:
		tfile.write(pack("<f", v[0]))
		tfile.write(pack("<f", v[1]))
		tfile.write(pack("<f", v[2]))
	
	#length of uvts -short
	for uvname, uvdata in uvlayers.items():
		uvt = uvdata[0]
		tfile.write(pack("<H", len(uvt)*2))
		for uv in uvt:
			tfile.write(pack("<f", uv[0]))
			tfile.write(pack("<f", uv[1]))
	
	#length of indices -short
	tfile.write(pack("<H", len(indices)))
	for i in indices:
		tfile.write(pack("<I", i))
		
	tfile.seek(0)
	
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
				file.write("0x%X," % unpack('B', byte))
				byte = tfile.read(1)
			else:
				break
	finally:
		tfile.close()
		
	file.write("];\n")

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
	
	uvlayers={}
	
	if hasFaceUV:
	
		#update tessface cache or there is no data
		mesh.update(calc_tessface=True)
		
		#add active layer first?
		#uvlayer = mesh.tessface_uv_textures.active
		
		y=0
		for uvlayer in mesh.tessface_uv_textures:
			uv_coord_list = []
			uvlayername = uvlayer.name
			uvlayers[uvlayername] = []
			#for face in uvlayer.data:
			for uv_index in range(len(mesh.polygons)):	
				#tmplist = [face.uv,face.image]
				#uvlayers[uvlayername].append(tmplist)
				face = uvlayer.data[uv_index]
				uvs = face.uv1, face.uv2, face.uv3, face.uv4
				for vertex_index, vertex_itself in enumerate(mesh.polygons[uv_index].vertices):
					uv_coord_list.append(uvs[vertex_index])
					if flipUV == 1:
						uv = [uv_coord_list[-1][0], 1.0 - uv_coord_list[-1][1]]
					else:
						uv = [uv_coord_list[-1][0], uv_coord_list[-1][1]]
					uvt.append(uv)
					y=y+1
			#tmplist = [uvt,face.image]
			uvlayers[uvlayername].append(uvt)
			uvt = []
		
					
		uvtex = mesh.uv_layers[0]
		uv_layer = mesh.uv_layers[0]
		for uv_index in range(len(mesh.polygons)):		
			for vertex_index, vertex_itself in enumerate(mesh.polygons[uv_index].vertices):
				vertex = mesh.vertices[vertex_itself]
				vertices_list.append(vertex_itself)
				vertices_co_list.append(vertex.co.xyz)
				normals_list.append(vertex.normal.xyz)
				vertices_index_list.append(new_index)
				new_index += 1
				vs.append([vertices_co_list[-1][0],vertices_co_list[-1][1],vertices_co_list[-1][2]])
				if mesh.polygons[uv_index].use_smooth:
					nr.append([normals_list[-1][0],normals_list[-1][1],normals_list[-1][2]])
				else:
					nr.append(mesh.polygons[uv_index].normal)
				ins.append(vertices_index_list[-1])
	else:
		# if there are no image textures, output the old way
		for face in mesh.polygons:
			if len(face.vertices) > 0:
				ins.append(face.vertices[0])
				ins.append(face.vertices[1])
				ins.append(face.vertices[2])
				#nr.append([[face.normal[0],face.normal[1],face.normal[2]]])
		for v in mesh.vertices:
			vs.append([v.co[0],v.co[1],v.co[2]])
			nr.append([v.normal[0],v.normal[1],v.normal[2]])

	if (len(uvlayers) > 0) and (len(nr) > 0):
		tan = calculateTangents(ins,vs,uv_coord_list,nr)		
	
	bb = getBoundBox(obj)
	trns = getObjTransform(obj)
	return vs,uvlayers,ins,nr,tan,bb,trns

def getCommonDataNoBmesh(obj,flipUV=1):
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
					#if face.use_smooth:
					#	v = mesh.vertices[face.vertices[i]]
					#	nr.append([v.normal[0],v.normal[1],v.normal[2]])
					#else:
					#	nr.append(face.normal)
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
	
def getObjWorldTransform(obj):
	trns = []
	c=0
	j=0
	for x in obj.matrix_world:
		j=0
		for y in x:
			if j == 3 and c != 3:
				trns.append(obj.location[c])
			else:
				trns.append(y)
			j=j+1
		c=c+1	
	return trns
	
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
			tangents.append(Vector((tangentX - anx*(anx*tangentX + any*tangentY + anz*tangentZ),tangentY - any*(anx*tangentX + any*tangentY + anz*tangentZ),tangentZ - anz*(anx*tangentX + any*tangentY + anz*tangentZ))))
			
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
			tangents.append(Vector((tangentX - bnx*(bnx*tangentX + bny*tangentY + bnz*tangentZ),tangentY - bny*(bnx*tangentX + bny*tangentY + bnz*tangentZ),tangentZ - bnz*(bnx*tangentX + bny*tangentY + bnz*tangentZ))))
			
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
			tangents.append(Vector((tangentX - cnx*(cnx*tangentX + cny*tangentY + cnz*tangentZ),tangentY - cny*(cnx*tangentX + cny*tangentY + cnz*tangentZ),tangentZ - cnz*(cnx*tangentX + cny*tangentY + cnz*tangentZ))))
		
		
		#Calculate handedness
		
		x = x + 3
	
	#normalize
	for tan in tangents:
		tan.normalize()
	
	return tangents
		
def getBoundBox(obj):
	#v = [list(bb) for bb in obj.bound_box]
	#bmin = min(v)
	#bmax = max(v)
	#minx = max(bmin[0] * obj.scale.x, -1e10)
	#miny = max(bmin[1] * obj.scale.y, -1e10)
	#minz = max(bmin[2] * obj.scale.z, -1e10)
	#maxx = min(bmax[0] * obj.scale.x, 1e10)
	#maxy = min(bmax[1] * obj.scale.y, 1e10)
	#maxz = min(bmax[2] * obj.scale.z, 1e10)
	#return [minx,miny,minz,maxx,maxy,maxz]
	d = obj.bound_box
	#return Vec((d[0])), Vec((d[6]))
	return [d[0][0],d[0][1],d[0][2],d[6][0],d[6][1],d[6][2]]

def writeTransform(file,obj,Config):
	mesh = obj.data
	
	loc, rot, sca = obj.matrix_local.decompose()
	rot1 = rot.to_euler()
	mtrx = obj.matrix_local
	
	file.write("\n")
	file.write("\t\t\tthis.x = %f;\n" % loc.x)
	file.write("\t\t\tthis.y = %f;\n" % loc.y)
	file.write("\t\t\tthis.z = %f;\n" % loc.z)
	file.write("\t\t\tthis.rotationX = %f;\n" % rot1.x)
	file.write("\t\t\tthis.rotationY = %f;\n" % rot1.y)
	file.write("\t\t\tthis.rotationZ = %f;\n" % rot1.z)
	file.write("\t\t\tthis.scaleX = %f;\n" % sca.x)
	file.write("\t\t\tthis.scaleY = %f;\n" % sca.y)
	file.write("\t\t\tthis.scaleZ = %f;\n" % sca.z)
	
def writeBoundBox(file,bb,Config):
	file.write("\n")
	if Config.A3DVersionSystem == 1:
		# version 5.6.0
		print("no boundbox for v5")
	elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3) or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
		# version 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0
		file.write("\t\t\tthis.boundMaxX = %f;\n" % bb[0])
		file.write("\t\t\tthis.boundMaxY = %f;\n" % bb[1])
		file.write("\t\t\tthis.boundMaxZ = %f;\n" % bb[2])
		file.write("\t\t\tthis.boundMinX = %f;\n" % bb[3])
		file.write("\t\t\tthis.boundMinY = %f;\n" % bb[4])
		file.write("\t\t\tthis.boundMinZ = %f;\n" % bb[5])
	elif (Config.A3DVersionSystem == 7) or (Config.A3DVersionSystem == 8) or (Config.A3DVersionSystem == 9) or (Config.A3DVersionSystem == 10) or (Config.A3DVersionSystem == 11):
		# version 8.5.0, 8.8.0, 8.12.0, 8.17.0, 8.27.0
		file.write("\t\t\tvar bb:BoundBox = new BoundBox();\n")
		file.write("\t\t\tbb.maxX = %f;\n" % bb[0])
		file.write("\t\t\tbb.maxY = %f;\n" % bb[1])
		file.write("\t\t\tbb.maxZ = %f;\n" % bb[2])
		file.write("\t\t\tbb.minX = %f;\n" % bb[3])
		file.write("\t\t\tbb.minY = %f;\n" % bb[4])
		file.write("\t\t\tbb.minZ = %f;\n" % bb[5])
		file.write("\t\t\tthis.boundBox = bb;\n")
	else:
		print("version not found")
	
def WriteClass8270(file,obj,Config):
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	hasFaceUV = len(mesh.uv_textures) > 0
	
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	mati = setupMaterials(file,obj,Config)
	
	if checkBMesh() == True:
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonData(obj)
	else:
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonDataNoBmesh(obj)
		
	#if bytearray
	if Config.ByClass == 1:
		file.write("\t\tprivate var values:Vector.<uint>;\n")
		file.write("\t\tprivate var bytedata:ByteArray = new ByteArray();\n")
	
	file.write("\t\tprivate var attributes:Array;\n\n")
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tattributes = [\n")

	if len(vs) > 0:
		file.write("\t\t\t\tVertexAttributes.POSITION,\n")
		file.write("\t\t\t\tVertexAttributes.POSITION,\n")
		file.write("\t\t\t\tVertexAttributes.POSITION,\n")
	if (len(uvlayers) > 0) and (Config.ExportUV == 1):
		j=0
		for uvname, uvdata in uvlayers.items():
			file.write("\t\t\t\tVertexAttributes.TEXCOORDS["+str(j)+"],\n")
			file.write("\t\t\t\tVertexAttributes.TEXCOORDS["+str(j)+"],\n")
			j=j+1
	if Config.ByClass == 0:
		file.write("\t\t\t\tVertexAttributes.NORMAL,\n")
		file.write("\t\t\t\tVertexAttributes.NORMAL,\n")
		file.write("\t\t\t\tVertexAttributes.NORMAL,\n")
		file.write("\t\t\t\tVertexAttributes.TANGENT4,\n")
		file.write("\t\t\t\tVertexAttributes.TANGENT4,\n")
		file.write("\t\t\t\tVertexAttributes.TANGENT4,\n")
		file.write("\t\t\t\tVertexAttributes.TANGENT4,\n")
	file.write("\t\t\t];\n")
	
	file.write("\t\t\tvar g:Geometry = new Geometry();\n")
	file.write("\t\t\tg.addVertexStream(attributes);\n")
		
			
	file.write("\t\t\tg.numVertices = "+str(len(vs))+";\n\n")
	
	if Config.ByClass == 0:
		if len(vs) > 0:
			file.write("\t\t\tvar vertices:Array = [\n")
			for v in vs:
				file.write("\t\t\t\t%.6g, %.6g, %.6g,\n" % (v[0],v[1],v[2]))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar vertices:Array = new Array();\n")
		
		if (len(uvlayers) > 0) and (Config.ExportUV == 1):
			j=0
			for uvname, uvdata in uvlayers.items():
				if j <= 7:
					file.write("\t\t\tvar uvlayer"+str(j)+":Array = [\n")
					for u in uvdata[0]:
						file.write("\t\t\t\t%.4g,%.4g,\n" % (u[0],u[1]))
					file.write("\t\t\t];\n")
					j=j+1
		else:
			file.write("\t\t\tvar uvlayer:Array = new Array();\n")
		
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
		
		if (len(nr) > 0) and (Config.ExportNormals == 1):
			file.write("\t\t\tvar normals:Array = [\n")
			for n in nr:
				file.write("\t\t\t\t%.6g, %.6g, %.6g,\n" % (n[0],n[1],n[2]))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar normals:Array = new Array();\n")
			
		if (len(tan) > 0) and (Config.ExportTangents == 1):
			file.write("\t\t\tvar tangent:Array = [\n")
			for t in tan:
				file.write("\t\t\t\t%.6g, %.6g, %.6g, %.6g,\n" % (t[0],t[1],t[2],-1))
			file.write("\t\t\t];\n")
		else:
			file.write("\t\t\tvar tangent:Array = new Array();\n\n")
		
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
		if (len(uvlayers) > 0) and (Config.ExportUV == 1):
			j=0
			for uvname, uvdata in uvlayers.items():
				if j <= 7:
					#file.write("\t\t\t//%s\n" % uvname)
					file.write("\t\t\tg.setAttributeValues(VertexAttributes.TEXCOORDS["+str(j)+"], Vector.<Number>(uvlayer"+str(j)+"));\n")
					j=j+1
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvlayer));\n")	
			
		if (len(nr) > 0) and (Config.ExportNormals == 1):
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
			
		if (len(tan) > 0) and (Config.ExportTangents == 1):
			file.write("\t\t\tg.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
		else:
			file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
		
		file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
		if Config.A3DVersionSystem == 11:
			file.write("\t\t\t//g.calculateNormals();\n")
			file.write("\t\t\t//g.calculateTangents(0);\n")
		file.write("\t\t\tthis.geometry = g;\n")
	else:
		writeByteArrayValues(file,vs,uvlayers,ins)
		file.write("\t\t\tfor each(var b:uint in values)\n")
		file.write("\t\t\t{\n")
		file.write("\t\t\t\tbytedata.writeByte(b);\n")
		file.write("\t\t\t}\n")
		file.write("\t\t\tvar vertices:Array = new Array();\n")
		j=0
		for uvname, uvdata in uvlayers.items():
			if j <= 7:
				file.write("\t\t\tvar uvlayer"+str(j)+":Array = new Array();\n")
				j=j+1
		file.write("\t\t\tvar ind:Array = new Array();\n")
		file.write("\t\t\tbytedata.endian = Endian.LITTLE_ENDIAN;\n")
		file.write("\t\t\tbytedata.uncompress();\n")
		file.write("\t\t\tbytedata.position=0;\n")
		file.write("\t\t\tvar vlen:uint = bytedata.readUnsignedShort();\n")
		file.write("\t\t\tg.numVertices = vlen/3;\n")
		file.write("\t\t\tfor(var i:int = 0; i < vlen; i++){vertices.push(bytedata.readFloat());}\n")
		j=0
		for uvname, uvdata in uvlayers.items():
			if j <= 7:
				file.write("\t\t\tvar uvlen:uint = bytedata.readUnsignedShort();\n")
				file.write("\t\t\tfor(var x:int = 0; x < uvlen; x++){uvlayer"+str(j)+".push(bytedata.readFloat());}\n")
				j=j+1
		file.write("\t\t\tvar ilen:uint = bytedata.readUnsignedShort();\n")
		file.write("\t\t\tfor(var j:int = 0; j < ilen; j++){ind.push(bytedata.readUnsignedInt());}\n")
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
		j=0
		for uvname, uvdata in uvlayers.items():
			if j <= 7:
				file.write("\t\t\tif(uvlen > 0){g.setAttributeValues(VertexAttributes.TEXCOORDS["+str(j)+"], Vector.<Number>(uvlayer"+str(j)+"));}\n")
				j=j+1
		file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
		file.write("\t\t\tg.calculateNormals();\n")
		file.write("\t\t\tg.calculateTangents(0);\n")
		file.write("\t\t\tthis.geometry = g;\n")

	start,end,mts,mats,uvimgs = collectSurfaces(mesh)
	
	if len(mts) > 0:
		for x in range(len(mts)):
			file.write("\t\t\tthis.addSurface("+mts[x]+", "+str(start[x])+", "+str(end[x])+");\n")
	else:
		file.write("\t\t\t//this.addSurface(new FillMaterial(0xFF0000), 0, "+str(len(ins))+");\n")
	
	file.write("\t\t\tthis.calculateBoundBox();\n")
	writeTransform(file,obj,Config)
	writeBoundBox(file,bb,Config)
	file.write("\t\t}\n")
	file.write("\t}\n")

def collectSurfaces(mesh):
	Materials = mesh.materials
	c=0
	triangles = -1
	lastmat = None
	lastimg = None
	start,end,items,mts,mats,uvimgs = [],[],[],[],[],[]
	if checkBMesh() == True:
		mefdata = mesh.polygons
	else:
		mefdata = mesh.faces
	
	if len(Materials) > 0:
		for face in mefdata:
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
	else:
		#no materials/tex slots
		#get active uv layer, per face image
		mesh.update(calc_tessface=True)
		if len(mesh.tessface_uv_textures) > 0:
			#for uvlayer in mesh.tessface_uv_textures:
			#uvlayer = mesh.tessface_uv_textures[0]
			uvlayer = mesh.tessface_uv_textures.active
			fc = 0
			for face in uvlayer.data:
				triangles = triangles + 1
				if face.image not in items:
					start.append(fc * 3)
					if c != 0:
						end.append(triangles)
						triangles = 0
					uvimgs.append(face.image)
				else:
					if face.image != lastimg:
						start.append(fc * 3)
						if c != 0:
							end.append(triangles)
							triangles = 0
						uvimgs.append(face.image)
				lastimg = face.image
				items.append(face.image)	
				c = c+1
				fc=fc+1
			end.append(triangles+1)
		
		#mesh.update(calc_tessface=True)
		#if len(mesh.tessface_uv_textures) > 0:
		#	uvlayer = mesh.tessface_uv_textures[0]
		#	fc = 0
		#	for face in uvlayer.data:
		#		triangles = triangles + 1
		#		start.append(fc * 3)
		#		end.append(triangles)
		#		triangles = 0
		#		uvimgs.append(face.image)
		#		fc=fc+1

	#print(start)
	#print(end)
	#print(mts)
	#print(mats)
	#print(uvimgs)
	
	return start,end,mts,mats,uvimgs
	
def WriteClass78(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	
	mati = setupMaterials(file,obj,Config)
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	
	if checkBMesh() == True:
		mefdata = mesh.polygons
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonData(obj)
		uvlayer = mesh.tessface_uv_textures.active
	else:
		mefdata = mesh.faces
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonDataNoBmesh(obj)
		uvlayer = mesh.uv_textures.active
		
	cn=-1
	for face in mefdata:
		cn +=1
		file.write('\t\t\t\taddFace(Vector.<Vertex>([\n')
		if len(face.vertices) > 0:
			for i in range(len(face.vertices)):
				hasFaceUV = len(mesh.uv_textures) > 0
				if (hasFaceUV) and (Config.ExportUV == 1):
					#uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
					uv = [uvlayer.data[face.index].uv[i][0], uvlayer.data[face.index].uv[i][1]]
					uv[1] = 1.0 - uv[1]
					file.write('\t\t\t\t\taddVertex(%f, %f, %f, %f, %f),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z, uv[0], uv[1]) )
				else:
					file.write('\t\t\t\t\taddVertex(%f, %f, %f, 0, 0),\n' % (verts[face.vertices[i]].co.x, verts[face.vertices[i]].co.y, verts[face.vertices[i]].co.z) )
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

	if Config.A3DVersionSystem == 4:
		#7.6.0
		file.write("\t\tcalculateNormals();\n")
		file.write("\t\tcalculateBounds();\n")
	else:
		#7.7.0 - 7.8.0
		file.write("\t\t\tcalculateFacesNormals();\n")
		file.write("\t\t\tcalculateVerticesNormals();\n")
		file.write("\t\t\tcalculateBounds();\n")
		
	writeTransform(file,obj,Config)
	writeBoundBox(file,bb,Config)
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass75(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
	
	mesh = obj.data
	verts = mesh.vertices
	Materials = mesh.materials
	
	mati = setupMaterials(file,obj,Config)
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")
	file.write("\t\t\tvar g:Geometry = new Geometry();\n\n")
	
	if checkBMesh() == True:
		mefdata = mesh.polygons
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonData(obj)
		uvlayer = mesh.tessface_uv_textures.active
	else:
		mefdata = mesh.faces
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonDataNoBmesh(obj)
		uvlayer = mesh.uv_textures.active
		
	for face in mefdata:
		file.write('\t\t\t\tg.addFace(Vector.<Vertex>([\n')
		for i in range(len(face.vertices)):
			hasFaceUV = len(mesh.uv_textures) > 0
			if (hasFaceUV) and (Config.ExportUV == 1):
				#uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
				uv = [uvlayer.data[face.index].uv[i][0], uvlayer.data[face.index].uv[i][1]]
				uv[1] = 1.0 - uv[1]
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
	writeTransform(file,obj,Config)
	writeBoundBox(file,bb,Config)
	file.write("\t\t}\n")
	file.write("\t}\n")
	
def WriteClass5(file,obj,Config):
	file.write("\tpublic class "+obj.data.name+" extends Mesh {\n\n")
		
	mesh = obj.data;
	verts = mesh.vertices
	Materials = mesh.materials
	hasFaceUV = len(mesh.uv_textures) > 0

	mati = setupMaterials(file,obj,Config)
	file.write("\t\tpublic function "+obj.data.name+"() {\n\n")

	if checkBMesh() == True:
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonData(obj,False)
	else:
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonDataNoBmesh(obj,False)

	if len(vs) > 0:
		count = 0
		for v in vs:
			file.write("\t\t\tcreateVertex(%.6g, %.6g, %.6g, %i);\n" % (v[0],v[1],v[2],count))
			count += 1
		file.write('\n')
		
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
	
	if (len(uvlayers) > 0) and (Config.ExportUV == 1):
		count = 0
		file.write('\t\t\tsetUVsToFace(')
		x=0
		j=0
		uvlayercount = 0
		for uvname, uvdata in uvlayers.items():
			if uvlayercount <= 0:
				uvt = uvdata[0]
				for u in uvt:
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
				uvlayercount=uvlayercount+1
		file.write('\n')
		
	x=0
	lastmat = None
	items,mts,fcs,temp = [],[],[],[]
	if checkBMesh() == True:
		mefdata = mesh.polygons
	else:
		mefdata = mesh.faces
	for face in mefdata:
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
		
	writeTransform(file,obj,Config)
	file.write("\t\t}\n")
	file.write("\t}\n")

def WriteDocuClass(ofile,objs,aobjs,Config,fp):
	fp = os.path.dirname(fp) + os.sep + "main.as"
	
	if os.path.exists(fp) == True:
		print("Docuclass "+fp+" Already exists")
	else:
		if not fp.lower().endswith('.as'):
			fp += '.as'
		try:
			file = open(fp, 'w')
		except Exception as e:
			print(e)

		WriteDocPackageHeader(file,Config)
		file.write("\tpublic class main extends Sprite {\n\n")
		
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
			file.write("\t\tprivate var controller:CameraController;\n\n")
			file.write("\t\tpublic function main() {\n\n")
			file.write("\t\t\tstage.align = StageAlign.TOP_LEFT;\n")
			file.write("\t\t\tstage.scaleMode = StageScaleMode.NO_SCALE;\n\n")
			file.write('\t\t\tcamera = new Camera3D("camera");\n')
			file.write("\t\t\tcamera.fov = MathUtils.DEG1*100;\n")
			file.write("\t\t\tcamera.x = 10;\n")
			file.write("\t\t\trootContainer.addChild(camera);\n\n")
			file.write('\t\t\tcontroller = new CameraController(stage);\n')
			file.write('\t\t\tcontroller.camera = camera;\n')
			file.write('\t\t\tcontroller.lookAt(new Point3D(0,0,0));\n\n')
			
			for i, obj in enumerate(objs):
				file.write("\t\t\tobj"+str(i)+" = new "+cleanupString(obj.data.name)+"();\n")
				file.write("\t\t\trootContainer.addChild(obj"+str(i)+");\n")
			file.write("\n")
			
			file.write("\t\t\tview = new View(camera);\n")
			file.write("\t\t\taddChild(view);\n")
			file.write("\t\t\tview.interactive = true;\n")
			file.write("\t\t\tFPS.init(this);\n\n")
			file.write("\t\t\taddEventListener(Event.ENTER_FRAME, onEnterFrame);\n")
			file.write("\t\t\tstage.addEventListener(Event.RESIZE, onResize);\n")
			file.write("\t\t\tonResize();\n")
			file.write("\t\t}\n\n")
			file.write("\t\tprivate function onEnterFrame(e:Event=null):void {\n")
			file.write("\t\t\tscene.calculate();\n")
			file.write("\t\t\tcontroller.processInput();\n")
			file.write("\t\t}\n\n")
			file.write("\t\tprivate function onResize(e:Event=null):void {\n")
			file.write("\t\t\tview.width = stage.stageWidth;\n")
			file.write("\t\t\tview.height = stage.stageHeight;\n")
			file.write("\t\t\tonEnterFrame();\n")
			file.write("\t\t}\n\n")
		elif (Config.A3DVersionSystem == 2) or (Config.A3DVersionSystem == 3) or (Config.A3DVersionSystem == 4) or (Config.A3DVersionSystem == 5) or (Config.A3DVersionSystem == 6):
			# version 7.5.0, 7.5.1, 7.6.0, 7.7.0, 7.8.0
			file.write("\t\tprivate var rootContainer:Object3DContainer = new Object3DContainer();\n")
			file.write("\t\tprivate var camera:Camera3D;\n")
			file.write("\t\tprivate var controller:SimpleObjectController;\n\n")
			file.write("\t\tpublic function main() {\n\n")
			file.write("\t\t\tstage.align = StageAlign.TOP_LEFT;\n")
			file.write("\t\t\tstage.scaleMode = StageScaleMode.NO_SCALE;\n\n")
			file.write("\t\t\tcamera = new Camera3D();\n")
			file.write("\t\t\tcamera.view = new View(stage.stageWidth, stage.stageHeight);\n")
			file.write("\t\t\taddChild(camera.view);\n")
			file.write("\t\t\taddChild(camera.diagram);\n")
			file.write("\t\t\tcamera.x = 10;\n")
			file.write("\t\t\trootContainer.addChild(camera);\n\n")
			file.write("\t\t\tcontroller = new SimpleObjectController(stage,camera,100);\n")
			file.write("\t\t\tcontroller.lookAt(new Vector3D(0,0,0));\n\n")
			
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
			file.write("\t\tprivate var stage3D:Stage3D;\n")
			file.write("\t\tprivate var controller:SimpleObjectController;\n\n")
			file.write("\t\tpublic function main() {\n\n")
			file.write("\t\t\tstage.align = StageAlign.TOP_LEFT;\n")
			file.write("\t\t\tstage.scaleMode = StageScaleMode.NO_SCALE;\n\n")
			file.write("\t\t\tcamera = new Camera3D(0.1, 10000);\n")
			file.write("\t\t\tcamera.view = new View(stage.stageWidth, stage.stageHeight);\n")
			file.write("\t\t\taddChild(camera.view);\n")
			file.write("\t\t\taddChild(camera.diagram);\n")
			file.write("\t\t\tcamera.x = 10;\n")
			file.write("\t\t\trootContainer.addChild(camera);\n\n")
			file.write("\t\t\tcontroller = new SimpleObjectController(stage,camera,100);\n")
			file.write("\t\t\tcontroller.lookAt(new Vector3D(0,0,0));\n\n")
			
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

class A3DExporterSettings:
	def __init__(self,A3DVersionSystem=4,ExportMode=1,CompressData=1,ExportAnim=0,ExportUV=1,ExportNormals=1,ExportTangents=1,ExportParentObj=0,ExportBoundBoxes=1):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.ExportMode = int(ExportMode)
		self.CompressData = int(CompressData)
		self.ExportAnim = int(ExportAnim)
		self.ExportUV = int(ExportUV)
		self.ExportNormals = int(ExportNormals)
		self.ExportTangents = int(ExportTangents)
		self.ExportParentObj = int(ExportParentObj)
		self.ExportBoundBoxes = int(ExportBoundBoxes)

class A3DExporter(bpy.types.Operator):
	bl_idname = "ops.a3dexporter"
	bl_label = "Export to A3D (Alternativa)"
	bl_description = "Export to A3D (Alternativa)"
	
	A3DVersions = []
	A3DVersions.append(("1", "2.6", ""))
	A3DVersions.append(("2", "2.5", ""))
	A3DVersions.append(("3", "2.4", ""))
	A3DVersions.append(("4", "2.0", ""))
	#A3DVersions.append(("5", "1.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D .A3D to export to", items=A3DVersions, default="1")
	
	ExportModes = []
	ExportModes.append(("1", "Selected Objects", ""))
	ExportModes.append(("2", "All Objects", ""))
	ExportMode = EnumProperty(name="Export", description="Select which objects to export", items=ExportModes, default="1")
	
	CompressData = BoolProperty(name="Compress Data", description="Zlib Compress data as per .a3d spec", default=True)
	
	#ExportAnim = BoolProperty(name="Animation", description="Animation", default=False)
	ExportUV = BoolProperty(name="Include UVs", description="Normals", default=True)
	ExportNormals = BoolProperty(name="Include Normals", description="Normals", default=True)
	ExportTangents = BoolProperty(name="Include Tangents", description="Tangents", default=True)
	ExportParentObj = BoolProperty(name="Include Pivot Objects", description="Export meshes with parent objects which contain pivot transformation data", default=False)
	ExportBoundBoxes = BoolProperty(name="Include Bound Boxes", description="Export with boundbox data", default=True)
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		if not filePath.lower().endswith('.a3d'):
			filePath += '.a3d'
		try:
			time1 = time.clock()
			print('Output file : %s' %filePath)
			file = open(filePath, 'wb')
			file.close()
			file = open(filePath, 'ab')
			Config = A3DExporterSettings(A3DVersionSystem=self.A3DVersionSystem,ExportMode=self.ExportMode,CompressData=self.CompressData,ExportAnim=False,ExportUV=self.ExportUV,ExportNormals=self.ExportNormals,ExportTangents=self.ExportTangents,ExportParentObj=self.ExportParentObj,ExportBoundBoxes=self.ExportBoundBoxes)
			
			if self.A3DVersionSystem == "5":
				A3DExport1(file,Config)
			else:
				A3DExport2(file,Config)
			
			file.close()
			print(".a3d export time: %.2f" % (time.clock() - time1))
		except Exception as e:
			print(e)
			file.close()
		return {'FINISHED'}
	def invoke (self, context, event):		
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}

def A3DExport1(file,Config):
	if Config.ExportMode == 1:
		#get selected objects that are mesh
		objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
		print('Export selection only...\n')
	else:
		#get all objects that are mesh
		objs = [obj for obj in bpy.data.objects if obj.type == 'MESH']
		print('Export all meshes...\n')
		
	boxes = []
	geometries = []
	indexBuffers = []
	vertexBuffers = []
	images = []
	maps = []
	materials = []
	objects = []
	
	if len(objs) > 0:
		print("Exporting meshes...\n")
		for obj in objs:
			#convert to triangles
			ConvertQuadsToTris(obj)
		
			#data
			mesh = obj.data
			
			#get raw geometry data
			if checkBMesh() == True:
				vs,uvlayers,ins,nr,tan,bb,trns = getCommonData(obj)
			else:
				vs,uvlayers,ins,nr,tan,bb,trns = getCommonDataNoBmesh(obj)
			#get surface data
			start,end,mts,mats,uvimgs = collectSurfaces(mesh)
					
			#create mesh boundbox
			a3dbox = A3DBox(Config)
			a3dbox._box = bb
			a3dbox._id = len(boxes)
			boxes.append(a3dbox)
			
			#create indexbuffer
			a3dibuf = A3DIndexBuffer(Config)
			for x in range(len(ins)):
				a3dibuf._byteBuffer.append(ins[x])
			a3dibuf._indexCount = len(a3dibuf._byteBuffer)
			indexBuffers.append(a3dibuf)
			
			#create vertexbuffer
			vbuffers = []
			a3dvbuf = A3DVertexBuffer(Config)
			attar = []
			if len(vs) > 0:
				attar.append(0)
			if (len(uvt) > 0) and (Config.ExportUV == 1):
				attar.append(5)
			if (len(nr) > 0) and (Config.ExportNormals == 1):
				attar.append(1)
			if (len(tan) > 0) and (Config.ExportTangents == 1):
				attar.append(2)
			a3dvbuf._attributes = attar
			j=0
			for v in vs:
				if 0 in attar:
					a3dvbuf._byteBuffer.append(v[0]) #vert1
					a3dvbuf._byteBuffer.append(v[1]) #vert2
					a3dvbuf._byteBuffer.append(v[2]) #vert3
				if 5 in attar and (Config.ExportUV == 1):
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
			a3dvbuf._vertexCount = int(len(vs)) #this works for cube
			vbuffers.append(a3dvbuf)
			
			#create geometry
			a3dgeom = A3DGeometry(Config)
			a3dgeom._id = len(geometries)
			a3dgeom._indexBuffer = a3dibuf
			a3dgeom._vertexBuffers = vbuffers
			geometries.append(a3dgeom)
			
			#images
			a3dimg = A3DImage(Config)
			a3dimg._id = 0
			a3dimg._url = 0
			#images.append(a3dimg)
			
			#maps
			a3dmap = A3DMap(Config)
			a3dmap._channel = 0
			a3dmap._id = 0
			a3dmap._imageId = 0
			a3dmap._uOffset = 0
			a3dmap._uScale = 0
			a3dmap._vOffset = 0
			a3dmap._vScale = 0
			#maps.append(a3dmap)
			
			#materials
			a3dmat = A3DMaterial(Config)
			a3dmat._diffuseMapId = None
			a3dmat._glossinessMapId = None
			a3dmat._id = 0
			a3dmat._lightMapId = None
			a3dmat._normalMapId = None
			a3dmat._opacityMapId = None
			a3dmat._specularMapId = None
			#materials.append(a3dmat)
			
			#objects
			a3dstr = A3DString()
			a3dstr.name = "test"
			
			a3dtrans = A3DTransform(Config)
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
			
			a3dobj = A3DObject(Config)
			a3dobj._boundBoxId = a3dbox._id
			a3dobj._geometryId = a3dgeom._id
			a3dobj._id = len(objects)
			a3dobj._name = a3dstr
			a3dobj._parentId = 0
			a3dobj._surfaces = []
			a3dobj._transformation = a3dtrans
			a3dobj._visible = 1
			objects.append(a3dobj)
	
	a3d = A3D(boxes,geometries,images,maps,materials,objects,Config)
	a3d.write(file)
	
	print('Export Completed...\n')

def A3DExport2(file,Config):
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
	objs_empties = []
	objs_a3ditems = []
	
	for obj in objs:
		if "a3dtype" in obj:
			objs_a3ditems.append(obj)
		else:
			if obj.type == 'MESH':
				objs_mesh.append(obj)
			if obj.type == 'ARMATURE':
				objs_arm.append(obj)
			if obj.type == 'LAMP':
				objs_lights.append(obj)
			if obj.type == 'CAMERA':
				objs_cameras.append(obj)
			if obj.type == 'EMPTY':
				objs_empties.append(obj)
	
	
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
	#for ids
	mesh_objects = []
	
	linkedimgdata = {}
	linkedimg = False
	linkeddata = {}
	linkedmesh = False
	
	#a3d custom objs
	if len(objs_a3ditems) > 0:
		for obj in objs_a3ditems:
			if obj["a3dtype"] == 'A3DSprite3D':
				print('A3DSprite3D Found')
				mesh = obj.data
				start,end,mts,mats,uvimgs = collectSurfaces(mesh)
				
				#create material
				if Config.ExportBoundBoxes == 1:
					a3dbox = A3D2Box(Config)
					a3dbox._box = getBoundBox(obj)
					a3dbox._id = len(boxes)
					boxes.append(a3dbox)
			
				#name
				a3dstr = A3DString()
				a3dstr.name = cleanupString(mesh.name)
				
				#create transform/matrix
				a3dtrans = A3DTransform(Config)
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
								
				for x in range(len(mts)):
					difmap = int("ffffffff",16)
					glossmap = int("ffffffff",16)
					lighmap = int("ffffffff",16)
					normmap = int("ffffffff",16)
					opacmap = int("ffffffff",16)
					specmap = int("ffffffff",16)
					reflmap = int("ffffffff",16)
					
					for tex in mats[x].texture_slots:
						if (tex is not None) and (tex.texture.type == "IMAGE"):
							if tex.texture.image is not None:
								name=tex.name.lower()
								a3dstr = A3DString()
								#a3dstr.name = os.path.basename(tex.texture.image.filepath)
								a3dstr.name = os.path.basename(bpy.path.abspath(tex.texture.image.filepath))
								a3dimg = A3D2Image(Config)
								a3dimg._id = len(images)
								a3dimg._url = a3dstr
								images.append(a3dimg)
								
								a3dmap = A3D2Map(Config)
								a3dmap._channel = 0
								a3dmap._id = len(maps)
								a3dmap._imageId = a3dimg._id
								maps.append(a3dmap)
								
								if name == 'diffuse':
									difmap = a3dmap._id
								elif name == 'normal':
									normmap = a3dmap._id
								elif name == 'specular':
									specmap = a3dmap._id
								elif name == 'opacity':
									opacmap = a3dmap._id
								elif name == 'glossiness':
									glossmap = a3dmap._id
								elif name == 'light':
									lighmap = a3dmap._id
								elif name == 'reflection':
									reflmap = a3dmap._id
								else:
									#just write as diffuse if no matches
									difmap = a3dmap._id
							else:
								print("A3DSprite is missing an image..")
						else:
							print("A3DSprite is missing an image..")
											
				a3dmat = A3D2Material(Config)
				a3dmat._diffuseMapId = difmap
				a3dmat._glossinessMapId = glossmap
				a3dmat._id = len(materials)
				a3dmat._lightMapId = lighmap
				a3dmat._normalMapId = normmap
				a3dmat._opacityMapId = opacmap
				a3dmat._reflectionCubeMapId = reflmap
				a3dmat._specularMapId = specmap
				materials.append(a3dmat)
				
				a3dsprite = A3D2Sprite(Config)
				a3dsprite._alwaysOnTop = 0
				if Config.ExportBoundBoxes == 1:
					a3dsprite._boundBoxId = a3dbox._id
				a3dsprite._height = 500
				a3dsprite._id = len(sprites)
				a3dsprite._materialId = a3dmat._id
				a3dsprite._name = a3dstr
				a3dsprite._originX = 0.5
				a3dsprite._originY = 0.5
				#a3dsprite._parentId = None
				a3dsprite._perspectiveScale = 1
				a3dsprite._rotation = 0
				a3dsprite._transform = a3dtrans
				a3dsprite._visible = 1
				a3dsprite._width = 500
				sprites.append(a3dsprite)
				
			elif obj["a3dtype"] == 'A3DLOD':
				print('A3DLOD Found')
				if Config.A3DVersionSystem <= 2:
					
					distances = []
					lodobjects = []
					for childobj in obj.children:
						print(childobj.name)
						if "a3ddistance" in childobj:
							me = childobj.data
							
							#ConvertQuadsToTris(childobj)
							
							a3dmesh = createMesh(Config,childobj,linkedimgdata,linkedimg,linkeddata,linkedmesh,meshes,objects,mesh_objects,boxes,indexBuffers,images,maps,materials,vertexBuffers)
							
							lodobjects.append(a3dmesh._id)
							distances.append(int(childobj["a3ddistance"]))
						
					if Config.ExportBoundBoxes == 1:
						a3dbox = A3D2Box(Config)
						a3dbox._box = getBoundBox(obj)
						a3dbox._id = len(boxes)
						boxes.append(a3dbox)
					
					a3dtrans = A3DTransform(Config)
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
					
					a3dstr = A3DString()
					a3dstr.name = cleanupString(obj.name)
				
					a3dlod = A3D2LOD(Config)
					if Config.ExportBoundBoxes == 1:
						a3dlod._boundBoxId = a3dbox._id
					a3dlod._distances = distances
					#a3dlod._id = len(lods)
					a3dlod._id = len(mesh_objects)
					a3dlod._name = a3dstr
					a3dlod._objects = lodobjects
					#a3dlod._parentId = None
					#a3dlod._transform = a3dtrans
					a3dlod._visible = 1
					lods.append(a3dlod)
					mesh_objects.append(a3dlod)
			
			elif obj["a3dtype"] == 'A3DSkybox':
				print("skybox")
				a3dmesh = createMesh(Config,obj,linkedimgdata,linkedimg,linkeddata,linkedmesh,meshes,objects,mesh_objects,boxes,indexBuffers,images,maps,materials,vertexBuffers)
				
	if len(objs_lights) > 0:
		print("Exporting lights...\n")
		#loop over every light
		for obj in objs_lights:
			light = obj.data
			
			#name
			a3dstr = A3DString()
			a3dstr.name = cleanupString(light.name)
			
			#create transform/matrix
			a3dtrans = A3DTransform(Config)
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

				a3damb = A3D2AmbientLight(Config)
				if Config.ExportBoundBoxes == 1:
					boxes.append(a3dbox)
					a3damb._boundBoxId = a3dbox._id
				a3damb._color = fromRgb(light.color.r,light.color.g,light.color.b)
				a3damb._id = int(len(ambientLights))
				a3damb._intensity = int(light.energy)
				a3damb._name = a3dstr
				#a3damb._parentId = None
				a3damb._transform = a3dtrans
				a3damb._visible = 1
				
				ambientLights.append(a3damb)
			elif light.type == 'POINT':
				#omniLights
				print("omniLight")
				
				a3domn = A3D2OmniLight(Config)
				a3domn._attenuationBegin = 0
				a3domn._attenuationEnd = 0
				if Config.ExportBoundBoxes == 1:
					boxes.append(a3dbox)
					a3domn._boundBoxId = a3dbox._id
				a3domn._color = fromRgb(light.color.r,light.color.g,light.color.b)
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
				
				a3dspot = A3D2SpotLight(Config)
				a3dspot._attenuationBegin = 0
				a3dspot._attenuationEnd = 0
				if Config.ExportBoundBoxes == 1:
					boxes.append(a3dbox)
					a3dspot._boundBoxId = a3dbox._id
				a3dspot._color = fromRgb(light.color.r,light.color.g,light.color.b)
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

				a3ddir = A3D2DirectionalLight(Config)
				if Config.ExportBoundBoxes == 1:
					boxes.append(a3dbox)
					a3ddir._boundBoxId = a3dbox._id
				a3ddir._color = fromRgb(light.color.r,light.color.g,light.color.b)
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
			
				a3dstr = A3DString()
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
					BoneMatrix = Matrix()
				BoneMatrix *= PoseBone.matrix
				
				#a3djnt._transform = [BoneMatrix[0][0],BoneMatrix[0][1],BoneMatrix[0][2],BoneMatrix[1][0],BoneMatrix[1][1],BoneMatrix[1][2],BoneMatrix[2][0],BoneMatrix[2][1],BoneMatrix[2][2],BoneMatrix[3][0],BoneMatrix[3][1],BoneMatrix[3][2]]
				joints.append(a3djnt)
				
				#now do same as above for bone children
				#Bone.children
			
			#print(arm.name)
			#for b in bones:
				
			#	a3dstr = A3DString()
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
			
			#create the mesh if parent isn't lod
			hasparentlod = False
			if obj.parent != None:
				parentobj = obj.parent
				if "a3dtype" in parentobj:
					if parentobj["a3dtype"] == 'A3DLOD':
						hasparentlod = True
						
			if hasparentlod == 0:
				a3dmesh = createMesh(Config,obj,linkedimgdata,linkedimg,linkeddata,linkedmesh,meshes,objects,mesh_objects,boxes,indexBuffers,images,maps,materials,vertexBuffers)
			else:
				print("didn't write mesh as parent is lod")
		
	if Config.A3DVersionSystem <= 3:
		print("Exporting layers...\n")
			
	if Config.A3DVersionSystem <= 2:
		if len(objs_cameras) > 0:
			print("Exporting cameras...\n")
			for obj in objs_cameras:
				camera = obj.data
				
				#name
				a3dstr = A3DString()
				a3dstr.name = cleanupString(camera.name)
				
				#create transform/matrix
				a3dtrans = A3DTransform(Config)
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
				
				if Config.ExportBoundBoxes == 1:
					a3dbox = A3D2Box(Config)
					a3dbox._box = getBoundBox(obj)
					a3dbox._id = len(boxes)
					boxes.append(a3dbox)
				
				camtype = False
				if camera.type == "PERSP":
					camtype = False
				else:
					camtype = True

				a3dcam = A3D2Camera(Config)
				if Config.ExportBoundBoxes == 1:
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

def createMesh(Config,obj,linkedimgdata,linkedimg,linkeddata,linkedmesh,meshes,objects,mesh_objects,boxes,indexBuffers,images,maps,materials,vertexBuffers):
	mesh = obj.data
	if mesh.users > 1:
		print('this has is used for other objs aka linked copy')
		#linked mesh uses same name e.g "Cube"
		if mesh.name in linkeddata:
			#user already exists, retrieve ids
			ibufid = linkeddata[mesh.name][0]
			vbufids = linkeddata[mesh.name][1]
			#set to true so we don't add buffers with data we don't need
			linkedmesh=True
		else:
			#user doesn't exist yet
			ibufid = len(indexBuffers)
			vbufids = [len(vertexBuffers)]
			#assign for other users
			linkeddata[mesh.name] = [ibufid,vbufids]
			linkedmesh=False
	else:
		#print("single user mesh")
		linkedmesh=False
		ibufid = len(indexBuffers)
		vbufids = [len(vertexBuffers)]
	
	#get raw geometry data
	if checkBMesh() == True:
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonData(obj)
	else:
		vs,uvlayers,ins,nr,tan,bb,trns = getCommonDataNoBmesh(obj)
	#get surface data
	start,end,mts,mats,uvimgs = collectSurfaces(mesh)
	
	#create parent object
	if Config.ExportParentObj == 1:
		a3dstr2 = A3DString()
		a3dstr2.name = "obj_"+cleanupString(obj.data.name)
		
		#create transform/matrix
		wtrns = getObjWorldTransform(obj)
		a3dtrans = A3DTransform(Config)
		a3dtrans._matrix.a = wtrns[0]
		a3dtrans._matrix.b = wtrns[1]
		a3dtrans._matrix.c = wtrns[2]
		a3dtrans._matrix.d = wtrns[3]
		a3dtrans._matrix.e = wtrns[4]
		a3dtrans._matrix.f = wtrns[5]
		a3dtrans._matrix.g = wtrns[6]
		a3dtrans._matrix.h = wtrns[7]
		a3dtrans._matrix.i = wtrns[8]
		a3dtrans._matrix.j = wtrns[9]
		a3dtrans._matrix.k = wtrns[10]
		a3dtrans._matrix.l = wtrns[11]
	
		a3dobj = A3D2Object(Config)
		#a3dobj._boundBoxId = 0
		a3dobj._id = len(mesh_objects)
		a3dobj._name = a3dstr2
		#a3dobj._parentId = 0
		a3dobj._transform = a3dtrans
		a3dobj._visible = 1
		objects.append(a3dobj)
		mesh_objects.append(a3dobj)
			
	
	if Config.ExportBoundBoxes == 1:
		#create mesh boundbox
		a3dbox = A3D2Box(Config)
		a3dbox._box = bb
		a3dbox._id = len(boxes)
		boxes.append(a3dbox)
	
	#create indexbuffer
	if linkedmesh == False:
		a3dibuf = A3D2IndexBuffer(Config)
		for x in range(len(ins)):
			a3dibuf._byteBuffer.append(ins[x])
		#a3dibuf._id = len(indexBuffers)
		a3dibuf._id = ibufid
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
			
			difmap = int("ffffffff",16)
			glossmap = int("ffffffff",16)
			lighmap = int("ffffffff",16)
			normmap = int("ffffffff",16)
			opacmap = int("ffffffff",16)
			specmap = int("ffffffff",16)
			reflmap = int("ffffffff",16)
			
			for tex in mats[x].texture_slots:
				if (tex is not None) and (tex.texture.type == "IMAGE"):
					name=tex.name.lower()
					
					print("filepath="+str(tex.texture.image.filepath))
					print("basename="+str(os.path.basename(tex.texture.image.filepath)))
					print(os.path.basename(bpy.path.display_name_from_filepath(tex.texture.image.filepath)))
					print(os.path.basename(bpy.path.abspath(tex.texture.image.filepath)))
					
					if tex.texture.image.filepath in linkedimgdata:
						#user already exists, retrieve ids
						imgid = linkedimgdata[tex.texture.image.filepath][0]
						#set to true so we don't add buffers with data we don't need
						linkedimg=True
					else:
						#user doesn't exist yet
						imgid = len(images)
						#assign for other users
						linkedimgdata[tex.texture.image.filepath] = [imgid]
						linkedimg = False

					#create image
					if linkedimg == False:
						a3dstr = A3DString()
						#a3dstr.name = os.path.basename(tex.texture.image.filepath)
						a3dstr.name = os.path.basename(bpy.path.abspath(tex.texture.image.filepath))
						
						a3dimg = A3D2Image(Config)
						a3dimg._id = imgid
						a3dimg._url = a3dstr
						images.append(a3dimg)
					
					a3dmap = A3D2Map(Config)
					a3dmap._channel = 0
					a3dmap._id = len(maps)
					a3dmap._imageId = imgid
					maps.append(a3dmap)
					
					if name == 'diffuse':
						difmap = a3dmap._id
					elif name == 'normal':
						normmap = a3dmap._id
					elif name == 'specular':
						specmap = a3dmap._id
					elif name == 'opacity':
						opacmap = a3dmap._id
					elif name == 'glossiness':
						glossmap = a3dmap._id
					elif name == 'light':
						lighmap = a3dmap._id
					elif name == 'reflection':
						reflmap = a3dmap._id
					else:
						#just write as diffuse if no matches
						difmap = a3dmap._id
			
			#matname = GetMaterialTexture(mats[x])
			#if matname is not None:
			#	#create images
			#	a3dstr = A3DString()
			#	a3dstr.name = matname
			#	a3dimg = A3D2Image(Config)
			#	a3dimg._id = len(images)
			#	a3dimg._url = a3dstr
			#	images.append(a3dimg)
			#	#create maps
			#	a3dmap = A3D2Map(Config)
			#	a3dmap._channel = 0
			#	a3dmap._id = len(maps)
			#	a3dmap._imageId = a3dimg._id
			#	maps.append(a3dmap)
			
			#create material
			a3dmat = A3D2Material(Config)
			#if matname is not None:
			#	a3dmat._diffuseMapId = a3dmap._id
			#else:
			#	a3dmat._diffuseMapId = int("ffffffff",16)
			a3dmat._diffuseMapId = difmap
			a3dmat._glossinessMapId = glossmap
			a3dmat._id = len(materials)
			a3dmat._lightMapId = lighmap
			a3dmat._normalMapId = normmap
			a3dmat._opacityMapId = opacmap
			a3dmat._reflectionCubeMapId = reflmap
			a3dmat._specularMapId = specmap
			materials.append(a3dmat)
			
			#create surface
			a3dsurf = A3D2Surface(Config)
			a3dsurf._indexBegin = int(start[x])
			#a3dsurf._materialId = int("ffffffff",16)
			a3dsurf._materialId = a3dmat._id
			a3dsurf._numTriangles = int(end[x])
			mesh_surfaces.append(a3dsurf)
	elif len(uvimgs) > 0:
		#no materials, try image per face surfaces
		
		for x in range(len(uvimgs)):
			difmap = int("ffffffff",16)
			glossmap = int("ffffffff",16)
			lighmap = int("ffffffff",16)
			normmap = int("ffffffff",16)
			opacmap = int("ffffffff",16)
			specmap = int("ffffffff",16)
			reflmap = int("ffffffff",16)
			
			if uvimgs[x] != None:
				if uvimgs[x].filepath in linkedimgdata:
					#user already exists, retrieve ids
					imgid = linkedimgdata[uvimgs[x].filepath][0]
					#set to true so we don't add buffers with data we don't need
					linkedimg=True
				else:
					#user doesn't exist yet
					imgid = len(images)
					#assign for other users
					linkedimgdata[uvimgs[x].filepath] = [imgid]
					linkedimg = False
				
			#create image
			if (linkedimg == False) and (uvimgs[x] != None):
				a3dstr = A3DString()
				a3dstr.name = os.path.basename(bpy.path.abspath(uvimgs[x].filepath))
				
				a3dimg = A3D2Image(Config)
				a3dimg._id = imgid
				a3dimg._url = a3dstr
				images.append(a3dimg)
			
			if uvimgs[x] != None:
				a3dmap = A3D2Map(Config)
				a3dmap._channel = 0
				a3dmap._id = len(maps)
				a3dmap._imageId = imgid
				maps.append(a3dmap)	
				
				#just set to diffuse
				difmap = a3dmap._id
			
			a3dmat = A3D2Material(Config)
			a3dmat._diffuseMapId = difmap
			a3dmat._glossinessMapId = glossmap
			a3dmat._id = len(materials)
			a3dmat._lightMapId = lighmap
			a3dmat._normalMapId = normmap
			a3dmat._opacityMapId = opacmap
			a3dmat._reflectionCubeMapId = reflmap
			a3dmat._specularMapId = specmap
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
	a3dtrans = A3DTransform(Config)
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
	a3dstr = A3DString()
	a3dstr.name = cleanupString(obj.data.name)
	
	#create mesh
	a3dmesh = A3D2Mesh(Config)
	
	if Config.ExportBoundBoxes == 1:
		a3dmesh._boundBoxId = a3dbox._id
		
	a3dmesh._id = len(mesh_objects)
	#a3dmesh._indexBufferId = a3dibuf._id
	a3dmesh._indexBufferId = ibufid
	a3dmesh._name = a3dstr
	if Config.ExportParentObj == 1:
		a3dmesh._parentId = a3dobj._id
	a3dmesh._surfaces = mesh_surfaces
	a3dmesh._transform = a3dtrans
	#a3dmesh._vertexBuffers = [len(vertexBuffers)] #vertex buffer ids
	a3dmesh._vertexBuffers = vbufids #vertex buffer ids
	a3dmesh._visible = 1
	if obj.hide == True:
		a3dmesh._visible = 0
	else:
		a3dmesh._visible = 1
	meshes.append(a3dmesh)
	mesh_objects.append(a3dmesh)
	
	#reverse uvlayers, because a3d player loads latest uvlayer as default
	revkeys = sorted(uvlayers.keys(), reverse=True)
	uvlayersr = {}
	i=0
	for k in revkeys:
		uvlayersr[i] = uvlayers[k]
		i = i +1
	uvlayers = uvlayersr
	
	if linkedmesh == False:
		#create vertexbuffer
		a3dvbuf = A3D2VertexBuffer(Config)
		#POSITION = 0, NORMAL = 1, TANGENT4 = 2, JOINT = 3,TEXCOORD = 4
		attar = []
		if len(vs) > 0:
			attar.append(0)
		if (len(uvlayers) > 0) and (Config.ExportUV == 1):
			for uvname, uvdata in uvlayers.items():
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
				for uvname, uvdata in uvlayers.items():
					uvt = uvdata[0]
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
		#print("vs="+str(len(vs)))
	return a3dmesh
	
#==================================
# A3D IMPORTER
#==================================

class A3DImporterSettings:
	def __init__(self,FilePath="",ApplyTransforms=1,ImportLighting=1,ImportCameras=1):
		self.FilePath = str(FilePath)
		self.ApplyTransforms = int(ApplyTransforms)
		self.ImportLighting = int(ImportLighting)
		self.ImportCameras = int(ImportCameras)

class A3DImporter(bpy.types.Operator):
	bl_idname = "ops.a3dimporter"
	bl_label = "Import A3D (Alternativa)"
	bl_description = "Import A3D (Alternativa)"
	
	ApplyTransforms = BoolProperty(name="Apply Transforms", description="Apply transforms to objects", default=True)
	ImportLighting = BoolProperty(name="Import Lighting", description="Import the lighting setup", default=True)
	ImportCameras = BoolProperty(name="Import Cameras", description="Import any scene cameras", default=True)
	filepath= StringProperty(name="File Path", description="Filepath used for importing the A3D file", maxlen=1024, default="")

	def execute(self, context):
		time1 = time.clock()
		file = open(self.filepath,'rb')
		file.seek(0)
		version = ord(file.read(1))
		Config = A3DImporterSettings(FilePath=self.filepath,ApplyTransforms=self.ApplyTransforms,ImportLighting=self.ImportLighting,ImportCameras=self.ImportCameras)
		if version == 0:
			A3DImport1(file,Config)
		else:
			A3DImport2(file,Config)
		file.close()
		print(".a3d import time: %.2f" % (time.clock() - time1))
		return {'FINISHED'}
	def invoke (self, context, event):
		wm = context.window_manager
		wm.fileselect_add(self)
		return {'RUNNING_MODAL'}

def A3DImport1(file,Config):	
	file.seek(4)
	
	a3dnull = A3D2Null(Config)
	a3dnull.read(file)
	
	print(a3dnull._mask)
	print(a3dnull._byte_list)
	print('A3D Version %i.%i' %(1,0))
	
	a3d = A3D(file)
	a3d.setConfig(Config)
	a3d.read(file,a3dnull._mask)
	file.close()
	
	a3d2 = a3d.convert1_2()
	a3d2.render()
	a3dnull.reset()
	a3d2.reset()
	return {'FINISHED'}

def A3DImport2(file,Config):	
	file.seek(0)

	a3dpackage = A3D2Package(Config)
	a3dpackage.read(file)
	
	curpos = file.tell()
	
	if a3dpackage._packed == 1:
		data = file.read(a3dpackage._length)
		data = zlib.decompress(data)
		file.close()

		file = tempfile.TemporaryFile()
		file.write(data)
		file.seek(0)
		
	a3dnull = A3D2Null(Config)
	a3dnull.read(file)
	print(a3dnull._mask)
	print(a3dnull._byte_list)
	
	ver = A3DVersion(Config)
	ver.read(file)
	print('A3D Version %i.%i' %(ver.baseversion,ver.pointversion))
	
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
	
	a3d2 = A3D2()
	a3d2.setConfig(Config)
	a3d2.read(file,a3dnull._mask,ver)
	file.close()
	
	a3d2.render()
	a3dpackage.reset()
	a3dnull.reset()
	ver.reset()
	a3d2.reset()
	return {'FINISHED'}

#==================================
# A3D SHARED
#==================================

class A3DVersion:
	def __init__(self,Config):
		self.baseversion = 2
		self.pointversion = 0
		self.Config = Config
	def reset(self):
		self.baseversion = 2
		self.pointversion = 0
	def read(self,file):
		temp_data = file.read(calcsize('H'))
		self.baseversion = int(unpack('>H', temp_data)[0]) 
		temp_data = file.read(calcsize('H'))
		self.pointversion = int(unpack('>H', temp_data)[0])
	def write(self,file):
		file.write(pack('>H', self.baseversion))
		file.write(pack('>H', self.pointversion))

class A3DArray:
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
		self.length = int(numelements,2)
		
	def write(self,file,bylen):
		bitnum = bylen.bit_length()
		if bitnum <= 7:
			file.write(pack("B", bylen))
		elif bitnum > 7 and bitnum <= 14:
			byte1 = int((bylen >> 8) & 255)
			byte1 = byte1 + 128 #add 10000000 bits
			byte2 = int(bylen & 255)
			file.write(pack("B", byte1))
			file.write(pack("B", byte2))
		elif bitnum > 14 and bitnum <= 22:
			byte1 = int( (bylen >> 16) & 255 )
			byte1 = byte1 + 192 #add 11000000 bits
			byte2 = int( (bylen >> 8) & 255 )
			byte3 = int(bylen & 255)
			file.write(pack("B", byte1))
			file.write(pack("B", byte2))
			file.write(pack("B", byte3))
		else:
			print("Array bytes too long!\n")

class A3DString:
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
		ar = A3DArray()
		ar.write(file,bylen)
		self.writeName(file)
	
	def writeName(self,file):
		file.write(pack(str(len(self.name))+"s",self.name.encode("utf-8")))

class A3DTransform:
	def __init__(self,Config):
		self._matrix = A3DMatrix()
		self.Config = Config
		self._mskindex = 0
		
	def reset(self):
		self._matrix = A3DMatrix()
		self._mskindex = 0
		self._matrix.reset()
		
	def getMatrix(self):	
		matrx = Matrix()
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
		self.a = unpack('>f',temp)[0]
		temp = file.read(4)
		self.b = unpack('>f',temp)[0]
		temp = file.read(4)
		self.c = unpack('>f',temp)[0]
		temp = file.read(4)
		self.d = unpack('>f',temp)[0]
		temp = file.read(4)
		self.e = unpack('>f',temp)[0]
		temp = file.read(4)
		self.f = unpack('>f',temp)[0]
		temp = file.read(4)
		self.g = unpack('>f',temp)[0]
		temp = file.read(4)
		self.h = unpack('>f',temp)[0]
		temp = file.read(4)
		self.i = unpack('>f',temp)[0]
		temp = file.read(4)
		self.j = unpack('>f',temp)[0]
		temp = file.read(4)
		self.k = unpack('>f',temp)[0]
		temp = file.read(4)
		self.l = unpack('>f',temp)[0]
	
	def write(self,file):
		file.write(pack('>f',self.a))
		file.write(pack('>f',self.b))
		file.write(pack('>f',self.c))
		file.write(pack('>f',self.d))
		file.write(pack('>f',self.e))
		file.write(pack('>f',self.f))
		file.write(pack('>f',self.g))
		file.write(pack('>f',self.h))
		file.write(pack('>f',self.i))
		file.write(pack('>f',self.j))
		file.write(pack('>f',self.k))
		file.write(pack('>f',self.l))
		
class Float16Compressor:
	def __init__(self):
		self.temp = 0
		
	def compress(self,float32):
		F16_EXPONENT_BITS = 0x1F
		F16_EXPONENT_SHIFT = 10
		F16_EXPONENT_BIAS = 15
		F16_MANTISSA_BITS = 0x3ff
		F16_MANTISSA_SHIFT =  (23 - F16_EXPONENT_SHIFT)
		F16_MAX_EXPONENT =  (F16_EXPONENT_BITS << F16_EXPONENT_SHIFT)

		a = pack('>f',float32)
		b = hexlify(a)

		f32 = int(b,16)
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
		return f16
		
	def decompress(self,float16):
		s = int((float16 >> 15) & 0x00000001)    # sign
		e = int((float16 >> 10) & 0x0000001f)    # exponent
		f = int(float16 & 0x000003ff)            # fraction

		if e == 0:
			if f == 0:
				return int(s << 31)
			else:
				while not (f & 0x00000400):
					f = f << 1
					e -= 1
				e += 1
				f &= ~0x00000400
				#print(s,e,f)
		elif e == 31:
			if f == 0:
				return int((s << 31) | 0x7f800000)
			else:
				return int((s << 31) | 0x7f800000 | (f << 13))

		e = e + (127 -15)
		f = f << 13
		return int((s << 31) | (e << 23) | f)

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
	
	def	setConfig(self,Config):
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
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+1])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+2])
							c = c+3
						if 2 in attar:
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+1])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+2])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+3])
							c = c+4
						if 3 in attar:
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+1])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+2])
							a3dvbuf._byteBuffer.append(geom._vertexBuffers[x]._byteBuffer[c+3])
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
	
	def write(self,file):
		print("write a3d")
		
		tfile = tempfile.TemporaryFile(mode ='w+b')
		
		if len(self.boxes) > 0:
			#write
			arr = A3DArray()
			arr.write(tfile,len(self.boxes))
			self.nullmask = self.nullmask + str(0)
			for cla in self.boxes:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.geometries) > 0:
			arr = A3DArray()
			arr.write(tfile,len(self.geometries))
			self.nullmask = self.nullmask + str(0)
			for cla in self.geometries:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.images) > 0:
			arr = A3DArray()
			arr.write(tfile,len(self.images))
			self.nullmask = self.nullmask + str(0)
			for cla in self.images:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.maps) > 0:
			arr = A3DArray()
			arr.write(tfile,len(self.maps))
			self.nullmask = self.nullmask + str(0)
			for cla in self.maps:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.materials) > 0:
			arr = A3DArray()
			arr.write(tfile,len(self.materials))
			self.nullmask = self.nullmask + str(0)
			for cla in self.materials:
				cla.write(tfile)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
			
		if len(self.objects) > 0:
			arr = A3DArray()
			arr.write(tfile,len(self.objects))
			self.nullmask = self.nullmask + str(0)
			for cla in self.objects:
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
		ver.baseversion = 1
		ver.pointversion = 0
		ver.write(tfile2)
		
		#a3d
		tfile.seek(0)
		data = tfile.read()
		tfile2.write(data)
		tfile.close()

		#write package length
		a3dpack = A3D2Package(self.Config)
		a3dpack._length = tfile2.tell()
		a3dpack._packed = 0
		a3dpack.write(file)

		# uncompressed
		tfile2.seek(0)
		data = tfile2.read()
		file.write(data)
		tfile2.close()
			
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
		#mask = mask[16:]
		#print(mask)
		#print(str(len(mask)))
		
		
		#counter that just deals with the func keys
		findex = 0
		#mask counter that increments with the options of class
		mskindex = 0
		for i in range(len(mask)):
			#exit if we gone past amount
			if i >= len(funcs):
				break
			print("mask="+str(mask[:mskindex]))
			if mask[mskindex] == "0":
				#read array of classes
				arr = A3DArray()
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
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._box = []
		self._id = 0
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DBox - "+str(mask[mskindex]))
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			for a in range(arr.length):
				self._box.append( unpack(">f",file.read(calcsize(">f")))[0] )
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._id = unpack('>L',file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		print("box="+str(self._box))
		print("id="+str(self._id))
		
	def write(self,file):
		print("write boundbox\n")		
		self._optmask = self._optmask + str(0)
		arr = A3DArray()
		arr.write(file,len(self._box))
		for x in range(len(self._box)):
			file.write(pack('>f',self._box[x]))
		
		self._optmask = self._optmask + str(0)
		file.write(pack('>L',self._id))	

class A3DGeometry:
	def __init__(self,Config):
		self._id = 0
		self._indexBuffer = 0
		self._vertexBuffers = []
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._indexBuffer = 0
		self._vertexBuffers = []
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DGeometry - "+str(mask[mskindex]))
		
		if mask[mskindex + self._mskindex] == "0":
			self._id = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			ibuf = A3DIndexBuffer(self.Config)
			self._indexBuffer = ibuf.read(file,mask,mskindex + self._mskindex)
			self._mskindex = self._mskindex + ibuf._mskindex
		
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			for a in range(arr.length):
				vbuf = A3DVertexBuffer(self.Config)
				self._vertexBuffers.append(vbuf.read(file,mask,mskindex + self._mskindex))
				self._mskindex = self._mskindex + vbuf._mskindex

		print("id="+str(self._id))
					
	def write(self,file):
		print("write A3DGeometry")
		self._optmask = self._optmask + str(0)
		file.write(pack('>L',self._id))
		
		self._indexBuffer.write(file)
		
		for vbuf in self._vertexBuffers:
			vbuf.write(file)

class A3DImage:
	def __init__(self,Config):
		self._id = 0
		self._url = 0
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._id = 0
		self._url = 0
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DImage - "+str(mask[mskindex]))
		
		#if mask[mskindex + self._mskindex] == "0":
		self._id = unpack(">L", file.read(calcsize(">L")))[0]
		#self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._url = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print("id="+str(self._id))
		print("url="+str(self._url))
		
	def write(self,file):
		print("write A3DImage")
		file.write(pack('>L',self._id))
		
		self._optmask = self._optmask + str(0)
		self._url.write(file)
		
class A3DMap:
	def __init__(self,Config):
		self._channel = 0
		self._id = 0
		self._imageId = 0
		self._uOffset = 0
		self._uScale = 0
		self._vOffset = 0
		self._vScale = 0
		self._optmask = ""
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
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DMap - "+str(mask[mskindex]))
		
		if mask[mskindex + self._mskindex] == "0":
			self._channel = unpack(">H", file.read(calcsize(">H")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":		
			self._id = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._imageId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1

		if mask[mskindex + self._mskindex] == "0":
			self._uOffset = unpack(">f", file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._uScale = unpack(">f", file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._vOffset = unpack(">f", file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1

		if mask[mskindex + self._mskindex] == "0":
			self._vScale = unpack(">f", file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		print("channel="+str(self._channel))
		print("id="+str(self._id))
		print("imageId="+str(self._imageId))
		print("uOffset="+str(self._uOffset))
		print("uScale="+str(self._uScale))
		print("vOffset="+str(self._vOffset))
		print("vScale="+str(self._vScale))
		
	def write(self,file):
		print("write A3DMap")
		self._optmask = self._optmask + str(0)
		file.write(pack(">H",self._channel))
		self._optmask = self._optmask + str(0)
		file.write(pack(">L",self._id))
		self._optmask = self._optmask + str(0)
		file.write(pack(">L",self._imageId))
		self._optmask = self._optmask + str(0)
		file.write(pack(">f",self._uOffset))
		self._optmask = self._optmask + str(0)
		file.write(pack(">f",self._vOffset))
		self._optmask = self._optmask + str(0)
		file.write(pack(">f",self._vScale))
		
class A3DMaterial:
	def __init__(self,Config):
		self._diffuseMapId = None
		self._glossinessMapId = None
		self._id = 0
		self._lightMapId = None
		self._normalMapId = None
		self._opacityMapId = None
		self._specularMapId = None
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
		self._specularMapId = None
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3dMaterial - "+str(mask[mskindex])+str(mask[mskindex+1])+str(mask[mskindex+2]))
		if mask[mskindex + self._mskindex] == "0":
			self._diffuseMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":	
			self._glossinessMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":	
			self._id = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._lightMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._normalMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._opacityMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._specularMapId = unpack(">L",file.read(calcsize(">L")))[0]
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
		if self._diffuseMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._diffuseMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._glossinessMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._glossinessMapId))
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(pack(">L",self._id))
		
		if self._lightMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._lightMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._normalMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._normalMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._opacityMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._opacityMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._specularMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._specularMapId))
		else:
			self._optmask = self._optmask + str(1)

class A3DObject:
	def __init__(self,Config):
		self._boundBoxId = 0
		self._geometryId = 0
		self._id = 0
		self._name = 0
		self._parentId = 0
		self._surfaces = []
		self._transformation = 0
		self._visible = 1
		self._optmask = ""
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
		self._visible = 1
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DObject - "+str(mask[mskindex]))
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack('>L',file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._geometryId = unpack('>L',file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._id = unpack('>L',file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack('>L',file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			for a in range(arr.length):
				a3dsurf = A3DSurface(self.Config)
				self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
				self._mskindex = self._mskindex + a3dsurf._mskindex
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transformation = a3dtran
		self._mskindex = self._mskindex + 1
		
		#if mask[mskindex + self._mskindex] == "0":
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		#self._mskindex = self._mskindex + 1
			
		print("boundBoxId="+str(self._boundBoxId))
		print("geometryId="+str(self._geometryId))
		print("id="+str(self._id))
		print("name="+self._name)
		print("parentId="+str(self._parentId))
		print("visible="+str(self._visible))
		
	def write(self,file):
		print("write A3DObject")
		#bbid, id, indexbufid
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		
		if self._geometryId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._geometryId))
		else:
			self._optmask = self._optmask + str(1)
		
		self._optmask = self._optmask + str(0)
		file.write(pack(">L",self._id))
		
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
			
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
			
		if self._transformation is not None:
			self._optmask = self._optmask + str(0)
			self._transformation.write(file)
		else:
			self._optmask = self._optmask + str(1)
			
		#visible
		file.write(pack("B",self._visible))

class A3DIndexBuffer:
	def __init__(self,Config):
		self._byteBuffer = []
		self._indexCount = 0
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._byteBuffer = []
		self._indexCount = 0
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DIndexBuffer - "+str(mask[mskindex]))
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			for a in range(int(arr.length/2)):
				self._byteBuffer.append( unpack("<H",file.read(calcsize("<H")))[0] )
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._indexCount = unpack('>L',file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		return self
		
	def write(self,file):
		print("write A3DIndexBuffer")
		self._optmask = self._optmask + str(0)
		arr = A3DArray()
		# multiply by 2 because its length of bytes and we are using 2 bytes
		vbuflen = int(len(self._byteBuffer) * 2)
		arr.write(file,vbuflen) 
		for x in range(len(self._byteBuffer)):
			file.write(pack('<H',self._byteBuffer[x]))

		#write indexcount
		self._optmask = self._optmask + str(0)
		file.write(pack('>L',self._indexCount))
		
class A3DVertexBuffer:
	def __init__(self,Config):
		self._attributes = []
		self._byteBuffer = []
		self._vertexCount = 0
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._attributes = []
		self._byteBuffer = []
		self._vertexCount = 0
		self._optmask = ""
		self._mskindex = 0

	def read(self,file,mask,mskindex):
		print("read A3DVertexBuffer - "+str(mask[mskindex]))
		
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			self._attributes = []
			for a in range(arr.length):
				self._attributes.append(unpack("B",file.read(calcsize("B")))[0])
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			for a in range(int(arr.length/4)):
				self._byteBuffer.append(unpack("<f",file.read(calcsize("<f")))[0])
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._vertexCount  = unpack(">H",file.read(calcsize(">H")))[0]
		self._mskindex = self._mskindex + 1
		
		return self
		
	def write(self,file):
		print("write A3DVertexBuffer")
		self._optmask = self._optmask + str(0)
		arr = A3DArray()
		arr.write(file,len(self._attributes))
		for x in range(len(self._attributes)):
			file.write(pack("B",self._attributes[x]))
		
		self._optmask = self._optmask + str(0)
		arr = A3DArray()
		bybufsize = int(len(self._byteBuffer)*4)
		arr.write(file,bybufsize) 
		for byte in self._byteBuffer:
			file.write(pack("<f",byte))
		
		self._optmask = self._optmask + str(0)
		file.write(pack(">H",self._vertexCount))
		
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
		if mask[mskindex + self._mskindex] == "0":
			self._indexBegin = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._materialId = unpack(">L",file.read(calcsize(">L")))[0]			
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._numTriangles = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
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
		temp_data = ord(file.read(1))
		temp_data = bin(temp_data)[2:].rjust(8, '0')
		
		if temp_data[0] == '0':
			temp = ord(file.read(1))
			temp = bin(temp)[2:].rjust(8, '0')
			plen = temp_data[2:8] + temp
			print('Package length %i bytes' % int(plen,2))
			self._length = int(plen,2)
			
			if temp_data[1] == '0':
				self._packed = 0
				print('Package not packed')
			elif temp_data[1] == '1':
				self._packed = 1
				print('Package is packed')
			else:
				print('Error reading package Z')
				
		elif temp_data[0] == '1':
			temp = ord(file.read(1))
			temp = bin(temp)[2:].rjust(8, '0')
			temp1 = ord(file.read(1))
			temp1 = bin(temp1)[2:].rjust(8, '0')
			temp2 = ord(file.read(1))
			temp2 = bin(temp2)[2:].rjust(8, '0')
			plen = temp_data[1:8] + temp + temp1 + temp2
			print('Package length of %i bytes' % int(plen,2))
			
			self._length = int(plen,2)
			self._packed = 1
			print('Package is packed')
		else:
			print('Error reading package L')
	
	def write(self,file):
		#print(self._length)
		bitnum = self._length.bit_length()
		if self._length <= 16383:
			#6bits + next 1 byte (14bits)
			if self._packed == 1:
				data = 16384 + self._length
			else:
				data = self._length
			file.write(pack(">H", data))
		elif bitnum > 6 and bitnum <= 31:
			#7bits + next 3 bytes (31bits)
			byte1 = int((self._length >> 24) & 255)
			byte1 = byte1 + 128
			byte2 = int((self._length >> 16) & 255)
			byte3 = int((self._length >> 8) & 255)
			byte4 = int(self._length & 255)
			file.write(pack("B",byte1))
			file.write(pack("B",byte2))
			file.write(pack("B",byte3))
			file.write(pack("B",byte4))
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
		temp_data = ord(file.read(1))

		temp_data = bin(temp_data)[2:].rjust(8, '0')
	
		if temp_data[0] == '0':
			#short null
			print('Short null-mask')
			if temp_data[1] == '0':
				if temp_data[2] == '0':
					#00
					nulldata = temp_data[3:8]
					#print('Null mask %s' % str(nulldata))
					print('(LL=00) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					self._mask = nulldata
				elif temp_data[2] == '1':
					#01
					temp = ord(file.read(1))
					temp = bin(temp)[2:].rjust(8, '0')
					nulldata = temp_data[3:8] + temp
					print('(LL=01) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
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
					print('(LL=10) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
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
					print('(LL=11) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
					self._mask = nulldata
				else:
					print('Error reading short Null...')
			else:
				print('Error reading short Null..')
		else:
			print('Long null-mask')
			if temp_data[1] == '0':
				nulldata = temp_data[2:8]
				print('(L=0) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
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
				print('(L=1) Null mask length %i (%i bits)' % (int(nulldata,2), (int(nulldata,2)*8)))
				for x in range(int(nulldata,2)):
					byt = file.read(1)
					self._mask += '{0:08b}'.format(ord(byt))
					self._byte_list.append('%02X' % ord(byt))
			else:
				print('Error reading long Null..')
		
	def setBits(self):
		bits = len(self._mask)
		#temp3 = bits >> 3
		#temp4 = 7 ^ bits & 7
		
		#fill bytelist
		bytelist = []
		rem = bits % 8
		if rem == 0:
			#if fits exactly in bytes
			bytenum = int(bits/8)
		else:
			#if doesn't fit exactly round up
			bytenum = int((bits+(8-rem))/8)
		for x in range(bytenum):
			bytelist.append(0)
			
		for x in range(len(self._mask)):	
			#bits = len(bytelist)
			
			#get current byte
			rem = x % 8
			if rem == 0:
				#if fits exactly in bytes
				byteweareon = int(x/8)
			else:
				#if doesn't fit exactly round up
				byteweareon = int((x+(8-rem))/8)
			
			#temp3 = byteweareon >> 3
			#temp4 = 7 ^ byteweareon & 7
			#print("byteweareon="+str(byteweareon))
			bits = x
			temp3 = bits >> 3
			temp4 = 7 ^ bits & 7
			#print("temp3="+str(temp3))
					
			if self._mask[x] == "1":
				#bytelist.append(int(bytelist[temp3] | 1 << temp4))
				bytelist[temp3] = int(bytelist[temp3] | 1 << temp4)
			else:
				#bytelist.append(int(bytelist[temp3] & (255 ^ 1 << temp4)))
				bytelist[temp3] = int(bytelist[temp3] & (255 ^ 1 << temp4))
		
		#bytelist.append(
		return bytelist
	
	def write(self,file):
		bytelist = self.setBits()
		#print("bytelist")
		#print(bytelist)
		bits = len(self._mask)
		x=int(self._mask,2)
		
		INPLACE_MASK_FLAG = 128
		MASK_LENGTH_2_BYTES_FLAG = 64
		INPLACE_MASK_1_BYTES = 32
		INPLACE_MASK_3_BYTES = 96
		INPLACE_MASK_2_BYTES = 64
		MASK_LENGTH_1_BYTE = 128
		MASK_LEGTH_3_BYTE = 12582912
		temp5 = 0
		temp6 = 0
		temp7 = 0
		temp8 = 0
		temp9 = 0
		bits = len(self._mask)
		temp3 = bytelist
		
		#print("bits="+str(bits))
		
		if bits <= 5:
			#print("<= 5")
			byte1 = int(rshift(temp3[0] & 255,3))
			print(byte1)
			file.write(pack("B",byte1))
		elif bits > 5 and bits <= 13:
			#print("<= 13")
			byte1 = int(rshift(temp3[0] & 255,3) + INPLACE_MASK_1_BYTES)
			byte2 = int(rshift(temp3[1] & 255,3) + (temp3[0] << 5))
			print(byte1)
			print(byte2 & 255)
			file.write(pack("B",byte1))
			file.write(pack("B",byte2 & 255))
		elif bits > 13 and bits <= 21:
			#print("<= 21")
			for j in range(3):
				if j not in temp3:
					temp3.append(0)
			byte1 = int(rshift(temp3[0] & 255,3) + INPLACE_MASK_2_BYTES)
			byte2 = int(rshift(temp3[1] & 255,3) + (temp3[0] << 5))
			byte3 = int(rshift(temp3[2] & 255,3) + (temp3[1] << 5))
			print(byte1)
			print(byte2 & 255)
			print(byte3 & 255)
			file.write(pack("B",byte1))
			file.write(pack("B",byte2 & 255))
			file.write(pack("B",byte3 & 255))
		elif bits > 21 and bits <= 29:
			#print("<= 29")
			for j in range(4):
				if j not in temp3:
					temp3.append(0)
			byte1 = int(rshift(temp3[0] & 255,3) + INPLACE_MASK_3_BYTES)
			byte2 = int(rshift(temp3[1] & 255,3) + (temp3[0] << 5))
			byte3 = int(rshift(temp3[2] & 255,3) + (temp3[1] << 5))
			byte4 = int(rshift(temp3[3] & 255,3) + (temp3[2] << 5))
			print(byte1)
			print(byte2 & 255)
			print(byte3 & 255)
			print(byte4 & 255)
			file.write(pack("B",byte1))
			file.write(pack("B",byte2 & 255))
			file.write(pack("B",byte3 & 255))
			file.write(pack("B",byte4 & 255))
		else:
			if bits <= 504:
				#print("<= 504")				
				temp5 = len(temp3)
				byte1 = int((temp5 & 255) + MASK_LENGTH_1_BYTE)
				print(byte1)
				file.write(pack("B",byte1))
				for y in range(len(temp3)):
					file.write(pack("B",temp3[y]))
			else:
				if bits <= 33554432:
					#temp5 = len(temp3)
					#temp7 = temp5 + MASK_LEGTH_3_BYTE
					#temp6 = int((temp7 & 16711680) >> 16)
					#temp8 = int((temp7 & 65280) >> 8)
					#temp9 = int(temp7 & 255)
					#file.write(pack("B",temp6))
					#file.write(pack("B",temp8))
					#file.write(pack("B",temp9))
					#for y in range(len(temp3)):
					#	file.write(pack("B",temp3[y]))
					#print("even longer")
					rem = bits % 8
					if rem == 0:
						#if fits exactly in bytes
						bytenum = bits/8
					else:
						#if doesn't fit exactly round up
						bytenum = int((bits+(8-rem))/8)

					tbits = int(bytenum * 8)
					rbits = int(tbits - bits)

					#print("bytenum="+str(bytenum))
					lenbyte = int(bytenum + 12582912) #11000000 00000000 00000000
					lenbits = lenbyte.bit_length()

					#place bits right to left
					byte1 = int( (lenbyte >> 16) & 255 )
					byte2 = int( (lenbyte >> 8) & 255 )
					byte3 = int( lenbyte & 255 )

					#print("byte1="+str(byte1))
					#print("byte2="+str(byte2))		
					#print("byte3="+str(byte3))		
					file.write(pack("B",byte1))
					file.write(pack("B",byte2))
					file.write(pack("B",byte3))

					#nullmask write now

					#if fits exactly
					if bits == bytenum*8:
						#left to right
						for j in range(bytenum):
							byte = int( ( x >> (tbits - (8 * (j+1))) ) & 255 )
							file.write(pack("B",byte))
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
							file.write(pack("B",byte))
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
	
	def render(self):
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
			
		joints = {}
		for jnt in self.joints:
			print("id="+str(jnt._id))
			print("pid="+str(jnt._parentId))
			joints[jnt._id] = jnt
			
		meshes = {}
		for me in self.meshes:
			meshes[me._id] = me
			
		objects = {}
		for obje in self.objects:
			objects[obje._id] = obje
		
		if self.Config.ImportLighting == 1:
			for light in self.ambientLights:
				light.render(objects)
					
			for light in self.directionalLights:
				light.render(objects)
				
			for light in self.spotLights:
				light.render(objects)
				
			for light in self.omniLights:
				light.render(objects)
		
		if self.Config.ImportCameras == 1:
			for cam in self.cameras:
				cam.render()
			
		for mesh in self.meshes:
			mesh.render(ibuffers,vbuffers,materials,maps,images)
			
		for skin in self.skins:
			skin.render(ibuffers,vbuffers,materials,maps,images,joints,self.joints)
			
		for sprite in self.sprites:
			sprite.render(materials,maps,images)
			
		for decal in self.decals:
			decal.render()
			
		for lod in self.lods:
			lod.render(meshes)
		
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
				arr = A3DArray()
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
	
	def writeClass(self,file,listclass):
		#print(str(len(listclass)) + str(listclass))
		if len(listclass) > 0:
			arr = A3DArray()
			arr.write(file,len(listclass))
			#add class as option
			self.nullmask = self.nullmask + str(0)
			for cla in listclass:
				cla.write(file)
				self.nullmask = self.nullmask + cla._optmask
		else:
			self.nullmask = self.nullmask + str(1)
					
	def write(self,file):
		print("write a3d2\n")
		
		tfile = tempfile.TemporaryFile(mode ='w+b')
		
		self.writeClass(tfile,self.ambientLights)	
		self.writeClass(tfile,self.animationClips)	
		self.writeClass(tfile,self.animationTracks)	
		self.writeClass(tfile,self.boxes)	
		self.writeClass(tfile,self.cubeMaps)	
		self.writeClass(tfile,self.decals)	
		self.writeClass(tfile,self.directionalLights)	
		self.writeClass(tfile,self.images)	
		self.writeClass(tfile,self.indexBuffers)	
		self.writeClass(tfile,self.joints)	
		self.writeClass(tfile,self.maps)	
		self.writeClass(tfile,self.materials)	
		self.writeClass(tfile,self.meshes)	
		self.writeClass(tfile,self.objects)	
		self.writeClass(tfile,self.omniLights)
		self.writeClass(tfile,self.skins)		
		self.writeClass(tfile,self.spotLights)	
		self.writeClass(tfile,self.sprites)
		self.writeClass(tfile,self.vertexBuffers)
		if self.Config.A3DVersionSystem <= 3:
			self.writeClass(tfile,self.layers)
		if self.Config.A3DVersionSystem <= 2:
			self.writeClass(tfile,self.cameras)
			self.writeClass(tfile,self.lods)
		
		tfile2 = tempfile.TemporaryFile(mode ='w+b')
		
		#print("nullmask = "+self.nullmask)
		
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

# lighting	
	
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
		
	def read(self,file,mask,mskindex):
		print("read A3D2AmbientLight")
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._color = toRgb(unpack(">L", file.read(calcsize(">L")))[0])
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._intensity = unpack(">f", file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]

	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("<L",self._color))
		file.write(pack(">Q",self._id))
		file.write(pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("B",self._visible))
	
	def render(self,objects):
		if self._name is not None:
			nme = self._name
		else:
			nme = "Lamp"
	
		lamp = bpy.data.lamps.new(nme,"HEMI") 
		ob = bpy.data.objects.new(nme, lamp)
		
		lamp.color = self._color
		lamp.energy = self._intensity
		
		if self._parentId is not None:
			obj = objects[self._parentId]
			if obj._transform != None:
				print("ambient yes")
				ob.matrix_world = obj._transform.getMatrix()

		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
		
		if self._visible == False:
			ob.hide = False

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
		
	def read(self,file,mask,mskindex):
		print("read A3D2DirectionalLight")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._color = toRgb(unpack("I", file.read(calcsize("I")))[0])
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._intensity = unpack(">f", file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("I",self._color))
		file.write(pack(">Q",self._id))
		file.write(pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("B",self._visible))
	
	def render(self,objects):
		if self._name is not None:
			nme = self._name
		else:
			nme = "Lamp"
	
		lamp = bpy.data.lamps.new(nme,"AREA") 
		ob = bpy.data.objects.new(nme, lamp)
		
		lamp.color = self._color
		lamp.energy = self._intensity
		
		if self._parentId is not None:
			obj = objects[self._parentId]
			if obj._transform != None:
				print("direct yes")
				ob.matrix_world = obj._transform.getMatrix()

		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
		
		if self._visible == False:
			ob.hide = False

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
		
	def read(self,file,mask,mskindex):
		print("read A3D2OmniLight")
		self._attenuationBegin = unpack('>f',file.read(calcsize(">f")))[0]
		self._attenuationEnd = unpack('>f',file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._color = unpack("I",file.read(calcsize("I")))[0]
		self._id = unpack(">Q",file.read(calcsize(">Q")))[0]
		self._intensity = unpack(">f",file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		file.write(pack('>f',self._attenuationBegin))
		file.write(pack('>f',self._attenuationEnd))
		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)

		file.write(pack("I",self._color))			
		file.write(pack(">Q",self._id))
		file.write(pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("B",self._visible))
	
	def render(self,objects):
		if self._name is not None:
			nme = self._name
		else:
			nme = "Lamp"
	
		lamp = bpy.data.lamps.new(nme,"POINT") 
		ob = bpy.data.objects.new(nme, lamp)
		
		lamp.color = self._color
		lamp.energy = self._intensity
		
		if self._parentId is not None:
			obj = objects[self._parentId]
			if obj._transform != None:
				print("omni yes")
				ob.matrix_world = obj._transform.getMatrix()

		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
		
		if self._visible == False:
			ob.hide = False

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
		
	def read(self,file,mask,mskindex):
		print("read A3D2SpotLight")
		self._attenuationBegin = unpack('>f', file.read(calcsize(">f")))[0]
		self._attenuationEnd = unpack('>f', file.read(calcsize(">f")))[0]
		
		print(self._attenuationBegin)
		print(self._attenuationEnd)
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		print(self._boundBoxId)
		
		self._color = unpack("I",file.read(calcsize("I")))[0]
		print(self._color)
		
		if mask[mskindex + self._mskindex] == "0":
			self._falloff = unpack('>f', file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._hotspot = unpack('>f', file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">Q",file.read(calcsize(">Q")))[0]
		self._intensity = unpack(">f",file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print(self._name)
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
		
		file.write(pack("B",self._visible))
		
	def write(self,file):
		file.write(pack('>f',self._attenuationBegin))
		file.write(pack('>f',self._attenuationEnd))
		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)

		file.write(pack("I",self._color))
		
		if self._falloff is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">f",self._falloff))
		else:
			self._optmask = self._optmask + str(1)
			
		if self._hotspot is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">f",self._hotspot))
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(pack(">Q",self._id))
		file.write(pack(">f",self._intensity))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("B",self._visible))
	
	def render(self,objects):
		if self._name is not None:
			nme = self._name
		else:
			nme = "Lamp"
	
		lamp = bpy.data.lamps.new(nme,"SPOT") 
		ob = bpy.data.objects.new(nme, lamp)
		
		lamp.color = self._color
		lamp.energy = self._intensity
		
		if self._parentId is not None:
			obj = objects[self._parentId]
			if obj._transform != None:
				print("spot yes")
				ob.matrix_world = obj._transform.getMatrix()

		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			ob.location = bpy.context.scene.cursor_location
		bpy.context.scene.objects.link(ob)
		
		if self._visible == False:
			ob.hide = False

# 3d
			
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
		self._optmask = ""
		self._mskindex = 0
				
	def read(self,file,mask,mskindex):
		print("read A3D2Mesh")
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._indexBufferId = unpack(">L", file.read(calcsize(">L")))[0]

		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		#surfaces
		arr = A3DArray()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3D2Surface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			self._mskindex = self._mskindex + a3dsurf._mskindex
		
		#transform
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		#buffer
		arr = A3DArray()
		arr.read(file)
		self._vertexBuffers = []
		for a in range(arr.length):
			self._vertexBuffers.append(unpack(">L", file.read(calcsize(">L")))[0])
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		#print("write mesh\n")
		#bbid, id, indexbufid
		#print(self._boundBoxId)
		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(pack(">Q",self._id))
		file.write(pack(">L",self._indexBufferId))
		
		#string
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#parentid
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		#surfaces
		arr = A3DArray()
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
		arr = A3DArray()
		arr.write(file,len(self._vertexBuffers))
		for x in range(len(self._vertexBuffers)):
			file.write(pack(">L",self._vertexBuffers[x]))
		#visible
		file.write(pack("B",self._visible))
	
	def render(self,ibuffers,vbuffers,materials,maps,images):
		verts = []
		faces = []
		uvs = []
		norms = []
		tans = []
		joints = []
	
		#index buff
		ibuf = ibuffers[self._indexBufferId]
		i=0
		for x in range(int(len(ibuf._byteBuffer)/3)):
			temp = (ibuf._byteBuffer[i],ibuf._byteBuffer[i+1],ibuf._byteBuffer[i+2])
			faces.append(temp)
			i=i+3
		
		#vert buff
		for v in self._vertexBuffers:
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
			
			uvc = 0
			uvlayers = {}
			
			i = 0
			for p in range(points):
				uvc = 0
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
						ai = vbuf._byteBuffer[i]
						i = i + 1
						aw = vbuf._byteBuffer[i]
						i = i + 1
						bi = vbuf._byteBuffer[i]
						i = i + 1
						bw = vbuf._byteBuffer[i]
						i = i + 1
						#jointA.index, jointA.weight, jointB.index, jointB.weight
						joints.append((ai, aw, bi, bw))
					if att == 4:
						if uvc not in uvlayers:
							uvlayers[uvc] = []
						uv1 = vbuf._byteBuffer[i]
						i = i + 1
						uv2 = vbuf._byteBuffer[i]
						uv2 = 1.0 - uv2
						i = i + 1
						uvlayers[uvc].append([uv1,uv2])
						uvc=uvc+1
			
		#print(verts)
		#print(faces)
		#print(uvs)
		#print(self._name)
		#print(uvlayers)
		
		if self._name is not None:
			nme = self._name
		else:
			nme = "Mesh"
		
		# create a new mesh  
		me = bpy.data.meshes.new(nme) 
		
		# create an object with that mesh
		ob = bpy.data.objects.new(nme, me)  
		
		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			# position object at 3d-cursor
			ob.location = bpy.context.scene.cursor_location
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# Fill the mesh with verts, edges, faces 
		# from_pydata doesn't work correctly, it swaps vertices in some triangles 
		me.from_pydata(verts,[],faces)   # edges or faces should be [], or you ask for problems
		
		#me.vertices.add(len(verts))
		#me.faces.add(len(faces))
		
		#for i in range(len(verts)):
		#	me.vertices[i].co=verts[i]
			
		#for i in range(len(faces)):
		#	me.faces[i].vertices=faces[i]
		
		#select object
		for object in bpy.data.objects:
			object.select = False
		ob.select = True
		bpy.context.scene.objects.active = ob
		
		#me.update(calc_edges=True)    # Update mesh with new data
		
		diffuseimg = None
		
		if self._visible == False:
			ob.hide = True
		
		for surf in self._surfaces:
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
					#mtex.uv_layer = uvname
					
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
					#mtex.uv_layer = uvname
					
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
					#mtex.uv_layer = uvname
					
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
					#mtex.uv_layer = uvname
					
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
					#mtex.uv_layer = uvname
					
				if (mat._reflectionCubeMapId is not None) and (mat._reflectionCubeMapId != int("0xFFFFFFFF",16)):
					#get map
					map = maps[mat._reflectionCubeMapId]
					#get img
					img = images[map._imageId]
					
					#new image
					texture = bpy.data.textures.new("reflection", type='IMAGE')
					DIR = os.path.dirname(self.Config.FilePath)
					image = load_image(img._url, DIR)
					texture.image = image
				
					#new texture
					mtex = surf_mat.texture_slots.add()
					mtex.texture = texture
					mtex.texture_coords = 'UV'
					mtex.use_map_color_diffuse = False
					#mtex.uv_layer = uvname
					
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
					#mtex.uv_layer = uvname
		
		#set norms
		if len(norms) > 0:
			for i in range(len(norms)):
				me.vertices[i].normal=norms[i]
		
		
		#add uv layer
		if len(uvlayers) > 0:
			for uvindex, uvdata in uvlayers.items():
				uvname = "UV"+str(uvindex)
				uvlayer = me.uv_textures.new(uvname)
				uvs = uvdata
				if checkBMesh() == True:
					uv_faces = me.uv_layers[uvindex].data
					fcc=0
					for fc in range(len(uv_faces)):
						if fcc >= len(uv_faces):
							break
						face = faces[fc]
						v1, v2, v3 = face
						if diffuseimg is not None:
							me.uv_textures[uvindex].data[0].image = diffuseimg
						uv_faces[fcc].uv = uvs[v1]
						uv_faces[fcc+1].uv = uvs[v2]
						uv_faces[fcc+2].uv = uvs[v3]
						fcc = fcc + 3
				else:
					uv_faces = me.uv_textures.active.data[:]
					for fidx, uf in enumerate(uv_faces):
						face = faces[fidx]
						v1, v2, v3 = face
						if diffuseimg is not None:
							uf.image = diffuseimg
						uf.uv1 = uvs[v1]
						uf.uv2 = uvs[v2]
						uf.uv3 = uvs[v3]
		
		me.validate()
		me.update(calc_edges=True)

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
		
	def read(self,file,mask,mskindex):
		print("read A3D2Skin")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._indexBufferId = unpack(">L", file.read(calcsize(">L")))[0]
		
		arr = A3DArray()
		arr.read(file)
		for x in range(arr.length):
			a3djntbnd = A3D2JointBindTransform(self.Config)
			self._jointBindTransforms.append(a3djntbnd.read(file,mask,mskindex))
			
		arr = A3DArray()
		arr.read(file)
		for x in range(arr.length):
			self._joints.append(unpack(">Q", file.read(calcsize(">Q")))[0])
			
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print(self._name)
		
		arr = A3DArray()
		arr.read(file)
		for x in range(arr.length):
			self._numJoints.append(unpack(">H", file.read(calcsize(">H")))[0])
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3D2Surface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			self._mskindex = self._mskindex + a3dsurf._mskindex
			
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		self._vertexBuffers = []
		for a in range(arr.length):
			self._vertexBuffers.append(unpack(">L", file.read(calcsize(">L")))[0])
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		print("write")
	
	def render(self,ibuffers,vbuffers,materials,maps,images,indexedJoints,joints):
		verts = []
		faces = []
		uvs = []
		norms = []
		tans = []
		jnts = []
	
		#index buff
		ibuf = ibuffers[self._indexBufferId]
		i=0
		for x in range(int(len(ibuf._byteBuffer)/3)):
			temp = (ibuf._byteBuffer[i],ibuf._byteBuffer[i+1],ibuf._byteBuffer[i+2])
			faces.append(temp)
			i=i+3
		
		#vert buff
		for v in self._vertexBuffers:
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
						ai = vbuf._byteBuffer[i]
						i = i + 1
						aw = vbuf._byteBuffer[i]
						i = i + 1
						bi = vbuf._byteBuffer[i]
						i = i + 1
						bw = vbuf._byteBuffer[i]
						i = i + 1
						#jointA.index, jointA.weight, jointB.index, jointB.weight
						jnts.append((ai, aw, bi, bw))
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
		
		if self._name is not None:
			nme = self._name
		else:
			nme = "Skin"
		
		# create a new mesh  
		me = bpy.data.meshes.new(nme) 
		
		# create an object with that mesh
		ob = bpy.data.objects.new(nme, me)  
		
		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			# position object at 3d-cursor
			ob.location = bpy.context.scene.cursor_location
		
		# Link object to scene
		bpy.context.scene.objects.link(ob)  
		
		# Fill the mesh with verts, edges, faces 
		# from_pydata doesn't work correctly, it swaps vertices in some triangles 
		me.from_pydata(verts,[],faces)   # edges or faces should be [], or you ask for problems
		
		#me.vertices.add(len(verts))
		#me.faces.add(len(faces))
		
		#for i in range(len(verts)):
		#	me.vertices[i].co=verts[i]
			
		#for i in range(len(faces)):
		#	me.faces[i].vertices=faces[i]
		
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
		
		if self._visible == False:
			ob.hide = True
		
		for surf in self._surfaces:
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
					texture = bpy.data.textures.new("reflection", type='IMAGE')
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
		
		#set norms
		if len(norms) > 0:
			for i in range(len(norms)):
				me.vertices[i].normal=norms[i]
		
		if len(uvs) > 0:
			if checkBMesh() == True:
				uv_faces = me.uv_layers[0].data
				fcc=0
				for fc in range(len(uv_faces)):
					if fcc >= len(uv_faces):
						break
					face = faces[fc]
					v1, v2, v3 = face
					if diffuseimg is not None:
						me.uv_textures[0].data[0].image = diffuseimg
					uv_faces[fcc].uv = uvs[v1]
					uv_faces[fcc+1].uv = uvs[v2]
					uv_faces[fcc+2].uv = uvs[v3]
					fcc = fcc + 3
			else:
				uv_faces = me.uv_textures.active.data[:]
				for fidx, uf in enumerate(uv_faces):
					face = faces[fidx]
					v1, v2, v3 = face
					if diffuseimg is not None:
						uf.image = diffuseimg
					uf.uv1 = uvs[v1]
					uf.uv2 = uvs[v2]
					uf.uv3 = uvs[v3]

		me.validate()
		me.update(calc_edges=True)
		
		#boneTable1 = [
		#	('Base', None, (1,0,0)),
		#	('Mid', 'Base', (1,0,0)),
		#	('Tip', 'Mid', (0,0,1))
		#]
		#
		#print("joints"+str(self._joints))
		#print("numJoints"+str(self._numJoints))
		#jnts jointA.index, jointA.weight, jointB.index, jointB.weight
		
		#myboneTable = []
		#for j in joints:
		#	if j._parentId == None:
		#		par = None
		#	else:
		#		if j._parentId in indexedJoints:
		#			par = indexedJoints[j._parentId]._name
		#		else:
		#			par = None
		#	
		#	if j._transform != None:
		#		mat = j._transform.getMatrix()
		#		(trans, rot, scale) = mat.decompose()
		#	else:
		#		trans = (0,0,0)
		#	bne = (j._name,par,trans)
		#	myboneTable.append(bne)

		
		#origin = Vector((0,0,0))
		#bent = self.createRig('Bent', origin, myboneTable)
		
		#bone.parent = anotherbone
			#bone.use_connect = True
			
		#self.skinMesh(ob,arm)
		
		#bpy.ops.object.armature_add()
		#obj = bpy.context.scene.objects.active
		#obj.name = "Armature"
		#arm = obj.data
		
		
		#create bonetable
		boneTable1 = []
		
		for j in joints:
			if j._parentId in indexedJoints:
				nameparent = indexedJoints[j._parentId]._name
			else:
				nameparent=None
			mat = j._transform.getMatrix()
			(pos, rot, scale) = mat.decompose()
			tmp = (j._name,nameparent,pos,mat)
			boneTable1.append(tmp)
		rig = self.createRig('Rig', (0,0,0), boneTable1)
		
		
				
		# New Armatures include a default bone, remove it.
		#bones.remove(bones[0])

		#make bones
		#bpy.ops.object.mode_set(mode='EDIT')
		#for j in joints:
		#	bone = arm.edit_bones.new(j._name)
		#	bone.head = (0,0,0)
		#	bone.tail = (0,0,1)
		#bpy.context.scene.update()
		
		#make bone parents
		#for j in joints:
		#	print(j._name)
		#	print(j._transform.getMatrix())
		#	nameparent=None
		#	if j._parentId in indexedJoints:
		#		nameparent = indexedJoints[j._parentId]._name
		#	if nameparent != None:
		#		bone = arm.edit_bones[j._name]
		#		parentbone = arm.edit_bones[nameparent]
		#		bone.parent = parentbone
		#		#bone.head = parentbone.tail
		#		bone.use_connect = True
		#bpy.context.scene.update()
		
		#for j in joints:
		#	#parented bone transform
		#	if bone.parent != None:
		#		q = bone.matrix.to_quaternion()
		#		quat = Quaternion((q.w,-q.x,-q.y,-q.z))
		#		quat_parent	= bone.parent.matrix.to_quaternion().inverted()
		#		parent_head	= quat_parent * bone.parent.head
		#		parent_tail	= quat_parent * bone.parent.tail
		#		translation	= (parent_tail - parent_head) + bone.head
		#	else:
		#		#root bone -armature is parent so use armature world space
		#		translation	= ob.matrix_world * bone.head
		#		rot_matrix	= bone.matrix * ob.matrix_world.to_3x3()
		#		quat		= rot_matrix.to_quaternion()
		#bpy.context.scene.update()
		
		#for j in joints:
		#	bone = arm.edit_bones[j._name]
		#	mat = j._transform.getMatrix()
		#	(pos, rot, scale) = mat.decompose()
		#	
		#	globalVector = pos
		#	mw = obj.matrix_world
		#	matrix = Matrix()
		#	matrix = obj.matrix_world.inverted()*(Matrix.Translation(globalVector)+mw.to_3x3().to_4x4())
		#	bone.transform(matrix,False,False)
		
		#set bone positioning/matrix
		#c=0
		#for j in joints:
		#	mat = j._transform.getMatrix()
		#	(pos, rot, scale) = mat.decompose()
#
#			qx,qy,qz,qw = rot[0],rot[1],rot[2],rot[3]
#
#			bone = arm.edit_bones[j._name]
#			
#			if c==0:
#				rot = Quaternion((qw,-qx,-qy,-qz))
#			if c!=0:
#				rot = Quaternion((qw,qx,qy,qz))
#			matrix = Matrix()
#			rot = rot.to_matrix().inverted()
#			print("rot")
#			print(rot)
#			matrix[0][:3] = rot[0]
#			matrix[1][:3] = rot[1]
#			matrix[2][:3] = rot[2]
#			matrix[3][:3] = pos
#			if c>0:
#				matrix*bone.parent.matrix
#				
#			if c!=0:
#				bone.head = bone.parent.head+Vector(pos) * bone.parent.matrix
#				tempM = rot.to_4x4()*bone.parent.matrix
#				bone.transform(tempM, scale=False, roll=True)
#			else:
#				bone.head = Vector(pos)
#				bone.transform(rot, scale=False, roll=True)
#			bvec = bone.tail- bone.head
#			bvec.normalize()
#			bone.tail = bone.head + 0.1 * bvec
				
#		bpy.context.scene.update()
			
			#bone.transform(mat, scale=False, roll=False)

		#	if c != 0:
		#		bone.head = bone.parent.head + pos * bone.parent.matrix
		#		tempM = rot.to_4x4()*bone.parent.matrix
		#		bone.transform(tempM, scale=False, roll=True)
		#	else:
		#		#root bone
		#		bone.head = (0,0,0)
		#		rot = Matrix.Translation((0,0,0))
		#		bone.align_roll(t3[2])
		#		bone.transform(rot, scale=False, roll=True)
		#	bone.tail = t2
		#	c=c+1
		
		#http://www.blender.org/forum/viewtopic.php?t=7214&view=next&sid=91abf6afab7d448a668be39d001f5c26
		#for bone in arm.edit_bones:
		#	objectmat = bone.matrix #globalspace
		#	if bone.parent != None:
		#		parentmat = bone.parent.matrix #globalspace
		#		parentmatIn = bone.parent.matrix.copy()
		#		parentmatIn.invert()
		#		mat = objectmat * parentmatIn 
		#	else:
		#		mat = objectmat
		#	#mat is now localspace
		#	bone.transform(mat, scale=False, roll=False)
			
		#c=0
		#for j in joints:
		#	bone = arm.edit_bones[j._name]
		#	#bone.transform(j._transform.getMatrix(), scale=True, roll=True)
		#	mat = j._transform.getMatrix()
		#	(pos, rot, scale) = mat.decompose()
		#	
		#	rot = rot.to_matrix()
		#	
		#	if c != 0:
		#		bone.head = bone.parent.head+Vector(pos) * bone.parent.matrix
		#		tempM = rot.to_4x4()*bone.parent.matrix
		#		bone.transform(tempM, scale=False, roll=True)
		#	else:
		#		bone.head = Vector(pos)
		#		bone.transform(rot, scale=False, roll=True)
		#	c=c+1
		
		#for j in joints:
		#	mat = j._transform.getMatrix()
		#	(pos, rot, scale) = mat.decompose()
		#	bone = arm.edit_bones[j._name]
		#	bone.head = pos
		
		#c=0
		#for j in joints:
		#	mat = j._transform.getMatrix()
		#	bone = arm.edit_bones[j._name]
		#	#bone.roll = self.getRollFromMatrix(mat)
		#	#bone.transform(mat)
			
		#	pos = mat[4:7]
		#	rot = mat[0:4]
		#	qx,qy,qz,qw = rot[0],rot[1],rot[2],rot[3]
			
			#bone.transform(matrix)
			

		#	if bone.parent != None:
		#		bone.head = parent.tail
		#	else:
		#	#	# calc root bone transform
		#		bone.head = (0,0,0)
		#		rot = Matrix.Translation((0,0,0))
		#		Vector(pos)
		#	bone.tail = rot * pos + bone.head
		#	c=c+1
		
		bpy.context.scene.update()
		
		# Vertex group for every bone
		#for bone in arm.bones:
		#	vertgroup = obj.vertex_groups.new(name=bone.name)
	
		bpy.ops.object.mode_set(mode='OBJECT')
	
	def getRollFromMatrix(self,mat):
		newmat = mat.to_3x3()
		quat = newmat.to_quaternion()
		if abs(quat.w) < 1e-4:
			roll = pi
		else:
			roll = 2*atan(quat.y/quat.w)
		return roll
			
	def skinMesh(ob, rig):
		# List of vertex groups, in the form (vertex, weight)
		vgroups = {}
		vgroups['Base'] = [
			(0, 1.0), (1, 1.0), (2, 1.0), (3, 1.0),
			(4, 0.5), (5, 0.5), (6, 0.5), (7, 0.5)]
		vgroups['Mid'] = [
			(4, 0.5), (5, 0.5), (6, 0.5), (7, 0.5),
			(8, 1.0), (9, 1.0), (10, 1.0), (11, 1.0)]
		vgroups['Tip'] = [(12, 1.0), (13, 1.0), (14, 1.0), (15, 1.0)]
	 
		# Create vertex groups, and add verts and weights
		# First arg in assignment is a list, can assign several verts at once
		for name, vgroup in vgroups.items():
			grp = ob.vertex_groups.new(name)
			for (v, w) in vgroup:
				grp.add([v], w, 'REPLACE')
	 
		# Give mesh object an armature modifier, using vertex groups but
		# not envelopes
		mod = ob.modifiers.new('MyRigModif', 'ARMATURE')
		mod.object = rig
		mod.use_bone_envelopes = False
		mod.use_vertex_groups = True
		
	def createRig(self, name, origin, boneTable):
		# Create armature and object
		bpy.ops.object.add(
			type='ARMATURE', 
			enter_editmode=True,
			location=origin)
		ob = bpy.context.object
		ob.show_x_ray = True
		ob.name = name
		amt = ob.data
		amt.name = name+'Amt'
		amt.show_axes = True
	 
		# Create bones
		bpy.ops.object.mode_set(mode='EDIT')
		for (bname, pname, vector, matrix) in boneTable:        
			bone = amt.edit_bones.new(bname)
			
			if pname:
				parent = amt.edit_bones[pname]
				bone.parent = parent
				bone.head = parent.tail
				bone.use_connect = False
				(trans, rot, scale) = parent.matrix.decompose()
				
				#convert parent from global to local
				mW = parent.matrix #armature space
				imW = mW.copy() #copy 
				imW.invert() #create inverted
				m1 = mW * imW
				(trans, rot, scale) = m1.decompose()
			else:
				bone.head = (0,0,0)
				rot = Matrix.Translation((0,0,0))	# identity matrix
			bone.tail = rot * Vector(vector) + bone.head
		bpy.ops.object.mode_set(mode='OBJECT')
		return ob

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
		self._optmask = ""
		self._mskindex = 0
				
	def read(self,file,mask,mskindex):
		print("read A3D2Object")
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]

		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		print(self._name)
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		#transform
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
				
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		
		#bbid, id, indexbufid
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack(">Q",self._id))
		#string
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#parentid
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		#transform
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#visible
		file.write(pack("B",self._visible))

# anim/rigging
		
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
		
	def read(self,file,mask,mskindex):
		print("read A3D2AnimationClip")
		self._id = unpack(">L", file.read(calcsize(">L")))[0]
		self._loop = unpack("B", file.read(calcsize("B")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			arr = A3DArray()
			arr.read(file)
			self._objectIDs = []
			for x in range(arr.length):
				self._objectIDs.append(unpack(">Q", file.read(calcsize(">Q")))[0])
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		for x in range(arr.length):
			self._tracks.append(unpack(">L", file.read(calcsize(">L")))[0])		
		
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
		
	def read(self,file,mask,mskindex):
		print("read A3D2Track")
		self._id = unpack(">L", file.read(calcsize(">L")))[0]
		
		arr = A3DArray()
		arr.read(file)
		print(str(arr.length)+" x keyframes")
		if arr.length > 0:
			for a in range(arr.length):
				a3dkeyf = A3D2Keyframe(self.Config)
				self._keyframes.append(a3dkeyf.read(file,mask,mskindex + self._mskindex))
				self._mskindex = self._mskindex + a3dkeyf._mskindex
		
		a3dstr = A3DString()
		a3dstr.read(file)
		self._objectName = a3dstr.name
		
		print(self._objectName)
		
	def write(self,file):
		print("write")

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
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("Q",self._id))
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack("B",self._visible))

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
		
	def read(self,file,mask,mskindex):
		print("read A3D2JointBindTransform")
		a3dtran = A3DTransform(self.Config)
		a3dtran.read(file)
		self._bindPoseTransform = a3dtran
		self._id = unpack("Q", file.read(calcsize("Q")))[0]
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
		
	def read(self,file,mask,mskindex):
		#print("read A3D2Keyframe")
		self._time = unpack(">f",file.read(calcsize(">f")))[0]
		a3dtran = A3DTransform(self.Config)
		a3dtran.read(file)
		return self
		
	def write(self,file):
		print("write")

# Buffers
		
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
				
	def read(self,file,mask,mskindex):
		print("read A3D2IndexBuffer")
		arr = A3DArray()
		arr.read(file)
		for a in range(int(arr.length/2)):
			self._byteBuffer.append( unpack("<H",file.read(calcsize("<H")))[0] )
		self._id = unpack('>L',file.read(calcsize(">L")))[0]
		self._indexCount = unpack('>L',file.read(calcsize(">L")))[0]
		
	def write(self,file):
		arr = A3DArray()
		# multiply by 2 because its length of bytes and we are using 2 bytes
		vbuflen = int(len(self._byteBuffer) * 2)
		#vbuflen = len(self._byteBuffer) 
		#vbuflen = int((len(self._byteBuffer) * 3) * 2)
		arr.write(file,vbuflen) 
		for x in range(len(self._byteBuffer)):
			#each index uses 2 bytes (little-endian)
			file.write(pack('<H',self._byteBuffer[x]))
		#write id
		file.write(pack('>L',self._id))
		#write indexcount
		file.write(pack('>L',self._indexCount))
		#print("ibuf_indexCount="+str(self._indexCount))
		#print("ibuf_byteBufferlength="+str(vbuflen))

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
				
	def read(self,file,mask,mskindex):
		print("read A3D2VertexBuffer")
		arr = A3DArray()
		arr.read(file)
		self._attributes = []
		for a in range(arr.length):
			self._attributes.append(unpack(">L",file.read(calcsize(">L")))[0])
		arr = A3DArray()
		arr.read(file)
		if self.Config.A3DVersionSystem == "1":
			#2.6
			for a in range(int(arr.length/2)):
				h = unpack(">H",file.read(calcsize(">H")))[0]
				fcomp = Float16Compressor()
				x = fcomp.decompress(h)
				str = pack('I',x)
				hf = unpack('f',str)[0]
				self._byteBuffer.append(hf)
		else:
			for a in range(int(arr.length/4)):
				self._byteBuffer.append(unpack("<f",file.read(calcsize("<f")))[0])
		self._id  = unpack(">L",file.read(calcsize(">L")))[0]
		self._vertexCount  = unpack(">H",file.read(calcsize(">H")))[0]
		
	def write(self,file):
		#print("write vertexbuffer")
		#attributes
		arr = A3DArray()
		arr.write(file,len(self._attributes))
		for x in range(len(self._attributes)):
			file.write(pack(">L",self._attributes[x]))
		arr = A3DArray()
		bybufsize = int(len(self._byteBuffer)*4)

		#if version 2.6 then compressed vertex buffer
		if self.Config.A3DVersionSystem == 1:
			#2.6
			arr.write(file,int(bybufsize/2)) #half it because we storing shorts now
			for float32 in self._byteBuffer:
				fcomp = Float16Compressor()
				f16 = fcomp.compress(float32)
				file.write(pack(">H",f16))
		else:
			arr.write(file,bybufsize) 
			for byte in self._byteBuffer:
				file.write(pack("<f",byte))
		file.write(pack(">L",self._id))
		file.write(pack(">H",self._vertexCount))

# Other
	
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
				
	def read(self,file,mask,mskindex):
		print("read A3D2Box")
		arr = A3DArray()
		arr.read(file)
		for a in range(arr.length):
			self._box.append( unpack(">f",file.read(calcsize(">f")))[0] )
		self._id = unpack('>L',file.read(calcsize(">L")))[0]
		
	def write(self,file):
		#print("write boundbox\n")
		arr = A3DArray()
		arr.write(file,len(self._box))
		for x in range(len(self._box)):
			file.write(pack('>f',self._box[x]))
		file.write(pack('>L',self._id))		

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
		self._optmask = ""
		self._mskindex = 0	
		
	def read(self,file,mask,mskindex):
		print("read A3D2CubeMap")
		if mask[mskindex + self._mskindex] == "0":
			self._backId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":	
			self._bottomId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">L",file.read(calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._frontId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		#id
		self._id = unpack(">L",file.read(calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._leftId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._rightId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._topId = unpack(">L",file.read(calcsize(">L")))[0]
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
		self._optmask = ""
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Decal")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack("Q", file.read(calcsize("Q")))[0]
		self._indexBufferId = unpack(">L", file.read(calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._offset = unpack(">f", file.read(calcsize(">f")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack("Q", file.read(calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		for a in range(arr.length):
			a3dsurf = A3D2Surface(self.Config)
			self._surfaces.append(a3dsurf.read(file,mask,mskindex + self._mskindex))
			self._mskindex = self._mskindex + a3dsurf._mskindex
			
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		self._vertexBuffers = []
		for a in range(arr.length):
			self._vertexBuffers.append(unpack(">L", file.read(calcsize(">L")))[0])
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		print("write")

	def render():
		print('render decal')
		
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
		self._optmask = ""
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Image")
		self._id = unpack(">L", file.read(calcsize(">L")))[0]
		a3dstr = A3DString()
		a3dstr.read(file)
		self._url = a3dstr.name
		
	def write(self,file):
		file.write(pack(">L",self._id))
		self._url.write(file)
		
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
		self._optmask = ""
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Map")
		self._channel = unpack(">H", file.read(calcsize(">H")))[0]
		self._id = unpack(">L", file.read(calcsize(">L")))[0]
		self._imageId = unpack(">L", file.read(calcsize(">L")))[0]
		
	def write(self,file):
		file.write(pack(">H",self._channel))
		file.write(pack(">L",self._id))
		file.write(pack(">L",self._imageId))

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
		self._optmask = ""
		self._mskindex = 0
	
	def read(self,file,mask,mskindex):
		print("read A3D2Material")
				
		if mask[mskindex + self._mskindex] == "0":
			self._diffuseMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":	
			self._glossinessMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._id = unpack(">L",file.read(calcsize(">L")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._lightMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._normalMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._opacityMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			self._reflectionCubeMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
			
		if mask[mskindex + self._mskindex] == "0":
			self._specularMapId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
	def write(self,file):
		if self._diffuseMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._diffuseMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._glossinessMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._glossinessMapId))
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(pack(">L",self._id))
		
		if self._lightMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._lightMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._normalMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._normalMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._opacityMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._opacityMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._reflectionCubeMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._reflectionCubeMapId))
		else:
			self._optmask = self._optmask + str(1)
		if self._specularMapId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._specularMapId))
		else:
			self._optmask = self._optmask + str(1)

class A3D2Sprite:
	def __init__(self,Config):
		self._alwaysOnTop = 0
		self._boundBoxId = None
		self._height = 100
		self._id = 0
		self._materialId = None
		self._name = None
		self._originX = 0.5
		self._originY = 0.5
		self._parentId = None
		self._perspectiveScale = 1
		self._rotation = 0
		self._transform = None
		self._visible = 1
		self._width = 100
		
		self._optionals = [self._boundBoxId,self._name,self._parentId,self._transform]
		self._optmask = ""
		self.Config = Config
		self._mskindex = 0
	
	def reset(self):
		self._alwaysOnTop = 0
		self._boundBoxId = None
		self._height = 100
		self._id = 0
		self._materialId = None
		self._name = None
		self._originX = 0.5
		self._originY = 0.5
		self._parentId = None
		self._perspectiveScale = 1
		self._rotation = 0
		self._transform = None
		self._visible = 1
		self._width = 100
		self._optmask = ""
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Sprite")

		self._alwaysOnTop = unpack("B", file.read(calcsize("B")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._height = unpack(">f", file.read(calcsize(">f")))[0]
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._materialId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		self._originX = unpack(">f", file.read(calcsize(">f")))[0]
		self._originY = unpack(">f", file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		self._perspectiveScale = unpack("B", file.read(calcsize("B")))[0]
		self._rotation = unpack(">f", file.read(calcsize(">f")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		self._width = unpack(">f", file.read(calcsize(">f")))[0]
	
	def write(self,file):
		file.write(pack("B",self._alwaysOnTop))
		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(pack(">f",self._height))
		file.write(pack("Q",self._id))
		
		if self._materialId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._materialId))
		else:
			self._optmask = self._optmask + str(1)
		
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)

		file.write(pack(">f",self._originX))
		file.write(pack(">f",self._originY))
			
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(pack("B",self._perspectiveScale))
		file.write(pack(">f",self._rotation))
		
		#transform
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(pack("B",self._visible))
		file.write(pack(">f",self._width))
	
	def render(self,materials,maps,images):
		coords=[ (1, 1, 0), (1, -1, 0), (-1, -0.9999998, 0), (-0.9999997, 1, 0) ]
		faces=[ (0, 3, 2, 1) ]
		
		me = bpy.data.meshes.new("A3DSprite3D") 
		ob = bpy.data.objects.new("A3DSprite3D", me)  
		
		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			ob.matrix_local = self._transform.getMatrix()
		else:
			ob.location = bpy.context.scene.cursor_location
			
		ob.rotation_euler = (1.57079633,0,1) 
		bpy.context.scene.objects.link(ob)  
		
		ob["a3dtype"] = "A3DSprite3D"

		me.from_pydata(coords,[],faces)
		me.update(calc_edges=True)
		
		mat = materials[self._materialId]
		
		surf_mat = bpy.data.materials.new("SpriteMaterial")
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
			#mtex.uv_layer = uvname
			
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
			#mtex.uv_layer = uvname
			
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
			#mtex.uv_layer = uvname
			
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
			#mtex.uv_layer = uvname
			
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
			#mtex.uv_layer = uvname
			
		if (mat._reflectionCubeMapId is not None) and (mat._reflectionCubeMapId != int("0xFFFFFFFF",16)):
			#get map
			map = maps[mat._reflectionCubeMapId]
			#get img
			img = images[map._imageId]
			
			#new image
			texture = bpy.data.textures.new("reflection", type='IMAGE')
			DIR = os.path.dirname(self.Config.FilePath)
			image = load_image(img._url, DIR)
			texture.image = image
		
			#new texture
			mtex = surf_mat.texture_slots.add()
			mtex.texture = texture
			mtex.texture_coords = 'UV'
			mtex.use_map_color_diffuse = False
			#mtex.uv_layer = uvname
			
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
			#mtex.uv_layer = uvname
	
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
		self._optmask = ""
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2Camera")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		self._farClipping = unpack(">f", file.read(calcsize(">f")))[0]
		self._fov = unpack(">f", file.read(calcsize(">f")))[0]
		self._id = unpack("Q", file.read(calcsize("Q")))[0]

		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		self._nearClipping = unpack(">f", file.read(calcsize(">f")))[0]
		self._orthographic = unpack("B", file.read(calcsize("B")))[0]
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack("Q", file.read(calcsize("Q")))[0]
		self._mskindex = self._mskindex + 1
		
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]
		
	def write(self,file):
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(pack(">f",self._farClipping))
		file.write(pack(">f",self._fov))
		file.write(pack("Q",self._id))
		
		#string
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
			
		file.write(pack(">f",self._nearClipping))
		file.write(pack("B",self._orthographic))
			
		#parentid
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack("Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		#transform
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		#visible
		file.write(pack("B",self._visible))
	
	def render(self):
		data = bpy.data.cameras.new(self._name)
		cam = bpy.data.objects.new(self._name, data)
		
		cam.matrix_local = self._transform.getMatrix()
		
		data.lens = self._fov
		data.shift_x = 0.0
		data.shift_y = 0.0
		data.dof_distance = 0.0
		data.clip_start = self._nearClipping
		data.clip_end = self._farClipping
		data.draw_size = 0.5
		if self._orthographic == True:
			data.type = 'ORTHO'
		else:
			data.type = 'PERSP'
		bpy.context.scene.objects.link(cam)
		
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
		self._optmask = ""
		self._mskindex = 0
		
	def read(self,file,mask,mskindex):
		print("read A3D2LOD")
		if mask[mskindex + self._mskindex] == "0":
			self._boundBoxId = unpack(">L", file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		for a in range(arr.length):
			self._distances.append(unpack(">f",file.read(calcsize(">f")))[0])
			
		self._id = unpack(">Q", file.read(calcsize(">Q")))[0]
			
		if mask[mskindex + self._mskindex] == "0":
			a3dstr = A3DString()
			a3dstr.read(file)
			self._name = a3dstr.name
		self._mskindex = self._mskindex + 1
		
		arr = A3DArray()
		arr.read(file)
		for a in range(arr.length):
			self._objects.append(unpack(">Q",file.read(calcsize(">Q")))[0])
		
		if mask[mskindex + self._mskindex] == "0":
			self._parentId = unpack(">Q", file.read(calcsize(">Q")))[0]
		self._mskindex = self._mskindex + 1
		
		#transform
		if mask[mskindex + self._mskindex] == "0":
			a3dtran = A3DTransform(self.Config)
			a3dtran.read(file)
			self._transform = a3dtran
		self._mskindex = self._mskindex + 1
		
		self._visible = unpack("B", file.read(calcsize("B")))[0]		
		
	def write(self,file):
		print("write LOD")
		
		print(self._boundBoxId)		
		if self._boundBoxId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._boundBoxId))
		else:
			self._optmask = self._optmask + str(1)
		
		print("distances")
		print(self._distances)
		#distances
		arr = A3DArray()
		arr.write(file,len(self._distances))
		for distance in self._distances:
			file.write(pack(">f",distance)) #8byte float
		
		file.write(pack(">Q",self._id))
		
		#string
		if self._name is not None:
			self._optmask = self._optmask + str(0)
			self._name.write(file)
		else:
			self._optmask = self._optmask + str(1)
				
		#objects
		print("objects")
		print(self._objects)
		arr = A3DArray()
		arr.write(file,len(self._objects))
		for obid in self._objects:
			file.write(pack(">Q",obid))
		
		#parentid
		if self._parentId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">Q",self._parentId))
		else:
			self._optmask = self._optmask + str(1)
		
		#transform
		if self._transform is not None:
			self._optmask = self._optmask + str(0)
			self._transform.write(file)
		else:
			self._optmask = self._optmask + str(1)
		
		file.write(pack("B",self._visible))
		
	def render(self,meshes):
		bpy.ops.object.add(type='EMPTY')
		empty = bpy.context.object
		
		empty.name = "A3DLOD"	

		#set draw type
		empty.empty_draw_type = 'CUBE'

		# give custom property type
		empty["a3dtype"] = "A3DLOD"
		
		# position object at 3d-cursor
		if (self._transform is not None) and (self.Config.ApplyTransforms == True):
			empty.matrix_local = self._transform.getMatrix()
		else:
			empty.location = bpy.context.scene.cursor_location
			
		for x in range(len(self._objects)):
			obj = bpy.data.objects[meshes[self._objects[x]]._name]
			obj.parent = empty
			obj['a3ddistance'] = self._distances[x]
		
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
		self._optmask = ""
		self._mskindex = 0
			
	def read(self,file,mask,mskindex):
		print("read A3D2Surface")
		self._indexBegin = unpack(">L",file.read(calcsize(">L")))[0]
		if mask[mskindex + self._mskindex] == "0":
			self._materialId = unpack(">L",file.read(calcsize(">L")))[0]
		self._mskindex = self._mskindex + 1
		self._numTriangles = unpack(">L",file.read(calcsize(">L")))[0]
		return self
		
	def write(self,file):
		file.write(pack(">L",self._indexBegin))
		if self._materialId is not None:
			self._optmask = self._optmask + str(0)
			file.write(pack(">L",self._materialId))
		else:
			self._optmask = self._optmask + str(1)
		file.write(pack(">L",self._numTriangles))
		#print("surf_numTriangles="+str(self._numTriangles))

		
#==================================
# CUSTOM MESHES/MENUS
#==================================

class A3d_submenu(bpy.types.Menu):
	bl_idname = "A3d_submenu"
	bl_label = "Alternativa3D"

	def draw(self, context):
		layout = self.layout
		layout.operator_context = 'INVOKE_REGION_WIN'
		layout.operator("a3dobj.a3d_sprite3d", text="Sprite3D", icon='MESH_PLANE')
		layout.operator("a3dobj.a3d_lod", text="LOD", icon='MESH_CUBE')
		layout.operator("a3dobj.a3d_skybox", text="Skybox", icon='MESH_CUBE')
		layout.operator("a3dobj.a3d_ambientlight", text="AmbientLight", icon='OUTLINER_OB_LAMP')
		layout.operator("a3dobj.a3d_directionallight", text="DirectionalLight", icon='OUTLINER_OB_LAMP')
		layout.operator("a3dobj.a3d_omnilight", text="OmniLight", icon='OUTLINER_OB_LAMP')
		layout.operator("a3dobj.a3d_spotlight", text="SpotLight", icon='OUTLINER_OB_LAMP')
		layout.separator()
		layout.operator(LODSettings.bl_idname, text="Add Mesh To LOD", icon='MESH_CUBE')

class AddSprite3D(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_sprite3d"
	bl_label = "Add Sprite3D"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		coords=[ (1, 1, 0), (1, -1, 0), (-1, -0.9999998, 0), (-0.9999997, 1, 0) ]
		faces=[ (0, 3, 2, 1) ]
		
		me = bpy.data.meshes.new("A3DSprite3D") 
		ob = bpy.data.objects.new("A3DSprite3D", me)  
		
		ob.location = bpy.context.scene.cursor_location   
		ob.rotation_euler = (1.57079633,0,1) 
		bpy.context.scene.objects.link(ob)  
		
		ob["a3dtype"] = "A3DSprite3D"
		ob["a3dalwaysOnTop"] = True
		ob["a3dheight"] = "0"
		ob["a3dwidth"] = "0"
		ob["a3doriginX"] = "0"
		ob["a3doriginY"] = "0"
		ob["a3dperspectiveScale"] = "0"

		me.from_pydata(coords,[],faces)
		me.update(calc_edges=True)

		mat = bpy.data.materials.new("SpriteMaterial")
		me.materials.append(mat)
		texture = bpy.data.textures.new("diffuse", type='IMAGE')
		mtex = mat.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture
		return {'FINISHED'}

class AddLOD(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_lod"
	bl_label = "Add LOD"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		bpy.ops.object.add(type='EMPTY')
		empty = bpy.context.object
		
		empty.name = "A3DLOD"	

		#set draw type
		empty.empty_draw_type = 'CUBE'

		# give custom property type
		empty["a3dtype"] = "A3DLOD"
		
		# position object at 3d-cursor
		empty.location = bpy.context.scene.cursor_location   
				
		return {'FINISHED'}	

class AddSkybox(bpy.types.Operator):
	bl_idname = "a3dobj.a3d_skybox"
	bl_label = "Add Skybox"
	bl_options = {'REGISTER', 'UNDO'}
		
	def execute(self, context):
		# Define the coordinates of the vertices. Each vertex is defined by 3 consecutive floats.
		coords=[(1.000000,1.000000,-1.000000),(1.000000,-1.000000,-1.000000),(-1.000000,-1.000000,-1.000000),(-1.000000,1.000000,-1.000000),(1.000000,1.000000,1.000000),(0.999999,-1.000001,1.000000),(-1.000000,-1.000000,1.000000),(-1.000000,1.000000,1.000000)]
		faces=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(4,7,3,0)]
		uvs=[(0.003059,0.000000),(1.000000,0.003059),(0.996942,1.000000),(0.000000,0.996941),(0.000000,0.003058),(0.996942,0.000000),(1.000000,0.996942),(0.003058,1.000000),(0.003058,0.000000),(1.000000,0.003059),(0.996942,1.000000),(0.000000,0.996942),(0.000000,0.003058),(0.996942,0.000000),(1.000000,0.996942),(0.003059,1.000000),(0.000000,0.003058),(0.996942,0.000000),(1.000000,0.996942),(0.003058,1.000000),(1.000000,0.996941),(0.003058,1.000000),(0.000000,0.003058),(0.996941,0.000000)]
		
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
		
		#set uvs
		if len(uvs) > 0:
			uvlayer = me.uv_textures.new()
			uv_faces = me.uv_layers[0].data
			x=0
			for vert in uv_faces:
				vert.uv = uvs[x]
				x=x+1
		
		# flip the normals as we want it inside the cube not outside
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		#bpy.ops.mesh.flip_normals()
		bpy.ops.mesh.normals_make_consistent(inside=True)
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		#bpy.ops.object.select_all(action='DESELECT')
		
		#add materials for each face
		slot = bpy.ops.object.material_slot_add()
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		for face in me.polygons:
			face.select=False
		me.polygons[0].select=True
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.object.material_slot_assign()
		#Assign a material to the last slot 
		matbottom = bpy.data.materials.new("Bottom")
		matbottom.use_shadeless = True
		ob.material_slots[ob.material_slots.__len__() - 1].material = matbottom
		#slot.material = matbottom
		#me.materials.append(matbottom)
		#new texture
		texture = bpy.data.textures.new("Bottom", type='IMAGE')
		mtex = matbottom.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture
		
		
		slot = bpy.ops.object.material_slot_add()
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		for face in me.polygons:
			face.select=False
		me.polygons[1].select=True
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.object.material_slot_assign()
		mattop = bpy.data.materials.new("Top")
		mattop.use_shadeless = True
		ob.material_slots[ob.material_slots.__len__() - 1].material = mattop
		#me.materials.append(mattop)
		texture = bpy.data.textures.new("Top", type='IMAGE')
		mtex = mattop.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture

		slot = bpy.ops.object.material_slot_add()
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		for face in me.polygons:
			face.select=False
		me.polygons[2].select=True
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.object.material_slot_assign()
		matback = bpy.data.materials.new("Back")
		matback.use_shadeless = True
		ob.material_slots[ob.material_slots.__len__() - 1].material =  matback
		#me.materials.append(matback)
		texture = bpy.data.textures.new("Back", type='IMAGE')
		mtex = matback.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture

		slot = bpy.ops.object.material_slot_add()
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		for face in me.polygons:
			face.select=False
		me.polygons[3].select=True
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.object.material_slot_assign()
		matleft = bpy.data.materials.new("Left")
		matleft.use_shadeless = True
		ob.material_slots[ob.material_slots.__len__() - 1].material = matleft
		#me.materials.append(matleft)
		texture = bpy.data.textures.new("Left", type='IMAGE')
		mtex = matleft.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture
		
		slot = bpy.ops.object.material_slot_add()
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		for face in me.polygons:
			face.select=False
		me.polygons[4].select=True
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.object.material_slot_assign()
		matfront = bpy.data.materials.new("Front")
		matfront.use_shadeless = True
		ob.material_slots[ob.material_slots.__len__() - 1].material = matfront
		#me.materials.append(matfront)
		texture = bpy.data.textures.new("Front", type='IMAGE')
		mtex = matfront.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture

		slot = bpy.ops.object.material_slot_add()
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		for face in me.polygons:
			face.select=False
		me.polygons[5].select=True
		bpy.ops.object.mode_set(mode = 'EDIT')
		bpy.ops.object.material_slot_assign()
		matright = bpy.data.materials.new("Right")
		matright.use_shadeless = True
		ob.material_slots[ob.material_slots.__len__() - 1].material = matright
		#me.materials.append(matright)
		texture = bpy.data.textures.new("Right", type='IMAGE')
		mtex = matright.texture_slots.add()
		mtex.texture_coords = 'UV'
		mtex.use_map_color_diffuse = True
		mtex.texture = texture
		
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.object.mode_set(mode = 'OBJECT')
		
		#add texture to each material
		#set mapping to uv coords
		
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
	
		ob["a3dtype"] = "A3DAmbientLight"		
		
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
	
		ob["a3dtype"] = "A3DDirectionalLight"		
		
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
	
		ob["a3dtype"] = "A3DOmniLight"		
		
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
	
		ob["a3dtype"] = "A3DSpotLight"		
		
		bpy.context.scene.objects.active = ob
		return {'FINISHED'}

#==================================
# CUSTOM PANELS/OPERATORS
#==================================

def addlodchild(objs,distance):
	mesh = objs[0]
	lodcont = objs[1]
	
	#set parent to lodcontainer
	mesh.parent = lodcont
	
	#select lodcontainer
	mesh.select = False
	lodcont.select = True
	
	#snap, cursor to active
	bpy.ops.view3d.snap_cursor_to_active()
	
	#select lodobj
	mesh.select = True
	lodcont.select = False
	
	mesh['a3ddistance'] = distance
	
	#origin to 3d cursor
	bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
	#geometry to origin
	bpy.ops.object.origin_set()
	
	#select just lodcontainer
	mesh.select = False
	lodcont.select = True
	
class LODSettings(bpy.types.Operator):
	bl_idname = 'mesh.lod_settings'
	bl_label = 'Add Mesh A3D2LOD Child'
	bl_options = {'REGISTER', 'UNDO'}

	distance = bpy.props.IntProperty(name='Distance', default=300)

	@classmethod
	def poll(cls, context):
		#obj = context.active_object
		objs = [obj for obj in bpy.context.selected_objects]
		if len(objs) == 2:
			#if objs[1]["a3dtype"] == "A3DLOD":
			#	return True
			#else:
			#	print("Second selected obj was not the lod container..")
			#	return False
			return True
		else:
			return False

	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)

	def execute(self, context):
		objs = [obj for obj in bpy.context.selected_objects]
		addlodchild(objs,self.distance)
		#obj = context.active_object
		#mesh = obj.data
		#self.distance
		return {'FINISHED'}
		
class alternativa3DPanel(bpy.types.Panel):
	bl_label = "Alternativa3D Properties"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_default_closed = False
 
	def draw(self, context):
		l = self.layout
		obj = bpy.context.active_object
		
		#add a button for addchild child lod?
		
		if obj != None:
			if "a3dtype" in obj:
				
				l.prop(obj, '["a3dtype"]')
			
				if obj["a3dtype"] == "A3DLOD":
					box = l.box()
					columns = box.column()
					header = columns.split(0.6)
					header.label(text="Object")
					header.label(text="Distance")
					
					for child in obj.children:
						row = columns.split(0.6)
						row.label(child.name)
						row.prop(child,'["a3ddistance"]')
						row.enabled = True
				elif obj["a3dtype"] == "A3DSprite3D":
					print("spriteprops")
					box = l.box()
					columns = box.column()
					header = columns.split(0.6)
					header.label(text="Property")
					header.label(text="Value")
					
					row = columns.split(0.6)
					row.label("alwaysOnTop")
					row.prop(obj,'["a3dalwaysOnTop"]')
					row.enabled = True
					
					row = columns.split(0.6)
					row.label("width")
					row.prop(obj,'["a3dwidth"]')
					row.enabled = True
					
					row = columns.split(0.6)
					row.label("height")
					row.prop(obj,'["a3dheight"]')
					row.enabled = True					
					
					row = columns.split(0.6)
					row.label("originX")
					row.prop(obj,'["a3doriginX"]')
					row.enabled = True
					
					row = columns.split(0.6)
					row.label("originY")
					row.prop(obj,'["a3doriginY"]')
					row.enabled = True
					
					row = columns.split(0.6)
					row.label("perspectiveScale")
					row.prop(obj,'["a3dperspectiveScale"]')
					row.enabled = True
					
			if obj.parent != None:
				parentobj = obj.parent
				if "a3dtype" in parentobj:
					if parentobj["a3dtype"] == "A3DLOD":
						l.prop(obj, '["a3ddistance"]')
 		
#==================================
# REGISTRATION
#==================================

def menu_func2(self, context):
	self.layout.operator(LODSettings.bl_idname, text='Add Mesh A3D2LOD Child')
	
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
	bpy.types.VIEW3D_MT_object_specials.append(menu_func2)
	
def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_file_import.remove(menu_func_import)
	bpy.types.INFO_MT_file_export.remove(menu_func_export)
	bpy.types.INFO_MT_mesh_add.remove(menu_func)
	bpy.types.VIEW3D_MT_object_specials.remove(menu_func2)	

	
if __name__ == '__main__':
	register()