Attempt at automating export-based testing of Fast64

Doesn't work because fast64 uses operators too happily and the bpy.context is wrong, overriding context when calling fast64 ops may work but I don't want to figure that out
