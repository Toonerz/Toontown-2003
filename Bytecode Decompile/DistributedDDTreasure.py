import DistributedSZTreasure

class DistributedDDTreasure(DistributedSZTreasure.DistributedSZTreasure):
    __module__ = __name__

    def __init__(self, cr):
        DistributedSZTreasure.DistributedSZTreasure.__init__(self, cr)
        self.modelPath = 'phase_6/models/props/starfish_treasure'
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.mp3'