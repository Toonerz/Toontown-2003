from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from SuitBase import *
from AvatarDNA import *
from BattleSounds import *
import MovieCamera, DirectNotifyGlobal, MovieUtil, ToontownBattleGlobals, BattleParticles, BattleProps
notify = DirectNotifyGlobal.directNotify.newCategory('MovieLures')

def doLures(lures):
    if len(lures) == 0:
        return (None, None)
    ivals = []
    for l in lures:
        ival = __doLureLevel(l)
        if ival:
            ivals.append(Track([ival]))

    mtrack = MultiTrack(ivals)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseLureShot(lures, camDuration)
    return (
     mtrack, camTrack)
    return


def __doLureLevel(lure):
    level = lure['level']
    if level == 0:
        return __lureOneDollar(lure)
    else:
        if level == 1:
            return __lureSmallMagnet(lure)
        else:
            if level == 2:
                return __lureFiveDollar(lure)
            else:
                if level == 3:
                    return __lureLargeMagnet(lure)
                else:
                    if level == 4:
                        return __lureTenDollar(lure)
                    else:
                        if level == 5:
                            return __lureHypnotize(lure)
    return None
    return


def getSoundTrack(fileName, delay=0.01, duration=None, node=None):
    soundEffect = globalBattleSoundCache.getSound(fileName)
    if duration:
        return Track([(delay, SoundInterval(soundEffect, duration=duration, node=node))])
    else:
        return Track([(delay, SoundInterval(soundEffect, node=node))])


def __createFishingPoleMultiTrack(lure, dollar, dollarName):
    toon = lure['toon']
    target = lure['target']
    battle = lure['battle']
    sidestep = lure['sidestep']
    hp = target['hp']
    kbbonus = target['kbbonus']
    suit = target['suit']
    targetPos = suit.getPos(battle)
    died = target['died']
    reachAnimDuration = 3.5
    trapProp = suit.battleTrapProp
    pole = globalPropPool.getProp('fishing-pole')
    pole2 = MovieUtil.copyProp(pole)
    poles = [pole, pole2]
    hands = toon.getRightHands()

    def positionDollar(dollar, suit):
        dollar.reparentTo(suit)
        dollar.setPos(0, MovieUtil.SUIT_LURE_DOLLAR_DISTANCE, 0)

    dollarIvals = []
    dollarIvals.append(FunctionInterval(positionDollar, extraArgs=[dollar, suit]))
    dollarAnims = []
    dollarAnims.append(FunctionInterval(dollar.wrtReparentTo, extraArgs=[battle]))
    dollarAnims.append(ActorInterval(dollar, dollarName, duration=3))
    dollarAnims.extend(getSplicedLerpAnims(dollar, dollarName, 0.7, 2.0, startTime=3))
    dollarAnims.append(LerpPosInterval(dollar, 0.2, Point3(0, -10, 7)))
    dollarIvals.extend(dollarAnims)
    dollarIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs=[dollar]))
    dollarTrack = Track(dollarIvals)
    poleIvals = []
    poleIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs=[poles, hands]))
    poleIvals.append(ActorInterval(pole, 'fishing-pole'))
    poleIvals.append(FunctionInterval(MovieUtil.removeProps, extraArgs=[poles]))
    poleTrack = Track(poleIvals)
    toonTrack = Track([FunctionInterval(toon.headsUp, extraArgs=[battle, targetPos]), ActorInterval(toon, 'cast'), FunctionInterval(toon.loop, extraArgs=['neutral'])])
    tracks = [
     dollarTrack, poleTrack, toonTrack]
    if sidestep == 0:
        if kbbonus == 1 or hp > 0:
            suitIvals = []
            opos, ohpr = battle.getActorPosHpr(suit)
            reachDist = MovieUtil.SUIT_LURE_DISTANCE
            reachPos = Point3(opos[0], opos[1] - reachDist, opos[2])
            suitIvals.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
            suitIvals.append(WaitInterval(3.5))
            suitName = suit.getStyleName()
            retardPos, retardHpr = battle.getActorPosHpr(suit)
            retardPos.setY(retardPos.getY() + MovieUtil.SUIT_EXTRA_REACH_DISTANCE)
            if suitName in MovieUtil.largeSuits:
                moveTrack = lerpSuit(suit, 0.0, reachAnimDuration / 2.5, retardPos, battle, trapProp)
                reachTrack = Track([ActorInterval(suit, 'reach', duration=reachAnimDuration)])
                suitIvals.append(MultiTrack([moveTrack, reachTrack]))
            else:
                suitIvals.append(ActorInterval(suit, 'reach', duration=reachAnimDuration))
            if trapProp:
                suitIvals.append(FunctionInterval(trapProp.wrtReparentTo, extraArgs=[battle]))
            suitIvals.append(FunctionInterval(suit.setPos, extraArgs=[battle, reachPos]))
            if trapProp:
                suitIvals.append(FunctionInterval(trapProp.wrtReparentTo, extraArgs=[suit]))
                suit.battleTrapProp = trapProp
            suitIvals.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
            suitIvals.append(FunctionInterval(battle.lureSuit, extraArgs=[suit]))
            if hp > 0:
                suitIvals.append(__createSuitDamageTrack(battle, suit, hp, lure, trapProp))
            if died != 0:
                suitIvals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
            tracks.append(Track(suitIvals))
    else:
        tracks.append(Track([(3.7, FunctionInterval(MovieUtil.indicateMissed, extraArgs=[suit]))]))
    tracks.append(getSoundTrack('TL_fishing_pole.mp3', delay=0.5, node=toon))
    return MultiTrack(tracks)


