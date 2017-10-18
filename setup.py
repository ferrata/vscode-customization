import os
import shutil

settings_folder = os.path.join( os.environ['APPDATA'], 'Code - Insiders', 'User' )
shutil.copytree( './settings', settings_folder )
