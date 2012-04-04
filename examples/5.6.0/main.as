package {
	
	import alternativa.engine3d.core.Scene3D;
	import alternativa.engine3d.core.Object3D;
	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.display.View;
	import alternativa.utils.MathUtils;
	import alternativa.utils.FPS;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	
	import mycube;
	import mysuzanne;
	import mytorus;
	
	[SWF(backgroundColor="#000000", frameRate="100", width="800", height="600")]
	
	public class main extends Sprite 
	{	
		private var obj1:mycube;
		private var obj2:mysuzanne;
		private var obj3:mytorus;
		private var scene:Scene3D = new Scene3D();
		private var rootContainer:Object3D = scene.root = new Object3D("root");
		private var camera:Camera3D;
		private var view:View;
		
		private var qualitySwitchTime:uint = 300;
		private var qualityTimerId:int = -1;
		
		public function main():void 
		{
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			camera = new Camera3D("camera");
			camera.fov = MathUtils.DEG1*100;
			camera.z = -10;
			rootContainer.addChild(camera);
			
			obj1 = new mycube();
			obj2 = new mysuzanne();
			obj3 = new mytorus();
			
			rootContainer.addChild(obj1);
			obj1.x = -5;
			rootContainer.addChild(obj2);
			obj2.rotationX = 180*Math.PI/180;
			rootContainer.addChild(obj3);
			obj3.x = 5;
			
			view = new View(camera);
			addChild(view);
			view.interactive = true;
			FPS.init(this);
			
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
			stage.addEventListener(Event.RESIZE, onResize);
			onResize();
		}
		
		private function onEnterFrame(e:Event = null):void {
			scene.calculate();
		}
		
		private function onResize(e:Event = null):void {
			view.width = stage.stageWidth;
			view.height = stage.stageHeight;
			onEnterFrame();
		}		
	}
}