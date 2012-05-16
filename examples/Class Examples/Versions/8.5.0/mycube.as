//Alternativa3D Class Export For Blender 2.62 and above
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

	public class mycube extends Mesh {

		private var CubeMaterial:FillMaterial = new FillMaterial(0xcc00b9);

		private var attributes:Array;

		public function mycube() {

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

			this.geometry = g;
			this.addSurface(CubeMaterial, 0, 12);
			this.calculateBoundBox();

			this.x = 0.000000;
			this.y = -6.000000;
			this.z = 0.000000;
			this.rotationX = 0.000000;
			this.rotationY = -0.000000;
			this.rotationZ = 0.000000;
			this.scaleX = 1.000000;
			this.scaleY = 1.000000;
			this.scaleZ = 1.000000;
		}
	}
}