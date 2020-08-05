# Object Rings Addon
### An add-on for Blender 2.8+

This add-on introduces an operator for creating a ring of objects. This operation can be accessed through the **Object** button in the top-left of the 3D Viewport and selecting **Create Ring of Objects**.

This operator takes a selected object and duplicates it several times in a ring centered at the selected object. The duplicates will all face the original object.

When the operator is selected, a menu with 4 options will appear to set variables, which are used as follows:

Duplicates:
- integer value that must be at least 2.
- it describes the number of objects that will be in the ring around the original object

Radius (m):
- float value that must be greater than 0
- it is the distance away from the original object that the duplicates will be placed

Offset: 
- float value
- changing this value will shift the position of all of the objects in the ring by an angle

Degrees:
- when the box is checked, the offset angle will be measured in degrees
- when the box is unchecked, the offset angle will be measured in radians