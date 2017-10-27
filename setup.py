import os
import distutils
from distutils import dir_util

settings_folder = os.path.join( os.environ['APPDATA'], 'Code - Insiders', 'User' )
distutils.dir_util.copy_tree( os.path.join( os.path.dirname( __file__ ), './settings' ), settings_folder, update=1 )
