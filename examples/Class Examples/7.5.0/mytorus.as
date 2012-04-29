//Alternativa3D Class Export For Blender 2.62 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.core.Vertex;
	import alternativa.engine3d.core.Geometry;
	import __AS3__.vec.Vector;
	import flash.display.Bitmap;

	public class mytorus extends Mesh {

		private var TorusMaterial2:FillMaterial = new FillMaterial(0x001bcc);

		private var TorusMaterial1:FillMaterial = new FillMaterial(0xb2cc00);

		public function mytorus() {

			var g:Geometry = new Geometry();

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, -0.114210, -0.216506, 0, 0),
					g.addVertex(0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(1.000000, 0.000000, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, -0.114210, -0.216506, 0, 0),
					g.addVertex(1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(0.991445, -0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
					g.addVertex(1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(1.086667, -0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
					g.addVertex(1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(1.039364, -0.430519, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, -0.500000, -0.250000, 0, 0),
					g.addVertex(0.923879, -0.382684, -0.250000, 0, 0),
					g.addVertex(1.039364, -0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, -0.500000, -0.250000, 0, 0),
					g.addVertex(1.039364, -0.430519, -0.216506, 0, 0),
					g.addVertex(0.974279, -0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(1.039364, -0.430519, 0.216506, 0, 0),
					g.addVertex(0.923879, -0.382684, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(0.923879, -0.382684, 0.250000, 0, 0),
					g.addVertex(0.866025, -0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(1.053525, -0.608253, 0.125000, 0, 0),
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(0.892523, -0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, -0.618719, -0.216506, 0, 0),
					g.addVertex(0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(0.793353, -0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, -0.618719, -0.216506, 0, 0),
					g.addVertex(0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(0.707106, -0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684856, -0.892523, 0.216506, 0, 0),
					g.addVertex(0.795495, -0.795496, 0.216506, 0, 0),
					g.addVertex(0.707106, -0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684856, -0.892523, 0.216506, 0, 0),
					g.addVertex(0.707106, -0.707107, 0.250000, 0, 0),
					g.addVertex(0.608761, -0.793354, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(0.532666, -0.694184, -0.216506, 0, 0),
					g.addVertex(0.608761, -0.793354, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(0.608761, -0.793354, -0.250000, 0, 0),
					g.addVertex(0.500000, -0.866025, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(0.391747, -0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(0.299830, -0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(0.382684, -0.923879, 0.250000, 0, 0),
					g.addVertex(0.334848, -0.808394, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(0.334848, -0.808394, 0.216506, 0, 0),
					g.addVertex(0.226466, -0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
					g.addVertex(0.102266, -0.776791, -0.125000, 0, 0),
					g.addVertex(0.114210, -0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
					g.addVertex(0.114210, -0.867514, -0.216506, 0, 0),
					g.addVertex(0.000000, -0.875000, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.783494, 0.125000, 0, 0),
					g.addVertex(0.102266, -0.776791, 0.125000, 0, 0),
					g.addVertex(0.097895, -0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.783494, 0.125000, 0, 0),
					g.addVertex(0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(0.000000, -0.750000, 0.000000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.125000, 0.216506, 0, 0),
					g.addVertex(0.146842, -1.115376, 0.216506, 0, 0),
					g.addVertex(0.130526, -0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.125000, 0.216506, 0, 0),
					g.addVertex(0.130526, -0.991445, 0.250000, 0, 0),
					g.addVertex(0.000000, -1.000000, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, -0.808395, -0.216506, 0, 0),
					g.addVertex(-0.226467, -0.845185, -0.216506, 0, 0),
					g.addVertex(-0.258819, -0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, -0.808395, -0.216506, 0, 0),
					g.addVertex(-0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(-0.382684, -0.923880, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, -0.923880, 0.250000, 0, 0),
					g.addVertex(-0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, -0.923880, 0.250000, 0, 0),
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
					g.addVertex(-0.334848, -0.808395, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(-0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(-0.287013, -0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(-0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(-0.375000, -0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(-0.618719, -0.618718, 0.216506, 0, 0),
					g.addVertex(-0.554014, -0.554013, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(-0.554014, -0.554013, 0.125000, 0, 0),
					g.addVertex(-0.621587, -0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808395, -0.334848, -0.216506, 0, 0),
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(-0.866026, -0.500000, -0.250000, 0, 0),
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923880, -0.382683, 0.250000, 0, 0),
					g.addVertex(-0.866026, -0.500000, 0.250000, 0, 0),
					g.addVertex(-0.757772, -0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923880, -0.382683, 0.250000, 0, 0),
					g.addVertex(-0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(-0.808395, -0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(-0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(-0.808395, -0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(-0.808395, -0.334848, -0.216506, 0, 0),
					g.addVertex(-0.845185, -0.226467, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(-0.776791, -0.102267, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-0.776791, -0.102267, -0.125000, 0, 0),
					g.addVertex(-0.783494, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-0.867514, -0.114211, 0.216506, 0, 0),
					g.addVertex(-0.776791, -0.102267, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-0.776791, -0.102267, 0.125000, 0, 0),
					g.addVertex(-0.783494, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(-1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(-1.125000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(-1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-1.115376, 0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(-0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(-0.621587, 0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(-0.618719, 0.618718, -0.216506, 0, 0),
					g.addVertex(-0.707107, 0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(-0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(-0.608761, 0.793353, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(-0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(-0.608253, 1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(-0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(-0.465537, 1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(-0.382684, 0.923880, -0.250000, 0, 0),
					g.addVertex(-0.430519, 1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(-0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(-0.291171, 1.086667, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.125000, -0.216506, 0, 0),
					g.addVertex(-0.146842, 1.115375, -0.216506, 0, 0),
					g.addVertex(-0.158786, 1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.125000, -0.216506, 0, 0),
					g.addVertex(-0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(0.000000, 1.216506, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(0.114210, 0.867514, -0.216506, 0, 0),
					g.addVertex(0.130526, 0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(0.258819, 0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(0.291171, 1.086666, -0.216506, 0, 0),
					g.addVertex(0.314855, 1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(0.465537, 1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(0.291171, 1.086666, 0.216506, 0, 0),
					g.addVertex(0.258819, 0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(0.382684, 0.923879, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(0.608762, 0.793353, -0.250000, 0, 0),
					g.addVertex(0.684857, 0.892522, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(0.795495, 0.795495, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(0.608762, 0.793353, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(0.608762, 0.793353, 0.250000, 0, 0),
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(0.860200, 0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(0.965119, 0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(0.795495, 0.795495, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(0.892523, 0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(0.974279, 0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(1.039365, 0.430519, 0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(0.808395, 0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(0.808395, 0.334848, -0.216506, 0, 0),
					g.addVertex(0.845185, 0.226467, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(1.086667, 0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(1.115376, 0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(0.991445, 0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(1.000000, 0.000000, 0.250000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(1.206099, 0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(1.216506, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0x001bcc));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(1.206099, -0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(1.216506, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(1.216506, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(1.216506, 0.000000, -0.125000, 0, 0),
					g.addVertex(1.206099, -0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(1.125000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(1.115376, -0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, -0.102266, -0.125000, 0, 0),
					g.addVertex(0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(0.875000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, -0.102266, -0.125000, 0, 0),
					g.addVertex(0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(0.867514, -0.114210, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(0.783494, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(0.776791, -0.102266, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, -0.102266, 0.125000, 0, 0),
					g.addVertex(0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(0.750000, 0.000000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, -0.102266, 0.125000, 0, 0),
					g.addVertex(0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(0.743584, -0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, -0.114210, 0.216506, 0, 0),
					g.addVertex(0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(0.783494, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, -0.114210, 0.216506, 0, 0),
					g.addVertex(0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(0.776791, -0.102266, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(0.875000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(0.867514, -0.114210, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(1.000000, 0.000000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(0.991445, -0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(1.125000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(1.115376, -0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.216506, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(1.206099, -0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(1.239306, -0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(1.207407, -0.323523, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(1.206099, -0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(1.175055, -0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(1.115376, -0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(1.086667, -0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, -0.226466, -0.216506, 0, 0),
					g.addVertex(0.867514, -0.114210, -0.216506, 0, 0),
					g.addVertex(0.991445, -0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, -0.226466, -0.216506, 0, 0),
					g.addVertex(0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(0.965926, -0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(0.776791, -0.102266, -0.125000, 0, 0),
					g.addVertex(0.867514, -0.114210, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(0.867514, -0.114210, -0.216506, 0, 0),
					g.addVertex(0.845185, -0.226466, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(0.776791, -0.102266, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(0.776791, -0.102266, -0.125000, 0, 0),
					g.addVertex(0.756797, -0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(0.776791, -0.102266, 0.125000, 0, 0),
					g.addVertex(0.743584, -0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(0.724444, -0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, -0.226466, 0.216506, 0, 0),
					g.addVertex(0.867514, -0.114210, 0.216506, 0, 0),
					g.addVertex(0.776791, -0.102266, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, -0.226466, 0.216506, 0, 0),
					g.addVertex(0.776791, -0.102266, 0.125000, 0, 0),
					g.addVertex(0.756797, -0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(0.867514, -0.114210, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(0.867514, -0.114210, 0.216506, 0, 0),
					g.addVertex(0.845185, -0.226466, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(0.991445, -0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(0.965926, -0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(1.115376, -0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(1.086667, -0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.207407, -0.323523, 0.000000, 0, 0),
					g.addVertex(1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(1.206099, -0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.207407, -0.323523, 0.000000, 0, 0),
					g.addVertex(1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(1.175055, -0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, -0.465537, -0.125000, 0, 0),
					g.addVertex(1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(1.207407, -0.323523, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, -0.465537, -0.125000, 0, 0),
					g.addVertex(1.207407, -0.323523, 0.000000, 0, 0),
					g.addVertex(1.154849, -0.478355, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039364, -0.430519, -0.216506, 0, 0),
					g.addVertex(1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(1.175055, -0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039364, -0.430519, -0.216506, 0, 0),
					g.addVertex(1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(1.123905, -0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923879, -0.382684, -0.250000, 0, 0),
					g.addVertex(0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(1.086667, -0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923879, -0.382684, -0.250000, 0, 0),
					g.addVertex(1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(1.039364, -0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808394, -0.334848, -0.216506, 0, 0),
					g.addVertex(0.845185, -0.226466, -0.216506, 0, 0),
					g.addVertex(0.965926, -0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808394, -0.334848, -0.216506, 0, 0),
					g.addVertex(0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(0.923879, -0.382684, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(0.845185, -0.226466, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(0.845185, -0.226466, -0.216506, 0, 0),
					g.addVertex(0.808394, -0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.692909, -0.287013, 0.000000, 0, 0),
					g.addVertex(0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(0.756797, -0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.692909, -0.287013, 0.000000, 0, 0),
					g.addVertex(0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(0.723854, -0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(0.724444, -0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(0.692909, -0.287013, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808394, -0.334848, 0.216506, 0, 0),
					g.addVertex(0.845185, -0.226466, 0.216506, 0, 0),
					g.addVertex(0.756797, -0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808394, -0.334848, 0.216506, 0, 0),
					g.addVertex(0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(0.723854, -0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923879, -0.382684, 0.250000, 0, 0),
					g.addVertex(0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(0.845185, -0.226466, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923879, -0.382684, 0.250000, 0, 0),
					g.addVertex(0.845185, -0.226466, 0.216506, 0, 0),
					g.addVertex(0.808394, -0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039364, -0.430519, 0.216506, 0, 0),
					g.addVertex(1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(0.965926, -0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039364, -0.430519, 0.216506, 0, 0),
					g.addVertex(0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(0.923879, -0.382684, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.154849, -0.478355, 0.000000, 0, 0),
					g.addVertex(1.207407, -0.323523, 0.000000, 0, 0),
					g.addVertex(1.175055, -0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.154849, -0.478355, 0.000000, 0, 0),
					g.addVertex(1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, -0.608253, -0.125000, 0, 0),
					g.addVertex(1.123905, -0.465537, -0.125000, 0, 0),
					g.addVertex(1.154849, -0.478355, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, -0.608253, -0.125000, 0, 0),
					g.addVertex(1.154849, -0.478355, 0.000000, 0, 0),
					g.addVertex(1.082532, -0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(1.039364, -0.430519, -0.216506, 0, 0),
					g.addVertex(1.123905, -0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(1.123905, -0.465537, -0.125000, 0, 0),
					g.addVertex(1.053525, -0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(0.808394, -0.334848, -0.216506, 0, 0),
					g.addVertex(0.923879, -0.382684, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(0.923879, -0.382684, -0.250000, 0, 0),
					g.addVertex(0.866025, -0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, -0.391747, -0.125000, 0, 0),
					g.addVertex(0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(0.808394, -0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, -0.391747, -0.125000, 0, 0),
					g.addVertex(0.808394, -0.334848, -0.216506, 0, 0),
					g.addVertex(0.757772, -0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(0.692909, -0.287013, 0.000000, 0, 0),
					g.addVertex(0.723854, -0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(0.678525, -0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, -0.391747, 0.125000, 0, 0),
					g.addVertex(0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(0.692909, -0.287013, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, -0.391747, 0.125000, 0, 0),
					g.addVertex(0.692909, -0.287013, 0.000000, 0, 0),
					g.addVertex(0.649519, -0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(0.808394, -0.334848, 0.216506, 0, 0),
					g.addVertex(0.723854, -0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(0.678525, -0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, -0.500000, 0.250000, 0, 0),
					g.addVertex(0.923879, -0.382684, 0.250000, 0, 0),
					g.addVertex(0.808394, -0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, -0.500000, 0.250000, 0, 0),
					g.addVertex(0.808394, -0.334848, 0.216506, 0, 0),
					g.addVertex(0.757772, -0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, -0.608253, 0.125000, 0, 0),
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
					g.addVertex(1.039364, -0.430519, 0.216506, 0, 0),
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(1.154849, -0.478355, 0.000000, 0, 0),
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(1.123905, -0.465537, 0.125000, 0, 0),
					g.addVertex(1.053525, -0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(1.053525, -0.608253, -0.125000, 0, 0),
					g.addVertex(1.082532, -0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(0.991692, -0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(1.053525, -0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(1.053525, -0.608253, -0.125000, 0, 0),
					g.addVertex(0.965119, -0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(0.866025, -0.500000, -0.250000, 0, 0),
					g.addVertex(0.974279, -0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(0.892523, -0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(0.866025, -0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(0.866025, -0.500000, -0.250000, 0, 0),
					g.addVertex(0.793353, -0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(0.678525, -0.391747, -0.125000, 0, 0),
					g.addVertex(0.757772, -0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(0.694184, -0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(0.678525, -0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(0.678525, -0.391747, -0.125000, 0, 0),
					g.addVertex(0.621587, -0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(0.678525, -0.391747, 0.125000, 0, 0),
					g.addVertex(0.649519, -0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(0.595015, -0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(0.678525, -0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(0.678525, -0.391747, 0.125000, 0, 0),
					g.addVertex(0.621587, -0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(0.866025, -0.500000, 0.250000, 0, 0),
					g.addVertex(0.757772, -0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(0.694184, -0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(0.866025, -0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(0.866025, -0.500000, 0.250000, 0, 0),
					g.addVertex(0.793353, -0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(1.053525, -0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(1.053525, -0.608253, 0.125000, 0, 0),
					g.addVertex(0.965119, -0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860199, -0.860200, -0.125000, 0, 0),
					g.addVertex(0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(0.991692, -0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860199, -0.860200, -0.125000, 0, 0),
					g.addVertex(0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(0.883883, -0.883884, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, -0.795496, -0.216506, 0, 0),
					g.addVertex(0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(0.965119, -0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, -0.795496, -0.216506, 0, 0),
					g.addVertex(0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(0.860199, -0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707106, -0.707107, -0.250000, 0, 0),
					g.addVertex(0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(0.892523, -0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707106, -0.707107, -0.250000, 0, 0),
					g.addVertex(0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(0.795495, -0.795496, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554013, -0.554014, -0.125000, 0, 0),
					g.addVertex(0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(0.694184, -0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554013, -0.554014, -0.125000, 0, 0),
					g.addVertex(0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(0.618718, -0.618719, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(0.621587, -0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(0.554013, -0.554014, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554013, -0.554014, 0.125000, 0, 0),
					g.addVertex(0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(0.595015, -0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554013, -0.554014, 0.125000, 0, 0),
					g.addVertex(0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(0.530330, -0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, -0.618719, 0.216506, 0, 0),
					g.addVertex(0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(0.621587, -0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, -0.618719, 0.216506, 0, 0),
					g.addVertex(0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(0.554013, -0.554014, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707106, -0.707107, 0.250000, 0, 0),
					g.addVertex(0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(0.694184, -0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707106, -0.707107, 0.250000, 0, 0),
					g.addVertex(0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(0.618718, -0.618719, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, -0.795496, 0.216506, 0, 0),
					g.addVertex(0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(0.793353, -0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, -0.795496, 0.216506, 0, 0),
					g.addVertex(0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(0.707106, -0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860199, -0.860200, 0.125000, 0, 0),
					g.addVertex(0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(0.892523, -0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860199, -0.860200, 0.125000, 0, 0),
					g.addVertex(0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(0.795495, -0.795496, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.883883, -0.883884, 0.000000, 0, 0),
					g.addVertex(0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(0.965119, -0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.883883, -0.883884, 0.000000, 0, 0),
					g.addVertex(0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(0.860199, -0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, -0.965120, -0.125000, 0, 0),
					g.addVertex(0.860199, -0.860200, -0.125000, 0, 0),
					g.addVertex(0.883883, -0.883884, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, -0.965120, -0.125000, 0, 0),
					g.addVertex(0.883883, -0.883884, 0.000000, 0, 0),
					g.addVertex(0.760952, -0.991692, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684856, -0.892523, -0.216506, 0, 0),
					g.addVertex(0.795495, -0.795496, -0.216506, 0, 0),
					g.addVertex(0.860199, -0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684856, -0.892523, -0.216506, 0, 0),
					g.addVertex(0.860199, -0.860200, -0.125000, 0, 0),
					g.addVertex(0.740562, -0.965120, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608761, -0.793354, -0.250000, 0, 0),
					g.addVertex(0.707106, -0.707107, -0.250000, 0, 0),
					g.addVertex(0.795495, -0.795496, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608761, -0.793354, -0.250000, 0, 0),
					g.addVertex(0.795495, -0.795496, -0.216506, 0, 0),
					g.addVertex(0.684856, -0.892523, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, -0.694184, -0.216506, 0, 0),
					g.addVertex(0.618718, -0.618719, -0.216506, 0, 0),
					g.addVertex(0.707106, -0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, -0.694184, -0.216506, 0, 0),
					g.addVertex(0.707106, -0.707107, -0.250000, 0, 0),
					g.addVertex(0.608761, -0.793354, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(0.554013, -0.554014, -0.125000, 0, 0),
					g.addVertex(0.618718, -0.618719, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(0.618718, -0.618719, -0.216506, 0, 0),
					g.addVertex(0.532666, -0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(0.554013, -0.554014, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(0.554013, -0.554014, -0.125000, 0, 0),
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(0.554013, -0.554014, 0.125000, 0, 0),
					g.addVertex(0.530330, -0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(0.456571, -0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, -0.694184, 0.216506, 0, 0),
					g.addVertex(0.618718, -0.618719, 0.216506, 0, 0),
					g.addVertex(0.554013, -0.554014, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, -0.694184, 0.216506, 0, 0),
					g.addVertex(0.554013, -0.554014, 0.125000, 0, 0),
					g.addVertex(0.476961, -0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608761, -0.793354, 0.250000, 0, 0),
					g.addVertex(0.707106, -0.707107, 0.250000, 0, 0),
					g.addVertex(0.618718, -0.618719, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608761, -0.793354, 0.250000, 0, 0),
					g.addVertex(0.618718, -0.618719, 0.216506, 0, 0),
					g.addVertex(0.532666, -0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, -0.965120, 0.125000, 0, 0),
					g.addVertex(0.860199, -0.860200, 0.125000, 0, 0),
					g.addVertex(0.795495, -0.795496, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, -0.965120, 0.125000, 0, 0),
					g.addVertex(0.795495, -0.795496, 0.216506, 0, 0),
					g.addVertex(0.684856, -0.892523, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.760952, -0.991692, 0.000000, 0, 0),
					g.addVertex(0.883883, -0.883884, 0.000000, 0, 0),
					g.addVertex(0.860199, -0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.760952, -0.991692, 0.000000, 0, 0),
					g.addVertex(0.860199, -0.860200, 0.125000, 0, 0),
					g.addVertex(0.740562, -0.965120, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(0.740562, -0.965120, -0.125000, 0, 0),
					g.addVertex(0.760952, -0.991692, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(0.760952, -0.991692, 0.000000, 0, 0),
					g.addVertex(0.625000, -1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(0.684856, -0.892523, -0.216506, 0, 0),
					g.addVertex(0.740562, -0.965120, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(0.740562, -0.965120, -0.125000, 0, 0),
					g.addVertex(0.608253, -1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, -0.866025, -0.250000, 0, 0),
					g.addVertex(0.608761, -0.793354, -0.250000, 0, 0),
					g.addVertex(0.684856, -0.892523, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, -0.866025, -0.250000, 0, 0),
					g.addVertex(0.684856, -0.892523, -0.216506, 0, 0),
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(0.532666, -0.694184, -0.216506, 0, 0),
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(0.391747, -0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(0.456571, -0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(0.375000, -0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(0.532666, -0.694184, 0.216506, 0, 0),
					g.addVertex(0.476961, -0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(0.391747, -0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, -0.866025, 0.250000, 0, 0),
					g.addVertex(0.608761, -0.793354, 0.250000, 0, 0),
					g.addVertex(0.532666, -0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, -0.866025, 0.250000, 0, 0),
					g.addVertex(0.532666, -0.694184, 0.216506, 0, 0),
					g.addVertex(0.437500, -0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(0.684856, -0.892523, 0.216506, 0, 0),
					g.addVertex(0.608761, -0.793354, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(0.608761, -0.793354, 0.250000, 0, 0),
					g.addVertex(0.500000, -0.866025, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(0.740562, -0.965120, 0.125000, 0, 0),
					g.addVertex(0.684856, -0.892523, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(0.684856, -0.892523, 0.216506, 0, 0),
					g.addVertex(0.562500, -0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(0.760952, -0.991692, 0.000000, 0, 0),
					g.addVertex(0.740562, -0.965120, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(0.740562, -0.965120, 0.125000, 0, 0),
					g.addVertex(0.608253, -1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(0.625000, -1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(0.478355, -1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, -0.923879, -0.250000, 0, 0),
					g.addVertex(0.500000, -0.866025, -0.250000, 0, 0),
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, -0.923879, -0.250000, 0, 0),
					g.addVertex(0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(0.430519, -1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, -0.808394, -0.216506, 0, 0),
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(0.500000, -0.866025, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, -0.808394, -0.216506, 0, 0),
					g.addVertex(0.500000, -0.866025, -0.250000, 0, 0),
					g.addVertex(0.382684, -0.923879, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(0.334848, -0.808394, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(0.375000, -0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(0.287013, -0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, -0.808394, 0.216506, 0, 0),
					g.addVertex(0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(0.391747, -0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, -0.808394, 0.216506, 0, 0),
					g.addVertex(0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(0.299830, -0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, -0.923879, 0.250000, 0, 0),
					g.addVertex(0.500000, -0.866025, 0.250000, 0, 0),
					g.addVertex(0.437500, -0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, -0.923879, 0.250000, 0, 0),
					g.addVertex(0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(0.334848, -0.808394, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(0.500000, -0.866025, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(0.500000, -0.866025, 0.250000, 0, 0),
					g.addVertex(0.382684, -0.923879, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(0.562500, -0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.478355, -1.154849, 0.000000, 0, 0),
					g.addVertex(0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(0.608253, -1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.478355, -1.154849, 0.000000, 0, 0),
					g.addVertex(0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(0.465537, -1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314854, -1.175055, -0.125000, 0, 0),
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(0.478355, -1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314854, -1.175055, -0.125000, 0, 0),
					g.addVertex(0.478355, -1.154849, 0.000000, 0, 0),
					g.addVertex(0.323523, -1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, -1.086667, -0.216506, 0, 0),
					g.addVertex(0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, -1.086667, -0.216506, 0, 0),
					g.addVertex(0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(0.314854, -1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(0.382684, -0.923879, -0.250000, 0, 0),
					g.addVertex(0.430519, -1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(0.291171, -1.086667, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226466, -0.845185, -0.216506, 0, 0),
					g.addVertex(0.334848, -0.808394, -0.216506, 0, 0),
					g.addVertex(0.382684, -0.923879, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226466, -0.845185, -0.216506, 0, 0),
					g.addVertex(0.382684, -0.923879, -0.250000, 0, 0),
					g.addVertex(0.258819, -0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(0.334848, -0.808394, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(0.334848, -0.808394, -0.216506, 0, 0),
					g.addVertex(0.226466, -0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.194114, -0.724445, 0.000000, 0, 0),
					g.addVertex(0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(0.299830, -0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.194114, -0.724445, 0.000000, 0, 0),
					g.addVertex(0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(0.202783, -0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(0.287013, -0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(0.194114, -0.724445, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226466, -0.845185, 0.216506, 0, 0),
					g.addVertex(0.334848, -0.808394, 0.216506, 0, 0),
					g.addVertex(0.299830, -0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226466, -0.845185, 0.216506, 0, 0),
					g.addVertex(0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(0.202783, -0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, -1.086667, 0.216506, 0, 0),
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(0.382684, -0.923879, 0.250000, 0, 0),
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314854, -1.175055, 0.125000, 0, 0),
					g.addVertex(0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314854, -1.175055, 0.125000, 0, 0),
					g.addVertex(0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(0.291171, -1.086667, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.323523, -1.207407, 0.000000, 0, 0),
					g.addVertex(0.478355, -1.154849, 0.000000, 0, 0),
					g.addVertex(0.465537, -1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.323523, -1.207407, 0.000000, 0, 0),
					g.addVertex(0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(0.314854, -1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, -1.206099, -0.125000, 0, 0),
					g.addVertex(0.314854, -1.175055, -0.125000, 0, 0),
					g.addVertex(0.323523, -1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, -1.206099, -0.125000, 0, 0),
					g.addVertex(0.323523, -1.207407, 0.000000, 0, 0),
					g.addVertex(0.163158, -1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, -1.115376, -0.216506, 0, 0),
					g.addVertex(0.291171, -1.086667, -0.216506, 0, 0),
					g.addVertex(0.314854, -1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, -1.115376, -0.216506, 0, 0),
					g.addVertex(0.314854, -1.175055, -0.125000, 0, 0),
					g.addVertex(0.158786, -1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, -0.991445, -0.250000, 0, 0),
					g.addVertex(0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(0.291171, -1.086667, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, -0.991445, -0.250000, 0, 0),
					g.addVertex(0.291171, -1.086667, -0.216506, 0, 0),
					g.addVertex(0.146842, -1.115376, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, -0.867514, -0.216506, 0, 0),
					g.addVertex(0.226466, -0.845185, -0.216506, 0, 0),
					g.addVertex(0.258819, -0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, -0.867514, -0.216506, 0, 0),
					g.addVertex(0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(0.130526, -0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, -0.776791, -0.125000, 0, 0),
					g.addVertex(0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(0.226466, -0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, -0.776791, -0.125000, 0, 0),
					g.addVertex(0.226466, -0.845185, -0.216506, 0, 0),
					g.addVertex(0.114210, -0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(0.194114, -0.724445, 0.000000, 0, 0),
					g.addVertex(0.202783, -0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(0.102266, -0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, -0.776791, 0.125000, 0, 0),
					g.addVertex(0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(0.194114, -0.724445, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, -0.776791, 0.125000, 0, 0),
					g.addVertex(0.194114, -0.724445, 0.000000, 0, 0),
					g.addVertex(0.097895, -0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, -0.867514, 0.216506, 0, 0),
					g.addVertex(0.226466, -0.845185, 0.216506, 0, 0),
					g.addVertex(0.202783, -0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, -0.867514, 0.216506, 0, 0),
					g.addVertex(0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(0.102266, -0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, -0.991445, 0.250000, 0, 0),
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(0.226466, -0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, -0.991445, 0.250000, 0, 0),
					g.addVertex(0.226466, -0.845185, 0.216506, 0, 0),
					g.addVertex(0.114210, -0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, -1.115376, 0.216506, 0, 0),
					g.addVertex(0.291171, -1.086667, 0.216506, 0, 0),
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, -1.115376, 0.216506, 0, 0),
					g.addVertex(0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(0.130526, -0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, -1.206099, 0.125000, 0, 0),
					g.addVertex(0.314854, -1.175055, 0.125000, 0, 0),
					g.addVertex(0.291171, -1.086667, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, -1.206099, 0.125000, 0, 0),
					g.addVertex(0.291171, -1.086667, 0.216506, 0, 0),
					g.addVertex(0.146842, -1.115376, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.163158, -1.239306, 0.000000, 0, 0),
					g.addVertex(0.323523, -1.207407, 0.000000, 0, 0),
					g.addVertex(0.314854, -1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.163158, -1.239306, 0.000000, 0, 0),
					g.addVertex(0.314854, -1.175055, 0.125000, 0, 0),
					g.addVertex(0.158786, -1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.216506, -0.125000, 0, 0),
					g.addVertex(0.158786, -1.206099, -0.125000, 0, 0),
					g.addVertex(0.163158, -1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.216506, -0.125000, 0, 0),
					g.addVertex(0.163158, -1.239306, 0.000000, 0, 0),
					g.addVertex(0.000000, -1.250000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.125000, -0.216506, 0, 0),
					g.addVertex(0.146842, -1.115376, -0.216506, 0, 0),
					g.addVertex(0.158786, -1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.125000, -0.216506, 0, 0),
					g.addVertex(0.158786, -1.206099, -0.125000, 0, 0),
					g.addVertex(0.000000, -1.216506, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.000000, -0.250000, 0, 0),
					g.addVertex(0.130526, -0.991445, -0.250000, 0, 0),
					g.addVertex(0.146842, -1.115376, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.000000, -0.250000, 0, 0),
					g.addVertex(0.146842, -1.115376, -0.216506, 0, 0),
					g.addVertex(0.000000, -1.125000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.875000, -0.216506, 0, 0),
					g.addVertex(0.114210, -0.867514, -0.216506, 0, 0),
					g.addVertex(0.130526, -0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.875000, -0.216506, 0, 0),
					g.addVertex(0.130526, -0.991445, -0.250000, 0, 0),
					g.addVertex(0.000000, -1.000000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.750000, 0.000000, 0, 0),
					g.addVertex(0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(0.102266, -0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.750000, 0.000000, 0, 0),
					g.addVertex(0.102266, -0.776791, -0.125000, 0, 0),
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.875000, 0.216506, 0, 0),
					g.addVertex(0.114210, -0.867514, 0.216506, 0, 0),
					g.addVertex(0.102266, -0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.875000, 0.216506, 0, 0),
					g.addVertex(0.102266, -0.776791, 0.125000, 0, 0),
					g.addVertex(0.000000, -0.783494, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.000000, 0.250000, 0, 0),
					g.addVertex(0.130526, -0.991445, 0.250000, 0, 0),
					g.addVertex(0.114210, -0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.000000, 0.250000, 0, 0),
					g.addVertex(0.114210, -0.867514, 0.216506, 0, 0),
					g.addVertex(0.000000, -0.875000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.216506, 0.125000, 0, 0),
					g.addVertex(0.158786, -1.206099, 0.125000, 0, 0),
					g.addVertex(0.146842, -1.115376, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.216506, 0.125000, 0, 0),
					g.addVertex(0.146842, -1.115376, 0.216506, 0, 0),
					g.addVertex(0.000000, -1.125000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.250000, 0.000000, 0, 0),
					g.addVertex(0.163158, -1.239306, 0.000000, 0, 0),
					g.addVertex(0.158786, -1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.250000, 0.000000, 0, 0),
					g.addVertex(0.158786, -1.206099, 0.125000, 0, 0),
					g.addVertex(0.000000, -1.216506, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158787, -1.206099, -0.125000, 0, 0),
					g.addVertex(0.000000, -1.216506, -0.125000, 0, 0),
					g.addVertex(0.000000, -1.250000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158787, -1.206099, -0.125000, 0, 0),
					g.addVertex(0.000000, -1.250000, 0.000000, 0, 0),
					g.addVertex(-0.163159, -1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
					g.addVertex(0.000000, -1.125000, -0.216506, 0, 0),
					g.addVertex(0.000000, -1.216506, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
					g.addVertex(0.000000, -1.216506, -0.125000, 0, 0),
					g.addVertex(-0.158787, -1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130527, -0.991445, -0.250000, 0, 0),
					g.addVertex(0.000000, -1.000000, -0.250000, 0, 0),
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -1.000000, -0.250000, 0, 0),
					g.addVertex(0.000000, -1.125000, -0.216506, 0, 0),
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, -0.867514, -0.216506, 0, 0),
					g.addVertex(0.000000, -0.875000, -0.216506, 0, 0),
					g.addVertex(-0.130527, -0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.875000, -0.216506, 0, 0),
					g.addVertex(0.000000, -1.000000, -0.250000, 0, 0),
					g.addVertex(-0.130527, -0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, -0.776791, -0.125000, 0, 0),
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
					g.addVertex(-0.114211, -0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
					g.addVertex(0.000000, -0.875000, -0.216506, 0, 0),
					g.addVertex(-0.114211, -0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(0.000000, -0.750000, 0.000000, 0, 0),
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(0.000000, -0.783494, -0.125000, 0, 0),
					g.addVertex(-0.102267, -0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, -0.776791, 0.125000, 0, 0),
					g.addVertex(0.000000, -0.783494, 0.125000, 0, 0),
					g.addVertex(0.000000, -0.750000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, -0.776791, 0.125000, 0, 0),
					g.addVertex(0.000000, -0.750000, 0.000000, 0, 0),
					g.addVertex(-0.097895, -0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, -0.867514, 0.216506, 0, 0),
					g.addVertex(0.000000, -0.875000, 0.216506, 0, 0),
					g.addVertex(0.000000, -0.783494, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, -0.867514, 0.216506, 0, 0),
					g.addVertex(0.000000, -0.783494, 0.125000, 0, 0),
					g.addVertex(-0.102267, -0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130527, -0.991445, 0.250000, 0, 0),
					g.addVertex(0.000000, -1.000000, 0.250000, 0, 0),
					g.addVertex(0.000000, -0.875000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130527, -0.991445, 0.250000, 0, 0),
					g.addVertex(0.000000, -0.875000, 0.216506, 0, 0),
					g.addVertex(-0.114211, -0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
					g.addVertex(0.000000, -1.125000, 0.216506, 0, 0),
					g.addVertex(0.000000, -1.000000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
					g.addVertex(0.000000, -1.000000, 0.250000, 0, 0),
					g.addVertex(-0.130527, -0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158787, -1.206099, 0.125000, 0, 0),
					g.addVertex(0.000000, -1.216506, 0.125000, 0, 0),
					g.addVertex(0.000000, -1.125000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158787, -1.206099, 0.125000, 0, 0),
					g.addVertex(0.000000, -1.125000, 0.216506, 0, 0),
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.163159, -1.239306, 0.000000, 0, 0),
					g.addVertex(0.000000, -1.250000, 0.000000, 0, 0),
					g.addVertex(0.000000, -1.216506, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.163159, -1.239306, 0.000000, 0, 0),
					g.addVertex(0.000000, -1.216506, 0.125000, 0, 0),
					g.addVertex(-0.158787, -1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, -1.175055, -0.125000, 0, 0),
					g.addVertex(-0.158787, -1.206099, -0.125000, 0, 0),
					g.addVertex(-0.163159, -1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, -1.175055, -0.125000, 0, 0),
					g.addVertex(-0.163159, -1.239306, 0.000000, 0, 0),
					g.addVertex(-0.323524, -1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291172, -1.086666, -0.216506, 0, 0),
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
					g.addVertex(-0.158787, -1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291172, -1.086666, -0.216506, 0, 0),
					g.addVertex(-0.158787, -1.206099, -0.125000, 0, 0),
					g.addVertex(-0.314855, -1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(-0.130527, -0.991445, -0.250000, 0, 0),
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(-0.146843, -1.115375, -0.216506, 0, 0),
					g.addVertex(-0.291172, -1.086666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, -0.845185, -0.216506, 0, 0),
					g.addVertex(-0.114211, -0.867514, -0.216506, 0, 0),
					g.addVertex(-0.130527, -0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, -0.845185, -0.216506, 0, 0),
					g.addVertex(-0.130527, -0.991445, -0.250000, 0, 0),
					g.addVertex(-0.258819, -0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(-0.102267, -0.776791, -0.125000, 0, 0),
					g.addVertex(-0.114211, -0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(-0.114211, -0.867514, -0.216506, 0, 0),
					g.addVertex(-0.226467, -0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.194114, -0.724444, 0.000000, 0, 0),
					g.addVertex(-0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(-0.102267, -0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.194114, -0.724444, 0.000000, 0, 0),
					g.addVertex(-0.102267, -0.776791, -0.125000, 0, 0),
					g.addVertex(-0.202783, -0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(-0.102267, -0.776791, 0.125000, 0, 0),
					g.addVertex(-0.097895, -0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(-0.097895, -0.743584, 0.000000, 0, 0),
					g.addVertex(-0.194114, -0.724444, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
					g.addVertex(-0.114211, -0.867514, 0.216506, 0, 0),
					g.addVertex(-0.102267, -0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
					g.addVertex(-0.102267, -0.776791, 0.125000, 0, 0),
					g.addVertex(-0.202783, -0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(-0.130527, -0.991445, 0.250000, 0, 0),
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130527, -0.991445, 0.250000, 0, 0),
					g.addVertex(-0.114211, -0.867514, 0.216506, 0, 0),
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291172, -1.086666, 0.216506, 0, 0),
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
					g.addVertex(-0.258819, -0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
					g.addVertex(-0.130527, -0.991445, 0.250000, 0, 0),
					g.addVertex(-0.258819, -0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, -1.175055, 0.125000, 0, 0),
					g.addVertex(-0.158787, -1.206099, 0.125000, 0, 0),
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, -1.175055, 0.125000, 0, 0),
					g.addVertex(-0.146843, -1.115375, 0.216506, 0, 0),
					g.addVertex(-0.291172, -1.086666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.323524, -1.207407, 0.000000, 0, 0),
					g.addVertex(-0.163159, -1.239306, 0.000000, 0, 0),
					g.addVertex(-0.158787, -1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.323524, -1.207407, 0.000000, 0, 0),
					g.addVertex(-0.158787, -1.206099, 0.125000, 0, 0),
					g.addVertex(-0.314855, -1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(-0.314855, -1.175055, -0.125000, 0, 0),
					g.addVertex(-0.323524, -1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(-0.323524, -1.207407, 0.000000, 0, 0),
					g.addVertex(-0.478354, -1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(-0.291172, -1.086666, -0.216506, 0, 0),
					g.addVertex(-0.314855, -1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(-0.314855, -1.175055, -0.125000, 0, 0),
					g.addVertex(-0.465537, -1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, -0.923880, -0.250000, 0, 0),
					g.addVertex(-0.258819, -0.965926, -0.250000, 0, 0),
					g.addVertex(-0.291172, -1.086666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, -0.923880, -0.250000, 0, 0),
					g.addVertex(-0.291172, -1.086666, -0.216506, 0, 0),
					g.addVertex(-0.430519, -1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(-0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(-0.226467, -0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(-0.226467, -0.845185, -0.216506, 0, 0),
					g.addVertex(-0.334848, -0.808395, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(-0.194114, -0.724444, 0.000000, 0, 0),
					g.addVertex(-0.202783, -0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(-0.202783, -0.756797, -0.125000, 0, 0),
					g.addVertex(-0.299830, -0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(-0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(-0.194114, -0.724444, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(-0.194114, -0.724444, 0.000000, 0, 0),
					g.addVertex(-0.287013, -0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, -0.808395, 0.216506, 0, 0),
					g.addVertex(-0.226467, -0.845185, 0.216506, 0, 0),
					g.addVertex(-0.202783, -0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, -0.808395, 0.216506, 0, 0),
					g.addVertex(-0.202783, -0.756797, 0.125000, 0, 0),
					g.addVertex(-0.299830, -0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(-0.291172, -1.086666, 0.216506, 0, 0),
					g.addVertex(-0.258819, -0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(-0.258819, -0.965926, 0.250000, 0, 0),
					g.addVertex(-0.382684, -0.923880, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(-0.314855, -1.175055, 0.125000, 0, 0),
					g.addVertex(-0.291172, -1.086666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(-0.291172, -1.086666, 0.216506, 0, 0),
					g.addVertex(-0.430519, -1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.478354, -1.154849, 0.000000, 0, 0),
					g.addVertex(-0.323524, -1.207407, 0.000000, 0, 0),
					g.addVertex(-0.314855, -1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.478354, -1.154849, 0.000000, 0, 0),
					g.addVertex(-0.314855, -1.175055, 0.125000, 0, 0),
					g.addVertex(-0.465537, -1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(-0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(-0.478354, -1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(-0.478354, -1.154849, 0.000000, 0, 0),
					g.addVertex(-0.625000, -1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(-0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(-0.465537, -1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(-0.465537, -1.123905, -0.125000, 0, 0),
					g.addVertex(-0.608253, -1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, -0.866026, -0.250000, 0, 0),
					g.addVertex(-0.382684, -0.923880, -0.250000, 0, 0),
					g.addVertex(-0.430519, -1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, -0.866026, -0.250000, 0, 0),
					g.addVertex(-0.430519, -1.039364, -0.216506, 0, 0),
					g.addVertex(-0.562500, -0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(-0.334848, -0.808395, -0.216506, 0, 0),
					g.addVertex(-0.382684, -0.923880, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(-0.382684, -0.923880, -0.250000, 0, 0),
					g.addVertex(-0.500000, -0.866026, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(-0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(-0.334848, -0.808395, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(-0.334848, -0.808395, -0.216506, 0, 0),
					g.addVertex(-0.437500, -0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(-0.287013, -0.692910, 0.000000, 0, 0),
					g.addVertex(-0.299830, -0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(-0.299830, -0.723854, -0.125000, 0, 0),
					g.addVertex(-0.391747, -0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(-0.334848, -0.808395, 0.216506, 0, 0),
					g.addVertex(-0.299830, -0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(-0.299830, -0.723854, 0.125000, 0, 0),
					g.addVertex(-0.391747, -0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, -0.866026, 0.250000, 0, 0),
					g.addVertex(-0.382684, -0.923880, 0.250000, 0, 0),
					g.addVertex(-0.334848, -0.808395, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, -0.866026, 0.250000, 0, 0),
					g.addVertex(-0.334848, -0.808395, 0.216506, 0, 0),
					g.addVertex(-0.437500, -0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(-0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(-0.382684, -0.923880, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(-0.382684, -0.923880, 0.250000, 0, 0),
					g.addVertex(-0.500000, -0.866026, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(-0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(-0.430519, -1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(-0.430519, -1.039364, 0.216506, 0, 0),
					g.addVertex(-0.562500, -0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(-0.478354, -1.154849, 0.000000, 0, 0),
					g.addVertex(-0.465537, -1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(-0.465537, -1.123905, 0.125000, 0, 0),
					g.addVertex(-0.608253, -1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740563, -0.965119, -0.125000, 0, 0),
					g.addVertex(-0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(-0.625000, -1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740563, -0.965119, -0.125000, 0, 0),
					g.addVertex(-0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(-0.760952, -0.991691, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, -0.892522, -0.216506, 0, 0),
					g.addVertex(-0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(-0.608253, -1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, -0.892522, -0.216506, 0, 0),
					g.addVertex(-0.608253, -1.053525, -0.125000, 0, 0),
					g.addVertex(-0.740563, -0.965119, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608762, -0.793353, -0.250000, 0, 0),
					g.addVertex(-0.500000, -0.866026, -0.250000, 0, 0),
					g.addVertex(-0.562500, -0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608762, -0.793353, -0.250000, 0, 0),
					g.addVertex(-0.562500, -0.974279, -0.216506, 0, 0),
					g.addVertex(-0.684857, -0.892522, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532667, -0.694184, -0.216506, 0, 0),
					g.addVertex(-0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(-0.500000, -0.866026, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532667, -0.694184, -0.216506, 0, 0),
					g.addVertex(-0.500000, -0.866026, -0.250000, 0, 0),
					g.addVertex(-0.608762, -0.793353, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(-0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(-0.437500, -0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(-0.437500, -0.757772, -0.216506, 0, 0),
					g.addVertex(-0.532667, -0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(-0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(-0.391747, -0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(-0.391747, -0.678525, -0.125000, 0, 0),
					g.addVertex(-0.476961, -0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(-0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(-0.375000, -0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(-0.375000, -0.649519, 0.000000, 0, 0),
					g.addVertex(-0.456571, -0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532667, -0.694184, 0.216506, 0, 0),
					g.addVertex(-0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(-0.391747, -0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532667, -0.694184, 0.216506, 0, 0),
					g.addVertex(-0.391747, -0.678525, 0.125000, 0, 0),
					g.addVertex(-0.476961, -0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608762, -0.793353, 0.250000, 0, 0),
					g.addVertex(-0.500000, -0.866026, 0.250000, 0, 0),
					g.addVertex(-0.437500, -0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608762, -0.793353, 0.250000, 0, 0),
					g.addVertex(-0.437500, -0.757772, 0.216506, 0, 0),
					g.addVertex(-0.532667, -0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, -0.892522, 0.216506, 0, 0),
					g.addVertex(-0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(-0.500000, -0.866026, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, -0.892522, 0.216506, 0, 0),
					g.addVertex(-0.500000, -0.866026, 0.250000, 0, 0),
					g.addVertex(-0.608762, -0.793353, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740563, -0.965119, 0.125000, 0, 0),
					g.addVertex(-0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(-0.562500, -0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740563, -0.965119, 0.125000, 0, 0),
					g.addVertex(-0.562500, -0.974279, 0.216506, 0, 0),
					g.addVertex(-0.684857, -0.892522, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.760952, -0.991691, 0.000000, 0, 0),
					g.addVertex(-0.625000, -1.082532, 0.000000, 0, 0),
					g.addVertex(-0.608253, -1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.760952, -0.991691, 0.000000, 0, 0),
					g.addVertex(-0.608253, -1.053525, 0.125000, 0, 0),
					g.addVertex(-0.740563, -0.965119, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, -0.860200, -0.125000, 0, 0),
					g.addVertex(-0.740563, -0.965119, -0.125000, 0, 0),
					g.addVertex(-0.760952, -0.991691, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, -0.860200, -0.125000, 0, 0),
					g.addVertex(-0.760952, -0.991691, 0.000000, 0, 0),
					g.addVertex(-0.883884, -0.883883, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, -0.795495, -0.216506, 0, 0),
					g.addVertex(-0.684857, -0.892522, -0.216506, 0, 0),
					g.addVertex(-0.740563, -0.965119, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, -0.795495, -0.216506, 0, 0),
					g.addVertex(-0.740563, -0.965119, -0.125000, 0, 0),
					g.addVertex(-0.860200, -0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, -0.707107, -0.250000, 0, 0),
					g.addVertex(-0.608762, -0.793353, -0.250000, 0, 0),
					g.addVertex(-0.684857, -0.892522, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, -0.707107, -0.250000, 0, 0),
					g.addVertex(-0.684857, -0.892522, -0.216506, 0, 0),
					g.addVertex(-0.795495, -0.795495, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, -0.618718, -0.216506, 0, 0),
					g.addVertex(-0.532667, -0.694184, -0.216506, 0, 0),
					g.addVertex(-0.608762, -0.793353, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, -0.618718, -0.216506, 0, 0),
					g.addVertex(-0.608762, -0.793353, -0.250000, 0, 0),
					g.addVertex(-0.707107, -0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, -0.554013, -0.125000, 0, 0),
					g.addVertex(-0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(-0.532667, -0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, -0.554013, -0.125000, 0, 0),
					g.addVertex(-0.532667, -0.694184, -0.216506, 0, 0),
					g.addVertex(-0.618719, -0.618718, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(-0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(-0.476961, -0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(-0.476961, -0.621587, -0.125000, 0, 0),
					g.addVertex(-0.554014, -0.554013, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, -0.554013, 0.125000, 0, 0),
					g.addVertex(-0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(-0.456571, -0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, -0.554013, 0.125000, 0, 0),
					g.addVertex(-0.456571, -0.595015, 0.000000, 0, 0),
					g.addVertex(-0.530330, -0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, -0.618718, 0.216506, 0, 0),
					g.addVertex(-0.532667, -0.694184, 0.216506, 0, 0),
					g.addVertex(-0.476961, -0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, -0.618718, 0.216506, 0, 0),
					g.addVertex(-0.476961, -0.621587, 0.125000, 0, 0),
					g.addVertex(-0.554014, -0.554013, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, -0.707107, 0.250000, 0, 0),
					g.addVertex(-0.608762, -0.793353, 0.250000, 0, 0),
					g.addVertex(-0.532667, -0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, -0.707107, 0.250000, 0, 0),
					g.addVertex(-0.532667, -0.694184, 0.216506, 0, 0),
					g.addVertex(-0.618719, -0.618718, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, -0.795495, 0.216506, 0, 0),
					g.addVertex(-0.684857, -0.892522, 0.216506, 0, 0),
					g.addVertex(-0.608762, -0.793353, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, -0.795495, 0.216506, 0, 0),
					g.addVertex(-0.608762, -0.793353, 0.250000, 0, 0),
					g.addVertex(-0.707107, -0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, -0.860200, 0.125000, 0, 0),
					g.addVertex(-0.740563, -0.965119, 0.125000, 0, 0),
					g.addVertex(-0.684857, -0.892522, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, -0.860200, 0.125000, 0, 0),
					g.addVertex(-0.684857, -0.892522, 0.216506, 0, 0),
					g.addVertex(-0.795495, -0.795495, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.883884, -0.883883, 0.000000, 0, 0),
					g.addVertex(-0.760952, -0.991691, 0.000000, 0, 0),
					g.addVertex(-0.740563, -0.965119, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.883884, -0.883883, 0.000000, 0, 0),
					g.addVertex(-0.740563, -0.965119, 0.125000, 0, 0),
					g.addVertex(-0.860200, -0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(-0.860200, -0.860200, -0.125000, 0, 0),
					g.addVertex(-0.883884, -0.883883, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(-0.883884, -0.883883, 0.000000, 0, 0),
					g.addVertex(-0.991692, -0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(-0.795495, -0.795495, -0.216506, 0, 0),
					g.addVertex(-0.860200, -0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(-0.860200, -0.860200, -0.125000, 0, 0),
					g.addVertex(-0.965119, -0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(-0.707107, -0.707107, -0.250000, 0, 0),
					g.addVertex(-0.795495, -0.795495, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(-0.795495, -0.795495, -0.216506, 0, 0),
					g.addVertex(-0.892523, -0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(-0.618719, -0.618718, -0.216506, 0, 0),
					g.addVertex(-0.707107, -0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(-0.707107, -0.707107, -0.250000, 0, 0),
					g.addVertex(-0.793353, -0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(-0.554014, -0.554013, -0.125000, 0, 0),
					g.addVertex(-0.618719, -0.618718, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(-0.618719, -0.618718, -0.216506, 0, 0),
					g.addVertex(-0.694184, -0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(-0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(-0.554014, -0.554013, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(-0.554014, -0.554013, -0.125000, 0, 0),
					g.addVertex(-0.621587, -0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(-0.554014, -0.554013, 0.125000, 0, 0),
					g.addVertex(-0.530330, -0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(-0.530330, -0.530330, 0.000000, 0, 0),
					g.addVertex(-0.595015, -0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(-0.707107, -0.707107, 0.250000, 0, 0),
					g.addVertex(-0.618719, -0.618718, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(-0.618719, -0.618718, 0.216506, 0, 0),
					g.addVertex(-0.694184, -0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(-0.795495, -0.795495, 0.216506, 0, 0),
					g.addVertex(-0.707107, -0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(-0.707107, -0.707107, 0.250000, 0, 0),
					g.addVertex(-0.793353, -0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(-0.860200, -0.860200, 0.125000, 0, 0),
					g.addVertex(-0.795495, -0.795495, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(-0.795495, -0.795495, 0.216506, 0, 0),
					g.addVertex(-0.892523, -0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(-0.883884, -0.883883, 0.000000, 0, 0),
					g.addVertex(-0.860200, -0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(-0.860200, -0.860200, 0.125000, 0, 0),
					g.addVertex(-0.965119, -0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
					g.addVertex(-0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(-0.991692, -0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
					g.addVertex(-0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(-1.082532, -0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(-0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(-0.965119, -0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(-0.965119, -0.740562, -0.125000, 0, 0),
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866026, -0.500000, -0.250000, 0, 0),
					g.addVertex(-0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(-0.892523, -0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866026, -0.500000, -0.250000, 0, 0),
					g.addVertex(-0.892523, -0.684857, -0.216506, 0, 0),
					g.addVertex(-0.974279, -0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(-0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(-0.793353, -0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(-0.793353, -0.608761, -0.250000, 0, 0),
					g.addVertex(-0.866026, -0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678526, -0.391747, -0.125000, 0, 0),
					g.addVertex(-0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(-0.694184, -0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678526, -0.391747, -0.125000, 0, 0),
					g.addVertex(-0.694184, -0.532666, -0.216506, 0, 0),
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(-0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(-0.621587, -0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(-0.621587, -0.476961, -0.125000, 0, 0),
					g.addVertex(-0.678526, -0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678526, -0.391747, 0.125000, 0, 0),
					g.addVertex(-0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(-0.595015, -0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678526, -0.391747, 0.125000, 0, 0),
					g.addVertex(-0.595015, -0.456571, 0.000000, 0, 0),
					g.addVertex(-0.649519, -0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(-0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(-0.621587, -0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(-0.621587, -0.476961, 0.125000, 0, 0),
					g.addVertex(-0.678526, -0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866026, -0.500000, 0.250000, 0, 0),
					g.addVertex(-0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(-0.694184, -0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866026, -0.500000, 0.250000, 0, 0),
					g.addVertex(-0.694184, -0.532666, 0.216506, 0, 0),
					g.addVertex(-0.757772, -0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(-0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(-0.793353, -0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(-0.793353, -0.608761, 0.250000, 0, 0),
					g.addVertex(-0.866026, -0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053526, -0.608253, 0.125000, 0, 0),
					g.addVertex(-0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(-0.892523, -0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053526, -0.608253, 0.125000, 0, 0),
					g.addVertex(-0.892523, -0.684857, 0.216506, 0, 0),
					g.addVertex(-0.974279, -0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(-0.991692, -0.760952, 0.000000, 0, 0),
					g.addVertex(-0.965119, -0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(-0.965119, -0.740562, 0.125000, 0, 0),
					g.addVertex(-1.053526, -0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123906, -0.465536, -0.125000, 0, 0),
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
					g.addVertex(-1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039365, -0.430518, -0.216506, 0, 0),
					g.addVertex(-0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039365, -0.430518, -0.216506, 0, 0),
					g.addVertex(-1.053526, -0.608253, -0.125000, 0, 0),
					g.addVertex(-1.123906, -0.465536, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
					g.addVertex(-0.866026, -0.500000, -0.250000, 0, 0),
					g.addVertex(-0.974279, -0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
					g.addVertex(-0.974279, -0.562500, -0.216506, 0, 0),
					g.addVertex(-1.039365, -0.430518, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(-0.678526, -0.391747, -0.125000, 0, 0),
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(-0.757772, -0.437500, -0.216506, 0, 0),
					g.addVertex(-0.808395, -0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.692910, -0.287012, 0.000000, 0, 0),
					g.addVertex(-0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(-0.678526, -0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.692910, -0.287012, 0.000000, 0, 0),
					g.addVertex(-0.678526, -0.391747, -0.125000, 0, 0),
					g.addVertex(-0.723854, -0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(-0.678526, -0.391747, 0.125000, 0, 0),
					g.addVertex(-0.649519, -0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(-0.649519, -0.375000, 0.000000, 0, 0),
					g.addVertex(-0.692910, -0.287012, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808395, -0.334848, 0.216506, 0, 0),
					g.addVertex(-0.757772, -0.437500, 0.216506, 0, 0),
					g.addVertex(-0.678526, -0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808395, -0.334848, 0.216506, 0, 0),
					g.addVertex(-0.678526, -0.391747, 0.125000, 0, 0),
					g.addVertex(-0.723854, -0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
					g.addVertex(-0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(-0.866026, -0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
					g.addVertex(-0.866026, -0.500000, 0.250000, 0, 0),
					g.addVertex(-0.923880, -0.382683, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123906, -0.465536, 0.125000, 0, 0),
					g.addVertex(-1.053526, -0.608253, 0.125000, 0, 0),
					g.addVertex(-0.974279, -0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123906, -0.465536, 0.125000, 0, 0),
					g.addVertex(-0.974279, -0.562500, 0.216506, 0, 0),
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
					g.addVertex(-1.082532, -0.625000, 0.000000, 0, 0),
					g.addVertex(-1.053526, -0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
					g.addVertex(-1.053526, -0.608253, 0.125000, 0, 0),
					g.addVertex(-1.123906, -0.465536, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(-1.123906, -0.465536, -0.125000, 0, 0),
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
					g.addVertex(-1.207407, -0.323524, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(-1.039365, -0.430518, -0.216506, 0, 0),
					g.addVertex(-1.123906, -0.465536, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(-1.123906, -0.465536, -0.125000, 0, 0),
					g.addVertex(-1.175055, -0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
					g.addVertex(-1.039365, -0.430518, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(-1.039365, -0.430518, -0.216506, 0, 0),
					g.addVertex(-1.086667, -0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, -0.226467, -0.216506, 0, 0),
					g.addVertex(-0.808395, -0.334848, -0.216506, 0, 0),
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, -0.226467, -0.216506, 0, 0),
					g.addVertex(-0.923880, -0.382683, -0.250000, 0, 0),
					g.addVertex(-0.965926, -0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(-0.692910, -0.287012, 0.000000, 0, 0),
					g.addVertex(-0.723854, -0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(-0.723854, -0.299830, -0.125000, 0, 0),
					g.addVertex(-0.756797, -0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(-0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(-0.692910, -0.287012, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(-0.692910, -0.287012, 0.000000, 0, 0),
					g.addVertex(-0.724444, -0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, -0.226467, 0.216506, 0, 0),
					g.addVertex(-0.808395, -0.334848, 0.216506, 0, 0),
					g.addVertex(-0.723854, -0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, -0.226467, 0.216506, 0, 0),
					g.addVertex(-0.723854, -0.299830, 0.125000, 0, 0),
					g.addVertex(-0.756797, -0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(-0.923880, -0.382683, 0.250000, 0, 0),
					g.addVertex(-0.808395, -0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(-0.808395, -0.334848, 0.216506, 0, 0),
					g.addVertex(-0.845185, -0.226467, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
					g.addVertex(-0.923880, -0.382683, 0.250000, 0, 0),
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(-1.123906, -0.465536, 0.125000, 0, 0),
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(-1.039365, -0.430518, 0.216506, 0, 0),
					g.addVertex(-1.086667, -0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.207407, -0.323524, 0.000000, 0, 0),
					g.addVertex(-1.154850, -0.478354, 0.000000, 0, 0),
					g.addVertex(-1.123906, -0.465536, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.207407, -0.323524, 0.000000, 0, 0),
					g.addVertex(-1.123906, -0.465536, 0.125000, 0, 0),
					g.addVertex(-1.175055, -0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(-1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(-1.207407, -0.323524, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(-1.207407, -0.323524, 0.000000, 0, 0),
					g.addVertex(-1.239306, -0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(-1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(-1.175055, -0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(-1.175055, -0.314855, -0.125000, 0, 0),
					g.addVertex(-1.206099, -0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(-0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(-1.086667, -0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(-1.086667, -0.291171, -0.216506, 0, 0),
					g.addVertex(-1.115376, -0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, -0.114211, -0.216506, 0, 0),
					g.addVertex(-0.845185, -0.226467, -0.216506, 0, 0),
					g.addVertex(-0.965926, -0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, -0.114211, -0.216506, 0, 0),
					g.addVertex(-0.965926, -0.258819, -0.250000, 0, 0),
					g.addVertex(-0.991445, -0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, -0.102267, -0.125000, 0, 0),
					g.addVertex(-0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(-0.845185, -0.226467, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, -0.102267, -0.125000, 0, 0),
					g.addVertex(-0.845185, -0.226467, -0.216506, 0, 0),
					g.addVertex(-0.867514, -0.114211, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(-0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(-0.756797, -0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(-0.756797, -0.202783, -0.125000, 0, 0),
					g.addVertex(-0.776791, -0.102267, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, -0.102267, 0.125000, 0, 0),
					g.addVertex(-0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(-0.724444, -0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, -0.102267, 0.125000, 0, 0),
					g.addVertex(-0.724444, -0.194114, 0.000000, 0, 0),
					g.addVertex(-0.743584, -0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, -0.114211, 0.216506, 0, 0),
					g.addVertex(-0.845185, -0.226467, 0.216506, 0, 0),
					g.addVertex(-0.756797, -0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, -0.114211, 0.216506, 0, 0),
					g.addVertex(-0.756797, -0.202783, 0.125000, 0, 0),
					g.addVertex(-0.776791, -0.102267, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(-0.845185, -0.226467, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(-0.845185, -0.226467, 0.216506, 0, 0),
					g.addVertex(-0.867514, -0.114211, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(-1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(-0.965926, -0.258819, 0.250000, 0, 0),
					g.addVertex(-0.991445, -0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(-1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(-1.086667, -0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(-1.086667, -0.291171, 0.216506, 0, 0),
					g.addVertex(-1.115376, -0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(-1.207407, -0.323524, 0.000000, 0, 0),
					g.addVertex(-1.175055, -0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(-1.175055, -0.314855, 0.125000, 0, 0),
					g.addVertex(-1.206099, -0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.216506, 0.000000, -0.125000, 0, 0),
					g.addVertex(-1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(-1.239306, -0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.216506, 0.000000, -0.125000, 0, 0),
					g.addVertex(-1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(-1.250000, 0.000000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(-1.206099, -0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-1.206099, -0.158786, -0.125000, 0, 0),
					g.addVertex(-1.216506, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(-0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(-1.115376, -0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(-1.115376, -0.146842, -0.216506, 0, 0),
					g.addVertex(-1.125000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-0.867514, -0.114211, -0.216506, 0, 0),
					g.addVertex(-0.991445, -0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-0.991445, -0.130526, -0.250000, 0, 0),
					g.addVertex(-1.000000, 0.000000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(-0.776791, -0.102267, -0.125000, 0, 0),
					g.addVertex(-0.867514, -0.114211, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(-0.867514, -0.114211, -0.216506, 0, 0),
					g.addVertex(-0.875000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(-0.776791, -0.102267, 0.125000, 0, 0),
					g.addVertex(-0.743584, -0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(-0.743584, -0.097895, 0.000000, 0, 0),
					g.addVertex(-0.750000, 0.000000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(-0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(-0.867514, -0.114211, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(-0.867514, -0.114211, 0.216506, 0, 0),
					g.addVertex(-0.875000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(-0.991445, -0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-0.991445, -0.130526, 0.250000, 0, 0),
					g.addVertex(-1.000000, 0.000000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(-1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(-1.115376, -0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(-1.115376, -0.146842, 0.216506, 0, 0),
					g.addVertex(-1.125000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-1.239306, -0.163158, 0.000000, 0, 0),
					g.addVertex(-1.206099, -0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-1.206099, -0.158786, 0.125000, 0, 0),
					g.addVertex(-1.216506, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(-1.216506, 0.000000, -0.125000, 0, 0),
					g.addVertex(-1.250000, 0.000000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(-1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-1.239306, 0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(-1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-1.216506, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(-1.216506, 0.000000, -0.125000, 0, 0),
					g.addVertex(-1.206099, 0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, 0.114211, -0.216506, 0, 0),
					g.addVertex(-0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-1.000000, 0.000000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, 0.114211, -0.216506, 0, 0),
					g.addVertex(-1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(-0.991445, 0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, 0.102267, -0.125000, 0, 0),
					g.addVertex(-0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(-0.875000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, 0.102267, -0.125000, 0, 0),
					g.addVertex(-0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(-0.867514, 0.114211, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(-0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-0.783494, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(-0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(-0.776791, 0.102267, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, 0.102267, 0.125000, 0, 0),
					g.addVertex(-0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(-0.750000, 0.000000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.776791, 0.102267, 0.125000, 0, 0),
					g.addVertex(-0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-0.743584, 0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, 0.114211, 0.216506, 0, 0),
					g.addVertex(-0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-0.783494, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.867514, 0.114211, 0.216506, 0, 0),
					g.addVertex(-0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(-0.776791, 0.102267, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(-1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(-0.875000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(-0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-0.867514, 0.114211, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(-1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-1.000000, 0.000000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(-1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(-0.991445, 0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(-1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(-1.125000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(-1.125000, 0.000000, 0.216506, 0, 0),
					g.addVertex(-1.115376, 0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(-1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(-1.216506, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(-1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(-1.206099, 0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(-1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(-1.239306, 0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(-1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(-1.207407, 0.323524, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(-1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(-1.206099, 0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(-1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(-1.175055, 0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(-0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(-1.115376, 0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(-1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(-1.086667, 0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(-0.867514, 0.114211, -0.216506, 0, 0),
					g.addVertex(-0.991445, 0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(-0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(-0.965926, 0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(-0.776791, 0.102267, -0.125000, 0, 0),
					g.addVertex(-0.867514, 0.114211, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(-0.867514, 0.114211, -0.216506, 0, 0),
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(-0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(-0.776791, 0.102267, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(-0.776791, 0.102267, -0.125000, 0, 0),
					g.addVertex(-0.756797, 0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(-0.776791, 0.102267, 0.125000, 0, 0),
					g.addVertex(-0.743584, 0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(-0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(-0.724444, 0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(-0.867514, 0.114211, 0.216506, 0, 0),
					g.addVertex(-0.776791, 0.102267, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(-0.776791, 0.102267, 0.125000, 0, 0),
					g.addVertex(-0.756797, 0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(-0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(-0.867514, 0.114211, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(-0.867514, 0.114211, 0.216506, 0, 0),
					g.addVertex(-0.845185, 0.226467, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(-1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(-0.991445, 0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(-0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(-0.965926, 0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(-1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(-1.115376, 0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(-1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(-1.086667, 0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(-1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(-1.206099, 0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(-1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(-1.175055, 0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(-1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(-1.207407, 0.323524, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(-1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(-1.154849, 0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039364, 0.430519, -0.216506, 0, 0),
					g.addVertex(-1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(-1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923879, 0.382683, -0.250000, 0, 0),
					g.addVertex(-0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(-1.039364, 0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(-1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(-1.039364, 0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808394, 0.334848, -0.216506, 0, 0),
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(-0.923879, 0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(-0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(-0.923879, 0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(-0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(-0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(-0.808394, 0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(-0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(-0.756797, 0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(-0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(-0.723854, 0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(-0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(-0.724444, 0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(-0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(-0.692910, 0.287013, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808394, 0.334848, 0.216506, 0, 0),
					g.addVertex(-0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(-0.756797, 0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808394, 0.334848, 0.216506, 0, 0),
					g.addVertex(-0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(-0.723854, 0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923879, 0.382683, 0.250000, 0, 0),
					g.addVertex(-0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(-0.845185, 0.226467, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923879, 0.382683, 0.250000, 0, 0),
					g.addVertex(-0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(-0.808394, 0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039364, 0.430519, 0.216506, 0, 0),
					g.addVertex(-1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(-0.965926, 0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039364, 0.430519, 0.216506, 0, 0),
					g.addVertex(-0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(-0.923879, 0.382683, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(-1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(-1.086667, 0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(-1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(-1.039364, 0.430519, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.154849, 0.478354, 0.000000, 0, 0),
					g.addVertex(-1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(-1.175055, 0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.154849, 0.478354, 0.000000, 0, 0),
					g.addVertex(-1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(-1.154849, 0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(-1.154849, 0.478354, 0.000000, 0, 0),
					g.addVertex(-1.082532, 0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(-1.039364, 0.430519, -0.216506, 0, 0),
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(-1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(-1.053525, 0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(-0.923879, 0.382683, -0.250000, 0, 0),
					g.addVertex(-1.039364, 0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(-1.039364, 0.430519, -0.216506, 0, 0),
					g.addVertex(-0.974279, 0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(-0.808394, 0.334848, -0.216506, 0, 0),
					g.addVertex(-0.923879, 0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(-0.923879, 0.382683, -0.250000, 0, 0),
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(-0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(-0.808394, 0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(-0.808394, 0.334848, -0.216506, 0, 0),
					g.addVertex(-0.757772, 0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(-0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(-0.723854, 0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(-0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(-0.678525, 0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(-0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(-0.692910, 0.287013, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(-0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(-0.649519, 0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(-0.808394, 0.334848, 0.216506, 0, 0),
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.808394, 0.334848, 0.216506, 0, 0),
					g.addVertex(-0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(-0.923879, 0.382683, 0.250000, 0, 0),
					g.addVertex(-0.757772, 0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.923879, 0.382683, 0.250000, 0, 0),
					g.addVertex(-0.808394, 0.334848, 0.216506, 0, 0),
					g.addVertex(-0.757772, 0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(-1.039364, 0.430519, 0.216506, 0, 0),
					g.addVertex(-0.866025, 0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.039364, 0.430519, 0.216506, 0, 0),
					g.addVertex(-0.923879, 0.382683, 0.250000, 0, 0),
					g.addVertex(-0.866025, 0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(-0.974279, 0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(-1.039364, 0.430519, 0.216506, 0, 0),
					g.addVertex(-0.974279, 0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(-1.154849, 0.478354, 0.000000, 0, 0),
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(-1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(-1.053525, 0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(-1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(-1.082532, 0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(-1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(-0.991692, 0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(-0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(-1.053525, 0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(-1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(-0.965119, 0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(-0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(-0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(-0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(-0.793353, 0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(-0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(-0.757772, 0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(-0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(-0.694184, 0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(-0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(-0.678525, 0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(-0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(-0.621587, 0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(-0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(-0.649519, 0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(-0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(-0.595015, 0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(-0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(-0.757772, 0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(-0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(-0.694184, 0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(-0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(-0.866025, 0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(-0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(-0.793353, 0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(-1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(-0.974279, 0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(-0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(-0.892523, 0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(-1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(-1.053525, 0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(-1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(-0.965119, 0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(-0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(-0.991692, 0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(-0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(-0.965119, 0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(-0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(-0.860200, 0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(-0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(-0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(-0.795495, 0.795495, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, 0.618718, -0.216506, 0, 0),
					g.addVertex(-0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(-0.793353, 0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, 0.618718, -0.216506, 0, 0),
					g.addVertex(-0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(-0.707107, 0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, 0.554013, -0.125000, 0, 0),
					g.addVertex(-0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(-0.694184, 0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, 0.554013, -0.125000, 0, 0),
					g.addVertex(-0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(-0.618719, 0.618718, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(-0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(-0.621587, 0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(-0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(-0.554014, 0.554013, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, 0.554013, 0.125000, 0, 0),
					g.addVertex(-0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(-0.595015, 0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.554014, 0.554013, 0.125000, 0, 0),
					g.addVertex(-0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(-0.530330, 0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
					g.addVertex(-0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(-0.621587, 0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
					g.addVertex(-0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(-0.554014, 0.554013, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(-0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(-0.694184, 0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(-0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(-0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(-0.793353, 0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(-0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(-0.707107, 0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(-0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(-0.892523, 0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(-0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(-0.795495, 0.795495, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
					g.addVertex(-0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(-0.965119, 0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
					g.addVertex(-0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(-0.860200, 0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(-0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
					g.addVertex(-0.760952, 0.991692, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(-0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(-0.860200, 0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(-0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(-0.740562, 0.965119, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608761, 0.793353, -0.250000, 0, 0),
					g.addVertex(-0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(-0.795495, 0.795495, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608761, 0.793353, -0.250000, 0, 0),
					g.addVertex(-0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(-0.684857, 0.892522, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(-0.554014, 0.554013, -0.125000, 0, 0),
					g.addVertex(-0.618719, 0.618718, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(-0.618719, 0.618718, -0.216506, 0, 0),
					g.addVertex(-0.532666, 0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(-0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(-0.554014, 0.554013, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(-0.554014, 0.554013, -0.125000, 0, 0),
					g.addVertex(-0.476961, 0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(-0.554014, 0.554013, 0.125000, 0, 0),
					g.addVertex(-0.530330, 0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(-0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(-0.456571, 0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
					g.addVertex(-0.554014, 0.554013, 0.125000, 0, 0),
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608761, 0.793353, 0.250000, 0, 0),
					g.addVertex(-0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608761, 0.793353, 0.250000, 0, 0),
					g.addVertex(-0.618719, 0.618718, 0.216506, 0, 0),
					g.addVertex(-0.532666, 0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(-0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(-0.707107, 0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(-0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(-0.608761, 0.793353, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(-0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(-0.795495, 0.795495, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(-0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(-0.684857, 0.892522, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.760952, 0.991692, 0.000000, 0, 0),
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
					g.addVertex(-0.740562, 0.965119, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.883884, 0.883883, 0.000000, 0, 0),
					g.addVertex(-0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(-0.740562, 0.965119, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(-0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(-0.760952, 0.991692, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(-0.760952, 0.991692, 0.000000, 0, 0),
					g.addVertex(-0.625000, 1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(-0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(-0.740562, 0.965119, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(-0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(-0.608253, 1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, 0.866026, -0.250000, 0, 0),
					g.addVertex(-0.608761, 0.793353, -0.250000, 0, 0),
					g.addVertex(-0.684857, 0.892522, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, 0.866026, -0.250000, 0, 0),
					g.addVertex(-0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(-0.562500, 0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(-0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(-0.608761, 0.793353, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(-0.608761, 0.793353, -0.250000, 0, 0),
					g.addVertex(-0.500000, 0.866026, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(-0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(-0.532666, 0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(-0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(-0.437500, 0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(-0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(-0.476961, 0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(-0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(-0.391747, 0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(-0.456571, 0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(-0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(-0.375000, 0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(-0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(-0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(-0.391747, 0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, 0.866026, 0.250000, 0, 0),
					g.addVertex(-0.608761, 0.793353, 0.250000, 0, 0),
					g.addVertex(-0.532666, 0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.500000, 0.866026, 0.250000, 0, 0),
					g.addVertex(-0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(-0.437500, 0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(-0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(-0.608761, 0.793353, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(-0.608761, 0.793353, 0.250000, 0, 0),
					g.addVertex(-0.500000, 0.866026, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(-0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(-0.684857, 0.892522, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(-0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(-0.562500, 0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(-0.760952, 0.991692, 0.000000, 0, 0),
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.760952, 0.991692, 0.000000, 0, 0),
					g.addVertex(-0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(-0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(-0.625000, 1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(-0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(-0.478354, 1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, 0.923880, -0.250000, 0, 0),
					g.addVertex(-0.500000, 0.866026, -0.250000, 0, 0),
					g.addVertex(-0.562500, 0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, 0.923880, -0.250000, 0, 0),
					g.addVertex(-0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(-0.430519, 1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, 0.808395, -0.216506, 0, 0),
					g.addVertex(-0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(-0.500000, 0.866026, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, 0.808395, -0.216506, 0, 0),
					g.addVertex(-0.500000, 0.866026, -0.250000, 0, 0),
					g.addVertex(-0.382684, 0.923880, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(-0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(-0.437500, 0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(-0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(-0.334848, 0.808395, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(-0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(-0.391747, 0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(-0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(-0.299830, 0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(-0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(-0.375000, 0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(-0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(-0.287013, 0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, 0.808395, 0.216506, 0, 0),
					g.addVertex(-0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(-0.391747, 0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.334848, 0.808395, 0.216506, 0, 0),
					g.addVertex(-0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(-0.299830, 0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, 0.923880, 0.250000, 0, 0),
					g.addVertex(-0.500000, 0.866026, 0.250000, 0, 0),
					g.addVertex(-0.437500, 0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.382684, 0.923880, 0.250000, 0, 0),
					g.addVertex(-0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(-0.334848, 0.808395, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(-0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(-0.500000, 0.866026, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(-0.500000, 0.866026, 0.250000, 0, 0),
					g.addVertex(-0.382684, 0.923880, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(-0.562500, 0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(-0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(-0.430519, 1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.478354, 1.154849, 0.000000, 0, 0),
					g.addVertex(-0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.478354, 1.154849, 0.000000, 0, 0),
					g.addVertex(-0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(-0.465537, 1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(-0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(-0.478354, 1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(-0.478354, 1.154849, 0.000000, 0, 0),
					g.addVertex(-0.323524, 1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291171, 1.086667, -0.216506, 0, 0),
					g.addVertex(-0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(-0.465537, 1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291171, 1.086667, -0.216506, 0, 0),
					g.addVertex(-0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(-0.314855, 1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(-0.334848, 0.808395, -0.216506, 0, 0),
					g.addVertex(-0.382684, 0.923880, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(-0.382684, 0.923880, -0.250000, 0, 0),
					g.addVertex(-0.258819, 0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(-0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(-0.334848, 0.808395, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(-0.334848, 0.808395, -0.216506, 0, 0),
					g.addVertex(-0.226467, 0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(-0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(-0.299830, 0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(-0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(-0.202783, 0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(-0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(-0.287013, 0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(-0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(-0.194114, 0.724444, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(-0.334848, 0.808395, 0.216506, 0, 0),
					g.addVertex(-0.299830, 0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(-0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(-0.202783, 0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(-0.382684, 0.923880, 0.250000, 0, 0),
					g.addVertex(-0.334848, 0.808395, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(-0.334848, 0.808395, 0.216506, 0, 0),
					g.addVertex(-0.226467, 0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291171, 1.086667, 0.216506, 0, 0),
					g.addVertex(-0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(-0.382684, 0.923880, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.291171, 1.086667, 0.216506, 0, 0),
					g.addVertex(-0.382684, 0.923880, 0.250000, 0, 0),
					g.addVertex(-0.258819, 0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(-0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(-0.430519, 1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(-0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(-0.291171, 1.086667, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(-0.478354, 1.154849, 0.000000, 0, 0),
					g.addVertex(-0.465537, 1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(-0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(-0.314855, 1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(-0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(-0.323524, 1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(-0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(-0.163158, 1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146842, 1.115375, -0.216506, 0, 0),
					g.addVertex(-0.291171, 1.086667, -0.216506, 0, 0),
					g.addVertex(-0.314855, 1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146842, 1.115375, -0.216506, 0, 0),
					g.addVertex(-0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(-0.158786, 1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(-0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(-0.291171, 1.086667, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(-0.291171, 1.086667, -0.216506, 0, 0),
					g.addVertex(-0.146842, 1.115375, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, 0.867514, -0.216506, 0, 0),
					g.addVertex(-0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(-0.258819, 0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, 0.867514, -0.216506, 0, 0),
					g.addVertex(-0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(-0.130526, 0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, 0.776791, -0.125000, 0, 0),
					g.addVertex(-0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(-0.226467, 0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, 0.776791, -0.125000, 0, 0),
					g.addVertex(-0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(-0.114211, 0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(-0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(-0.202783, 0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(-0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(-0.102267, 0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, 0.776791, 0.125000, 0, 0),
					g.addVertex(-0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(-0.194114, 0.724444, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.102267, 0.776791, 0.125000, 0, 0),
					g.addVertex(-0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(-0.097895, 0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, 0.867514, 0.216506, 0, 0),
					g.addVertex(-0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(-0.202783, 0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.114211, 0.867514, 0.216506, 0, 0),
					g.addVertex(-0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(-0.102267, 0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(-0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(-0.226467, 0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(-0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(-0.114211, 0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146842, 1.115375, 0.216506, 0, 0),
					g.addVertex(-0.291171, 1.086667, 0.216506, 0, 0),
					g.addVertex(-0.258819, 0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.146842, 1.115375, 0.216506, 0, 0),
					g.addVertex(-0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(-0.130526, 0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(-0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(-0.291171, 1.086667, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(-0.291171, 1.086667, 0.216506, 0, 0),
					g.addVertex(-0.146842, 1.115375, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(-0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(-0.314855, 1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(-0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(-0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(-0.158786, 1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.216506, -0.125000, 0, 0),
					g.addVertex(-0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(-0.163158, 1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.216506, -0.125000, 0, 0),
					g.addVertex(-0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(0.000000, 1.250000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.000000, -0.250000, 0, 0),
					g.addVertex(-0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(-0.146842, 1.115375, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.000000, -0.250000, 0, 0),
					g.addVertex(-0.146842, 1.115375, -0.216506, 0, 0),
					g.addVertex(0.000000, 1.125000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.875000, -0.216506, 0, 0),
					g.addVertex(-0.114211, 0.867514, -0.216506, 0, 0),
					g.addVertex(-0.130526, 0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.875000, -0.216506, 0, 0),
					g.addVertex(-0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(0.000000, 1.000000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.783494, -0.125000, 0, 0),
					g.addVertex(-0.102267, 0.776791, -0.125000, 0, 0),
					g.addVertex(-0.114211, 0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.783494, -0.125000, 0, 0),
					g.addVertex(-0.114211, 0.867514, -0.216506, 0, 0),
					g.addVertex(0.000000, 0.875000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.750000, 0.000000, 0, 0),
					g.addVertex(-0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(-0.102267, 0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.750000, 0.000000, 0, 0),
					g.addVertex(-0.102267, 0.776791, -0.125000, 0, 0),
					g.addVertex(0.000000, 0.783494, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.783494, 0.125000, 0, 0),
					g.addVertex(-0.102267, 0.776791, 0.125000, 0, 0),
					g.addVertex(-0.097895, 0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.783494, 0.125000, 0, 0),
					g.addVertex(-0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(0.000000, 0.750000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.875000, 0.216506, 0, 0),
					g.addVertex(-0.114211, 0.867514, 0.216506, 0, 0),
					g.addVertex(-0.102267, 0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 0.875000, 0.216506, 0, 0),
					g.addVertex(-0.102267, 0.776791, 0.125000, 0, 0),
					g.addVertex(0.000000, 0.783494, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.000000, 0.250000, 0, 0),
					g.addVertex(-0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(-0.114211, 0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.000000, 0.250000, 0, 0),
					g.addVertex(-0.114211, 0.867514, 0.216506, 0, 0),
					g.addVertex(0.000000, 0.875000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.125000, 0.216506, 0, 0),
					g.addVertex(-0.146842, 1.115375, 0.216506, 0, 0),
					g.addVertex(-0.130526, 0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.125000, 0.216506, 0, 0),
					g.addVertex(-0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(0.000000, 1.000000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.216506, 0.125000, 0, 0),
					g.addVertex(-0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(-0.146842, 1.115375, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.216506, 0.125000, 0, 0),
					g.addVertex(-0.146842, 1.115375, 0.216506, 0, 0),
					g.addVertex(0.000000, 1.125000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.250000, 0.000000, 0, 0),
					g.addVertex(-0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(-0.158786, 1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.000000, 1.250000, 0.000000, 0, 0),
					g.addVertex(-0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(0.000000, 1.216506, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(0.000000, 1.216506, -0.125000, 0, 0),
					g.addVertex(0.000000, 1.250000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(0.000000, 1.250000, 0.000000, 0, 0),
					g.addVertex(0.163158, 1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, 1.115376, -0.216506, 0, 0),
					g.addVertex(0.000000, 1.125000, -0.216506, 0, 0),
					g.addVertex(0.000000, 1.216506, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, 1.115376, -0.216506, 0, 0),
					g.addVertex(0.000000, 1.216506, -0.125000, 0, 0),
					g.addVertex(0.158786, 1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(0.000000, 1.000000, -0.250000, 0, 0),
					g.addVertex(0.000000, 1.125000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(0.000000, 1.125000, -0.216506, 0, 0),
					g.addVertex(0.146842, 1.115376, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, 0.867514, -0.216506, 0, 0),
					g.addVertex(0.000000, 0.875000, -0.216506, 0, 0),
					g.addVertex(0.000000, 1.000000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, 0.867514, -0.216506, 0, 0),
					g.addVertex(0.000000, 1.000000, -0.250000, 0, 0),
					g.addVertex(0.130526, 0.991445, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, 0.776791, -0.125000, 0, 0),
					g.addVertex(0.000000, 0.783494, -0.125000, 0, 0),
					g.addVertex(0.000000, 0.875000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, 0.776791, -0.125000, 0, 0),
					g.addVertex(0.000000, 0.875000, -0.216506, 0, 0),
					g.addVertex(0.114210, 0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(0.000000, 0.750000, 0.000000, 0, 0),
					g.addVertex(0.000000, 0.783494, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(0.000000, 0.783494, -0.125000, 0, 0),
					g.addVertex(0.102266, 0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, 0.776791, 0.125000, 0, 0),
					g.addVertex(0.000000, 0.783494, 0.125000, 0, 0),
					g.addVertex(0.000000, 0.750000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.102266, 0.776791, 0.125000, 0, 0),
					g.addVertex(0.000000, 0.750000, 0.000000, 0, 0),
					g.addVertex(0.097895, 0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, 0.867514, 0.216506, 0, 0),
					g.addVertex(0.000000, 0.875000, 0.216506, 0, 0),
					g.addVertex(0.000000, 0.783494, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.114210, 0.867514, 0.216506, 0, 0),
					g.addVertex(0.000000, 0.783494, 0.125000, 0, 0),
					g.addVertex(0.102266, 0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(0.000000, 1.000000, 0.250000, 0, 0),
					g.addVertex(0.000000, 0.875000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(0.000000, 0.875000, 0.216506, 0, 0),
					g.addVertex(0.114210, 0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, 1.115376, 0.216506, 0, 0),
					g.addVertex(0.000000, 1.125000, 0.216506, 0, 0),
					g.addVertex(0.000000, 1.000000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.146842, 1.115376, 0.216506, 0, 0),
					g.addVertex(0.000000, 1.000000, 0.250000, 0, 0),
					g.addVertex(0.130526, 0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(0.000000, 1.216506, 0.125000, 0, 0),
					g.addVertex(0.000000, 1.125000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(0.000000, 1.125000, 0.216506, 0, 0),
					g.addVertex(0.146842, 1.115376, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(0.000000, 1.250000, 0.000000, 0, 0),
					g.addVertex(0.000000, 1.216506, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(0.000000, 1.216506, 0.125000, 0, 0),
					g.addVertex(0.158786, 1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(0.163158, 1.239306, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(0.323524, 1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, 1.086666, -0.216506, 0, 0),
					g.addVertex(0.146842, 1.115376, -0.216506, 0, 0),
					g.addVertex(0.158786, 1.206099, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, 1.086666, -0.216506, 0, 0),
					g.addVertex(0.158786, 1.206099, -0.125000, 0, 0),
					g.addVertex(0.314855, 1.175055, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(0.130526, 0.991445, -0.250000, 0, 0),
					g.addVertex(0.146842, 1.115376, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(0.146842, 1.115376, -0.216506, 0, 0),
					g.addVertex(0.291171, 1.086666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(0.102266, 0.776791, -0.125000, 0, 0),
					g.addVertex(0.114210, 0.867514, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(0.114210, 0.867514, -0.216506, 0, 0),
					g.addVertex(0.226467, 0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(0.102266, 0.776791, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(0.102266, 0.776791, -0.125000, 0, 0),
					g.addVertex(0.202783, 0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(0.102266, 0.776791, 0.125000, 0, 0),
					g.addVertex(0.097895, 0.743584, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(0.097895, 0.743584, 0.000000, 0, 0),
					g.addVertex(0.194114, 0.724444, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(0.114210, 0.867514, 0.216506, 0, 0),
					g.addVertex(0.102266, 0.776791, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(0.102266, 0.776791, 0.125000, 0, 0),
					g.addVertex(0.202783, 0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(0.114210, 0.867514, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(0.114210, 0.867514, 0.216506, 0, 0),
					g.addVertex(0.226467, 0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, 1.086666, 0.216506, 0, 0),
					g.addVertex(0.146842, 1.115376, 0.216506, 0, 0),
					g.addVertex(0.130526, 0.991445, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.291171, 1.086666, 0.216506, 0, 0),
					g.addVertex(0.130526, 0.991445, 0.250000, 0, 0),
					g.addVertex(0.258819, 0.965926, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(0.146842, 1.115376, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(0.146842, 1.115376, 0.216506, 0, 0),
					g.addVertex(0.291171, 1.086666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(0.163158, 1.239306, 0.000000, 0, 0),
					g.addVertex(0.158786, 1.206099, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(0.158786, 1.206099, 0.125000, 0, 0),
					g.addVertex(0.314855, 1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(0.314855, 1.175055, -0.125000, 0, 0),
					g.addVertex(0.323524, 1.207407, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(0.478355, 1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, 0.923879, -0.250000, 0, 0),
					g.addVertex(0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(0.291171, 1.086666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, 0.923879, -0.250000, 0, 0),
					g.addVertex(0.291171, 1.086666, -0.216506, 0, 0),
					g.addVertex(0.430519, 1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, 0.808394, -0.216506, 0, 0),
					g.addVertex(0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(0.258819, 0.965926, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, 0.808394, -0.216506, 0, 0),
					g.addVertex(0.258819, 0.965926, -0.250000, 0, 0),
					g.addVertex(0.382684, 0.923879, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(0.226467, 0.845185, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(0.226467, 0.845185, -0.216506, 0, 0),
					g.addVertex(0.334848, 0.808394, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(0.202783, 0.756797, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(0.202783, 0.756797, -0.125000, 0, 0),
					g.addVertex(0.299830, 0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(0.194114, 0.724444, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(0.194114, 0.724444, 0.000000, 0, 0),
					g.addVertex(0.287013, 0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, 0.808394, 0.216506, 0, 0),
					g.addVertex(0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(0.202783, 0.756797, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.334848, 0.808394, 0.216506, 0, 0),
					g.addVertex(0.202783, 0.756797, 0.125000, 0, 0),
					g.addVertex(0.299830, 0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, 0.923879, 0.250000, 0, 0),
					g.addVertex(0.258819, 0.965926, 0.250000, 0, 0),
					g.addVertex(0.226467, 0.845185, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.382684, 0.923879, 0.250000, 0, 0),
					g.addVertex(0.226467, 0.845185, 0.216506, 0, 0),
					g.addVertex(0.334848, 0.808394, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(0.291171, 1.086666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(0.291171, 1.086666, 0.216506, 0, 0),
					g.addVertex(0.430519, 1.039364, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.478355, 1.154849, 0.000000, 0, 0),
					g.addVertex(0.323524, 1.207407, 0.000000, 0, 0),
					g.addVertex(0.314855, 1.175055, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.478355, 1.154849, 0.000000, 0, 0),
					g.addVertex(0.314855, 1.175055, 0.125000, 0, 0),
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(0.478355, 1.154849, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(0.478355, 1.154849, 0.000000, 0, 0),
					g.addVertex(0.625000, 1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(0.465537, 1.123905, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(0.465537, 1.123905, -0.125000, 0, 0),
					g.addVertex(0.608253, 1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, 0.866025, -0.250000, 0, 0),
					g.addVertex(0.382684, 0.923879, -0.250000, 0, 0),
					g.addVertex(0.430519, 1.039364, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, 0.866025, -0.250000, 0, 0),
					g.addVertex(0.430519, 1.039364, -0.216506, 0, 0),
					g.addVertex(0.562500, 0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(0.334848, 0.808394, -0.216506, 0, 0),
					g.addVertex(0.382684, 0.923879, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(0.382684, 0.923879, -0.250000, 0, 0),
					g.addVertex(0.500000, 0.866025, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(0.334848, 0.808394, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(0.334848, 0.808394, -0.216506, 0, 0),
					g.addVertex(0.437500, 0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(0.299830, 0.723854, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(0.299830, 0.723854, -0.125000, 0, 0),
					g.addVertex(0.391747, 0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(0.287013, 0.692910, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(0.287013, 0.692910, 0.000000, 0, 0),
					g.addVertex(0.375000, 0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(0.334848, 0.808394, 0.216506, 0, 0),
					g.addVertex(0.299830, 0.723854, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(0.299830, 0.723854, 0.125000, 0, 0),
					g.addVertex(0.391747, 0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, 0.866025, 0.250000, 0, 0),
					g.addVertex(0.382684, 0.923879, 0.250000, 0, 0),
					g.addVertex(0.334848, 0.808394, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.500000, 0.866025, 0.250000, 0, 0),
					g.addVertex(0.334848, 0.808394, 0.216506, 0, 0),
					g.addVertex(0.437500, 0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(0.430519, 1.039364, 0.216506, 0, 0),
					g.addVertex(0.382684, 0.923879, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(0.382684, 0.923879, 0.250000, 0, 0),
					g.addVertex(0.500000, 0.866025, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(0.478355, 1.154849, 0.000000, 0, 0),
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(0.465537, 1.123905, 0.125000, 0, 0),
					g.addVertex(0.608253, 1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(0.625000, 1.082532, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(0.760952, 0.991691, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(0.608253, 1.053525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(0.608253, 1.053525, -0.125000, 0, 0),
					g.addVertex(0.740562, 0.965119, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608762, 0.793353, -0.250000, 0, 0),
					g.addVertex(0.500000, 0.866025, -0.250000, 0, 0),
					g.addVertex(0.562500, 0.974279, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608762, 0.793353, -0.250000, 0, 0),
					g.addVertex(0.562500, 0.974279, -0.216506, 0, 0),
					g.addVertex(0.684857, 0.892522, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(0.500000, 0.866025, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(0.500000, 0.866025, -0.250000, 0, 0),
					g.addVertex(0.608762, 0.793353, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(0.437500, 0.757772, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(0.437500, 0.757772, -0.216506, 0, 0),
					g.addVertex(0.532666, 0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(0.391747, 0.678525, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(0.391747, 0.678525, -0.125000, 0, 0),
					g.addVertex(0.476961, 0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(0.375000, 0.649519, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(0.375000, 0.649519, 0.000000, 0, 0),
					g.addVertex(0.456571, 0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(0.391747, 0.678525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(0.391747, 0.678525, 0.125000, 0, 0),
					g.addVertex(0.476961, 0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608762, 0.793353, 0.250000, 0, 0),
					g.addVertex(0.500000, 0.866025, 0.250000, 0, 0),
					g.addVertex(0.437500, 0.757772, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.608762, 0.793353, 0.250000, 0, 0),
					g.addVertex(0.437500, 0.757772, 0.216506, 0, 0),
					g.addVertex(0.532666, 0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(0.500000, 0.866025, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(0.500000, 0.866025, 0.250000, 0, 0),
					g.addVertex(0.608762, 0.793353, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(0.562500, 0.974279, 0.216506, 0, 0),
					g.addVertex(0.684857, 0.892522, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.760952, 0.991691, 0.000000, 0, 0),
					g.addVertex(0.625000, 1.082532, 0.000000, 0, 0),
					g.addVertex(0.608253, 1.053525, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.760952, 0.991691, 0.000000, 0, 0),
					g.addVertex(0.608253, 1.053525, 0.125000, 0, 0),
					g.addVertex(0.740562, 0.965119, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(0.760952, 0.991691, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(0.760952, 0.991691, 0.000000, 0, 0),
					g.addVertex(0.883883, 0.883884, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(0.684857, 0.892522, -0.216506, 0, 0),
					g.addVertex(0.740562, 0.965119, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(0.740562, 0.965119, -0.125000, 0, 0),
					g.addVertex(0.860200, 0.860200, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, 0.618718, -0.216506, 0, 0),
					g.addVertex(0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(0.608762, 0.793353, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, 0.618718, -0.216506, 0, 0),
					g.addVertex(0.608762, 0.793353, -0.250000, 0, 0),
					g.addVertex(0.707107, 0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554014, 0.554014, -0.125000, 0, 0),
					g.addVertex(0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(0.532666, 0.694184, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554014, 0.554014, -0.125000, 0, 0),
					g.addVertex(0.532666, 0.694184, -0.216506, 0, 0),
					g.addVertex(0.618718, 0.618718, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(0.476961, 0.621587, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(0.476961, 0.621587, -0.125000, 0, 0),
					g.addVertex(0.554014, 0.554014, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554014, 0.554014, 0.125000, 0, 0),
					g.addVertex(0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(0.456571, 0.595015, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.554014, 0.554014, 0.125000, 0, 0),
					g.addVertex(0.456571, 0.595015, 0.000000, 0, 0),
					g.addVertex(0.530330, 0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, 0.618718, 0.216506, 0, 0),
					g.addVertex(0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(0.476961, 0.621587, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, 0.618718, 0.216506, 0, 0),
					g.addVertex(0.476961, 0.621587, 0.125000, 0, 0),
					g.addVertex(0.554014, 0.554014, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(0.608762, 0.793353, 0.250000, 0, 0),
					g.addVertex(0.532666, 0.694184, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(0.532666, 0.694184, 0.216506, 0, 0),
					g.addVertex(0.618718, 0.618718, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(0.684857, 0.892522, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(0.684857, 0.892522, 0.216506, 0, 0),
					g.addVertex(0.795495, 0.795495, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.883883, 0.883884, 0.000000, 0, 0),
					g.addVertex(0.760952, 0.991691, 0.000000, 0, 0),
					g.addVertex(0.740562, 0.965119, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.883883, 0.883884, 0.000000, 0, 0),
					g.addVertex(0.740562, 0.965119, 0.125000, 0, 0),
					g.addVertex(0.860200, 0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(0.860200, 0.860200, -0.125000, 0, 0),
					g.addVertex(0.883883, 0.883884, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(0.883883, 0.883884, 0.000000, 0, 0),
					g.addVertex(0.991692, 0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(0.795495, 0.795495, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(0.795495, 0.795495, -0.216506, 0, 0),
					g.addVertex(0.892523, 0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(0.618718, 0.618718, -0.216506, 0, 0),
					g.addVertex(0.707107, 0.707107, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(0.707107, 0.707107, -0.250000, 0, 0),
					g.addVertex(0.793353, 0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(0.554014, 0.554014, -0.125000, 0, 0),
					g.addVertex(0.618718, 0.618718, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(0.618718, 0.618718, -0.216506, 0, 0),
					g.addVertex(0.694184, 0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(0.554014, 0.554014, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(0.554014, 0.554014, -0.125000, 0, 0),
					g.addVertex(0.621587, 0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(0.554014, 0.554014, 0.125000, 0, 0),
					g.addVertex(0.530330, 0.530330, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(0.530330, 0.530330, 0.000000, 0, 0),
					g.addVertex(0.595015, 0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(0.618718, 0.618718, 0.216506, 0, 0),
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.618718, 0.618718, 0.216506, 0, 0),
					g.addVertex(0.554014, 0.554014, 0.125000, 0, 0),
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(0.694184, 0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(0.618718, 0.618718, 0.216506, 0, 0),
					g.addVertex(0.694184, 0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(0.795495, 0.795495, 0.216506, 0, 0),
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(0.707107, 0.707107, 0.250000, 0, 0),
					g.addVertex(0.793353, 0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(0.883883, 0.883884, 0.000000, 0, 0),
					g.addVertex(0.860200, 0.860200, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(0.860200, 0.860200, 0.125000, 0, 0),
					g.addVertex(0.965119, 0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(0.991692, 0.760952, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(1.082532, 0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(0.965119, 0.740562, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(0.965119, 0.740562, -0.125000, 0, 0),
					g.addVertex(1.053525, 0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(0.892523, 0.684857, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(0.892523, 0.684857, -0.216506, 0, 0),
					g.addVertex(0.974279, 0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(0.793353, 0.608761, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(0.793353, 0.608761, -0.250000, 0, 0),
					g.addVertex(0.866025, 0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(0.694184, 0.532666, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(0.694184, 0.532666, -0.216506, 0, 0),
					g.addVertex(0.757772, 0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(0.621587, 0.476961, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(0.621587, 0.476961, -0.125000, 0, 0),
					g.addVertex(0.678525, 0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(0.595015, 0.456571, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(0.595015, 0.456571, 0.000000, 0, 0),
					g.addVertex(0.649519, 0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(0.621587, 0.476961, 0.125000, 0, 0),
					g.addVertex(0.678525, 0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(0.694184, 0.532666, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(0.694184, 0.532666, 0.216506, 0, 0),
					g.addVertex(0.757772, 0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(0.793353, 0.608761, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(0.793353, 0.608761, 0.250000, 0, 0),
					g.addVertex(0.866025, 0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(0.892523, 0.684857, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(0.892523, 0.684857, 0.216506, 0, 0),
					g.addVertex(0.974279, 0.562500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(0.991692, 0.760952, 0.000000, 0, 0),
					g.addVertex(0.965119, 0.740562, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(0.965119, 0.740562, 0.125000, 0, 0),
					g.addVertex(1.053525, 0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(1.082532, 0.625000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(1.154850, 0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039365, 0.430519, -0.216506, 0, 0),
					g.addVertex(0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(1.053525, 0.608253, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039365, 0.430519, -0.216506, 0, 0),
					g.addVertex(1.053525, 0.608253, -0.125000, 0, 0),
					g.addVertex(1.123905, 0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923880, 0.382683, -0.250000, 0, 0),
					g.addVertex(0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(0.974279, 0.562500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923880, 0.382683, -0.250000, 0, 0),
					g.addVertex(0.974279, 0.562500, -0.216506, 0, 0),
					g.addVertex(1.039365, 0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808395, 0.334848, -0.216506, 0, 0),
					g.addVertex(0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(0.866025, 0.500000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808395, 0.334848, -0.216506, 0, 0),
					g.addVertex(0.866025, 0.500000, -0.250000, 0, 0),
					g.addVertex(0.923880, 0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(0.757772, 0.437500, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(0.757772, 0.437500, -0.216506, 0, 0),
					g.addVertex(0.808395, 0.334848, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(0.678525, 0.391747, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(0.678525, 0.391747, -0.125000, 0, 0),
					g.addVertex(0.723854, 0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(0.649519, 0.375000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(0.649519, 0.375000, 0.000000, 0, 0),
					g.addVertex(0.692910, 0.287013, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808395, 0.334848, 0.216506, 0, 0),
					g.addVertex(0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(0.678525, 0.391747, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.808395, 0.334848, 0.216506, 0, 0),
					g.addVertex(0.678525, 0.391747, 0.125000, 0, 0),
					g.addVertex(0.723854, 0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923880, 0.382683, 0.250000, 0, 0),
					g.addVertex(0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(0.757772, 0.437500, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.923880, 0.382683, 0.250000, 0, 0),
					g.addVertex(0.757772, 0.437500, 0.216506, 0, 0),
					g.addVertex(0.808395, 0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039365, 0.430519, 0.216506, 0, 0),
					g.addVertex(0.974279, 0.562500, 0.216506, 0, 0),
					g.addVertex(0.866025, 0.500000, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.039365, 0.430519, 0.216506, 0, 0),
					g.addVertex(0.866025, 0.500000, 0.250000, 0, 0),
					g.addVertex(0.923880, 0.382683, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.154850, 0.478354, 0.000000, 0, 0),
					g.addVertex(1.082532, 0.625000, 0.000000, 0, 0),
					g.addVertex(1.053525, 0.608253, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.154850, 0.478354, 0.000000, 0, 0),
					g.addVertex(1.053525, 0.608253, 0.125000, 0, 0),
					g.addVertex(1.123905, 0.465537, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(1.154850, 0.478354, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(1.154850, 0.478354, 0.000000, 0, 0),
					g.addVertex(1.207407, 0.323524, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(1.039365, 0.430519, -0.216506, 0, 0),
					g.addVertex(1.123905, 0.465537, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(1.123905, 0.465537, -0.125000, 0, 0),
					g.addVertex(1.175055, 0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(0.923880, 0.382683, -0.250000, 0, 0),
					g.addVertex(1.039365, 0.430519, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(1.039365, 0.430519, -0.216506, 0, 0),
					g.addVertex(1.086667, 0.291171, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(0.808395, 0.334848, -0.216506, 0, 0),
					g.addVertex(0.923880, 0.382683, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(0.923880, 0.382683, -0.250000, 0, 0),
					g.addVertex(0.965926, 0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(0.723854, 0.299830, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(0.723854, 0.299830, -0.125000, 0, 0),
					g.addVertex(0.756797, 0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(0.692910, 0.287013, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(0.692910, 0.287013, 0.000000, 0, 0),
					g.addVertex(0.724444, 0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(0.808395, 0.334848, 0.216506, 0, 0),
					g.addVertex(0.723854, 0.299830, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(0.723854, 0.299830, 0.125000, 0, 0),
					g.addVertex(0.756797, 0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(0.923880, 0.382683, 0.250000, 0, 0),
					g.addVertex(0.808395, 0.334848, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(0.808395, 0.334848, 0.216506, 0, 0),
					g.addVertex(0.845185, 0.226467, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(1.039365, 0.430519, 0.216506, 0, 0),
					g.addVertex(0.923880, 0.382683, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(0.923880, 0.382683, 0.250000, 0, 0),
					g.addVertex(0.965926, 0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(1.039365, 0.430519, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(1.039365, 0.430519, 0.216506, 0, 0),
					g.addVertex(1.086667, 0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(1.154850, 0.478354, 0.000000, 0, 0),
					g.addVertex(1.123905, 0.465537, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(1.123905, 0.465537, 0.125000, 0, 0),
					g.addVertex(1.175055, 0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(1.207407, 0.323524, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(1.239306, 0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(1.086667, 0.291171, -0.216506, 0, 0),
					g.addVertex(1.175055, 0.314855, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(1.175055, 0.314855, -0.125000, 0, 0),
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, 0.114210, -0.216506, 0, 0),
					g.addVertex(0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(0.965926, 0.258819, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, 0.114210, -0.216506, 0, 0),
					g.addVertex(0.965926, 0.258819, -0.250000, 0, 0),
					g.addVertex(0.991445, 0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, 0.102266, -0.125000, 0, 0),
					g.addVertex(0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(0.845185, 0.226467, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, 0.102266, -0.125000, 0, 0),
					g.addVertex(0.845185, 0.226467, -0.216506, 0, 0),
					g.addVertex(0.867514, 0.114210, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(0.756797, 0.202783, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(0.756797, 0.202783, -0.125000, 0, 0),
					g.addVertex(0.776791, 0.102266, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, 0.102266, 0.125000, 0, 0),
					g.addVertex(0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(0.724444, 0.194114, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.776791, 0.102266, 0.125000, 0, 0),
					g.addVertex(0.724444, 0.194114, 0.000000, 0, 0),
					g.addVertex(0.743584, 0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, 0.114210, 0.216506, 0, 0),
					g.addVertex(0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(0.756797, 0.202783, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.867514, 0.114210, 0.216506, 0, 0),
					g.addVertex(0.756797, 0.202783, 0.125000, 0, 0),
					g.addVertex(0.776791, 0.102266, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(0.845185, 0.226467, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(0.845185, 0.226467, 0.216506, 0, 0),
					g.addVertex(0.867514, 0.114210, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(0.965926, 0.258819, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(0.965926, 0.258819, 0.250000, 0, 0),
					g.addVertex(0.991445, 0.130526, 0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(1.086667, 0.291171, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(1.086667, 0.291171, 0.216506, 0, 0),
					g.addVertex(1.115376, 0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(1.207407, 0.323524, 0.000000, 0, 0),
					g.addVertex(1.175055, 0.314855, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.239306, 0.163158, 0.000000, 0, 0),
					g.addVertex(1.175055, 0.314855, 0.125000, 0, 0),
					g.addVertex(1.206099, 0.158786, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.216506, 0.000000, -0.125000, 0, 0),
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.250000, 0.000000, 0.000000, 0, 0),
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(1.239306, 0.163158, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.125000, 0.000000, -0.216506, 0, 0),
					g.addVertex(1.206099, 0.158786, -0.125000, 0, 0),
					g.addVertex(1.216506, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(1.115376, 0.146842, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.000000, -0.250000, 0, 0),
					g.addVertex(1.115376, 0.146842, -0.216506, 0, 0),
					g.addVertex(1.125000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(0.867514, 0.114210, -0.216506, 0, 0),
					g.addVertex(0.991445, 0.130526, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.875000, 0.000000, -0.216506, 0, 0),
					g.addVertex(0.991445, 0.130526, -0.250000, 0, 0),
					g.addVertex(1.000000, 0.000000, -0.250000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(0.776791, 0.102266, -0.125000, 0, 0),
					g.addVertex(0.867514, 0.114210, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.783494, 0.000000, -0.125000, 0, 0),
					g.addVertex(0.867514, 0.114210, -0.216506, 0, 0),
					g.addVertex(0.875000, 0.000000, -0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(0.776791, 0.102266, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.750000, 0.000000, 0.000000, 0, 0),
					g.addVertex(0.776791, 0.102266, -0.125000, 0, 0),
					g.addVertex(0.783494, 0.000000, -0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(0.776791, 0.102266, 0.125000, 0, 0),
					g.addVertex(0.743584, 0.097895, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.783494, 0.000000, 0.125000, 0, 0),
					g.addVertex(0.743584, 0.097895, 0.000000, 0, 0),
					g.addVertex(0.750000, 0.000000, 0.000000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(0.867514, 0.114210, 0.216506, 0, 0),
					g.addVertex(0.776791, 0.102266, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(0.875000, 0.000000, 0.216506, 0, 0),
					g.addVertex(0.776791, 0.102266, 0.125000, 0, 0),
					g.addVertex(0.783494, 0.000000, 0.125000, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(0.991445, 0.130526, 0.250000, 0, 0),
					g.addVertex(0.867514, 0.114210, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.000000, 0.000000, 0.250000, 0, 0),
					g.addVertex(0.867514, 0.114210, 0.216506, 0, 0),
					g.addVertex(0.875000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(1.206099, 0.158786, 0.125000, 0, 0),
					g.addVertex(1.115376, 0.146842, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

				g.addFace(Vector.<Vertex>([
					g.addVertex(1.216506, 0.000000, 0.125000, 0, 0),
					g.addVertex(1.115376, 0.146842, 0.216506, 0, 0),
					g.addVertex(1.125000, 0.000000, 0.216506, 0, 0),
				]),new FillMaterial(0xb2cc00));

			//g.weldVertices();
			//g.weldFaces();
			geometry = g;


			this.x = 0.000000;
			this.y = 6.000000;
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