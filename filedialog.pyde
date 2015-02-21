#add_library('G4P')

#import java.awt.Rectangle
#from java.util import ArrayList
import G4P
#from G4P import g4p_controls
from g4p_controls import GLabel
from g4p_controls import GCheckbox
from g4p_controls import GButton
from g4p_controls import GAlign
from g4p_controls import GTextField 
from g4p_controls import GToggleGroup 
from g4p_controls import GTextArea 
from g4p_controls import GOption
from g4p_controls import GSketchPad 
#from g4p_controls import PGraphics

rects = []

sel_col = -1


def setup():
   size(660, 420)
   #rects = ArrayList<Rectangle>
   createFileSystemGUI(340, 220, 300, 130, 6)


def draw():
   global rects
   background(200, 200, 255)
   #for (Rectangle r : rects)
   #    showFrame(r)
   for r in rects:
      showFrame(r)


# Simple graphical frame to group controls
def showFrame(r) :
   noFill()
   strokeWeight(1)
   stroke(color(240, 240, 255))
   rect(r["x"], r["y"], r["width"], r["height"])
   stroke(color(0))
   rect(r["x"]+1, r["y"]+1, r["width"], r["height"])

def handleButtonEvents(button, event) : 
   # Folder selection
   if (button == btnFolder or button == btnInput or button == btnOutput):
      handleFileDialog(button)

# G4P code for folder and file dialogs
def handleFileDialog(button) :
   # Folder selection
   if (button == btnFolder) :
      fname = G4P.selectFolder("Folder Dialog")
      lblFile.setText(fname)
   
   # File input selection
   elif (button == btnInput) :
      # Use file filter if possible
      fname = G4P.selectInput("Input Dialog", "png,gif,jpg,jpeg", "Image files")
      lblFile.setText(fname)
   
   # File output selection
   elif (button == btnOutput) :
      fname = G4P.selectOutput("Output Dialog")
      lblFile.setText(fname)
   

# The next methods are simply to create the GUI. So there is
# no more code related to the various dialogs.
def createFileSystemGUI(x, y, w, h, border) :
   global rects
   # Store picture frame
   r = {}
   r['x'] = x
   r['y'] = y
   r['width'] = w
   r['height'] = h
   print(r)
   rects.append(r)
   # Set inner frame position
   x += border 
   y += border
   w -= 2*border 
   h -= 2*border
   title = GLabel(this, x, y, w, 20)
   title.setText("File system dialogs", GAlign.LEFT, GAlign.MIDDLE)
   title.setOpaque(True)
   title.setTextBold()
   # Create buttons
   bgap = 8
   bw = round((w - 2 * bgap) / 3.0)
   bs = bgap + bw
   btnFolder = GButton(this, x, y+30, bw, 20, "Folder")
   btnInput = GButton(this, x+bs, y+30, bw, 20, "Input")
   btnOutput = GButton(this, x+2*bs, y+30, bw, 20, "Output")
   lblFile = GLabel(this, x, y+60, w, 44)
   lblFile.setTextAlign(GAlign.LEFT, GAlign.MIDDLE)
   lblFile.setOpaque(True)
   #lblFile.setLocalColorScheme(G4P.GREEN_SCHEME)
   # Use native or Java Swing dialogs
   cbxUseNative = GCheckbox(this, x, y + h - 14, w, 20, "Use native controls")
   cbxUseNative.setSelected(True)
   cbxUseNative.setTextItalic()

