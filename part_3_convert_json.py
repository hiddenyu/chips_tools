import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

jsonFile = "data/yujunwu_cc1.json"

with open(jsonFile, "r") as reader:
    jsonLevels = json.load(reader)

def defineLevels(file):
    # create a new level pack
    levelPack = cc_classes.CCLevelPack()
    levels = file["levels"]

    # loop through all levels
    for level in levels:
        # initialize new level
        newLevel = cc_classes.CCLevel()

        newLevel.level_number = level["levelNumber"]
        newLevel.time = level["time"]
        newLevel.num_chips = level["chipNumber"]
        newLevel.upper_layer = level["upperLayer"]

        levelTitle = cc_classes.CCMapTitleField(level["mapTitle"])
        levelHint = cc_classes.CCMapHintField(level["hintText"])
        levelPassword = cc_classes.CCEncodedPasswordField(level["encodedPassword"])

        newLevel.add_field(levelTitle)
        newLevel.add_field(levelHint)
        newLevel.add_field(levelPassword)

        levelPack.add_level(newLevel)

    return levelPack

print(defineLevels(jsonLevels))