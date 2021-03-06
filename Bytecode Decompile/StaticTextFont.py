import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, TextFont

class StaticTextFont(TextFont.TextFont, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self, fontDef):
        self.this = libpanda._inPmUk_9cW_(fontDef.this)
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpanda and libpanda._inPmUk_07Lc:
            libpanda._inPmUk_07Lc(self.this)

    def getClassType():
        returnValue = libpanda._inPmUk_rq7s()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)