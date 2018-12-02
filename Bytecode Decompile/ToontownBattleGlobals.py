from ToontownGlobals import *
import math, Localizer
BattleCamFaceOffFov = 30.0
BattleCamFaceOffPos = Point3(0, -10, 4)
BattleCamDefaultPos = Point3(0, -8.6, 16.5)
BattleCamDefaultHpr = Vec3(0, -61, 0)
BattleCamDefaultFov = 80.0
BattleCamMenuFov = 65.0
BattleCamJoinPos = Point3(0, -12, 13)
BattleCamJoinHpr = Vec3(0, -45, 0)
BaseHp = 15
Tracks = Localizer.BattleGlobalTracks
TrackColors = (
 (
  211 / 255.0, 148 / 255.0, 255 / 255.0), (249 / 255.0, 255 / 255.0, 93 / 255.0), (79 / 255.0, 190 / 255.0, 76 / 255.0), (93 / 255.0, 108 / 255.0, 239 / 255.0), (255 / 255.0, 145 / 255.0, 66 / 255.0), (255 / 255.0, 65 / 255.0, 199 / 255.0), (67 / 255.0, 243 / 255.0, 255 / 255.0))
HEAL_TRACK = 0
TRAP_TRACK = 1
LURE_TRACK = 2
SOUND_TRACK = 3
THROW_TRACK = 4
SQUIRT_TRACK = 5
DROP_TRACK = 6
MIN_TRACK_INDEX = 0
MAX_TRACK_INDEX = 6
MIN_LEVEL_INDEX = 0
MAX_LEVEL_INDEX = 5
Levels = [
 [
  0, 20, 200, 800, 2000, 6000], [0, 20, 100, 800, 2000, 6000], [0, 20, 100, 800, 2000, 6000], [0, 40, 200, 1000, 2500, 7500], [0, 10, 50, 400, 2000, 6000], [0, 10, 50, 400, 2000, 6000], [0, 20, 100, 500, 2000, 6000]]
