if "bpy" not in locals():
    print('STARTUP ALTERNATIVA!!')
    import bpy
    from . import version
else:
    print('RELOAD ALTERNATIVA!!')
    import importlib
    importlib.reload(version)
