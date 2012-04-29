//Alternativa3D Class Export For Blender 2.62 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.core.Mesh;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.types.Texture;
	import alternativa.types.Matrix3D;
	import alternativa.types.Point3D;
	import flash.display.BlendMode;
	import flash.geom.Point;
	import flash.display.Bitmap;

	public class mycube extends Mesh {

		private var CubeMaterial:FillMaterial = new FillMaterial(0xcc00b9);

		public function mycube() {

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