def __createMagnetMultiTrack(lure, magnet, pos, hpr, scale, isSmallMagnet=1):
    toon = lure['toon']
    battle = lure['battle']
    sidestep = lure['sidestep']
    targets = lure['target']
    tracks = []
    tracks.append(Track([ActorInterval(toon, 'hold-magnet'), FunctionInterval(toon.loop, extraArgs=['neutral'])]))
    hands = toon.getLeftHands()
    magnet2 = MovieUtil.copyProp(magnet)
    magnets = [magnet, magnet2]
    magnetIvals = []
    magnetIvals.append(WaitInterval(0.7))
    magnetIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs=[magnets, hands, pos, hpr, scale]))
    magnetIvals.append(WaitInterval(6.3))
    magnetIvals.append(FunctionInterval(MovieUtil.removeProps, extraArgs=[magnets]))
    tracks.append(Track(magnetIvals))
    for target in targets:
        suit = target['suit']
        trapProp = suit.battleTrapProp
        if sidestep == 0:
            hp = target['hp']
            kbbonus = target['kbbonus']
            died = target['died']
            if kbbonus == 1 or hp > 0:
                suitDelay = 2.6
                suitMoveDuration = 0.8
                suitIvals = []
                opos, ohpr = battle.getActorPosHpr(suit)
                reachDist = MovieUtil.SUIT_LURE_DISTANCE
                reachPos = Point3(opos[0], opos[1] - reachDist, opos[2])
                numShakes = 3.0
                shakeTotalDuration = 0.8
                shakeDuration = shakeTotalDuration / numShakes
                suitAnims = []
                suitAnims.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
                suitAnims.append(WaitInterval(suitDelay))
                suitAnims.append(ActorInterval(suit, 'landing', startTime=2.37, endTime=1.82))
                for i in range(0, numShakes):
                    suitAnims.append(ActorInterval(suit, 'landing', startTime=1.82, endTime=1.16, duration=shakeDuration))

                suitAnims.append(ActorInterval(suit, 'landing', startTime=1.16, endTime=0.7))
                suitAnims.append(ActorInterval(suit, 'landing', startTime=0.7, duration=1.3))
                suitIvals.extend(suitAnims)
                suitIvals.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
                suitIvals.append(FunctionInterval(battle.lureSuit, extraArgs=[suit]))
                if hp > 0:
                    suitIvals.append(__createSuitDamageTrack(battle, suit, hp, lure, trapProp))
                if died != 0:
                    suitIvals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
                tracks.append(Track(suitIvals))
                tracks.append(lerpSuit(suit, suitDelay + 0.55 + shakeTotalDuration, suitMoveDuration, reachPos, battle, trapProp))
        else:
            tracks.append(Track([(3.7, FunctionInterval(MovieUtil.indicateMissed, extraArgs=[suit]))]))

    if isSmallMagnet == 1:
        tracks.append(getSoundTrack('TL_small_magnet.mp3', delay=0.7, node=toon))
    else:
        tracks.append(getSoundTrack('TL_large_magnet.mp3', delay=0.7, node=toon))
    return MultiTrack(tracks)


