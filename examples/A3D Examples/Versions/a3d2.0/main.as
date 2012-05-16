package {

	import alternativa.engine3d.controllers.SimpleObjectController;
	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.core.Object3D;
	import alternativa.engine3d.core.Resource;
	import alternativa.engine3d.core.View;
	import alternativa.engine3d.loaders.Parser;
	import alternativa.engine3d.loaders.Parser3DS;
	import alternativa.engine3d.loaders.ParserA3D;
	import alternativa.engine3d.loaders.ParserCollada;
	import alternativa.engine3d.loaders.ParserMaterial;
	import alternativa.engine3d.loaders.TexturesLoader;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.materials.StandardMaterial;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.objects.Surface;
	import alternativa.engine3d.resources.ExternalTextureResource;
	import alternativa.engine3d.resources.BitmapTextureResource;
	import alternativa.engine3d.resources.Geometry;

	import flash.display.Sprite;
	import flash.display.Stage3D;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.net.URLLoader;
	import flash.net.URLLoaderDataFormat;
	import flash.net.URLRequest;
	
	import alternativa.engine3d.lights.*;
	
	import flash.geom.Vector3D;
	
	[SWF(backgroundColor="#000000", frameRate="60", width="800", height="600")]

	public class main extends Sprite {
		
		private var scene:Object3D = new Object3D();
		private var camera:Camera3D;
		private var controller:SimpleObjectController;
		private var stage3D:Stage3D;
		private var mesh:Mesh;
		
		public function main() {
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			camera = new Camera3D(1, 1000);
			camera.view = new View(stage.stageWidth, stage.stageHeight, false, 0, 0, 4);
			addChild(camera.view);
			addChild(camera.diagram);
			
			// Initial position
			camera.x = 2;
			camera.z = 5;
			camera.y = 5;
			controller = new SimpleObjectController(stage, camera, 50);
			controller.lookAt(new Vector3D(0,0,0));
			scene.addChild(camera);
			
			// Light sources
			var ambientLight:AmbientLight = new AmbientLight(0x333333);
			scene.addChild(ambientLight);
			var directionalLight:DirectionalLight = new DirectionalLight(0xFFFFFF);
			directionalLight.z = 10;
			directionalLight.y = 10;
			directionalLight.x = 10;
			directionalLight.lookAt(0, 0, 0);
			scene.addChild(directionalLight);
			
			stage3D = stage.stage3Ds[0];
			stage3D.addEventListener(Event.CONTEXT3D_CREATE, onContextCreate);
			stage3D.requestContext3D();
		}

		private function onContextCreate(e:Event):void {
			stage3D.removeEventListener(Event.CONTEXT3D_CREATE, onContextCreate);
			
			var loaderA3D:URLLoader = new URLLoader();
			loaderA3D.dataFormat = URLLoaderDataFormat.BINARY;
			loaderA3D.load(new URLRequest("./demo.a3d"));
			loaderA3D.addEventListener(Event.COMPLETE, onA3DLoad);

			stage.addEventListener(Event.ENTER_FRAME, onEnterFrame);
			stage.addEventListener(Event.RESIZE, onResize);
			onResize();
		}
		
		private function onA3DLoad(e:Event):void {
			var parser:ParserA3D = new ParserA3D();
			parser.parse((e.target as URLLoader).data);
			mesh = parser.getObjectByName("Crate") as Mesh;
			scene.addChild(mesh);
			uploadResources(mesh.getResources(false, Geometry));
			setMaterials(mesh);
		}
		
		private function setMaterials(mesh:Mesh):void
		{
			var textures:Vector.<ExternalTextureResource> = new Vector.<ExternalTextureResource>();
			for (var i:int = 0; i < mesh.numSurfaces; i++) {
				var surface:Surface = mesh.getSurface(i);
				var material:ParserMaterial = surface.material as ParserMaterial;
				if (material != null) {
					var ambient:ExternalTextureResource = material.textures["ambient"];
					var emission:ExternalTextureResource = material.textures["emission"];
					var diffuse:ExternalTextureResource = material.textures["diffuse"];
					var specular:ExternalTextureResource = material.textures["specular"];
					var shininess:ExternalTextureResource = material.textures["shininess"];
					var reflective:ExternalTextureResource = material.textures["reflective"];
					var transparent:ExternalTextureResource = material.textures["transparent"];
					var bump:ExternalTextureResource = material.textures["bump"];
					if (ambient != null) {
						ambient.url = "../" + ambient.url;
						textures.push(ambient);
					}
					if (emission != null) {
						emission.url = "../" + emission.url;
						textures.push(emission);
					}
					if (diffuse != null) {
						diffuse.url = "../" + diffuse.url;
						textures.push(diffuse);
					}
					if (specular != null) {
						specular.url = "../" + specular.url;
						textures.push(specular);
					}
					if (shininess != null) {
						shininess.url = "../" + shininess.url;
						textures.push(shininess);
					}
					if (reflective != null) {
						reflective.url = "../" + reflective.url;
						textures.push(reflective);
					}
					if (transparent != null) {
						transparent.url = "../" + transparent.url;
						textures.push(transparent);
					}
					if (bump != null) {
						bump.url = "../" + bump.url;
						textures.push(bump);
					}
					var sm:StandardMaterial = new StandardMaterial(diffuse, bump, specular, shininess, transparent);
					sm.alphaThreshold = 1;
					sm.lightMap = emission;
					surface.material = sm;
				}			
			}
			
			var texturesLoader:TexturesLoader = new TexturesLoader(stage3D.context3D);
			texturesLoader.loadResources(textures);
		}
		
		private function uploadResources(resources:Vector.<Resource>):void {
			for each (var resource:Resource in resources) {
				resource.upload(stage3D.context3D);
			}
		}

		private function onEnterFrame(e:Event):void {
			if (mesh != null) {
				mesh.rotationX += 0.01;
				mesh.rotationY += 0.01;
			}
			controller.update();
			camera.render(stage3D);
		}
		
		private function onResize(e:Event = null):void {
			camera.view.width = stage.stageWidth;
			camera.view.height = stage.stageHeight;
		}

	}
}
