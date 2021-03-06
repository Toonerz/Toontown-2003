import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, RenderAttrib

class DepthOffsetAttrib(RenderAttrib.RenderAttrib, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]

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
        if libpanda and libpanda._inPkJyoW3rf:
            libpanda._inPkJyoW3rf(self.this)

    def __overloaded_make_int(offset):
        returnValue = libpanda._inPkJyoYYvF(offset)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    __overloaded_make_int = staticmethod(__overloaded_make_int)

    def __overloaded_make():
        returnValue = libpanda._inPkJyoTJWU()
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    __overloaded_make = staticmethod(__overloaded_make)

    def getClassType():
        returnValue = libpanda._inPkJyosc0x()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def getOffset(self):
        returnValue = libpanda._inPkJyoR48q(self.this)
        return returnValue

    def make(*_args):
        numArgs = len(_args)
        if numArgs == 0:
            return DepthOffsetAttrib.__overloaded_make()
        else:
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return DepthOffsetAttrib.__overloaded_make_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

    make = staticmethod(make)