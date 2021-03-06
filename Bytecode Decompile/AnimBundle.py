import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, AnimGroup

class AnimBundle(AnimGroup.AnimGroup, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaDowncasts, libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self, name, fps, numFrames):
        self.this = libpanda._inPn9gM0LBr(name, fps, numFrames)
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpanda and libpanda._inPn9gMNcAI:
            libpanda._inPn9gMNcAI(self.this)

    def getClassType():
        returnValue = libpanda._inPn9gMzlnG()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def getBaseFrameRate(self):
        returnValue = libpanda._inPn9gM7Ty_(self.this)
        return returnValue

    def getNumFrames(self):
        returnValue = libpanda._inPn9gMRxeQ(self.this)
        return returnValue