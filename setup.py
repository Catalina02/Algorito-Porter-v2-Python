from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            "script": "porter.py",                    ### Main Python script    
            "icon_resources": [(0, "icono.ico")],     ### Icon to embed into the PE file.
            "base" : "Win32GUI"
        }
    ],
) 
