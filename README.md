Alternativa 3d Blender Tool
===========================

Created by David E Jones, [http://davidejones.com](http://davidejones.com)
Follow me on twitter [@david3jones](https://twitter.com/david3jones)

If you like this tool, then please tweet, like or googleplus my website http://davidejones.com

What is the alternativa 3d blender tool?
----------------------------------------

This python script can be installed as an addon to blender. Once installed it will allow you to import/export various formats that are compatible with the flash 3d library [alternativa](http://alternativaplatform.com/en/).

## Functionality

- Import/Export .A3D files
- Export 3d models to flash alternativa3d actionscript classes
- Export data to compressed bytearray variable within class in version 8.27.0+
- Create Document Classes

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

### 1.2.1
- Fixed a bug with importing a3d version 1 files
- Fixed a bug with the a3d1 object parsing to read visibility from mask
- Fix `error embedded null character` when loading images
- Use object names when converting a3d1 to 2, previously used the same name for all
- Fix export bugs with texture material accessing params that don't exist

### 1.2.0
- Fixed certain classes not assigning read transform
- Added a3d export Hierachy and included option to disable
- Fixed incorrect uv export when using bmesh data

### 1.1.9
- Fixed context error with add mesh to lod (kennylerma)
- Check object isn't selected in list and hidden

### 1.1.8
- Fixed error when key not found in materials list
- Add option to exclude hidden items from a3d file, to reduce filesize if needed
- Add option to export all uvlayers or only active/first uv layer
- Fixed context bug when exporting, failing to poll context
- Fixed bug in exporting nullmask in very large files taking value as float instead of int
- Add export option to copy images, as with export make work with per face uv diffuse images
- Fix export of lod not converting quads to tris.

### 1.1.7
- Added export and import of cameras
- Set images with multiple users to only export one copy
- Added option to export without boundboxes as they can be calculated in alternativa
- Added import options to include/excluding importing of lighting, cameras
- Added LOD to mesh menu and exporter
- Fixed bug in a3d export, relative path filenames starting with "//" not exporting images
- Added export multiple uv channels in actionscript v8 and a3d
- Import all uv channels from a3d model
- Bugfix, when exporting large files, [Error 12] Not enough space appears - fixed by removing print() which was overflowing the console
- When exporting if there are no materialslots for mesh an attempt to export with per face uv image as diffuse
- Import LOD, Sprites from a3d
- Changed how boundbox data is collected
- Output boundbox data to classes
- Fixed not being able to export with uvs in actionscript v7 due to bmesh changes
- Fixed import lights all showing as ambient to show correct light type
- Add panel details for sprite import/export
- Add menu option for converting selected mesh to a decal
- Add Decal in to menu and exporter, with panel details for import/export
- export materials check texture name begins with string rather than equals string as you can have diffuse diffuse.001 etc

### 1.1.6
- Updated min version of blender to be 2.63
- Fixed api changes relating to bmesh
- Fixed vertexbuffer compression export to a3d version 2.6
- Fixed vertexbuffer decompression import a3d 2.6
- Set version a3d 2.6 as default export now its working
- linked copies of meshes export properly, reducing filesize by removing unused buffers
- Removed all menu meshes except Sprite until better support
- Fixed importing of mesh from skin
- condensed code and removed redundant code
- Added compatibility to still work with non bmesh version releases of blender
- Add option to export parent object for meshes, parent object contains pivot transform
- Redone nullmask encoding based on alternativa

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
