from PandaModules import *
from DirectNotifyGlobal import *
import Interval, LerpBlendHelpers

class LerpNodePathInterval(CLerpNodePathInterval):
    __module__ = __name__
    lerpNodePathNum = 1

    def __init__(self, name, duration, blendType, bakeInStart, node, other):
        if name == None:
            name = '%s-%d' % (self.__class__.__name__, self.lerpNodePathNum)
            LerpNodePathInterval.lerpNodePathNum += 1
        blendType = self.stringBlendType(blendType)
        if other == None:
            other = NodePath()
        CLerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        return

    def anyCallable(self, *params):
        for param in params:
            if callable(param):
                return 1

        return 0

    def setupParam(self, func, param):
        if param != None:
            if callable(param):
                func(param())
            else:
                func(param)
        return


class LerpPosInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, pos, startPos=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.paramSetup = self.anyCallable(pos, startPos)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
        return

    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
        LerpNodePathInterval.privDoEvent(self, t, event)


class LerpHprInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, hpr, startHpr=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.paramSetup = self.anyCallable(hpr, startHpr)
        if self.paramSetup:
            self.endHpr = hpr
            self.startHpr = startHpr
            self.inPython = 1
        else:
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
        return

    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
        LerpNodePathInterval.privDoEvent(self, t, event)


class LerpScaleInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, scale, startScale=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.paramSetup = self.anyCallable(scale, startScale)
        if self.paramSetup:
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
        return

    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        LerpNodePathInterval.privDoEvent(self, t, event)


class LerpPosHprInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, pos, hpr, startPos=None, startHpr=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.paramSetup = self.anyCallable(pos, startPos, hpr, startHpr)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endHpr = hpr
            self.startHpr = startHpr
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
        return

    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
        LerpNodePathInterval.privDoEvent(self, t, event)


class LerpHprScaleInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, hpr, scale, startHpr=None, startScale=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.paramSetup = self.anyCallable(hpr, startHpr, scale, startScale)
        if self.paramSetup:
            self.endHpr = hpr
            self.startHpr = startHpr
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
        return

    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        LerpNodePathInterval.privDoEvent(self, t, event)


class LerpPosHprScaleInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, pos, hpr, scale, startPos=None, startHpr=None, startScale=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.paramSetup = self.anyCallable(pos, startPos, hpr, startHpr, scale, startScale)
        if self.paramSetup:
            self.endPos = pos
            self.startPos = startPos
            self.endHpr = hpr
            self.startHpr = startHpr
            self.endScale = scale
            self.startScale = startScale
            self.inPython = 1
        else:
            self.setEndPos(pos)
            if startPos != None:
                self.setStartPos(startPos)
            self.setEndHpr(hpr)
            if startHpr != None:
                self.setStartHpr(startHpr)
            self.setEndScale(scale)
            if startScale != None:
                self.setStartScale(startScale)
        return

    def privDoEvent(self, t, event):
        if self.paramSetup and event == CInterval.ETInitialize:
            self.setupParam(self.setEndPos, self.endPos)
            self.setupParam(self.setStartPos, self.startPos)
            self.setupParam(self.setEndHpr, self.endHpr)
            self.setupParam(self.setStartHpr, self.startHpr)
            self.setupParam(self.setEndScale, self.endScale)
            self.setupParam(self.setStartScale, self.startScale)
        LerpNodePathInterval.privDoEvent(self, t, event)


class LerpColorScaleInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, colorScale, startColorScale=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.setEndColorScale(colorScale)
        if startColorScale != None:
            self.setStartColorScale(startColorScale)
        return


class LerpColorInterval(LerpNodePathInterval):
    __module__ = __name__

    def __init__(self, node, duration, color, startColor=None, other=None, blendType='noBlend', bakeInStart=1, name=None):
        LerpNodePathInterval.__init__(self, name, duration, blendType, bakeInStart, node, other)
        self.setEndColor(color)
        if startColor != None:
            self.setStartColor(startColor)
        return


class LerpFunctionInterval(Interval.Interval):
    __module__ = __name__
    lerpFunctionIntervalNum = 1
    notify = directNotify.newCategory('LerpFunctionInterval')

    def __init__(self, function, fromData=0, toData=1, duration=0.0, blendType='noBlend', extraArgs=[], name=None):
        self.function = function
        self.fromData = fromData
        self.toData = toData
        self.blendType = self.getBlend(blendType)
        self.extraArgs = extraArgs
        if name == None:
            name = 'LerpFunctionInterval-%d' % LerpFunctionInterval.lerpFunctionIntervalNum
            LerpFunctionInterval.lerpFunctionIntervalNum += 1
        Interval.Interval.__init__(self, name, duration)
        return

    def privStep(self, t):
        if t >= self.duration:
            apply(self.function, [self.toData] + self.extraArgs)
        else:
            if self.duration == 0.0:
                apply(self.function, [self.toData] + self.extraArgs)
            else:
                bt = self.blendType(t / self.duration)
                data = self.fromData * (1 - bt) + self.toData * bt
                apply(self.function, [data] + self.extraArgs)
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))
        self.state = CInterval.SStarted
        self.currT = t

    def getBlend(self, blendType):
        if blendType == 'easeIn':
            return LerpBlendHelpers.easeIn
        else:
            if blendType == 'easeOut':
                return LerpBlendHelpers.easeOut
            else:
                if blendType == 'easeInOut':
                    return LerpBlendHelpers.easeInOut
                else:
                    if blendType == 'noBlend':
                        return LerpBlendHelpers.noBlend
                    else:
                        raise Exception('Error: LerpInterval.__getBlend: Unknown blend type')


class LerpFunc(LerpFunctionInterval):
    __module__ = __name__

    def __init__(self, *args, **kw):
        LerpFunctionInterval.__init__(self, *args, **kw)