def __createHypnoGogglesMultiTrack(lure):
    toon = lure['toon']
    targets = lure['target']
    battle = lure['battle']
    sidestep = lure['sidestep']
    goggles = globalPropPool.getProp('hypno-goggles')
    goggles2 = MovieUtil.copyProp(goggles)
    bothGoggles = [goggles, goggles2]
    pos = Point3(-1.03, 1.04, -0.3)
    hpr = Point3(97.65, 46.18, -97.25)
    scale = Point3(1.5, 1.5, 1.5)
    hands = toon.getLeftHands()
    gogglesIvals = []
    gogglesIvals.append(WaitInterval(0.6))
    gogglesIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs=[bothGoggles, hands, pos, hpr, scale]))
    gogglesIvals.append(ActorInterval(goggles, 'hypno-goggles', duration=2.2))
    gogglesIvals.append(FunctionInterval(MovieUtil.removeProps, extraArgs=[bothGoggles]))
    gogglesTrack = Track(gogglesIvals)
    toonTrack = Track([ActorInterval(toon, 'hypnotize'), FunctionInterval(toon.loop, extraArgs=['neutral'])])
    tracks = [
     gogglesTrack, toonTrack]
    for target in targets:
        suit = target['suit']
        trapProp = suit.battleTrapProp
        if sidestep == 0:
            hp = target['hp']
            kbbonus = target['kbbonus']
            died = target['died']
            if kbbonus == 1 or hp > 0:
                suitIvals = []
                suitDelay = 1.6
                suitAnimDuration = 1.5
                opos, ohpr = battle.getActorPosHpr(suit)
                reachDist = MovieUtil.SUIT_LURE_DISTANCE
                reachPos = Point3(opos[0], opos[1] - reachDist, opos[2])
                suitIvals.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
                suitIvals.append(WaitInterval(suitDelay))
                suitIvals.append(ActorInterval(suit, 'hypnotized', duration=3.1))
                suitIvals.append(FunctionInterval(suit.setPos, extraArgs=[battle, reachPos]))
                suitIvals.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
                suitIvals.append(FunctionInterval(battle.lureSuit, extraArgs=[suit]))
                if hp > 0:
                    suitIvals.append(__createSuitDamageTrack(battle, suit, hp, lure, trapProp))
                if died != 0:
                    suitIvals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
                tracks.append(Track(suitIvals))
                tracks.append(lerpSuit(suit, suitDelay + 1.7, 0.7, reachPos, battle, trapProp))
        else:
            tracks.append(Track([(2.3, FunctionInterval(MovieUtil.indicateMissed, extraArgs=[suit, 1.1]))]))

    tracks.append(getSoundTrack('TL_hypnotize.mp3', delay=0.5, node=toon))
    return MultiTrack(tracks)


def __lureOneDollar(lure):
    dollarProp = '1dollar'
    dollar = globalPropPool.getProp(dollarProp)
    return __createFishingPoleMultiTrack(lure, dollar, dollarProp)


def __lureSmallMagnet(lure):
    magnet = globalPropPool.getProp('small-magnet')
    pos = Point3(-0.27, 0.19, 0.29)
    hpr = Point3(90.0, -80.31, -176.14)
    scale = Point3(0.85, 0.85, 0.85)
    return __createMagnetMultiTrack(lure, magnet, pos, hpr, scale, isSmallMagnet=1)


