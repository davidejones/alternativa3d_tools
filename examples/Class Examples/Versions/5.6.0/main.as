//Alternativa3D Class Export For Blender 2.62 and above
//Plugin Author: David E Jones, http://davidejones.com

package {

	import alternativa.engine3d.controllers.CameraController;
	import alternativa.engine3d.core.Scene3D;
	import alternativa.engine3d.core.Object3D;
	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.display.View;
	import alternativa.utils.MathUtils;
	import alternativa.utils.FPS;
	import alternativa.types.Point3D;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;

	[SWF(backgroundColor="#000000", frameRate="100", width="800", height="600")]

	public class main extends Sprite {

		private var obj0:mycube;
		private var obj1:mysuzanne;
		private var obj2:mytorus;

		private var scene:Scene3D = new Scene3D();
		private var rootContainer:Object3D = scene.root = new Object3D("root");
		private var camera:Camera3D;
		private var view:View;

		private var controller:CameraController;

		public function main() {

			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;

			camera = new Camera3D("camera");
			camera.fov = MathUtils.DEG1*100;
			camera.x = 10;
			rootContainer.addChild(camera);

			controller = new CameraController(stage);
			controller.camera = camera;
			controller.lookAt(new Point3D(0,0,0));

			obj0 = new mycube();
			rootContainer.addChild(obj0);
			obj1 = new mysuzanne();
			rootContainer.addChild(obj1);
			obj2 = new mytorus();
			rootContainer.addChild(obj2);

			view = new View(camera);
			addChild(view);
			view.interactive = true;
			FPS.init(this);

			addEventListener(Event.ENTER_FRAME, onEnterFrame);
			stage.addEventListener(Event.RESIZE, onResize);
			onResize();
		}

		private function onEnterFrame(e:Event=null):void {
			scene.calculate();
			controller.processInput();
		}

		private function onResize(e:Event=null):void {
			view.width = stage.stageWidth;
			view.height = stage.stageHeight;
			onEnterFrame();
		}

	}
}