//Alternativa3D Class Export For Blender 2.62 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.core.Object3D;
	import alternativa.engine3d.core.Resource;
	import alternativa.engine3d.core.View;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.controllers.SimpleObjectController;
	import flash.display.Sprite;
	import flash.display.Stage3D;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.geom.Vector3D;

	[SWF(backgroundColor="#000000", frameRate="100", width="800", height="600")]

	public class main extends Sprite {

		private var obj0:mycube;
		private var obj1:mysuzanne;
		private var obj2:mytorus;

		private var rootContainer:Object3D = new Object3D();
		private var camera:Camera3D;
		private var stage3D:Stage3D;
		private var controller:SimpleObjectController;

		public function main() {

			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;

			camera = new Camera3D(0.1, 10000);
			camera.view = new View(stage.stageWidth, stage.stageHeight);
			addChild(camera.view);
			addChild(camera.diagram);
			camera.x = 10;
			rootContainer.addChild(camera);

			controller = new SimpleObjectController(stage,camera,100);
			controller.lookAt(new Vector3D(0,0,0));

			obj0 = new mycube();
			rootContainer.addChild(obj0);
			obj1 = new mysuzanne();
			rootContainer.addChild(obj1);
			obj2 = new mytorus();
			rootContainer.addChild(obj2);

			stage3D = stage.stage3Ds[0];
			stage3D.addEventListener(Event.CONTEXT3D_CREATE, onContextCreate);
			stage3D.requestContext3D();

		}

		private function onContextCreate(e:Event):void {
			for each (var resource:Resource in rootContainer.getResources(true)) {
				resource.upload(stage3D.context3D);
			}
			stage.addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}

		private function onEnterFrame(e:Event):void {
			camera.view.width = stage.stageWidth;
			camera.view.height = stage.stageHeight;
			camera.render(stage3D);
		}
	}
}