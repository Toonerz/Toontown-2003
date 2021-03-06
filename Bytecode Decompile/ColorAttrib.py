import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, RenderAttrib

class ColorAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]
    TVertex = 0
    TFlat = 1
    TOff = 2

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self):
        raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpanda and libpanda._inPkJyoF59D:
            libpanda._inPkJyoF59D(self.this)

    def makeVertex():
        returnValue = libpanda._inPkJyoUIQx()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    makeVertex = staticmethod(makeVertex)

    def makeFlat(color):
        returnValue = libpanda._inPkJyo_AHD(color.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    makeFlat = staticmethod(makeFlat)

    def makeOff():
        returnValue = libpanda._inPkJyotNeS()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    makeOff = staticmethod(makeOff)

    def getClassType():
        returnValue = libpanda._inPkJyoNqSX()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def getColorType(self):
        returnValue = libpanda._inPkJyouDIc(self.this)
        return returnValue

    def getColor(self):
        returnValue = libpanda._inPkJyoexu6(self.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return