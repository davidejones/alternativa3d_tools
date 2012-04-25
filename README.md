Alternativa 3d Blender Tool
===========================

Created by David E Jones, [http://davidejones.com](http://davidejones.com)
Follow me on twitter [@david3jones](https://twitter.com/david3jones)

If you like this tool, then please tweet, like or googleplus my website http://davidejones.com

What is the alternativa 3d blender tool?
----------------------------------------

This python script can be installed as an addon to blender. Once installed it will allow you to import/export various formats that are compatible with the flash 3d library [alternativa](http://alternativaplatform.com/en/).

##Functionality

- Create alternativa3d objects in blender and enable for export (Work in progress)
- Create Document Class (Work in progress)
- Import/Export .A3D files (Work in progress)
- Export 3d models to flash alternativa3d actionscript classes (Export fillmaterials or textures)
  For the following alternativa3d versions
	-5.6.0
	-7.5.1
	-7.6.0
	-7.7.0
	-7.8.0
	-8.5.0
	-8.8.0
	-8.12.0
	-8.17.0
	-8.27.0
- Export data to compressed bytearray variable within class in version 8.27.0+

Installation Notes
------------------

1. Open blender and go to File->User Preferences
2. Click the Addons tab
3. Click the install addon button at the bottom of this window
4. Browse to the io_alternativa3d_tools.py file
5. Find the addon in the list, this is easier if you click Import-Export category on the left.
6. Tick the checkbox next to the addon to enable it
7. Click save as default button if you want this addon and any other changes you have made to be enabled by default when you start up blender

Changelog
---------

### 1.1.5
- Updated min version of blender to be 2.62
- Fixed export class version 5.6.0 uv mapping
- Basic export to a3d 2.0
- Partial exporting to 2.4, 2.5, 2.6
- Basic import of a3d 2.0
- Partial importing of a3d 2.4, 2.5, 2.6
- Export tangents for classes and a3d
- Flat or Smooth normals exports
- Fixed export documentclass to do something useful
- Updated mesh menu with a3dclasses
- Updated examples

### 1.1.4
- Added example exports for each version with built swf
- Added in options for 7.5.0
- Condensed version 8 coding
- Condensed version 7 coding

### 1.1.3
- Fixed error when exporting in version 7.51
- Rebuilt version 5.6.0 as it wasn't exporting anything useful
- added check to see if importing .a3d file version 1 or 2

### 1.1.2
- Added support for compressed bytearray data in class rather than values v.8.27.0+ only

### 1.1.1
- Updated version 8 class export with textures. 
- Changed export to use material name instead of material0 material1 etc. 
- Works with multiple surface materials 

Example Output Code
----------

### Version 8.27.0

```actionscript
//Alternativa3D Class Export For Blender 2.57 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.core.VertexAttributes;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.resources.BitmapTextureResource;
	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.resources.Geometry;
	import __AS3__.vec.Vector;
	import flash.display.Bitmap;

	public class Cube extends Mesh {

		private var Material:FillMaterial = new FillMaterial(0xcccccc);

		private var attributes:Array;

		public function Cube() {

			attributes = new Array();
			attributes[0] = VertexAttributes.POSITION;
			attributes[1] = VertexAttributes.POSITION;
			attributes[2] = VertexAttributes.POSITION;
			attributes[3] = VertexAttributes.TEXCOORDS[0];
			attributes[4] = VertexAttributes.TEXCOORDS[0];
			attributes[5] = VertexAttributes.NORMAL;
			attributes[6] = VertexAttributes.NORMAL;
			attributes[7] = VertexAttributes.NORMAL;
			attributes[8] = VertexAttributes.TANGENT4;
			attributes[9] = VertexAttributes.TANGENT4;
			attributes[10] = VertexAttributes.TANGENT4;
			attributes[11] = VertexAttributes.TANGENT4;

			var g:Geometry = new Geometry();
			g.addVertexStream(attributes);
			g.numVertices = 8;

			var vertices:Array = [
				1, 1, -1,
				1, -1, -1,
				-1, -1, -1,
				-1, 1, -1,
				1, 0.999999, 1,
				0.999999, -1, 1,
				-1, -1, 1,
				-1, 1, 1,
			];
			var uvt:Array = new Array();
			var ind:Array = [
				4,0,3,
				4,3,7,
				2,6,7,
				2,7,3,
				1,5,2,
				5,6,2,
				0,4,1,
				4,5,1,
				4,7,5,
				7,6,5,
				0,1,2,
				0,2,3,
			];
			var normals:Array = [
				0.577349, 0.577349, -0.577349,
				0.577349, -0.577349, -0.577349,
				-0.577349, -0.577349, -0.577349,
				-0.577349, 0.577349, -0.577349,
				0.577349, 0.577349, 0.577349,
				0.577349, -0.577349, 0.577349,
				-0.577349, -0.577349, 0.577349,
				-0.577349, 0.577349, 0.577349,
			];
			var tangent:Array = new Array();

			g.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));
			//g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));
			g.setAttributeValues(VertexAttributes.NORMAL, Vector.<Number>(normals));
			//g.setAttributeValues(VertexAttributes.TANGENT4, Vector.<Number>(tangent));
			g.indices =  Vector.<uint>(ind);

			//g.calculateNormals();
			//g.calculateTangents(0);
			this.geometry = g;
			this.addSurface(Material, 0, 12);
			this.calculateBoundBox();
		}
	}
}
```

### Version 7.8.0
```actionscript
//Alternativa3D Class Export For Blender 2.57 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.core.Vertex;
	import __AS3__.vec.Vector;
	import flash.display.Bitmap;

	public class Cube extends Mesh {

		private var Material:FillMaterial = new FillMaterial(0xcccccc);

		public function Cube() {

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcccccc));

			calculateFacesNormals();
			calculateVerticesNormals();
			calculateBounds();
		}
	}
}
```

### Version 5.6.0

```actionscript
//Alternativa3D Class Export For Blender 2.57 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.core.Mesh;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.types.Texture;
	import flash.display.BlendMode;
	import flash.geom.Point;
	import flash.display.Bitmap;

	public class Cube extends Mesh {

		private var CubeMaterial:FillMaterial = new FillMaterial(0xcc00b9);

		public function Cube() {

			createVertex(1, 1, -1, 0);
			createVertex(1, -1, -1, 1);
			createVertex(-1, -1, -1, 2);
			createVertex(-1, 1, -1, 3);
			createVertex(1, 0.999999, 1, 4);
			createVertex(0.999999, -1, 1, 5);
			createVertex(-1, -1, 1, 6);
			createVertex(-1, 1, 1, 7);

			createFace([4,0,3], 0);
			createFace([4,3,7], 1);
			createFace([2,6,7], 2);
			createFace([2,7,3], 3);
			createFace([1,5,2], 4);
			createFace([5,6,2], 5);
			createFace([0,4,1], 6);
			createFace([4,5,1], 7);
			createFace([4,7,5], 8);
			createFace([7,6,5], 9);
			createFace([0,1,2], 10);
			createFace([0,2,3], 11);
			createSurface([0,1,2,3,4,5,6,7,8,9,10,11], "CubeMaterial");
			setMaterialToSurface(CubeMaterial, "CubeMaterial");
		}
	}
}
```