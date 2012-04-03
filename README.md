Alternativa 3d Blender Tool
===========================

Created by David E Jones, [http://davidejones.com](http://davidejones.com)
Follow me on twitter [@david3jones](https://twitter.com/david3jones)

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

Example Code
----------

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

	public class Cube.001 extends Mesh {

		private var Material:FillMaterial = new FillMaterial(0xcccccc);

		private var attributes:Array;

		public function Cube.001() {

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


Changelog
---------

### 1.1.3
1. Fixed error when exporting in version 7.51
2. Rebuilt version 5.6.0 as it wasn't exporting anything useful
3. added check to see if importing a3d version 1 or 2


### 1.1.2
Added support for bytearray class