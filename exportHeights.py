import FreeCAD as App
import Part
import os

doc = App.ActiveDocument
sheet = doc.getObject("Spreadsheet")
body = doc.getObject("Body001")

folder = os.path.dirname(doc.FileName)

for row in range(8, 12):
    height = sheet.get(f"B{row}")

    sheet.set("B1", str(height))
    doc.recompute()

    height_name = str(height).replace(" ", "")
    filename = os.path.join(folder, f"spacer_{height_name}.step")

    Part.export([body], filename)
    print(f"Exported: {filename}")