def __lureFiveDollar(lure):
    dollarProp = '5dollar'
    dollar = globalPropPool.getProp(dollarProp)
    return __createFishingPoleMultiTrack(lure, dollar, dollarProp)


def __lureLargeMagnet(lure):
    magnet = globalPropPool.getProp('big-magnet')
    pos = Point3(-0.27, 0.08, 0.29)
    hpr = Point3(90.0, -75.51, -171.34)
    scale = Point3(1.32, 1.32, 1.32)
    return __createMagnetMultiTrack(lure, magnet, pos, hpr, scale, isSmallMagnet=0)


def __lureTenDollar(lure):
    dollarProp = '10dollar'
    dollar = globalPropPool.getProp(dollarProp)
    return __createFishingPoleMultiTrack(lure, dollar, dollarProp)


def __lureHypnotize(lure):
    return __createHypnoGogglesMultiTrack(lure)


def __createSuitDamageTrack(battle, suit, hp, lure, trapProp):
    if trapProp == None or trapProp.isEmpty():
        return Track([FunctionInterval(suit.loop, extraArgs=['neutral'])])
    trapProp.wrtReparentTo(battle)
    trapTrack = ToontownBattleGlobals.TRAP_TRACK
    trapLevel = suit.battleTrap
    trapTrackNames = ToontownBattleGlobals.AvProps[trapTrack]
    trapName = trapTrackNames[trapLevel]
    ivals = []

    def reparentTrap(trapProp=trapProp, battle=battle):
        trapProp.wrtReparentTo(battle)

    ivals.append(FunctionInterval(reparentTrap))
    parent = battle
    if suit.battleTrapIsFresh == 1:
        if trapName == 'quicksand' or trapName == 'trapdoor':
            trapProp.hide()
            trapProp.reparentTo(suit)
            trapProp.setPos(Point3(0, MovieUtil.SUIT_TRAP_DISTANCE, 0))
            trapProp.setHpr(Point3(0, 0, 0))
            trapProp.wrtReparentTo(battle)
        else:
            if trapName == 'rake':
                trapProp.hide()
                trapProp.reparentTo(suit)
                trapProp.setPos(0, MovieUtil.SUIT_TRAP_RAKE_DISTANCE, 0)
                trapProp.setHpr(Point3(0, 270, 0))
                trapProp.setScale(Point3(0.7, 0.7, 0.7))
                rakeOffset = MovieUtil.getSuitRakeOffset(suit)
                trapProp.setY(trapProp.getY() + rakeOffset)
            else:
                parent = render
    if trapName == 'banana':
        slidePos = trapProp.getPos(parent)
        slidePos.setY(slidePos.getY() - 5.1)
        moveTrack = Track([WaitInterval(0.1), LerpPosInterval(trapProp, 0.1, slidePos, other=battle)])
        animTrack = Track([ActorInterval(trapProp, 'banana', startTime=3.1), WaitInterval(1.1), LerpScaleInterval(trapProp, 1, Point3(0.01, 0.01, 0.01))])
        suitTrack = Track([ActorInterval(suit, 'slip-backward')])
        damageTrack = Track([WaitInterval(0.5), FunctionInterval(suit.showLaffNumber, openEnded=0, extraArgs=[-hp]), FunctionInterval(suit.updateHealthBar, extraArgs=[hp])])
        soundTrack = Track([SoundInterval(globalBattleSoundCache.getSound('AA_pie_throw_only.mp3'), duration=0.55, node=suit), SoundInterval(globalBattleSoundCache.getSound('Toon_bodyfall_synergy.mp3'), node=suit)])
        ivals.append(MultiTrack([moveTrack, animTrack, suitTrack, damageTrack, soundTrack]))
    else:
        if trapName == 'rake' or trapName == 'rake-react':
            hpr = trapProp.getHpr(parent)
            upHpr = Vec3(hpr[0], 179.9999, hpr[2])
            bounce1Hpr = Vec3(hpr[0], 120, hpr[2])
            bounce2Hpr = Vec3(hpr[0], 100, hpr[2])
            rakeTrack = Track([WaitInterval(0.5), LerpHprInterval(trapProp, 0.1, upHpr, startHpr=hpr), WaitInterval(0.7), LerpHprInterval(trapProp, 0.4, hpr, startHpr=upHpr), LerpHprInterval(trapProp, 0.15, bounce1Hpr, startHpr=hpr), LerpHprInterval(trapProp, 0.05, hpr, startHpr=bounce1Hpr), LerpHprInterval(trapProp, 0.15, bounce2Hpr, startHpr=hpr), LerpHprInterval(trapProp, 0.05, hpr, startHpr=bounce2Hpr), WaitInterval(0.2), LerpScaleInterval(trapProp, 0.2, Point3(0.01, 0.01, 0.01))])
            rakeAnimDuration = 3.125
            suitTrack = Track([ActorInterval(suit, 'rake-react', duration=rakeAnimDuration)])
            damageTrack = Track([WaitInterval(0.5), FunctionInterval(suit.showLaffNumber, openEnded=0, extraArgs=[-hp]), FunctionInterval(suit.updateHealthBar, extraArgs=[hp])])
            soundTrack = getSoundTrack('TL_step_on_rake.mp3', delay=0.6, node=suit)
            ivals.append(MultiTrack([rakeTrack, suitTrack, damageTrack, soundTrack]))
        else:
            if trapName == 'marbles':
                slidePos = trapProp.getPos(parent)
                slidePos.setY(slidePos.getY() - 6.5)
                moveTrack = Track([WaitInterval(0.1), LerpPosInterval(trapProp, 0.8, slidePos, other=battle), WaitInterval(1.1), LerpScaleInterval(trapProp, 1, Point3(0.01, 0.01, 0.01))])
                animTrack = Track([ActorInterval(trapProp, 'marbles', startTime=3.1)])
                suitTrack = Track([ActorInterval(suit, 'slip-backward')])
                damageTrack = Track([WaitInterval(0.5), FunctionInterval(suit.showLaffNumber, openEnded=0, extraArgs=[-hp]), FunctionInterval(suit.updateHealthBar, extraArgs=[hp])])
                soundTrack = Track([SoundInterval(globalBattleSoundCache.getSound('AA_pie_throw_only.mp3'), duration=0.55, node=suit), SoundInterval(globalBattleSoundCache.getSound('Toon_bodyfall_synergy.mp3'), node=suit)])
                ivals.append(MultiTrack([moveTrack, animTrack, suitTrack, damageTrack, soundTrack]))
            else:
                if trapName == 'quicksand':
                    sinkPos1 = trapProp.getPos(battle)
                    sinkPos2 = trapProp.getPos(battle)
                    dropPos = trapProp.getPos(battle)
                    landPos = trapProp.getPos(battle)
                    sinkPos1.setZ(sinkPos1.getZ() - 3.1)
                    sinkPos2.setZ(sinkPos2.getZ() - 9.1)
                    dropPos.setZ(dropPos.getZ() + 15)
                    nameTag = suit.find('**/joint-nameTag')
                    trapTrack = Track([WaitInterval(2.4), LerpScaleInterval(trapProp, 0.8, Point3(0.01, 0.01, 0.01))])
                    moveTrack = Track([WaitInterval(0.9), LerpPosInterval(suit, 0.9, sinkPos1, other=battle), LerpPosInterval(suit, 0.4, sinkPos2, other=battle), FunctionInterval(suit.setPos, extraArgs=[battle, dropPos]), FunctionInterval(suit.wrtReparentTo, extraArgs=[hidden]), WaitInterval(1.1), FunctionInterval(suit.wrtReparentTo, extraArgs=[battle]), LerpPosInterval(suit, 0.3, landPos, other=battle)])
                    animTrack = Track([ActorInterval(suit, 'flail'), ActorInterval(suit, 'flail', startTime=1.1), WaitInterval(0.7), ActorInterval(suit, 'slip-forward', duration=2.1)])
                    damageTrack = Track([WaitInterval(3.5), FunctionInterval(suit.showLaffNumber, openEnded=0, extraArgs=[-hp]), FunctionInterval(suit.updateHealthBar, extraArgs=[hp])])
                    soundTrack = Track([WaitInterval(0.7), SoundInterval(globalBattleSoundCache.getSound('TL_quicksand.mp3'), node=suit), WaitInterval(0.1), SoundInterval(globalBattleSoundCache.getSound('Toon_bodyfall_synergy.mp3'), node=suit)])
                    ivals.append(MultiTrack([trapTrack, moveTrack, animTrack, damageTrack, soundTrack]))
                else:
                    if trapName == 'trapdoor':
                        sinkPos = trapProp.getPos(battle)
                        dropPos = trapProp.getPos(battle)
                        landPos = trapProp.getPos(battle)
                        sinkPos.setZ(sinkPos.getZ() - 9.1)
                        dropPos.setZ(dropPos.getZ() + 15)
                        trapTrack = Track([WaitInterval(2.4), LerpScaleInterval(trapProp, 0.8, Point3(0.01, 0.01, 0.01))])
                        moveTrack = Track([WaitInterval(2.2), LerpPosInterval(suit, 0.4, sinkPos, other=battle), FunctionInterval(suit.setPos, extraArgs=[battle, dropPos]), FunctionInterval(suit.wrtReparentTo, extraArgs=[hidden]), WaitInterval(1.6), FunctionInterval(suit.wrtReparentTo, extraArgs=[battle]), LerpPosInterval(suit, 0.3, landPos, other=battle)])
                        animIvals = []
                        animIvals.extend(getSplicedLerpAnims(suit, 'flail', 0.7, 0.25))
                        animIvals.append(FunctionInterval(trapProp.setColor, extraArgs=[Vec4(0, 0, 0, 1)]))
                        animIvals.append(ActorInterval(suit, 'flail', startTime=0.7, endTime=0))
                        animIvals.append(ActorInterval(suit, 'neutral', duration=0.5))
                        animIvals.append(ActorInterval(suit, 'flail', startTime=1.1))
                        animIvals.append(WaitInterval(1.1))
                        animIvals.append(ActorInterval(suit, 'slip-forward', duration=2.1))
                        animTrack = Track(animIvals)
                        damageTrack = Track([WaitInterval(3.5), FunctionInterval(suit.showLaffNumber, openEnded=0, extraArgs=[-hp]), FunctionInterval(suit.updateHealthBar, extraArgs=[hp])])
                        soundTrack = Track([WaitInterval(0.8), SoundInterval(globalBattleSoundCache.getSound('TL_trap_door.mp3'), node=suit), WaitInterval(0.8), SoundInterval(globalBattleSoundCache.getSound('Toon_bodyfall_synergy.mp3'), node=suit)])
                        ivals.append(MultiTrack([trapTrack, moveTrack, animTrack, damageTrack, soundTrack]))
                    else:
                        if trapName == 'tnt':
                            tntTrack = Track([ActorInterval(trapProp, 'tnt')])
                            explosionIvals = []
                            explosionIvals.append(WaitInterval(2.3))
                            explosionIvals.extend(createTNTExplosionIvals(battle, trapProp=trapProp, relativeTo=parent))
                            explosionTrack = Track(explosionIvals)
                            suitTrack = Track([ActorInterval(suit, 'flail', duration=0.7), ActorInterval(suit, 'flail', startTime=0.7, endTime=0.0), ActorInterval(suit, 'neutral', duration=0.4), ActorInterval(suit, 'flail', startTime=0.6, endTime=0.7), WaitInterval(0.4), ActorInterval(suit, 'slip-forward', startTime=2.48, duration=0.1), FunctionInterval(battle.movie.needRestoreColor), FunctionInterval(suit.setColorScale, extraArgs=[Vec4(0, 0, 0, 1)]), FunctionInterval(trapProp.reparentTo, extraArgs=[hidden]), ActorInterval(suit, 'slip-forward', startTime=2.58), FunctionInterval(suit.clearColorScale), FunctionInterval(trapProp.sparksEffect.cleanup), FunctionInterval(battle.movie.clearRestoreColor)])
                            damageTrack = Track([WaitInterval(2.3), FunctionInterval(suit.showLaffNumber, openEnded=0, extraArgs=[-hp]), FunctionInterval(suit.updateHealthBar, extraArgs=[hp])])
                            explosionSound = base.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
                            soundTrack = Track([SoundInterval(globalBattleSoundCache.getSound('TL_dynamite.mp3'), duration=2.0, node=suit), SoundInterval(explosionSound, duration=0.6, node=suit)])
                            ivals.append(MultiTrack([tntTrack, suitTrack, damageTrack, explosionTrack, soundTrack]))
                        else:
                            notify.warning('unknown trapName: %s detected on suit: %s' % trapName, suit)
    suit.battleTrapProp = trapProp
    ivals.append(FunctionInterval(battle.removeTrap, extraArgs=[suit]))
    ivals.append(FunctionInterval(battle.unlureSuit, extraArgs=[suit]))
    ivals.append(__createSuitResetPosTrack(suit, battle))
    ivals.append(FunctionInterval(suit.loop, extraArgs=['neutral']))
    return Track(ivals)
    return


def __createSuitResetPosTrack(suit, battle):
    resetPos, resetHpr = battle.getActorPosHpr(suit)
    moveDist = Vec3(suit.getPos(battle) - resetPos).length()
    moveDuration = 0.5
    walkTrack = Track([FunctionInterval(suit.setHpr, extraArgs=[battle, resetHpr]), ActorInterval(suit, 'walk', startTime=1, duration=moveDuration, endTime=0.0001), FunctionInterval(suit.loop, extraArgs=['neutral'])])
    moveTrack = Track([LerpPosInterval(suit, moveDuration, resetPos, other=battle)])
    return MultiTrack([walkTrack, moveTrack])


def getSplicedLerpAnims(object, animName, origDuration, newDuration, startTime=0, fps=30):
    ivals = []
    addition = 0
    numIvals = origDuration * fps
    timeInterval = newDuration / numIvals
    animInterval = origDuration / numIvals
    for i in range(0, numIvals):
        ivals.append(WaitInterval(timeInterval))
        ivals.append(ActorInterval(object, animName, startTime=startTime + addition, duration=animInterval))
        addition += animInterval

    return ivals


def lerpSuit(suit, delay, duration, reachPos, battle, trapProp):
    ivals = []
    if trapProp:
        ivals.append(FunctionInterval(trapProp.wrtReparentTo, extraArgs=[battle]))
    ivals.append(WaitInterval(delay))
    ivals.append(LerpPosInterval(suit, duration, reachPos, other=battle))
    if trapProp:
        ivals.append(FunctionInterval(trapProp.wrtReparentTo, extraArgs=[suit]))
        suit.battleTrapProp = trapProp
    return Track(ivals)


def createTNTExplosionIvals(parent, explosionPoint=None, trapProp=None, relativeTo=render):
    explosionIvals = []
    explosion = BattleProps.globalPropPool.getProp('kapow')
    explosion.setBillboardPointEye()
    if not explosionPoint:
        if trapProp:
            explosionPoint = trapProp.getPos(relativeTo)
            explosionPoint.setZ(explosionPoint.getZ() + 2.3)
        else:
            explosionPoint = Point3(0, 3.6, 2.1)
    explosionIvals.append(FunctionInterval(explosion.reparentTo, extraArgs=[parent]))
    explosionIvals.append(FunctionInterval(explosion.setPos, extraArgs=[explosionPoint]))
    explosionIvals.append(FunctionInterval(explosion.setScale, extraArgs=[0.11]))
    explosionIvals.append(ActorInterval(explosion, 'kapow'))
    explosionIvals.append(FunctionInterval(MovieUtil.removeProp, extraArgs=[explosion]))
    return explosionIvals