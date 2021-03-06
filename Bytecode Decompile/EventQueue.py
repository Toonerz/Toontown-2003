import types, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject

class EventQueue(FFIExternalObject.FFIExternalObject):
    __module__ = __name__
    __CModuleDowncasts__ = [libpandaexpressDowncasts]

    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return
        apply(self.constructor, _args)
        return

    def constructor(self):
        self.this = libpandaexpress._inPekxoIzfw()
        self.userManagesMemory = 1

    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()

    def destructor(self):
        if libpandaexpress and libpandaexpress._inPekxoa_QX:
            libpandaexpress._inPekxoa_QX(self.this)

    def getGlobalEventQueue():
        returnValue = libpandaexpress._inPekxosJeO()
        returnObject = EventQueue(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    getGlobalEventQueue = staticmethod(getGlobalEventQueue)

    def queueEvent(self, event):
        returnValue = libpandaexpress._inPekxonDd1(self.this, event.this)
        return returnValue

    def clear(self):
        returnValue = libpandaexpress._inPekxoRhuh(self.this)
        return returnValue

    def isQueueEmpty(self):
        returnValue = libpandaexpress._inPekxoXt8W(self.this)
        return returnValue

    def isQueueFull(self):
        returnValue = libpandaexpress._inPekxoDyXu(self.this)
        return returnValue

    def dequeueEvent(self):
        returnValue = libpandaexpress._inPekxoBDK_(self.this)
        import Event
        returnObject = Event.Event(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return