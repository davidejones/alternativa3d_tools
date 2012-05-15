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
	import flash.utils.ByteArray;
	import flash.utils.Endian;

	public class mycube extends Mesh {

		private var CubeMaterial:FillMaterial = new FillMaterial(0xcc00b9);

		private var values:Vector.<uint>;
		private var bytedata:ByteArray = new ByteArray();
		private var attributes:Array;

		public function mycube() {

			attributes = new Array();
			attributes[0] = VertexAttributes.POSITION;
			attributes[1] = VertexAttributes.POSITION;
			attributes[2] = VertexAttributes.POSITION;
			attributes[3] = VertexAttributes.TEXCOORDS[0];
			attributes[4] = VertexAttributes.TEXCOORDS[0];
			var g:Geometry = new Geometry();
			g.addVertexStream(attributes);
			g.numVertices = 8;

			values= new <uint>[0x78,0x9C,0x4D,0x8C,0x81,0x9,0xC0,0x20,0xC,0x4,0xA3,0x26,0xCD,0xA,0x1D,0xA0,0x7B,0x38,0x5A,0xDD,0xAC,0x4B,0x15,0xA,0x85,0x62,0x3F,0xF5,0xB,0xA,0xC7,0x9F,0xE6,0xCD,0x2A,0xBD,0xEF,0x35,0x10,0x69,0x7,0xFD,0x8,0x4F,0xE0,0xA1,0xDF,0xC8,0x22,0xED,0xEB,0x28,0xF2,0x1A,0xFD,0x7A,0x22,0xD,0x6F,0xE1,0x85,0xBD,0x70,0xEE,0xA8,0x83,0x4D,0x54,0xC6,0x29,0x40,0x99,0xE,0x32,0x58,0x26,0x77,0xCE,0x12,0x30,0xBE,0x19,0x3B,0x99,0x3B,0x94,0x73,0xE5,0xEC,0x77,0xE7,0xDD,0xD9,0x37,0xF6,0xD3,0xF4,0x37,0x73,0xFF,0xB,0xB1,0x3A,0x2C,0x76,];
			for each(var b:uint in values)
			{
				bytedata.writeByte(b);
			}
			var vertices:Array = new Array();
			var uvt:Array = new Array();
			var ind:Array = new Array();
			bytedata.endian = Endian.LITTLE_ENDIAN;
			bytedata.uncompress();
			bytedata.position=0;
			var vlen:uint = bytedata.readUnsignedShort();
			g.numVertices = vlen/3;
			for(var i:int = 0; i < vlen; i++){vertices.push(bytedata.readFloat());}
			var uvlen:uint = bytedata.readUnsignedShort();
			for(var x:int = 0; x < uvlen; x++){uvt.push(bytedata.readFloat());}
			var ilen:uint = bytedata.readUnsignedShort();
			for(var j:int = 0; j < ilen; j++){ind.push(bytedata.readUnsignedInt());}
			g.setAttributeValues(VertexAttributes.POSITION, Vector.<Number>(vertices));
			if(uvlen > 0){g.setAttributeValues(VertexAttributes.TEXCOORDS[0], Vector.<Number>(uvt));}
			g.indices =  Vector.<uint>(ind);

			g.calculateNormals();
			g.calculateTangents(0);
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