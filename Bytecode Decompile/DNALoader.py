import types, libtoontown, libtoontownDowncasts, FFIExternalObject

class DNALoader(FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libtoontownDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self):
        self.this = libtoontown._inPet4ynacW()
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libtoontown and libtoontown._inPet4yZRXO:
            libtoontown._inPet4yZRXO(self.this)

    def __overloaded_buildGraph_ptrDNALoader_ptrDNAStorage_int(self, dnaStore, editing):
        returnValue = libtoontown._inPet4yWgdC(self.this, dnaStore.this, editing)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def __overloaded_buildGraph_ptrDNALoader_ptrDNAStorage(self, dnaStore):
        returnValue = libtoontown._inPet4ySjxN(self.this, dnaStore.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getData(self):
        returnValue = libtoontown._inPet4yt8FI(self.this)
        import DNAData
        returnObject = DNAData.DNAData(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def buildGraph(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import DNAStorage
            if isinstance(_args[0], DNAStorage.DNAStorage):
                return self.__overloaded_buildGraph_ptrDNALoader_ptrDNAStorage(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
        else:
            if numArgs == 2:
                import DNAStorage
                if isinstance(_args[0], DNAStorage.DNAStorage):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_buildGraph_ptrDNALoader_ptrDNAStorage_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '