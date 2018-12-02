from DirectGui import *
import Quests, NPCToons, ToonHead, AvatarDNA, Suit, ZoneUtil, ToontownGlobals, Localizer, string, LaffMeter
from ToontownBattleGlobals import AvPropsNew
IMAGE_SCALE_LARGE = 0.2
IMAGE_SCALE_SMALL = 0.15
POSTER_WIDTH = 0.7
TEXT_SCALE = 0.045
TEXT_WORDWRAP = 15.6

class QuestPoster(DirectFrame):
    __module__ = __name__
    colors = {'white': (1, 1, 1, 1), 'blue': (0.45, 0.45, 0.8, 1), 'lightBlue': (0.42, 0.671, 1.0, 1.0), 'green': (0.45, 0.8, 0.45, 1), 'lightGreen': (0.784, 1, 0.863, 1), 'red': (0.8, 0.45, 0.45, 1), 'rewardRed': (0.8, 0.3, 0.3, 1), 'brightRed': (1.0, 0.16, 0.16, 1.0), 'brown': (0.52, 0.42, 0.22, 1)}
    normalTextColor = (
     0.3, 0.25, 0.2, 1)

    def __init__(self, parent=aspect2d, **kw):
        bookModel = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
        questCard = bookModel.find('**/questCard')
        optiondefs = (
         (
          'relief', None, None), ('reverse', 0, None), ('image', questCard, None), ('image_scale', (0.8, 1.0, 0.58), None), ('state', NORMAL, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, relief=None)
        self.initialiseoptions(QuestPoster)
        self.questFrame = DirectFrame(parent=self, relief=None)
        self.headline = DirectLabel(parent=self.questFrame, relief=None, text='', text_font=ToontownGlobals.getMinnieFont(), text_fg=self.normalTextColor, text_scale=0.05, text_align=TextNode.ACenter, text_wordwrap=12.0, textMayChange=1, pos=(0, 0, 0.23))
        self.questInfo = DirectLabel(parent=self.questFrame, relief=None, text='', text_fg=self.normalTextColor, text_scale=TEXT_SCALE, text_align=TextNode.ACenter, text_wordwrap=TEXT_WORDWRAP, textMayChange=1, pos=(0, 0, -0.0625))
        self.rewardText = DirectLabel(parent=self.questFrame, relief=None, text='', text_fg=self.colors['rewardRed'], text_scale=0.0425, text_align=TextNode.ALeft, text_wordwrap=17.0, textMayChange=1, pos=(-0.36, 0, -0.26))
        self.rewardText.hide()
        self.lPictureFrame = DirectFrame(parent=self.questFrame, relief=None, image=bookModel.find('**/questPictureFrame'), image_scale=IMAGE_SCALE_SMALL, text='', text_pos=(0, -0.11), text_fg=self.normalTextColor, text_scale=TEXT_SCALE, text_align=TextNode.ACenter, text_wordwrap=8.0, textMayChange=1)
        self.lPictureFrame.hide()
        self.rPictureFrame = DirectFrame(parent=self.questFrame, relief=None, image=bookModel.find('**/questPictureFrame'), image_scale=IMAGE_SCALE_SMALL, text='', text_pos=(0, -0.11), text_fg=self.normalTextColor, text_scale=TEXT_SCALE, text_align=TextNode.ACenter, text_wordwrap=8.0, textMayChange=1, pos=(0.18, 0, 0.13))
        self.rPictureFrame.hide()
        self.lQuestIcon = DirectFrame(parent=self.lPictureFrame, relief=None, text=' ', text_font=ToontownGlobals.getSuitFont(), text_pos=(0, -0.03), text_fg=self.normalTextColor, text_scale=0.13, text_align=TextNode.ACenter, text_wordwrap=13.0, textMayChange=1)
        self.lQuestIcon.setColorOff()
        self.rQuestIcon = DirectFrame(parent=self.rPictureFrame, relief=None, text=' ', text_font=ToontownGlobals.getSuitFont(), text_pos=(0, -0.03), text_fg=self.normalTextColor, text_scale=0.13, text_align=TextNode.ACenter, text_wordwrap=13.0, textMayChange=1)
        self.rQuestIcon.setColorOff()
        self.auxText = DirectLabel(parent=self.questFrame, relief=None, text='', text_scale=0.04, text_fg=self.normalTextColor, text_align=TextNode.ACenter, textMayChange=1)
        self.auxText.hide()
        self.questProgress = DirectWaitBar(parent=self.questFrame, relief=SUNKEN, frameSize=(-0.95, 0.95, -0.1, 0.12), borderWidth=(0.025, 0.025), scale=0.2, frameColor=(0.945, 0.875, 0.706, 1.0), barColor=(0.5, 0.7, 0.5, 1), text='0/0', text_scale=0.19, text_fg=(0.05, 0.14, 0.4, 1), text_align=TextNode.ACenter, text_pos=(0, -0.04), pos=(0, 0, -0.195))
        self.questProgress.hide()
        self.funQuest = DirectLabel(parent=self.questFrame, relief=None, text=Localizer.QuestPosterFun, text_fg=(0.0, 0.439, 1.0, 1.0), text_shadow=(0, 0, 0, 1), pos=(-0.28, 0, 0.19), scale=0.04)
        self.funQuest.setR(30)
        self.funQuest.hide()
        bookModel.removeNode()
        self.reverseBG(self['reverse'])
        self.laffMeter = None
        return

    def reverseBG(self, reverse=0):
        try:
            self.initImageScale
        except AttributeError:
            self.initImageScale = self['image_scale']
            if reverse:
                self.initImageScale.setX(-abs(self.initImageScale[0]))
                self.questFrame.setX(0.015)
            else:
                self.initImageScale.setX(abs(self.initImageScale[0]))
            self['image_scale'] = self.initImageScale

    def mouseEnterPoster(self, event):
        self.reparentTo(self.getParent())
        sc = Vec3(self.initImageScale)
        sc.setZ(sc[2] + 0.07)
        self['image_scale'] = sc
        self.questFrame.setZ(0.03)
        self.rewardText.show()

    def mouseExitPoster(self, event):
        self['image_scale'] = self.initImageScale
        self.questFrame.setZ(0)
        self.rewardText.hide()

    def createNpcToonHead(self, toNpcId):
        npcInfo = NPCToons.NPCToonDict[toNpcId]
        dnaList = npcInfo[2]
        gender = npcInfo[3]
        if dnaList == 'r':
            dnaList = NPCToons.getRandomDNA(toNpcId, gender)
        dna = AvatarDNA.AvatarDNA()
        dna.newToonFromProperties(*dnaList)
        head = ToonHead.ToonHead()
        head.setupHead(dna, forGui=1)
        self.fitGeometry(head, fFlip=1)
        return head

    def createLaffMeter(self, hp):
        lm = LaffMeter.LaffMeter(toonbase.localToon.style, hp, hp)
        lm.adjustText()
        return lm

    def createSuitHead(self, suitName):
        suitDNA = AvatarDNA.AvatarDNA()
        suitDNA.newSuit(suitName)
        suit = Suit.Suit()
        suit.setDNA(suitDNA)
        headParts = suit.getHeadParts()
        head = hidden.attachNewNode('head')
        for part in headParts:
            copyPart = part.copyTo(head)
            copyPart.setDepthTest(1)
            copyPart.setDepthWrite(1)

        self.fitGeometry(head, fFlip=1)
        suit.delete()
        suit = None
        return head
        return

    def loadElevator(self, building, numFloors):
        elevatorNodePath = hidden.attachNewNode('elevatorNodePath')
        elevatorModel = loader.loadModelCopy('phase_5/models/modules/elevator')
        floorIndicator = [
         None, None, None, None, None]
        npc = elevatorModel.findAllMatches('**/floor_light_?;+s')
        for i in range(npc.getNumPaths()):
            np = npc.getPath(i)
            floor = int(np.getName()[-1:]) - 1
            floorIndicator[floor] = np
            if floor < numFloors:
                np.setColor(Vec4(0.5, 0.5, 0.5, 1.0))
            else:
                np.hide()

        elevatorModel.reparentTo(elevatorNodePath)
        suitDoorOrigin = building.find('**/*_door_origin')
        elevatorNodePath.reparentTo(suitDoorOrigin)
        elevatorNodePath.setPosHpr(0, 0, 0, 0, 0, 0)
        return

    def fitGeometry(self, geom, fFlip=0, dimension=0.8):
        p1 = Point3()
        p2 = Point3()
        geom.calcTightBounds(p1, p2)
        if fFlip:
            t = p1[0]
            p1.setX(-p2[0])
            p2.setX(-t)
        d = p2 - p1
        biggest = max(d[0], d[2])
        s = dimension / biggest
        mid = (p1 + d / 2.0) * s
        geomXform = hidden.attachNewNode('geomXform')
        for child in geom.getChildrenAsList():
            child.reparentTo(geomXform)

        geomXform.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2], 180, 0, 0, s, s, s)
        geomXform.reparentTo(geom)

    def clear(self):
        self['image_color'] = Vec4(*self.colors['white'])
        self.headline['text'] = ''
        self.headline['text_fg'] = self.normalTextColor
        self.questInfo['text'] = ''
        self.questInfo['text_fg'] = self.normalTextColor
        self.rewardText['text'] = ''
        self.auxText['text'] = ''
        self.auxText['text_fg'] = self.normalTextColor
        self.funQuest.hide()
        self.lPictureFrame.hide()
        self.rPictureFrame.hide()
        self.questProgress.hide()
        if hasattr(self, 'chooseButton'):
            self.chooseButton.destroy()
            del self.chooseButton

    def showChoicePoster(self, questId, fromNpcId, toNpcId, rewardId, callback):
        self.update((questId, fromNpcId, toNpcId, rewardId, 0))
        quest = Quests.getQuest(questId)
        self.rewardText.show()
        self.rewardText.setZ(-0.205)
        self.questProgress.hide()
        if not hasattr(self, 'chooseButton'):
            guiButton = loader.loadModelOnce('phase_3/models/gui/quit_button')
            self.chooseButton = DirectButton(parent=self.questFrame, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=(0.7, 1, 1), text=Localizer.QuestPageChoose, text_scale=0.06, text_pos=(0, -0.02), pos=(0.27, 0, 0.24), scale=0.65)
            guiButton.removeNode()
        self.chooseButton['command'] = callback
        self.chooseButton['extraArgs'] = [questId]
        self.unbind(WITHIN)
        self.unbind(WITHOUT)
        return

    def update(self, questDesc):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        quest = Quests.getQuest(questId)
        if rewardId == Quests.NA:
            finalReward = Quests.getFinalRewardId(questId, fAll=1)
            transformedReward = Quests.transformReward(finalReward, toonbase.localToon)
            reward = Quests.getReward(transformedReward)
        else:
            reward = Quests.getReward(rewardId)
        if reward:
            rewardString = reward.getPosterString()
        else:
            rewardString = ''
        self.rewardText['text'] = rewardString
        self.fitLabel(self.rewardText)
        questEntry = Quests.QuestDict.get(questId)
        if questEntry:
            tier = questEntry[0]
            fOptional = Quests.isRewardOptional(tier, rewardId)
        else:
            fOptional = 0
        if fOptional:
            self.funQuest.show()
        else:
            self.funQuest.hide()
        fComplete = quest.getCompletionStatus(toonbase.localToon, questDesc) == Quests.COMPLETE
        fromNpcName = NPCToons.getNPCName(fromNpcId)
        npcZone = NPCToons.getNPCZone(fromNpcId)
        hoodId = ZoneUtil.getHoodId(npcZone)
        branchId = ZoneUtil.getBranchZone(npcZone)
        if fromNpcId == Quests.ToonHQ:
            locationName = Localizer.QuestPosterHQLocationName
            buildingName = Localizer.QuestPosterHQBuildingName
            streetName = Localizer.QuestPosterHQStreetName
        else:
            if fromNpcId == Quests.ToonTailor:
                locationName = Localizer.QuestPosterTailorLocationName
                buildingName = Localizer.QuestPosterTailorBuildingName
                streetName = Localizer.QuestPosterTailorStreetName
            else:
                locationName = toonbase.tcr.hoodMgr.getFullnameFromId(hoodId)
                buildingName = NPCToons.getBuildingTitle(npcZone)
                streetName = ZoneUtil.getStreetName(branchId)
        if toNpcId == Quests.ToonHQ:
            toNpcName = Localizer.QuestPosterHQOfficer
            toNpcBuildingName = Localizer.QuestPosterHQBuildingName
            toNpcStreetName = Localizer.QuestPosterHQStreetName
            toNpcLocationName = Localizer.QuestPosterHQLocationName
        else:
            if toNpcId == Quests.ToonTailor:
                toNpcName = Localizer.QuestPosterTailor
                toNpcBuildingName = Localizer.QuestPosterTailorBuildingName
                toNpcStreetName = Localizer.QuestPosterTailorStreetName
                toNpcLocationName = Localizer.QuestPosterTailorLocationName
            else:
                toNpcName = NPCToons.getNPCName(toNpcId)
                toNpcZone = NPCToons.getNPCZone(toNpcId)
                toNpcHoodId = ZoneUtil.getHoodId(toNpcZone)
                toNpcLocationName = toonbase.tcr.hoodMgr.getFullnameFromId(toNpcHoodId)
                toNpcBuildingName = NPCToons.getBuildingTitle(toNpcZone)
                toNpcBranchId = ZoneUtil.getBranchZone(toNpcZone)
                toNpcStreetName = ZoneUtil.getStreetName(toNpcBranchId)
        lPos = Vec3(0, 0, 0.13)
        lIconGeom = None
        lIconGeomScale = 1
        rIconGeom = None
        rIconGeomScale = 1
        infoText = ''
        infoZ = -0.0625
        auxText = None
        auxTextPos = Vec3(0, 0, 0.12)
        headlineString = quest.getHeadlineString()
        captions = map(string.capwords, quest.getObjectiveStrings())
        imageColor = Vec4(*self.colors['white'])
        if quest.getType() == Quests.DeliverGagQuest or quest.getType() == Quests.DeliverItemQuest:
            frameBgColor = 'red'
            if quest.getType() == Quests.DeliverGagQuest:
                invModel = loader.loadModelOnce('phase_3.5/models/gui/inventory_icons')
                track, item = quest.getGagType()
                lIconGeom = invModel.find('**/' + AvPropsNew[track][item])
                invModel.removeNode()
            else:
                bookModel = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = bookModel.find('**/package')
                lIconGeomScale = 0.12
                bookModel.removeNode()
            if not fComplete:
                captions.append(toNpcName)
                auxText = Localizer.QuestPosterAuxTo
                auxTextPos.setZ(0.12)
                lPos.setX(-0.18)
                infoText = Localizer.QuestPageDestination % (toNpcBuildingName, toNpcStreetName, toNpcLocationName)
                rIconGeom = self.createNpcToonHead(toNpcId)
                rIconGeomScale = IMAGE_SCALE_SMALL
        else:
            if quest.getType() == Quests.RecoverItemQuest:
                frameBgColor = 'green'
                bookModel = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = bookModel.find('**/package')
                lIconGeomScale = 0.12
                bookModel.removeNode()
                if not fComplete:
                    rIconGeomScale = IMAGE_SCALE_SMALL
                    holder = quest.getHolder()
                    holderType = quest.getHolderType()
                    if holder == Quests.Any:
                        cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                        rIconGeom = cogIcons.find('**/cog')
                        cogIcons.removeNode()
                        lPos.setX(-0.18)
                        auxText = Localizer.QuestPosterAuxFrom
                    else:
                        if holder == Quests.AnyFish:
                            headlineString = 'GO FISHING'
                            auxText = Localizer.QuestPosterAuxFor
                            auxTextPos.setX(-0.18)
                            captions = captions[:1]
                        else:
                            if holderType == 'track':
                                cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                                if holder == 'c':
                                    icon = cogIcons.find('**/CorpIcon')
                                else:
                                    if holder == 's':
                                        icon = cogIcons.find('**/SalesIcon')
                                    else:
                                        if holder == 'l':
                                            icon = cogIcons.find('**/LegalIcon')
                                        else:
                                            if holder == 'm':
                                                icon = cogIcons.find('**/MoneyIcon')
                                rIconGeom = icon.copyTo(hidden)
                                rIconGeom.setColor(Suit.Suit.medallionColors[holder])
                                rIconGeomScale = 0.12
                                cogIcons.removeNode()
                            else:
                                if holderType == 'level':
                                    cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                                    rIconGeom = cogIcons.find('**/cog')
                                    rIconGeomScale = IMAGE_SCALE_SMALL
                                    cogIcons.removeNode()
                                else:
                                    rIconGeom = self.createSuitHead(holder)
                            lPos.setX(-0.18)
                            auxText = Localizer.QuestPosterAuxFrom
                    infoText = string.capwords(quest.getLocationName())
                    if infoText == '':
                        infoText = Localizer.QuestPosterAnywhere
            else:
                if quest.getType() == Quests.VisitQuest:
                    frameBgColor = 'brown'
                    captions[0] = '%s' % toNpcName
                    lIconGeom = self.createNpcToonHead(toNpcId)
                    lIconGeomScale = IMAGE_SCALE_SMALL
                    if not fComplete:
                        infoText = Localizer.QuestPageDestination % (toNpcBuildingName, toNpcStreetName, toNpcLocationName)
                else:
                    if quest.getType() == Quests.TrackChoiceQuest:
                        frameBgColor = 'green'
                        invModel = loader.loadModelOnce('phase_3.5/models/gui/inventory_icons')
                        track1, track2 = quest.getChoices()
                        lIconGeom = invModel.find('**/' + AvPropsNew[track1][1])
                        if not fComplete:
                            auxText = Localizer.QuestPosterAuxOr
                            lPos.setX(-0.18)
                            rIconGeom = invModel.find('**/' + AvPropsNew[track2][1])
                            infoText = Localizer.QuestPageNameAndDestination % (toNpcName, toNpcBuildingName, toNpcStreetName, toNpcLocationName)
                            infoZ = -0.02
                        invModel.removeNode()
                    else:
                        if quest.getType() == Quests.BuildingQuest:
                            frameBgColor = 'blue'
                            track = quest.getBuildingTrack()
                            numFloors = quest.getNumFloors()
                            if track == 'c':
                                lIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_corp')
                            else:
                                if track == 'l':
                                    lIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_legal')
                                else:
                                    if track == 'm':
                                        lIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_money')
                                    else:
                                        if track == 's':
                                            lIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_sales')
                                        else:
                                            bookModel = loader.loadModelCopy('phase_3.5/models/gui/stickerbook_gui')
                                            lIconGeom = bookModel.find('**/COG_building')
                                            bookModel.removeNode()
                            if lIconGeom and track != Quests.Any:
                                self.loadElevator(lIconGeom, numFloors)
                                self.fitGeometry(lIconGeom, fFlip=1)
                                lIconGeomScale = IMAGE_SCALE_SMALL
                            else:
                                lIconGeomScale = 0.13
                            if not fComplete:
                                infoText = quest.getLocationName()
                                if infoText == '':
                                    infoText = Localizer.QuestPosterAnywhere
                        else:
                            if quest.getType() == Quests.BuildingNewbieQuest:
                                frameBgColor = 'blue'
                                track = quest.getBuildingTrack()
                                numFloors = quest.getNumFloors()
                                if track == 'c':
                                    rIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_corp')
                                else:
                                    if track == 'l':
                                        rIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_legal')
                                    else:
                                        if track == 'm':
                                            rIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_money')
                                        else:
                                            if track == 's':
                                                rIconGeom = loader.loadModelCopy('phase_5/models/modules/suit_landmark_sales')
                                            else:
                                                bookModel = loader.loadModelCopy('phase_3.5/models/gui/stickerbook_gui')
                                                rIconGeom = bookModel.find('**/COG_building')
                                                bookModel.removeNode()
                                if rIconGeom and track != Quests.Any:
                                    self.loadElevator(rIconGeom, numFloors)
                                    self.fitGeometry(rIconGeom, fFlip=1)
                                    rIconGeomScale = IMAGE_SCALE_SMALL
                                else:
                                    rIconGeomScale = 0.13
                                if not fComplete:
                                    headlineString = Localizer.QuestsNewbieQuestHeadline
                                    captions = [Localizer.QuestsCogNewbieQuestCaption % quest.getNewbieLevel()]
                                    captions.append(map(string.capwords, quest.getObjectiveStrings()))
                                    auxText = Localizer.QuestsCogNewbieQuestAux
                                    lPos.setX(-0.18)
                                    self.laffMeter = self.createLaffMeter(quest.getNewbieLevel())
                                    self.laffMeter.setScale(0.04)
                                    lIconGeom = None
                                    infoText = quest.getLocationName()
                                    if infoText == '':
                                        infoText = Localizer.QuestPosterAnywhere
                                else:
                                    lIconGeom = rIconGeom
                                    lIconGeomScale = rIconGeomScale
                            else:
                                if quest.getType() == Quests.FriendQuest:
                                    frameBgColor = 'brown'
                                    gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
                                    lIconGeom = gui.find('**/FriendsBox_Closed')
                                    lIconGeomScale = 0.45
                                    gui.removeNode()
                                    infoText = Localizer.QuestPosterAnywhere
                                else:
                                    if quest.getType() == Quests.FriendNewbieQuest:
                                        frameBgColor = 'brown'
                                        gui = loader.loadModelOnce('phase_3.5/models/gui/friendslist_gui')
                                        lIconGeom = gui.find('**/FriendsBox_Closed')
                                        lIconGeomScale = 0.45
                                        gui.removeNode()
                                        infoText = Localizer.QuestPosterAnywhere
                                    else:
                                        if quest.getType() == Quests.TrolleyQuest:
                                            frameBgColor = 'lightBlue'
                                            gui = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
                                            lIconGeom = gui.find('**/trolley')
                                            lIconGeomScale = 0.13
                                            gui.removeNode()
                                            infoText = Localizer.QuestPosterPlayground
                                        else:
                                            if quest.getType() == Quests.MinigameNewbieQuest:
                                                frameBgColor = 'lightBlue'
                                                gui = loader.loadModelOnce('phase_3.5/models/gui/stickerbook_gui')
                                                rIconGeom = gui.find('**/trolley')
                                                rIconGeomScale = 0.13
                                                gui.removeNode()
                                                infoText = Localizer.QuestPosterPlayground
                                                if not fComplete:
                                                    captions = [
                                                     Localizer.QuestsMinigameNewbieQuestCaption % quest.getNewbieLevel()]
                                                    captions.append(map(string.capwords, quest.getObjectiveStrings()))
                                                    auxText = Localizer.QuestsMinigameNewbieQuestAux
                                                    lPos.setX(-0.18)
                                                    self.laffMeter = self.createLaffMeter(quest.getNewbieLevel())
                                                    self.laffMeter.setScale(0.04)
                                                    lIconGeom = None
                                                else:
                                                    lIconGeom = rIconGeom
                                                    lIconGeomScale = rIconGeomScale
                                            else:
                                                frameBgColor = 'blue'
                                                if quest.getType() == Quests.CogTrackQuest:
                                                    dept = quest.getCogTrack()
                                                    cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                                                    lIconGeomScale = 0.13
                                                    if dept == 'c':
                                                        icon = cogIcons.find('**/CorpIcon')
                                                    else:
                                                        if dept == 's':
                                                            icon = cogIcons.find('**/SalesIcon')
                                                        else:
                                                            if dept == 'l':
                                                                icon = cogIcons.find('**/LegalIcon')
                                                            else:
                                                                if dept == 'm':
                                                                    icon = cogIcons.find('**/MoneyIcon')
                                                    lIconGeom = icon.copyTo(hidden)
                                                    lIconGeom.setColor(Suit.Suit.medallionColors[dept])
                                                    cogIcons.removeNode()
                                                else:
                                                    if quest.getType() == Quests.CogQuest:
                                                        if quest.getCogType() != Quests.Any:
                                                            lIconGeom = self.createSuitHead(quest.getCogType())
                                                            lIconGeomScale = IMAGE_SCALE_SMALL
                                                        else:
                                                            cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                                                            lIconGeom = cogIcons.find('**/cog')
                                                            lIconGeomScale = IMAGE_SCALE_SMALL
                                                            cogIcons.removeNode()
                                                    else:
                                                        if quest.getType() == Quests.CogLevelQuest:
                                                            cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                                                            lIconGeom = cogIcons.find('**/cog')
                                                            lIconGeomScale = IMAGE_SCALE_SMALL
                                                            cogIcons.removeNode()
                                                        else:
                                                            if quest.getType() == Quests.CogNewbieQuest:
                                                                if quest.getCogType() != Quests.Any:
                                                                    rIconGeom = self.createSuitHead(quest.getCogType())
                                                                    rIconGeomScale = IMAGE_SCALE_SMALL
                                                                else:
                                                                    cogIcons = loader.loadModelOnce('phase_3/models/gui/cog_icons')
                                                                    rIconGeom = cogIcons.find('**/cog')
                                                                    rIconGeomScale = IMAGE_SCALE_SMALL
                                                                    cogIcons.removeNode()
                                                                if not fComplete:
                                                                    headlineString = Localizer.QuestsNewbieQuestHeadline
                                                                    captions = [Localizer.QuestsCogNewbieQuestCaption % quest.getNewbieLevel()]
                                                                    captions.append(map(string.capwords, quest.getObjectiveStrings()))
                                                                    auxText = Localizer.QuestsCogNewbieQuestAux
                                                                    lPos.setX(-0.18)
                                                                    self.laffMeter = self.createLaffMeter(quest.getNewbieLevel())
                                                                    self.laffMeter.setScale(0.04)
                                                                    lIconGeom = None
                                                                else:
                                                                    lIconGeom = rIconGeom
                                                                    lIconGeomScale = rIconGeomScale
                                                if not fComplete:
                                                    infoText = string.capwords(quest.getLocationName())
                                                    if infoText == '':
                                                        infoText = Localizer.QuestPosterAnywhere
        if fComplete:
            textColor = (0, 0.3, 0, 1)
            imageColor = Vec4(*self.colors['lightGreen'])
            lPos.setX(-0.18)
            rIconGeom = self.createNpcToonHead(toNpcId)
            rIconGeomScale = IMAGE_SCALE_SMALL
            captions = captions[:1]
            captions.append(toNpcName)
            auxText = Localizer.QuestPosterAuxReturnTo
            headlineString = 'COMPLETE'
            infoText = Localizer.QuestPageDestination % (toNpcBuildingName, toNpcStreetName, toNpcLocationName)
            if self.laffMeter != None:
                self.laffMeter.reparentTo(hidden)
                self.laffMeter.destroy()
                self.laffMeter = None
        else:
            textColor = self.normalTextColor
        self.show()
        self['image_color'] = imageColor
        self.headline['text_fg'] = textColor
        self.headline['text'] = headlineString
        self.lPictureFrame.show()
        self.lPictureFrame.setPos(lPos)
        self.lPictureFrame['text'] = captions[0]
        self.lPictureFrame['image_color'] = Vec4(*self.colors[frameBgColor])
        if len(captions) > 1:
            self.rPictureFrame.show()
            self.rPictureFrame['text'] = captions[1]
            self.rPictureFrame['image_color'] = Vec4(*self.colors[frameBgColor])
        else:
            self.rPictureFrame.hide()
        self.lQuestIcon['geom'] = lIconGeom
        self.lQuestIcon['geom_pos'] = (0, 10, 0)
        if lIconGeom:
            self.lQuestIcon['geom_scale'] = lIconGeomScale
        if self.laffMeter != None:
            self.laffMeter.reparentTo(self.lQuestIcon)
        self.rQuestIcon['geom'] = rIconGeom
        self.rQuestIcon['geom_pos'] = (0, 10, 0)
        if rIconGeom:
            self.rQuestIcon['geom_scale'] = rIconGeomScale
        self.questInfo['text'] = infoText
        self.questInfo.setZ(infoZ)
        self.fitLabel(self.questInfo)
        if auxText:
            self.auxText.show()
            self.auxText['text'] = auxText
            self.auxText.setPos(auxTextPos)
        else:
            self.auxText.hide()
        self.bind(WITHIN, self.mouseEnterPoster)
        self.bind(WITHOUT, self.mouseExitPoster)
        numQuestItems = quest.getNumQuestItems()
        if fComplete or numQuestItems <= 1:
            self.questProgress.hide()
        else:
            self.questProgress.show()
            self.questProgress['value'] = toonProgress
            self.questProgress['range'] = numQuestItems
            self.questProgress['text'] = quest.getProgressString(toonbase.localToon, questDesc)
        return

    def fitLabel(self, label, lineNo=0):
        text = label['text']
        label['text_scale'] = TEXT_SCALE
        label['text_wordwrap'] = TEXT_WORDWRAP
        if len(text) > 0:
            lines = text.split('\n')
            lineWidth = ToontownGlobals.getInterfaceFont().calcWidth(lines[lineNo])
            if lineWidth > 0:
                textScale = POSTER_WIDTH / lineWidth
                label['text_scale'] = min(TEXT_SCALE, textScale)
                label['text_wordwrap'] = max(TEXT_WORDWRAP, lineWidth + 0.05)