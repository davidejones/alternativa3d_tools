//Alternativa3D Class Export For Blender 2.57 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.core.Vertex;
	import __AS3__.vec.Vector;
	import flash.display.Bitmap;

	public class mycube extends Mesh {

		private var CubeMaterial:FillMaterial = new FillMaterial(0xcc00b9);

		public function mycube() {

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 0.999999, 1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(-1.000000, 1.000000, 1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, 1.000000, 0, 0),
					addVertex(0.999999, -1.000001, 1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

				addFace(Vector.<Vertex>([
					addVertex(1.000000, 1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, -1.000000, -1.000000, 0, 0),
					addVertex(-1.000000, 1.000000, -1.000000, 0, 0),
				]),new FillMaterial(0xcc00b9));

		calculateNormals();
		calculateBounds();
		}
	}
}