MaxSkill = 9999
ExperienceCap = 200
MaxToonAcc = 95
StartingLevel = 0
CarryLimits = (
 (
  (
   10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((5, 0, 0, 0, 0, 0), (7, 3, 0, 0, 0, 0), (10, 7, 3, 0, 0, 0), (15, 10, 7, 3, 0, 0), (15, 15, 10, 5, 3, 0), (20, 15, 15, 10, 5, 2)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)))
MaxProps = (
 (
  15, 40), (30, 60), (75, 80))
AvProps = (
 (
  'feather', 'bullhorn', 'lipstick', 'bamboocane', 'pixiedust', 'baton'), ('banana', 'rake', 'marbles', 'quicksand', 'trapdoor', 'tnt'), ('1dollar', 'smmagnet', '5dollar', 'bigmagnet', '10dollar', 'hypnogogs'), ('bikehorn', 'whistle', 'bugle', 'aoogah', 'elephant', 'foghorn'), ('cupcake', 'fruitpieslice', 'creampieslice', 'fruitpie', 'creampie', 'cake'), ('flower', 'waterglass', 'waterballoon', 'bottle', 'firehose', 'stormcloud'), ('flowerpot', 'sandbag', 'anvil', 'weight', 'safe', 'piano'))
AvPropsNew = (
 (
  'inventory_feather', 'inventory_megaphone', 'inventory_lipstick', 'inventory_bamboo_cane', 'inventory_pixiedust', 'inventory_juggling_cubes'), ('inventory_bannana_peel', 'inventory_rake', 'inventory_marbles', 'inventory_quicksand_icon', 'inventory_trapdoor', 'inventory_tnt'), ('inventory_1dollarbill', 'inventory_small_magnet', 'inventory_5dollarbill', 'inventory_big_magnet', 'inventory_10dollarbill', 'inventory_hypno_goggles'), ('inventory_bikehorn', 'inventory_whistle', 'inventory_bugle', 'inventory_aoogah', 'inventory_elephant', 'inventory_fog_horn'), ('inventory_tart', 'inventory_fruit_pie_slice', 'inventory_cream_pie_slice', 'inventory_fruitpie', 'inventory_creampie', 'inventory_cake'), ('inventory_squirt_flower', 'inventory_glass_of_water', 'inventory_water_gun', 'inventory_seltzer_bottle', 'inventory_firehose', 'inventory_storm_cloud'), ('inventory_flower_pot', 'inventory_sandbag', 'inventory_anvil', 'inventory_weight', 'inventory_safe_box', 'inventory_piano'))
AvPropStrings = Localizer.BattleGlobalAvPropStrings
AvPropStringsSingular = Localizer.BattleGlobalAvPropStringsSingular
AvPropStringsPlural = Localizer.BattleGlobalAvPropStringsPlural
AvPropAccuracy = (
 (
  70, 70, 70, 70, 70, 70), (0, 0, 0, 0, 0, 0), (50, 50, 60, 60, 70, 70), (95, 95, 95, 95, 95, 95), (75, 75, 75, 75, 75, 75), (95, 95, 95, 95, 95, 95), (50, 50, 50, 50, 50, 50))
AvTrackAccStrings = Localizer.BattleGlobalAvTrackAccStrings
AvPropDamage = (
 (
  (
   (
    8, 10), (Levels[0][0], Levels[0][1])), ((15, 18), (Levels[0][1], Levels[0][2])), ((25, 30), (Levels[0][2], Levels[0][3])), ((40, 45), (Levels[0][3], Levels[0][4])), ((60, 70), (Levels[0][4], Levels[0][5])), ((90, 120), (Levels[0][5], MaxSkill))), (((10, 12), (Levels[1][0], Levels[1][1])), ((18, 20), (Levels[1][1], Levels[1][2])), ((30, 35), (Levels[1][2], Levels[1][3])), ((45, 50), (Levels[1][3], Levels[1][4])), ((60, 70), (Levels[1][4], Levels[1][5])), ((90, 180), (Levels[1][5], MaxSkill))), (((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0))), (((3, 4), (Levels[3][0], Levels[3][1])), ((5, 7), (Levels[3][1], Levels[3][2])), ((9, 11), (Levels[3][2], Levels[3][3])), ((14, 16), (Levels[3][3], Levels[3][4])), ((19, 21), (Levels[3][4], Levels[3][5])), ((25, 50), (Levels[3][5], MaxSkill))), (((4, 6), (Levels[4][0], Levels[4][1])), ((8, 10), (Levels[4][1], Levels[4][2])), ((14, 17), (Levels[4][2], Levels[4][3])), ((24, 27), (Levels[4][3], Levels[4][4])), ((36, 40), (Levels[4][4], Levels[4][5])), ((48, 100), (Levels[4][5], MaxSkill))), (((3, 4), (Levels[5][0], Levels[5][1])), ((6, 8), (Levels[5][1], Levels[5][2])), ((10, 12), (Levels[5][2], Levels[5][3])), ((18, 21), (Levels[5][3], Levels[5][4])), ((27, 30), (Levels[5][4], Levels[5][5])), ((36, 80), (Levels[5][5], MaxSkill))), (((10, 10), (Levels[6][0], Levels[6][1])), ((18, 18), (Levels[6][1], Levels[6][2])), ((30, 30), (Levels[6][2], Levels[6][3])), ((45, 45), (Levels[6][3], Levels[6][4])), ((60, 60), (Levels[6][4], Levels[6][5])), ((85, 170), (Levels[6][5], MaxSkill))))
ATK_SINGLE_TARGET = 0
ATK_GROUP_TARGET = 1
AvPropTargetCat = ((ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET), (ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET), (ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET))
AvPropTarget = (
 0, 1, 0, 2, 1, 1, 1)

def getAvPropDamage(attackTrack, attackLevel, exp):
    minD = AvPropDamage[attackTrack][attackLevel][0][0]
    maxD = AvPropDamage[attackTrack][attackLevel][0][1]
    minE = AvPropDamage[attackTrack][attackLevel][1][0]
    maxE = AvPropDamage[attackTrack][attackLevel][1][1]
    expVal = min(exp, maxE)
    expPerHp = float(maxE - minE + 1) / float(maxD - minD + 1)
    return math.floor((expVal - minE) / expPerHp) + minD


def isGroup(track, level):
    if track == SOUND_TRACK or (track == HEAL_TRACK or track == LURE_TRACK) and (level == 1 or level == 3 or level == 5):
        return 1
    else:
        return 0


def getCreditMultiplier(floorIndex):
    return 1 + floorIndex * 0.5


def getInvasionMultiplier():
    return 2.0