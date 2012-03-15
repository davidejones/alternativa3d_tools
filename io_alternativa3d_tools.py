bl_info = {
	'name': 'Export: Alternativa3d Tools',
	'author': 'David E Jones, http://davidejones.com',
	'version': (1, 0, 8),
	'blender': (2, 5, 7),
	'location': 'File > Import/Export;',
	'description': 'Importer and exporter for Alternativa3D engine. Supports A3D and Actionscript"',
	'warning': '',
	'wiki_url': '',
	'tracker_url': 'http://davidejones.com',
	'category': 'Import-Export'}

import math, os, time, bpy, random, mathutils, re, ctypes, struct, binascii
from bpy import ops
from bpy.props import *


#==================================
# EXPORTER - Actionscript (.as)
#==================================

#Container for the exporter settings
class ASExporterSettings:
	def __init__(self,A3DVersionSystem=1,CompilerOption=1,ExportMode=1,DocClass=False):
		self.A3DVersionSystem = int(A3DVersionSystem)
		self.CompilerOption = int(CompilerOption)
		self.ExportMode = int(ExportMode)
		self.DocClass = bool(DocClass)

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
	elif Config.A3DVersionSystem == 5:
		# version 7.8.0
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	elif Config.A3DVersionSystem == 6:
		# version 8.5.0
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.materials.TextureMaterial;\n")
		file.write("\timport alternativa.engine3d.core.Vertex;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	else:
		# version 8.8.0
		file.write("\timport alternativa.engine3d.core.VertexAttributes;\n")
		file.write("\timport alternativa.engine3d.materials.FillMaterial;\n")
		file.write("\timport alternativa.engine3d.objects.Mesh;\n")
		file.write("\timport alternativa.engine3d.resources.Geometry;\n")
		file.write("\timport __AS3__.vec.Vector;\n")
		file.write("\timport flash.display.Bitmap;\n\n")
	
def WritePackageEnd(file):
	file.write("}")
	
def WriteTexMaterial(file,image,id,Config):
	#base = 'Unknown'
	#if hasattr(image, 'filepath'):
	#	base=os.path.basename(image.filepath)
	#basename, extension = os.path.splitext(base)
	
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
			mati[x] = "material"+str(x)
			#mati[Material.name] = "material"+str(x)
			WriteMaterial(file,"material"+str(x),Config, Material[1])
			x += 1
	return mati
			
def WriteMaterial(file,id,Config,Material=None):
	if Material:
		#print(Material.name)
		Texture = GetMaterialTexture(Material)
		if Texture:
			#print(Texture)
			if Config.A3DVersionSystem == 1:
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(Material.name)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':Texture = new Texture(new bmp'+str(Material.name)+'().bitmapData, "'+str(Material.name)+'");\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(Material.name)+":Bitmap = new Bitmap(new bd"+str(Material.name)+"(0,0));\n")
					file.write('\t\tprivate var '+str(id)+':Texture = new Texture(bmp'+str(Material.name)+'.bitmapData, "'+str(Material.name)+'");\n\n')
			else:
				#if flex
				if Config.CompilerOption == 1:
					file.write('\t\t[Embed(source="'+str(Texture)+'")] private static const bmp'+str(Material.name)+':Class;\n')
					file.write('\t\tprivate static const '+str(id)+':TextureMaterial = new TextureMaterial(new bmp'+str(Material.name)+'().bitmapData, true, true);\n\n')
				else:
					file.write("\t\t//"+str(Texture)+"\n")
					file.write("\t\tprivate var bmp"+str(Material.name)+":Bitmap = new Bitmap(new bd"+str(Material.name)+"(0,0));\n")
					file.write("\t\tprivate var "+str(id)+":TextureMaterial = new TextureMaterial(bmp"+str(Material.name)+".bitmapData, true, true);\n\n")
		else:
			#no tex maybe vertex colour?
			Diffuse = list(Material.diffuse_color)
			Diffuse.append(Material.alpha)
			Specularity = Material.specular_intensity
			Specular = list(Material.specular_color)

			file.write('\t\tprivate var '+id+':FillMaterial = new FillMaterial('+rgb2hex((Diffuse[0], Diffuse[1], Diffuse[2]))+');\n\n')
	
def rgb2hex(rgb):
    #Given a len 3 rgb tuple of 0-1 floats, return the hex string
    return '0x%02x%02x%02x' % tuple([round(val*255) for val in rgb])
	
def GetMaterialTexture(Material):
    if Material:
        #Create a list of Textures that have type "IMAGE"
        ImageTextures = [Material.texture_slots[TextureSlot].texture for TextureSlot in Material.texture_slots.keys() if Material.texture_slots[TextureSlot].texture.type == "IMAGE"]
        #Refine a new list with only image textures that have a file source
        ImageFiles = [os.path.basename(Texture.image.filepath) for Texture in ImageTextures if Texture.image.source == "FILE"]
        if ImageFiles:
            return ImageFiles[0]
    return None
	
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
	file.write("\t\t\t//attributes[5] = VertexAttributes.NORMAL;\n")
	file.write("\t\t\t//attributes[6] = VertexAttributes.NORMAL;\n")
	file.write("\t\t\t//attributes[7] = VertexAttributes.NORMAL;\n")
	file.write("\t\t\t//attributes[8] = VertexAttributes.TANGENT4;\n")
	file.write("\t\t\t//attributes[9] = VertexAttributes.TANGENT4;\n")
	file.write("\t\t\t//attributes[10] = VertexAttributes.TANGENT4;\n")
	file.write("\t\t\t//attributes[11] = VertexAttributes.TANGENT4;\n\n")
	
	file.write("\t\t\tvar g:Geometry = new Geometry();\n")
	file.write("\t\t\tg.addVertexStream(attributes);\n")
	file.write("\t\t\tg.numVertices = "+str(numVertices)+";\n\n")
				
	# verts
	file.write("\t\t\tvar vertices:Array = [\n")
	vl =0
	for v in mesh.vertices:
		if vl != len(mesh.vertices)-1:
			file.write("\t\t\t\t%.6f, %.6f, %.6f,\n" % v.co[:])
		else:
			file.write("\t\t\t\t%.6f, %.6f, %.6f\n" % v.co[:])
		vl += 1
	file.write("\t\t\t];\n")
	
	for face in mesh.faces:
		normals.append(face.normal)
		if len(face.vertices) > 0:
			for i in range(len(face.vertices)):
				hasFaceUV = len(mesh.uv_textures) > 0
				if hasFaceUV:
					uv = [mesh.uv_textures.active.data[face.index].uv[i][0], mesh.uv_textures.active.data[face.index].uv[i][1]]
					uv[1] = 1.0 - uv[1]  # should we flip Y? yes, new in Blender 2.5x
					uvt.append(uv)
					
	if len(uvt) > 0:
		file.write("\t\t\tvar uvt:Array = [\n")
		for u in uvt:
			file.write("\t\t\t\t"+u[0][0]+","+u[0][1]+"")
			if i != len(uvt)-1:
				file.write(",\n")
			else:
				file.write("\n")
		file.write("\t\t\t];\n")
	else:
		file.write("\t\t\tvar uvt:Array = new Array();\n")
	
	#write out indices
	mesh_faces = mesh.faces[:]
	ind = 0
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
					file.write("\n")
				ind += 1
			else:
				file.write("\t\t\t\t%i, %i, %i,\n" % (fv[0], fv[1], fv[2]))
				file.write("\t\t\t\t%i, %i, %i" % (fv[0], fv[2], fv[3]))
				#print("%i %i %i -1, " % (fv[0], fv[1], fv[2]))
				#print("%i %i %i -1, " % (fv[0], fv[2], fv[3]))
				if i != len(mesh_faces)-1:
					file.write(",\n")
				else:
					file.write("\n")
				ind += 2
		file.write("\t\t\t];\n")
	else:
		file.write("\t\t\tvar ind:Array = new Array();\n")
	
	if len(normals) > 0:
		file.write("\t\t\tvar normals:Array = [\n")
		for i in range(len(normals)):
			file.write("\t\t\t\t%i, %i, %i" % (normals[i][0],normals[i][1],normals[i][2]))
			if i != len(normals)-1:
				file.write(",\n")
			else:
				file.write("\n")
		file.write("\t\t\t];\n")
	else:
		file.write("\t\t\tvar normals:Array = new Array();\n")
	file.write("\t\t\tvar tangent:Array = new Array();\n\n")
	
	file.write("\t\t\tg.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));\n")
	
	if len(uvt) > 0:
		file.write("\t\t\tg.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")
	else:
		file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));\n")	
		
	if len(normals) > 0:
		file.write("\t\t\t//g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
	else:
		file.write("\t\t\t//g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));\n")
	
	file.write("\t\t\t//g.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));\n")
	file.write("\t\t\tg.indices =  Vector.<uint>(ind);\n\n")
	
	file.write("\t\t\tthis.geometry = g;\n")
	
	file.write("\t\t\tthis.addSurface(new FillMaterial(0xFF0000), 0, "+str(ind)+");\n")
	
	#for x in range(len(mati)):
	#	file.write("\t\t\tthis.addSurface("+mati[x]+", 0, "+str(ind)+");\n")
	

	file.write("\t\t\tthis.calculateBoundBox();\n")
	
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
	else:
		# version 8.8.0
		file.write("\t\t\tvar sbox:SkyBox = new SkyBox();\n")
		file.write('\t\t\tsbox.x = %f; sbox.y = %f; sbox.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	
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
	else:
		# version 8.8.0
		file.write("\t\t\tvar occ:Occluder = new Occluder();\n")
		file.write('\t\t\tocc.x = %f; occ.y = %f; occ.z = %f;\n' % (obj.location[0],obj.location[1],obj.location[2]) )
	
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
	else:
		# version 8.8.0
		file.write("\t\tvar sp3d:Sprite3D = new Sprite3D();\n")
	
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
	aobjs = []
	for obj in objs:
		if "a3dtype" in obj:
			aobjs.append(obj)
		else:
			if Config.A3DVersionSystem == 7:
				WriteClass85(file,obj,Config)
			elif Config.A3DVersionSystem == 6:
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

	#close off package
	WritePackageEnd(file)
	
	#Create document class
	if Config.DocClass:
		WriteDocuClass(file,aobjs,Config)
	
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
	A3DVersions.append(("5", "7.8.0", ""))
	A3DVersions.append(("6", "8.5.0", ""))
	A3DVersions.append(("7", "8.8.0", ""))
	A3DVersionSystem = EnumProperty(name="Alternativa3D", description="Select a version of alternativa3D to export to", items=A3DVersions, default="7")
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
	
	filepath = bpy.props.StringProperty()

	def execute(self, context):
		filePath = self.properties.filepath
		if not filePath.lower().endswith('.as'):
			filePath += '.as'
		try:
			print('Output file : %s' %filePath)
			#file = open(filePath, 'wb')
			file = open(filePath, 'w')
			Config = ASExporterSettings(A3DVersionSystem=self.A3DVersionSystem,CompilerOption=self.CompilerOption,ExportMode=self.ExportMode, DocClass=self.DocClass)
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
			
	#readversion
	ver = A3DVersion(file)
	print('A3D Version %i.%i' %(ver.baseversion,ver.pointversion))
	
	#read a3dbox
	a3dbox = A3DBox(file)
	
	#read a3dgeometry
	a3dgeom = A3DGeometry(file)
	
	#read image
	#a3dimg = A3DImage(file)
	
	#read map
	#a3dmap = A3DMap(file)
	
	#read material
	#a3dmat = A3DMaterial(file)
	
	#read object
	#a3dobj = A3DObject(file)
	
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
# Common Functions/Classes
#==================================

class A3DVersion:
	def __init__(self, file):
		temp_data = file.read(struct.calcsize('H'))
		self.baseversion = int(struct.unpack('>H', temp_data)[0]) 
		temp_data = file.read(struct.calcsize('H'))
		self.pointversion = int(struct.unpack('>H', temp_data)[0])

class A3DBox:
	def __init__(self, file):
		#temp_data = file.read(struct.calcsize('i'))
		#self.id = struct.unpack('i', temp_data)
		#(vector float) [minX, minY, minZ, maxX, maxY, maxZ] 
		#self.box = box
		# ???? skip extra bytes if needed
		#temp_data = ord(file.read(1))
		#tem = temp_data%2
		#if tem != 0:
		#	file.seek(file.tell() + tem)
		#skip unknown
		#file.seek(file.tell() + 39)
		
		#read first byte 84,85,87
		temp_data = ord(file.read(1))
		
		#get units, eg 84 would be 4
		rem = temp_data % 10
		rem += 2
		
		# skip rem length
		file.seek(file.tell() + rem)
				
		#read how many objects
		oblen = ord(file.read(1))
		print('Number of Meshes: %i' %(oblen))
		
		for x in range(oblen):
			#read numfloats usually 6
			fllen = ord(file.read(1))
			
			#read 6 floats
			for i in range(fllen):
				file.seek(file.tell() + 4)			
			
			# skip 3 bytes
			file.seek(file.tell() + 3)
			
			# read obj id
			obid = ord(file.read(1))
			
		# skip 4 bytes
		file.seek(file.tell() + 5)

class A3DGeometry:
	def __init__(self, file):
		#self.id = id
		#self.indexbuffer = ib
		#self.vertexbuffer = vb
		
		# INDEX BUFFER
		#read length of indexes
		#ilen = ord(file.read(1))
		#temp_data = file.read(struct.calcsize('>H'))
		#ilen = int(struct.unpack('>H', temp_data)[0])
		#print('ilen %i' %ilen)
		#fc = int(ilen/2)
		
		#bitmask to get most significant bit
		bm1 = int("10000000", 2)
		#bm1 = int("100000000000", 2)
		
		#8bit integer bitmask
		#bm2 = int("0000111111111111", 2)
		bm2 = int("11110000", 2)
		
		#read first byte
		temp = ord(file.read(1))
		
		intsz1 = bm1 & temp
		print('intsz1 %i' %intsz1)
		
		#if msb is 0 then its 1 byte
		if intsz1 < 128:
			ilen = temp
		else:	
			if intsz1 >= 192:
				xdata = file.read(bc)
				tdat = binascii.hexlify(xdata)
				ilen = int(tdat)
			else:
				#go back a byte
				file.seek(file.tell() - 1)
				
				temp_data = file.read(struct.calcsize('>H'))
				val = int(struct.unpack('>H', temp_data)[0])
				print('val %i' %val)
				#ilen = bm2 & val
				ilen = val - 32768 # 0x8000
		
		print('ilen %i' %ilen)
		fc = int(ilen/2)
		
		#read indexes
		faces = []
		tupl = []
		for i in range(fc):
			temp_data = file.read(struct.calcsize('H'))
			f = int(struct.unpack('H', temp_data)[0])
			tupl.append(f)
			if (i+1)%3 == 0:
				#print('%i,%i,%i' % (tupl[0],tupl[1],tupl[2]))
				faces.append((tupl[0],tupl[1],tupl[2]))	
				tupl = []
		
		self.indexbuffer = faces
		
		#skip 5 bytes, not sure what this is
		file.seek(file.tell() + 5)
		
		#read length of attributes array
		alen = ord(file.read(1))
		
		#read attributes array
		attributes = []
		for x in range(alen):
			t = ord(file.read(1))
			attributes.append(t)
		
		#set to class
		self.attributes = attributes
		
		# VERTEX BUFFER
		#vlen = ord(file.read(1))
		#print('vlen %i' %vlen)
		
		#read first byte of vlen
		temp = ord(file.read(1))
		
		#get int size 0 or 8?
		intsz2 = bm1 & temp
		print('intsz2 %i' %intsz2)
		
		#if msb is 0 then its 1 byte
		if intsz2 < 128:
			vlen = temp
		else:
			#count set bits
			tz = bm2 & temp
			bc = bitCount(tz)
			#print("bc2 %i" %bc)
			
			if tz >= 192:
				xdata = file.read(bc)
				tdat = binascii.hexlify(xdata)
				vlen = int(tdat,16)
			else:
				#go back a byte
				file.seek(file.tell() - 1)
				
				temp_data = file.read(struct.calcsize('>H'))
				val = int(struct.unpack('>H', temp_data)[0])
				print('val %i' %val)
				#ilen = bm2 & val
				vlen = val - 32768
		
		#if bylen has bytes left over then either skip them or read them as part of bytelength
		#rem = vlen%2
		#if rem != 0:
			#file.seek(file.tell() + rem)
			#rembyte = ord(file.read(1))
			#vlen = vlen + rembyte
			#vlen = vlen * 2
			#vlen = vlen - 10
		
		#how many floats in the length of bytes
		flts = int(vlen/4)
		flcount = 0
		
		for a in range(len(attributes)):
			if attributes[a] == 0:
				#POSITION
				flcount += 3
			elif attributes[a] == 1:
				#NORMAL
				flcount += 3	
			elif attributes[a] == 2:
				#TANGENT
				print('tan:')
			elif attributes[a] == 3:
				#BINORMAL
				print('bin:')
			elif attributes[a] == 4:
				#COLOR
				print('color:')
			elif attributes[a] == 5:
				#TEXCOORD
				flcount += 2		
			elif attributes[a] == 6:
				#USER_DEF
				print('udef:')
			else:
				print('Cannot understand attribute')
		
		print("flcount: %i" %flcount)
		print("flts: %i" %flts)
		points = int(flts/flcount)
		
		#read coords
		coords = []
		for i in range(points):
			if 0 in attributes:
				temp_data = file.read(struct.calcsize('3f'))
				x, y, z = struct.unpack('<3f', temp_data)
				#print('pos: %f, %f, %f' % (x, y, z))
				coords.append((x, y, z))
			if 1 in attributes:
				temp_data = file.read(struct.calcsize('3f'))
				uva, uvb, uvc = struct.unpack('<3f', temp_data)
				#print('norm: %f, %f, %f' % (uva, uvb, uvc))
			if 5 in attributes:
				#print('yo')
				#temp_data = file.read(struct.calcsize('3f'))
				#u, v, w = struct.unpack('<3f', temp_data)
				#print('tex: %f, %f, %f' % (u, v, w))
				temp_data = file.read(struct.calcsize('2f'))
				s, t = struct.unpack('<2f', temp_data)
				print('tex: %f, %f' % (s, t))
				#temp_data = file.read(struct.calcsize('4f'))
				#u1, v1, u2, v2 = struct.unpack('<4f', temp_data)
				#print('tex: %f, %f, %f, %f' % (u1,v1,u2,v2))
			
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
		
class A3DObject:
	def __init__(self, id, trans, name, parentid, mesh, geometry, boundbox, visible):
		self.id = id
		self.transformation = trans
		self.name = name
		self.parentid = parentid
		self.mesh = mesh
		self.geometry = geometry
		self.boundbox = boundbox
		self.visible = visible

class A3DSurface:
	def __init__(self, material, indexbegin, numtriangles):
		self.material = material
		self.indexbegin = indexbegin
		self.numtriangles = numtriangles

class A3DVertexBuffer:
	def __init__(self, numverts, attribs, verts):
		self.numverts = numverts
		self.attribs = attribs
		self.verts = verts

class A3DIndexBuffer:
	def __init__(self, numindex, indices):
		self.numindex = numindex
		self.indices = indices

class A3DTransformation:
	def __init__(self,file):
		self.matrix = A3DMatrix(a,b,c,d,e,f,g,h,i,j,k,l)

class A3DMatrix:
	def __init__(self,a,b,c,d,e,f,g,h,i,j,k,l):
		self.a = a
		self.b = b
		self.c = c
		self.l = l
		
class A3DAnimation:
	def __init__(self, id, propid, keys, values):
		self.id = id
		self.propertyid = propid
		self.keys = keys
		self.values = values
		
class A3DMaterial:
	def __init__(self, id, dmap, lmap, nmap):
		self.id = id
		self.diffusemap = dmap
		self.lightmap = lmap
		self.normalmap = nmap

class A3DMap:
	def __init__(self, id, image):
		self.id = id
		self.image = image
		self.channel = channel
		self.uScale = uScale
		self.vScale = vScale
		self.uOffset = uOffset
		self.vOffset = vOffset
		
class A3DImage:
	def __init__(self, url):
		self.url = url

# count num of active bits		
def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)

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
	default_path = bpy.data.filepath.replace('.blend', '.as')
	self.layout.operator(ASExporter.bl_idname, text='Alternativa3D Class (.as)').filepath = default_path
	
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