//Alternativa3D Class Export For Blender 2.57 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.core.Vertex;
	import alternativa.engine3d.core.Geometry;
	import __AS3__.vec.Vector;
	import flash.display.Bitmap;

	public class mycube extends Mesh {

		private var CubeMaterial:FillMaterial = new FillMaterial(0xcc00b9);

		public function mycube() {

			var g:Geometry = new Geometry();

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					g.addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, -1.000000, -1.000000, 0, 0),
					g.addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					g.addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					g.addVertex(1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					g.addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					g.addVertex(1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					g.addVertex(0.999999, -1.000001, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					g.addVertex(0.999999, -1.000001, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					g.addVertex(1.000000, -1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					g.addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

			//g.weldVertices();
			//g.weldFaces();
			geometry = g;

		}
	}
}