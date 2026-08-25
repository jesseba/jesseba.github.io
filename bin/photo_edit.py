"""The photographic edit: which frames stay off the site, and two fixups.

Photographs are hotlinked from Flickr, so _data/photos/<slug>.yml is a guest
list, not a copy — dropping an entry removes an <img> from the page and leaves
the photograph itself untouched on Flickr. But a whole-collection re-import
rebuilds that guest list from scratch (the `whole_collection` branch in
import-flickr), which invites every frame back in. This file remembers the
decisions so bin/apply-edit can re-impose them in one command:

    bin/import-flickr kyrgyzstan-2026 --tags --user <you>
    bin/apply-edit

CUT is a denial list, not a keep list, and that is deliberate: a photograph it
has never heard of passes straight through. Upload a new leg, re-import, and the
new frames arrive untouched for you to review while the old decisions hold. To
put a frame back on the site, delete its id from CUT.

CHAPTERS overrides the chapter a photograph files under. Chapter normally comes
from its Flickr tags, and matching stops at the first chapter in
_data/photography.yml whose tag the photograph carries — so a frame tagged both
`second-suusamyr-homestay` and `bees` lands in the homestay and never reaches
Bees. Retagging on Flickr is the real fix; these are the stopgap, and turn into
harmless no-ops once the tags are right.

CAPTIONS repairs typos and duplicates. Each is guarded by the text it replaces,
so a caption you have since rewritten is never clobbered — a fix applies only to
the exact string it was written for, or to an empty caption.
"""

# id -> chapter name, which must match a `name:` in _data/photography.yml.
CHAPTERS = {
    "kyrgyzstan-2026": {
        "55484050249": "Bees",  # smoker, August — tagged for the homestay too, so precedence stranded it
        "55483993548": "Bees",  # honeycomb, August — tagged for the homestay too, so precedence stranded it
        "55483993663": "Bees",  # bees, August — tagged for the homestay too, so precedence stranded it
        # The portraits. Each is tagged for the place it was made, and Portraits
        # sits last in _data/photography.yml, so precedence files them under the
        # place and they never reach the suite on their own. Retagging them
        # `portraits` alone on Flickr would make these three no-ops.
        "55478963165": "Portraits",  # portrait 1, August — tagged toi-preparations
        "55478963590": "Portraits",  # portrait 2, August — tagged toi-preparations
        "55483023332": "Portraits",  # portrait, August — tagged korumdu-artifacts
        "55487258306": "Portraits",  # boy on the steps, August — tagged korumdu-artifacts
    },
}

# id -> (caption to replace, replacement). An empty caption also matches.
CAPTIONS = {
    "kyrgyzstan-2026": {
        "55477316177": ("everyone needs milk, August", "the calf waits, August"),
        "55479076691": ("kyz kuumai, August", "the chase, August"),
        "55479253119": ("kyz kuumai, August", "whip up, August"),
        "55478420278": ("Milking horses, August", "mare held for milking, August"),
        "55484026753": ("", "red badlands en route, August"),
        "55484131218": ("ridgeline climb, August23", "ridgeline climb, August"),
        "55485076103": ("landscapes en route, AugustC_3478", "landscapes en route, August"),
        # Uploaded 2026-08-25 with camera filenames for titles, so they imported
        # uncaptioned.
        "55486274502": ("", "bronze in hand, August"),
        "55487433754": ("", "coins in sleeves, August"),
        "55487258306": ("", "boy on the steps, August"),
    },
    "utah-arizona-2021": {
        "55477816799": ("Abandoned Town, April", "abandoned town below the cliffs, April"),
        "55477760313": ("Fairyland Point, April", "down into Fairyland, April"),
        "55477824079": ("Wahweap Hoodoos, April", "white veins at Wahweap, April"),
        "55478040330": ("Old Paria Mesa, April", "banded badlands at Old Paria, April"),
        "55476206027": ("Coyote Buttes North, April", "sandstone striations, April"),
        "55477646951": ("Buckskin Gulch, April", "light in Buckskin Gulch, April"),
        "55478038340": ("Coyote Buttes South, April", "the Wave, Coyote Buttes North, April"),  # the Wave is in Coyote Buttes North, not South
        "55477761853": ("Coyote Buttes North, April", "sandstone and one hiker, April"),
        "55477761358": ("Coyote Buttes North, April", "pink and cream, April"),
        "55478041760": ("Cane Beds, April", "cottonwood and wheelbarrow at dusk, April"),
        "55477766773": ("Cane Beds, April", "woodpecker on a dead limb, April"),
        "55477825069": ("Cane Beds, April", "welcome, April"),
        "55476657197": ("Cane Beds, April", "fence line and the road out, April"),
        "55476651757": ("Cane Beds, April", "clothesline at sunset, April"),
        "55477819674": ("Cane Beds, April", "last light on the mesa, April"),
    },
}

