#!/usr/bin/env python3
# coding: utf-8
#
# FastenersDummy.py



import os

import FreeCADGui as Gui
import FreeCAD as App
#from FastenerBase import FSBaseObject

import Asm4_libs as Asm4
from Asm4_Translate import translate
import Asm4_locator
Asm4_path = os.path.dirname( Asm4_locator.__file__ )
Asm4_trans = os.path.join(Asm4_path, "Resources/translations")
Gui.addLanguagePath(Asm4_trans)
Gui.updateLocale()

"""
    +-----------------------------------------------+
    |        a class to create all fasteners        |
    |       from the Fasteners WB (ScrewMaker)      |
    +-----------------------------------------------+

    import ScrewMaker
    sm = ScrewMaker.Instance()
    screwObj = sm.createFastener('ISO7046', 'M6', '20', 'simple', shapeOnly=False)
"""

class insertFastener:
    "My tool object"
    def __init__(self, fastenerType):
        self.fastenerType = fastenerType
        # Screw:
        if self.fastenerType=='Screw':
            self.menutext = translate("Fasteners", "Insert Screw")
            self.icon = os.path.join( Asm4.iconPath , 'Asm4_Screw.svg')
        # Nut:
        elif self.fastenerType=='Nut':
            self.menutext = translate("Fasteners", "Insert Nut")
            self.icon = os.path.join( Asm4.iconPath , 'Asm4_Nut.svg')
        # Washer:
        elif self.fastenerType=='Washer':
            self.menutext = translate("Fasteners", "Insert Washer")
            self.icon = os.path.join( Asm4.iconPath , 'Asm4_Washer.svg')
        # threaded rod:
        elif self.fastenerType=='ThreadedRod':
            self.menutext = translate("Fasteners", "Insert threaded rod")
            self.icon = os.path.join( Asm4.iconPath , 'Asm4_Rod.svg')


    def GetResources(self):
        return {"MenuText": self.menutext,
                "ToolTip": translate("Fasteners", "FastenersWorkbench is not installed.\n \nYou can install it with the FreeCAD AddonsManager:\nMenu Tools > Addon Manager > fasteners"),
                "Pixmap" : self.icon }


    def IsActive(self):
        # it's the dummy, always inactive
        return False


    def Activated(self):
        return




"""
    +-----------------------------------------------+
    |             dummy  placeFastener              |
    +-----------------------------------------------+
"""
class placeFastenerCmd():
    "My tool object"

    def __init__(self):
        super(placeFastenerCmd,self).__init__()

    def GetResources(self):
        return {"MenuText": translate("Asm4_Fasteners", "Edit Attachment of a Fastener"),
                "ToolTip": translate("Asm4_Fasteners", 'FastenersWorkbench is not installed.\n \nYou can install it with the FreeCAD AddonsManager:\nMenu Tools > Addon Manager > fasteners'),
                "Pixmap" : os.path.join( Asm4.iconPath , 'Asm4_mvFastener.svg')
                }

    def IsActive(self):
        # it's a dummy, always inactive
        return False 

    def Activated(self):
        return
    
    
"""
    +-----------------------------------------------+
    |                dummy parameters               |
    +-----------------------------------------------+
"""
class changeFSparametersCmd():
    def __init__(self):
        super(changeFSparametersCmd,self).__init__()

    def GetResources(self):
        return {"MenuText": translate("Asm4_Fasteners", "Change Fastener parameters"),
                "ToolTip": translate("Asm4_Fasteners", "Change Fastener parameters"),
                "Pixmap" : os.path.join( Asm4.iconPath , 'Asm4_FSparams.svg')
                }

    def IsActive(self):
        # it's a dummy, always inactive
        return False 

    def Activated(self):
        return



class cloneFastenersToAxesCmd():
    def __init__(self):
        super(cloneFastenersToAxesCmd,self).__init__()

    def GetResources(self):
        return {"MenuText": translate("Asm4_Fasteners", "Clone Fastener to Axes"),
                "ToolTip": translate("Asm4_Fasteners", 'FastenersWorkbench is not installed.\n \nYou can install it with the FreeCAD AddonsManager:\nMenu Tools > Addon Manager > fasteners'),
                "Pixmap" : os.path.join( Asm4.iconPath , 'Asm4_cloneFasteners.svg')
                }

    def IsActive(self):
        # it's a dummy, always inactive
        return False 

    def Activated(self):
        return



"""
    +-----------------------------------------------+
    |       add the commands to the workbench       |
    +-----------------------------------------------+
"""
Gui.addCommand( 'Asm4_insertScrew',    insertFastener('Screw') )
Gui.addCommand( 'Asm4_insertNut',      insertFastener('Nut') )
Gui.addCommand( 'Asm4_insertWasher',   insertFastener('Washer') )
Gui.addCommand( 'Asm4_insertRod',      insertFastener('ThreadedRod') )
Gui.addCommand( 'Asm4_placeFastener',  placeFastenerCmd() )
Gui.addCommand( 'Asm4_cloneFastenersToAxes',  cloneFastenersToAxesCmd() )
Gui.addCommand( 'Asm4_FSparameters',   changeFSparametersCmd()  )
