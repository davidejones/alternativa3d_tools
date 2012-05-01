Alternativa 3d Blender Tool
===========================

Created by David E Jones, [http://davidejones.com](http://davidejones.com)
Follow me on twitter [@david3jones](https://twitter.com/david3jones)

If you like this tool, then please tweet, like or googleplus my website http://davidejones.com

What is the alternativa 3d blender tool?
----------------------------------------

This python script can be installed as an addon to blender. Once installed it will allow you to import/export various formats that are compatible with the flash 3d library [alternativa](http://alternativaplatform.com/en/).

##Functionality

- Create alternativa3d objects in blender and enable for export (Work in progress)
- Create Document Class (Work in progress)
- Import/Export .A3D files (Work in progress)
- Export 3d models to flash alternativa3d actionscript classes (Export fillmaterials or textures)
  For the following alternativa3d versions
	-5.6.0
	-7.5.1
	-7.6.0
	-7.7.0
	-7.8.0
	-8.5.0
	-8.8.0
	-8.12.0
	-8.17.0
	-8.27.0
- Export data to compressed bytearray variable within class in version 8.27.0+

Installation Notes
------------------

1. Open blender and go to File->User Preferences
2. Click the Addons tab
3. Click the install addon button at the bottom of this window
4. Browse to the io_alternativa3d_tools.py file
5. Find the addon in the list, this is easier if you click Import-Export category on the left.
6. Tick the checkbox next to the addon to enable it
7. Click save as default button if you want this addon and any other changes you have made to be enabled by default when you start up blender

Changelog
---------

### 1.1.5
- Updated min version of blender to be 2.62
- Fixed export class version 5.6.0 uv mapping
- Basic export to a3d 2.0
- Partial exporting to 2.4, 2.5, 2.6
- Basic import of a3d 2.0
- Partial importing of a3d 2.4, 2.5, 2.6
- Export tangents for classes and a3d
- Flat or Smooth normals exports
- Fixed export documentclass to do something useful
- Partially Updated mesh menu with a3dclasses
- Updated class examples and added a3d examples
- Import of version 1.0 (limited testing, appears to work)
- Added debugplayers to show loaded a3d data

### 1.1.4
- Added example exports for each version with built swf
- Added in options for 7.5.0
- Condensed version 8 coding
- Condensed version 7 coding

### 1.1.3
- Fixed error when exporting in version 7.51
- Rebuilt version 5.6.0 as it wasn't exporting anything useful
- added check to see if importing .a3d file version 1 or 2

### 1.1.2
- Added support for compressed bytearray data in class rather than values v.8.27.0+ only

### 1.1.1
- Updated version 8 class export with textures. 
- Changed export to use material name instead of material0 material1 etc. 
- Works with multiple surface materials 

Examples
----------

For export samples please see the example folder