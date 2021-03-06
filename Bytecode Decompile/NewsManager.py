from ShowBaseGlobal import *
import DistributedObject, DirectNotifyGlobal, ToontownGlobals, ToontownBattleGlobals, SuitBattleGlobals, Localizer
from IntervalGlobal import *

class NewsManager(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('NewsManager')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.population = 0
        self.invading = 0
        toonbase.tcr.newsManager = self
        toonbase.localToon.inventory.setInvasionCreditMultiplier(1)

    def delete(self):
        self.cr.newsManager = None
        DistributedObject.DistributedObject.delete(self)
        return

    def setPopulation(self, population):
        self.population = population
        messenger.send('newPopulation', [population])

    def getPopulation(self):
        return population

    def setInvasionStatus(self, msgType, cogType, numRemaining):
        print ' NewsManager: Invasion Status: msgType: %s cogType: %s, numRemaining: %s' % (msgType, cogType, numRemaining)
        cogName = SuitBattleGlobals.SuitAttributes[cogType]['name']
        cogNameP = SuitBattleGlobals.SuitAttributes[cogType]['pluralname']
        if msgType == ToontownGlobals.SuitInvasionBegin:
            msg1 = Localizer.SuitInvasionBegin1
            msg2 = Localizer.SuitInvasionBegin2 % cogNameP
            self.invading = 1
        else:
            if msgType == ToontownGlobals.SuitInvasionUpdate:
                msg1 = Localizer.SuitInvasionUpdate1 % numRemaining
                msg2 = Localizer.SuitInvasionUpdate2 % cogNameP
                self.invading = 1
            else:
                if msgType == ToontownGlobals.SuitInvasionEnd:
                    msg1 = Localizer.SuitInvasionEnd1 % cogName
                    msg2 = Localizer.SuitInvasionEnd2
                    self.invading = 0
                else:
                    if msgType == ToontownGlobals.SuitInvasionBulletin:
                        msg1 = Localizer.SuitInvasionBulletin1
                        msg2 = Localizer.SuitInvasionBulletin2 % cogNameP
                        self.invading = 1
                    else:
                        self.notify.warning('setInvasionStatus: invalid msgType: %s' % msgType)
                        return
        if self.invading:
            mult = ToontownBattleGlobals.getInvasionMultiplier()
        else:
            mult = 1
        toonbase.localToon.inventory.setInvasionCreditMultiplier(mult)
        Sequence(Wait(1.0), Func(toonbase.localToon.setSystemMessage, 0, msg1), Wait(5.0), Func(toonbase.localToon.setSystemMessage, 0, msg2), name='newsManagerWait').start()
        return

    def getInvading(self):
        return self.invading