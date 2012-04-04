package {
	
	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.core.Object3DContainer;
	import alternativa.engine3d.core.View;
	
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	
	[SWF(backgroundColor="#000000", frameRate="100", width="800", height="600")]
	
	public class main extends Sprite {
	
		private var obj1:mycube;
		private var obj2:mysuzanne;
		private var obj3:mytorus;
		private var rootContainer:Object3DContainer = new Object3DContainer();
		private var camera:Camera3D;
		
		public function main():void
		{
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			camera = new Camera3D();
			camera.view = new View(stage.stageWidth, stage.stageHeight);
			addChild(camera.view);
			addChild(camera.diagram);

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
			
			stage.addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}
		
		private function onEnterFrame(e:Event):void {
			camera.view.width = stage.stageWidth;
			camera.view.height = stage.stageHeight;
			camera.render();
		}
	}
	
}
