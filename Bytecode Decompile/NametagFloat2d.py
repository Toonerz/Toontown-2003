import types, libtoontown, libtoontownDowncasts, libpandaexpress, libpandaexpressDowncasts, libpanda, libpandaDowncasts, FFIExternalObject, Nametag3d

class NametagFloat2d(Nametag3d.Nametag3d, FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libtoontownDowncasts, libpandaexpressDowncasts, libpandaDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self):
        self.this = libtoontown._inPPj7bhMMO()
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libtoontown and libtoontown._inPPj7b4h7N:
            libtoontown._inPPj7b4h7N(self.this)

    def getClassType():
        returnValue = libtoontown._inPPj7bEEjZ()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)