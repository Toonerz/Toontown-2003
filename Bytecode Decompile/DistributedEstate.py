from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from ClockDelta import *
import math, ToontownGlobals, DistributedObject, DirectNotifyGlobal, FSM, State, AvatarDNA, Toon, RandomNumGen, Localizer, random, whrandom, cPickle, DelayDelete, PythonUtil, Place, Estate, HouseGlobals

class DistributedEstate(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = directNotify.newCategory('DistributedEstate')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.load()
        self.initCamera()
        self.closestHouse = 0
        self.ground = None
        return

    def disable(self):
        self.notify.debug('disable')

    def delete(self):
        self.notify.debug('delete')
        self.unload()
        DistributedObject.DistributedObject.delete(self)

    def load(self):
        self.notify.debug('load')
        self.lt = toonbase.localToon
        self.lt.estate = self

    def unload(self):
        self.notify.debug('unload')
        self.ignoreAll()
        if self.ground:
            self.ground.removeNode()
            del self.ground
        self.lt.estate = None
        toonbase.localToon.stopChat()
        self.__killColorClosestHouseTask()
        self.__killAirplaneTask()
        if self.airplane:
            self.airplane.removeNode()
            del self.airplane
            self.airplane = None
        return

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.loadAirplane()

    def loadAirplane(self):
        self.airplane = loader.loadModel('phase_4/models/props/airplane.bam')
        self.airplane.setScale(8)
        self.airplane.setPos(0, 0, 1)
        self.banner = self.airplane.find('**/*banner')
        bannerText = TextNode('bannerText')
        bannerText.freeze()
        bannerText.setTextColor(1, 0, 0, 1)
        bannerText.setAlign(bannerText.ACenter)
        bannerText.setFont(ToontownGlobals.getSignFont())
        bannerText.setText('Cog invasion!!!')
        self.bn = self.banner.attachNewNode(bannerText.generate())
        self.bn.setHpr(180, 0, 0)
        self.bn.setPos(-1.8, 0.1, 0)
        self.bn.setScale(0.35)
        self.banner.hide()
        self.__startAirplaneTask()
        self.airplane.reparentTo(render)

    def initCamera(self):
        initCamPos = VBase3(0, -10, 5)
        initCamHpr = VBase3(0, -10, 0)

    def setEstateType(self, index):
        self.estateType = index

    def setHouseInfo(self, houseInfo):
        self.notify.debug('setHouseInfo')
        houseType, housePos = cPickle.loads(houseInfo)
        self.loadEstate(houseType, housePos)

    def loadEstate(self, indexList, posList):
        self.notify.debug('loadEstate')
        self.houseType = indexList
        self.housePos = posList
        self.numHouses = len(self.houseType)
        self.house = [None] * self.numHouses
        self.__startAirplaneTask()
        self.airplane.reparentTo(render)
        return

    def __startAirplaneTask(self):
        self.theta = 0
        self.phi = 0
        taskMgr.remove(self.taskName('estate-airplane'))
        taskMgr.add(self.airplaneFlyTask, self.taskName('estate-airplane'))

    def __pauseAirplaneTask(self):
        pause = 45
        self.phi = 0
        self.theta = (self.theta + 10) % 360
        taskMgr.remove(self.taskName('estate-airplane'))
        taskMgr.doMethodLater(pause, self.airplaneFlyTask, self.taskName('estate-airplane'))

    def __killAirplaneTask(self):
        taskMgr.remove(self.taskName('estate-airplane'))

    def airplaneFlyTask(self, task):
        rad = 300.0
        amp = 80.0
        self.theta += 0.25
        self.phi += 0.005
        sinPhi = math.sin(self.phi)
        if sinPhi <= 0:
            self.__pauseAirplaneTask()
        angle = math.pi * self.theta / 180.0
        x = rad * math.cos(angle)
        y = rad * math.sin(angle)
        z = amp * sinPhi
        self.airplane.setH(90 + self.theta)
        self.airplane.setPos(x, y, z)
        return Task.cont

    def sendHouseColor(self, index, r, g, b, a):
        self.house[index].setColor(r, g, b, a)

    def colorClosestHouse(self, task):
        try:
            pos = self.lt.getPos()
            tx = pos[0]
            ty = pos[1]
            tz = pos[2]
        except:
            self.__startColorClosestHouseTask()
            return Task.done
        else:
            minSqDist = 1000000
            minIndex = 0
            for i in range(self.numHouses):
                x, y, z, h, p, r = self.housePos[i]
                dx = x - tx
                dy = y - ty
                sqdist = dx * dx + dy * dy
                if sqdist < minSqDist:
                    minIndex = i
                    minSqDist = sqdist

            if minSqDist < 128 and minIndex != self.closestHouse:
                r = 0
                g = whrandom.random()
                b = whrandom.random()
                a = 1
                self.sendUpdate('setClosestHouse', [self.closestHouse])
                self.closestHouse = minIndex
                self.sendUpdate('setClosestHouse', [self.closestHouse])

        self.__startColorClosestHouseTask()
        return Task.done

    def __startColorClosestHouseTask(self):
        taskMgr.remove(self.taskName('color-closest-house'))
        taskMgr.doMethodLater(0.2, self.colorClosestHouse, self.taskName('color-closest-house'))

    def __killColorClosestHouseTask(self):
        taskMgr.remove(self.taskName('color-closest-house'))