# Frames that made the edit, in page order. Used for reporting only: a
# photograph in neither KEPT nor CUT has not been looked at yet, and
# bin/apply-edit says so instead of quietly passing it through.
KEPT = {
    "kyrgyzstan-2026": [
        # Bishkek
        "55478637904",  # WWII monument, August
        "55478582783",  # double-scooter, August
        "55477473372",  # Naan at Osh Bazaar, August
        # Ala Archa
        "55477851743",  # glacial shower, August
        "55478127445",  # camp spot before dinnertime, August
        "55478127490",  # Ala Archa peaks, August
        # Ala Archa to Suusamyr
        "55477757296",  # watermelon season, August
        "55477381222",  # mega yurt, August
        "55477165802",  # parking lot of Globus, August
        # Ala-Bel Pass
        "55478578075",  # Ala-Bel Pass
        # Suusamyr landscapes
        "55478578125",  # leftovers, August
        "55483965770",  # traffic, August
        # First Suusamyr homestay
        "55478417533",  # flight risk, August
        "55478421678",  # siblings, August
        "55478422208",  # love, August
        "55478696090",  # siblings of a different kind, August
        "55483691833",  # milkman, August
        # Morning rituals
        "55478696450",  # rider at dawn, August
        "55477314507",  # yurt at dawn, August
        "55478424228",  # coming back after herding, August
        "55478698935",  # everyone needs milk, August
        "55477316177",  # the calf waits, August
        # Toi Preparations
        "55478745399",  # stereos, August
        "55477579052",  # gathering, August
        "55478963980",  # give a dog a bone, August
        "55477580222",  # Plov prep, August
        # Alysh
        "55479014276",  # more fun, August
        "55479014396",  # get ready, August
        "55479129648",  # alysh womens' rounds, August
        # Er Enish
        "55479128548",  # rider on the ridge B&W, August
        "55479404715",  # wrestling on horses, August
        "55478021347",  # direct eye contact, August
        "55479013906",  # rolling deep, August
        # Kyz Kuumai
        "55479076691",  # the chase, August
        "55479253119",  # whip up, August
        "55479077206",  # boy chases girl, August
        # Ulak Tartysh
        "55483607623",  # bystanding on horse, August
        "55482498842",  # scoring, August
        "55483607788",  # front row seat, August
        "55482499597",  # horse was ok, August
        "55483609083",  # pre-game meditations, August
        "55483664009",  # aura, August
        # Milking horses for kumys
        "55478418793",  # Kumys barrel with fresh horse milk, August
        "55478420278",  # mare held for milking, August
        "55478420843",  # Milking horses, August
        # Second Suusamyr homestay
        "55484238305",  # kurut in mass, August
        "55484238595",  # sunrise in Suusamyr, August
        "55483844121",  # Go Pats!, August
        # Bees
        "55484050249",  # smoker, August
        "55483993548",  # honeycomb, August
        "55483993663",  # bees, August
        # Suusamyr to Korumdu
        "55484026753",  # red badlands en route, August
        # Earthquake during hike
        "55484131218",  # ridgeline climb, August
        "55484131343",  # earthquake rockslide, August
        "55484131933",  # alpine lake, August
        # Milky Way
        "55484838446",  # towering, August
        "55484956018",  # milky way in Korumdu, August
        # Korumdu Artifacts
        "55484402800",  # arrowhead, August
        "55483023302",  # sun wheel, August
        "55486274502",  # bronze in hand, August
        "55487433754",  # coins in sleeves, August
        # Korumdu to Bokonbayevo
        "55485075773",  # petroglyphs, August
        "55485076103",  # landscapes en route, August
        # Eagle Hunter
        "55485078093",  # treat, August
        "55483972187",  # eagle hunter and eagle, August
        "55485351610",  # pets, August
        "55485351950",  # wingspan, August
        "55483972542",  # talons, August
        # Issyk-Kul
        "55485171314",  # Buddha on mountain, August
        "55484995401",  # traffic jam, August
        "55485387445",  # Issyk-kul is cool, August
        # Skazka Canyon
        "55485387750",  # Issyk-kul in the distance, August
        "55485172504",  # shades of orange, August
        # Karakol
        "55485402920",  # spices, August
        "55485402930",  # chicks, August
        "55484023397",  # art, August
        # Altyn Arashan
        "55485168083",  # dust to dust; wood to wood, August
        "55484063152",  # mounds, August
        "55485443025",  # home for a bit, August
        "55485051551",  # UAZ up, August
        # Portraits — out of chronology, as the chapter is
        "55478963165",  # portrait 1, August
        "55478963590",  # portrait 2, August
        "55483023332",  # portrait, August
        "55487258306",  # boy on the steps, August
    ],
    "utah-arizona-2021": [
        # Zion National Park
        "55477816799",  # abandoned town below the cliffs, April
        # Bryce Canyon National Park
        "55477760313",  # down into Fairyland, April
        # Grand Staircase-Escalante National Monument
        "55477824079",  # white veins at Wahweap, April
        "55478040330",  # banded badlands at Old Paria, April
        # Vermilion Cliffs National Monument
        "55476206027",  # sandstone striations, April
        "55477646951",  # light in Buckskin Gulch, April
        "55478038340",  # the Wave, Coyote Buttes North, April
        "55477761853",  # sandstone and one hiker, April
        "55477761358",  # pink and cream, April
        # Cane Beds
        "55478041760",  # cottonwood and wheelbarrow at dusk, April
        "55477766773",  # woodpecker on a dead limb, April
        "55477825069",  # welcome, April
        "55476657197",  # fence line and the road out, April
        "55476651757",  # clothesline at sunset, April
        "55477819674",  # last light on the mesa, April
    ],
}

# Frames kept off the site, in the order they used to appear.
#
# Both collections are empty as of 2026-08-24: the site shows every photograph
# Flickr has, 306 of them. The mechanism stays because it is the only thing
# between a re-import and a future edit — put an id back here and bin/apply-edit
# drops that frame again. The edits this used to hold (146 Kyrgyzstan, 64 Utah)
# are recoverable from git history at d2fd227.
CUT = {
    "kyrgyzstan-2026": [],
    "utah-arizona-2021": [],
}
