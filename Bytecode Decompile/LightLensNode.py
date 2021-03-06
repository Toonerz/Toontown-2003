import types, libpanda, libpandaDowncasts, libpandaexpress, libpandaexpressDowncasts, FFIExternalObject, Light, LensNode

class LightLensNode(Light.Light, LensNode.LensNode, FFIExternalObject.FFIExternalObject):
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
        if libpanda and libpanda._inPkJyoBC2d:
            libpanda._inPkJyoBC2d(self.this)

    def getClassType():
        returnValue = libpanda._inPkJyoloD_()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    getClassType = staticmethod(getClassType)

    def output(self, out):
        returnValue = libpanda._inPkJyo1lQT(self.this, out.this)
        return returnValue

    def __overloaded_write_ptrConstLightLensNode_ptrOstream_int(self, out, indentLevel):
        returnValue = libpanda._inPkJyoJusW(self.this, out.this, indentLevel)
        return returnValue

    def __overloaded_write_ptrConstLightLensNode_ptrOstream(self, out):
        returnValue = libpanda._inPkJyoa_Tf(self.this, out.this)
        return returnValue

    def upcastToLensNode(self):
        returnValue = libpanda._inPkJyoP0SH(self.this)
        import LensNode
        returnObject = LensNode.LensNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    def asNode(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyoPU8w(upcastSelf.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getColor(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyolF_a(upcastSelf.this)
        import VBase4
        returnObject = VBase4.VBase4(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def setColor(self, color):
        upcastSelf = self
        returnValue = libpanda._inPkJyo7_hL(upcastSelf.this, color.this)
        return returnValue

    def upcastToReferenceCount(self):
        upcastSelf = self
        returnValue = libpanda._inPkJyopIAk(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    def copyLens(self, lens):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo1vNW(upcastSelf.this, lens.this)
        return returnValue

    def setLens(self, lens):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo_2fA(upcastSelf.this, lens.this)
        return returnValue

    def getLens(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoC5Ow(upcastSelf.this)
        import Lens
        returnObject = Lens.Lens(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def isInView(self, pos):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoVo66(upcastSelf.this, pos.this)
        return returnValue

    def copySubgraph(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoGYnx(upcastSelf.this)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getNumParents(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoI9bH(upcastSelf.this)
        return returnValue

    def getParent(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoh0xF(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def findParent(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoNWG_(upcastSelf.this, node.this)
        return returnValue

    def getNumChildren(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo68Bo(upcastSelf.this)
        return returnValue

    def getChild(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyonZg9(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getChildSort(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoMzeG(upcastSelf.this, n)
        return returnValue

    def findChild(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoKHuN(upcastSelf.this, node.this)
        return returnValue

    def __overloaded_addChild_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoA9tQ(upcastSelf.this, childNode.this, sort)
        return returnValue

    def __overloaded_addChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo37ri(upcastSelf.this, childNode.this)
        return returnValue

    def __overloaded_removeChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyozFZb(upcastSelf.this, childNode.this)
        return returnValue

    def __overloaded_removeChild_ptrPandaNode_int(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoCqN1(upcastSelf.this, n)
        return returnValue

    def replaceChild(self, origChild, newChild):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyogW5Y(upcastSelf.this, origChild.this, newChild.this)
        return returnValue

    def __overloaded_stashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyokC1w(upcastSelf.this, childNode.this)
        return returnValue

    def __overloaded_stashChild_ptrPandaNode_int(self, childIndex):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoqWqz(upcastSelf.this, childIndex)
        return returnValue

    def __overloaded_unstashChild_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoqJGM(upcastSelf.this, childNode.this)
        return returnValue

    def __overloaded_unstashChild_ptrPandaNode_int(self, stashedIndex):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoeWxF(upcastSelf.this, stashedIndex)
        return returnValue

    def getNumStashed(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoPR8_(upcastSelf.this)
        return returnValue

    def getStashed(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyol8qw(upcastSelf.this, n)
        import PandaNode
        returnObject = PandaNode.PandaNode(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getStashedSort(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoE1FX(upcastSelf.this, n)
        return returnValue

    def findStashed(self, node):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoyw9C(upcastSelf.this, node.this)
        return returnValue

    def __overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(self, childNode, sort):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoQQ0n(upcastSelf.this, childNode.this, sort)
        return returnValue

    def __overloaded_addStashed_ptrPandaNode_ptrPandaNode(self, childNode):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoswLI(upcastSelf.this, childNode.this)
        return returnValue

    def removeStashed(self, n):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoYHe7(upcastSelf.this, n)
        return returnValue

    def removeAllChildren(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoayap(upcastSelf.this)
        return returnValue

    def stealChildren(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoignr(upcastSelf.this, other.this)
        return returnValue

    def copyChildren(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyohfED(upcastSelf.this, other.this)
        return returnValue

    def __overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(self, attrib, override):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo48Bd(upcastSelf.this, attrib.this, override)
        return returnValue

    def __overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(self, attrib):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoAD5k(upcastSelf.this, attrib.this)
        return returnValue

    def getAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoaDfJ(upcastSelf.this, type.this)
        import RenderAttrib
        returnObject = RenderAttrib.RenderAttrib(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def hasAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo2W_P(upcastSelf.this, type.this)
        return returnValue

    def clearAttrib(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoCSEu(upcastSelf.this, type.this)
        return returnValue

    def setEffect(self, effect):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoKWvI(upcastSelf.this, effect.this)
        return returnValue

    def getEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo17Hl(upcastSelf.this, type.this)
        import RenderEffect
        returnObject = RenderEffect.RenderEffect(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def hasEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoJ1nr(upcastSelf.this, type.this)
        return returnValue

    def clearEffect(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoOUJ2(upcastSelf.this, type.this)
        return returnValue

    def setState(self, state):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoGDjV(upcastSelf.this, state.this)
        return returnValue

    def getState(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoIocj(upcastSelf.this)
        import RenderState
        returnObject = RenderState.RenderState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def clearState(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyotySF(upcastSelf.this)
        return returnValue

    def setEffects(self, effects):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo2lpj(upcastSelf.this, effects.this)
        return returnValue

    def getEffects(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo1WLf(upcastSelf.this)
        import RenderEffects
        returnObject = RenderEffects.RenderEffects(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def clearEffects(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo6yPH(upcastSelf.this)
        return returnValue

    def setTransform(self, transform):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo_5Ti(upcastSelf.this, transform.this)
        return returnValue

    def getTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo1dH2(upcastSelf.this)
        import TransformState
        returnObject = TransformState.TransformState(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def clearTransform(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoHjK_(upcastSelf.this)
        return returnValue

    def setDrawMask(self, mask):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoSSGr(upcastSelf.this, mask.this)
        return returnValue

    def getDrawMask(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoWJXI(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    def getNetCollideMask(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo4l_T(upcastSelf.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    def ls(self, out, indentLevel):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyouBSg(upcastSelf.this, out.this, indentLevel)
        return returnValue

    def __overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyond5g(upcastSelf.this, type)
        return returnValue

    def __overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo7Bq1(upcastSelf.this, volume.this)
        return returnValue

    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyohf0y(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def getInternalBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyoI_J4(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self.__overloaded_setBound_ptrPandaNode___enum__BoundingVolumeType(_args[0])
            else:
                if isinstance(_args[0], BoundingVolume.BoundingVolume):
                    return self.__overloaded_setBound_ptrPandaNode_ptrConstBoundingVolume(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    def addChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self.__overloaded_addChild_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            if numArgs == 2:
                import PandaNode
                if isinstance(_args[0], PandaNode.PandaNode):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_addChild_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    def unstashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self.__overloaded_unstashChild_ptrPandaNode_int(_args[0])
            else:
                if isinstance(_args[0], PandaNode.PandaNode):
                    return self.__overloaded_unstashChild_ptrPandaNode_ptrPandaNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    def addStashed(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], PandaNode.PandaNode):
                return self.__overloaded_addStashed_ptrPandaNode_ptrPandaNode(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
        else:
            if numArgs == 2:
                import PandaNode
                if isinstance(_args[0], PandaNode.PandaNode):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_addStashed_ptrPandaNode_ptrPandaNode_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PandaNode.PandaNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    def removeChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self.__overloaded_removeChild_ptrPandaNode_int(_args[0])
            else:
                if isinstance(_args[0], PandaNode.PandaNode):
                    return self.__overloaded_removeChild_ptrPandaNode_ptrPandaNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    def stashChild(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import PandaNode
            if isinstance(_args[0], types.IntType):
                return self.__overloaded_stashChild_ptrPandaNode_int(_args[0])
            else:
                if isinstance(_args[0], PandaNode.PandaNode):
                    return self.__overloaded_stashChild_ptrPandaNode_ptrPandaNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PandaNode.PandaNode> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    def setAttrib(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import RenderAttrib
            if isinstance(_args[0], RenderAttrib.RenderAttrib):
                return self.__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
        else:
            if numArgs == 2:
                import RenderAttrib
                if isinstance(_args[0], RenderAttrib.RenderAttrib):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_setAttrib_ptrPandaNode_ptrConstRenderAttrib_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <RenderAttrib.RenderAttrib> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

    def upcastToNamable(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyojprb(upcastSelf.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def upcastToBoundedObject(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyo8YS5(upcastSelf.this)
        import BoundedObject
        returnObject = BoundedObject.BoundedObject(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def upcastToReferenceCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpanda._inPkJyogdrc(upcastSelf.this)
        import ReferenceCount
        returnObject = ReferenceCount.ReferenceCount(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def getType(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpandaexpress._inPJoxt1uxI(upcastSelf.this)
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject
        return

    def getTypeIndex(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpandaexpress._inPJoxtm7AU(upcastSelf.this)
        return returnValue

    def isOfType(self, handle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpandaexpress._inPJoxtmFKt(upcastSelf.this, handle.this)
        return returnValue

    def isExactType(self, handle):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        returnValue = libpandaexpress._inPJoxtkXzz(upcastSelf.this, handle.this)
        return returnValue

    def assign(self, other):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtp1bI(upcastSelf.this, other.this)
        import Namable
        returnObject = Namable.Namable(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        return returnObject
        return

    def setName(self, name):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtLNBW(upcastSelf.this, name)
        return returnValue

    def clearName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtavUl(upcastSelf.this)
        return returnValue

    def hasName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtYjhC(upcastSelf.this)
        return returnValue

    def getName(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToNamable()
        returnValue = libpandaexpress._inPJoxtfARN(upcastSelf.this)
        return returnValue

    def __overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPC76J(upcastSelf.this, type)
        return returnValue

    def __overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPXVRr(upcastSelf.this, volume.this)
        return returnValue

    def getBound(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPtOIb(upcastSelf.this)
        import BoundingVolume
        returnObject = BoundingVolume.BoundingVolume(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()
        return

    def markBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPG4uI(upcastSelf.this)
        return returnValue

    def forceBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPi1Pw(upcastSelf.this)
        return returnValue

    def isBoundStale(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPjac5(upcastSelf.this)
        return returnValue

    def setFinal(self, flag):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPy9vH(upcastSelf.this, flag)
        return returnValue

    def isFinal(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToBoundedObject()
        returnValue = libpanda._inPMAKPUuL4(upcastSelf.this)
        return returnValue

    def setBound(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import BoundingVolume
            if isinstance(_args[0], types.IntType):
                return self.__overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(_args[0])
            else:
                if isinstance(_args[0], BoundingVolume.BoundingVolume):
                    return self.__overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
        else:
            raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

    def getRefCount(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtM11_(upcastSelf.this)
        return returnValue

    def ref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtVS5_(upcastSelf.this)
        return returnValue

    def unref(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtzyVy(upcastSelf.this)
        return returnValue

    def testRefCountIntegrity(self):
        upcastSelf = self
        upcastSelf = upcastSelf.upcastToLensNode()
        upcastSelf = upcastSelf.upcastToReferenceCount()
        returnValue = libpandaexpress._inPJoxtupj2(upcastSelf.this)
        return returnValue

    def write(self, *_args):
        numArgs = len(_args)
        if numArgs == 1:
            import Ostream
            if isinstance(_args[0], Ostream.Ostream):
                return self.__overloaded_write_ptrConstLightLensNode_ptrOstream(_args[0])
            else:
                raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
        else:
            if numArgs == 2:
                import Ostream
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.__overloaded_write_ptrConstLightLensNode_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '