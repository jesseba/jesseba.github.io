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
        "55483023332": "Korumdu of Naryn Region",  # portrait, August — a portrait, not an artifact
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
        "55478963165",  # portrait 1, August
        "55478963590",  # portrait 2, August
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
        # Korumdu of Naryn Region
        "55483023332",  # portrait, August
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
CUT = {
    "kyrgyzstan-2026": [
        # Bishkek
        "55478464691",  # Manas, Bishkek
        "55477473017",  # Kurut, August
        "55478638264",  # soviet-era buildings, August
        "55478583018",  # streets of Bishkek, August
        "55477473217",  # tree-lined, August
        "55478582428",  # accordianist, August
        # Ala Archa
        "55477851938",  # moody Ala Archa River, August
        "55477852038",  # coffee, August
        "55478127050",  # flora, August
        "55477910929",  # down river, August
        "55477853028",  # horse portrait, August
        "55476744152",  # low clouds, August
        "55477853483",  # Ala Archa, August
        "55477911599",  # river and flowers, August
        "55476744687",  # first glimpse of Tian Shan mountains, August
        # Ala Archa to Suusamyr
        "55478149700",  # Suusamyr Valley, August
        "55477757051",  # Up to Too-Ashuu Pass, August
        "55477932764",  # Up to Too-Ashuu Pass, August
        "55477933219",  # Up to Too-Ashuu Pass, August
        "55477138122",  # Right after Too-Ashuu Pass, August
        "55478317374",  # Other side of Too-Ashuu Pass, August
        # Ala-Bel Pass
        "55477306517",  # Manas near Ala-Bel Pass, August
        "55478690350",  # Toyota Sequoia 2008, August
        # Suusamyr landscapes
        "55478357234",  # Suus landscapes, August
        "55478357324",  # horses at river crossing, August
        "55478577205",  # Suusamyr Jailoo, August
        "55478183356",  # Herd, August
        "55478577630",  # Another Jailoo, August
        "55478357849",  # Suusamyr river en route to Issyk-kul, August
        "55478577790",  # Suus landscapes, August
        "55478358084",  # tributaries, August
        "55478690575",  # Suus
        "55483746794",  # river, August
        "55483746914",  # horses, August
        "55483569941",  # suus landscape, August
        # First Suusamyr homestay
        "55478690780",  # rolling plains to mountains, August
        "55478693195",  # Horse portrait 2, August
        "55477311017",  # Yin and yang, August
        "55478302561",  # Horse portrait 3, August
        "55478421038",  # grazing, August
        "55478303181",  # Landscape, August
        "55478695355",  # kitten ready for adventures, August
        "55478304001",  # kitten ready for adventures, August
        "55478304091",  # siblings, August
        "55478423863",  # sunset, August
        "55478479494",  # Leica the space dog, August
        "55483965495",  # rest, August
        "55483691978",  # leica, August
        # Morning rituals
        "55478423283",  # chores, August
        "55477315332",  # morning chores, August
        "55478425033",  # everyone needs milk, August
        # Toi Preparations
        "55478687068",  # gallop, August
        "55478962010",  # games to start, August
        "55478687143",  # vroom, August
        "55478745339",  # gathering, August
        "55478745644",  # gathering, August
        "55477579102",  # Toi is a feast, August
        "55478687988",  # gathering, August
        "55478571646",  # gathering, August
        "55478688213",  # pull up, August
        "55478963705",  # horse portraits, August
        "55478963770",  # ulak player in the distance, August
        "55477580322",  # landscape, August
        "55478572576",  # Plov prep, August
        "55478689243",  # Plov prep, August
        "55477578677",  # meeting of minds, August
        # Alysh
        "55479014491",  # alysh, August
        # Er Enish
        "55479187819",  # rider on the ridge, August
        "55479404975",  # also called Oodarysh, August
        "55479128778",  # playtime, August
        "55478021082",  # Er Enish, August
        "55478021197",  # round 3, August
        "55479405320",  # Er Enish, August
        # Kyz Kuumai
        "55479076171",  # kyz kuumai, August
        "55479468665",  # kyz kuumai, August
        "55479076636",  # kyz kuumai, August
        "55479192243",  # then girl chases boy, August
        "55479469375",  # kyz kuumai, August
        # Ulak Tartysh
        "55483879735",  # rider off horse, August
        "55483607078",  # front row seaters need to be agile, August
        "55483482951",  # second game start, August
        "55483607223",  # the game and the scene, August
        "55483880375",  # horse and rider profile, August
        "55483483191",  # (uncaptioned)
        "55483881030",  # (uncaptioned)
        "55483662944",  # (uncaptioned)
        "55483608188",  # brute strength, August
        "55483484271",  # goal, August
        "55483484311",  # post-goal celebrations, August
        "55483608558",  # goal, August
        "55483608778",  # bystanding, August
        "55483881970",  # bystanding, August
        "55483484916",  # goal, August
        "55483649018",  # skirmish, August
        # Milking horses for kumys
        "55478419563",  # Milking horses, August
        "55478301766",  # Milking horses, August
        # Second Suusamyr homestay
        "55484021294",  # Kyrgyz yurt, August
        "55484021404",  # sunrise, August
        "55483843856",  # stallion, August
        "55483964748",  # sunrise, August
        "55483964898",  # candy-colored, August
        "55482858367",  # hills and mountains, August
        "55483844116",  # horses to graze, August
        "55482858667",  # a natural washing machine, August
        "55484050534",  # (uncaptioned)
        "55484050619",  # (uncaptioned)
        # Suusamyr to Korumdu
        "55484026808",  # (uncaptioned)
        "55484083549",  # (uncaptioned)
        "55484300495",  # (uncaptioned)
        "55482919767",  # (uncaptioned)
        "55483906416",  # (uncaptioned)
        "55484300700",  # (uncaptioned)
        # Earthquake during hike
        "55484185539",  # rest, August
        "55484403130",  # ridgeline climb, August
        "55483023942",  # ridgeline climb, August
        "55484010801",  # earthquake rockslide, August
        "55484403960",  # a valley traversed, August
        "55484011241",  # alpine lake, August
        "55484404015",  # 12000 feet elevation, August
        # Milky Way
        "55483848512",  # cloudy milky way, August
        "55485228520",  # glimpse of Perseid meteor shower, August
        "55484838386",  # home under stars, August
        "55483849552",  # Korumdu of Naryn region, August
        "55484838981",  # stardust, August
        # Korumdu to Bokonbayevo
        "55484958716",  # landscapes en route, August
        "55485075978",  # landscapes en route, August
        # Eagle Hunter
        "55485077943",  # Bokonbayevo, August
        "55484960981",  # Eagle profile, August
        "55483972082",  # hunting, August
        "55485351660",  # eagle hunter and eagle, August
        "55485351650",  # eagle hunter and eagle, August
        "55485078453",  # hunting, August
        # Issyk-Kul
        "55485171819",  # post-beach day, August
        "55484007752",  # end route to Karakol, August
        # Skazka Canyon
        "55484007727",  # Fairtytale canyon, August
        "55484007792",  # Skazka, August
        # Karakol
        "55484023227",  # chicks in Karakol, August
        # Altyn Arashan
        "55485167238",  # GG in the mountains, August
        "55485050201",  # camping, August
        "55485441955",  # horses and mountains, August
        "55484062522",  # more yurts, August
        "55485167878",  # short hike, August
        "55485442630",  # more mounds, August
        "55485168478",  # babbling brook, August
        "55485442925",  # river route, August
        "55485227504",  # hunting for hot springs, August
    ],
    "utah-arizona-2021": [
        # Zion National Park
        "55477818054",  # Zion National Park, April
        "55477642171",  # At Zion National Park, April
        "55478034465",  # At Zion National Park, April
        "55477642201",  # GG at Zion National Park, April
        "55477642006",  # Benthic Cyanobacteria at Zion National Park, April
        "55477641731",  # GG at Zion National Park, April
        "55477758388",  # Zion National Park, April
        "55477817124",  # Abandoned Town, April
        "55476648617",  # Angel's Landing, April
        "55477816309",  # Angel's Landing, April
        "55477756713",  # Vultures at Angel's Landing, April
        "55477640461",  # Angel's Landing, April
        "55478032785",  # Angel's Landing, April
        "55478032600",  # Angel's Landing, April
        # Bryce Canyon National Park
        "55478036310",  # Bryce Canyon National Park, April
        "55477643981",  # Bryce Point, April
        "55476651322",  # Bryce Canyon National Park, April
        "55476651252",  # Fairyland Point, April
        "55477643681",  # Bryce Canyon National Park, April
        "55478035495",  # Swamp Canyon, April
        "55477643191",  # Bryce Canyon National Park, April
        "55478035440",  # Swamp Canyon, April
        "55477818709",  # Bryce Canyon National Park, April
        "55476650182",  # Bryce Canyon National Park, April
        "55476650247",  # Bryce Canyon National Park, April
        "55477759328",  # Sunrise Point at Bryce Canyon National Park, April
        # Grand Staircase-Escalante National Monument
        "55477824319",  # Wiregrass Canyon, April
        "55477824254",  # Wiregrass Canyon, April
        "55477648461",  # Wahweap Hoodoos, April
        "55477648411",  # Old Paria Mesa, April
        "55477823909",  # Old Paria Mesa, April
        "55477647986",  # Toadstool Hoodoos, April
        "55477765008",  # Toadstool Hoodoos, April
        "55478040105",  # Toadstool Hoodoos, April
        "55477823119",  # Toadstool Hoodoos, April
        "55476655247",  # Nautilus Rock Formation, April
        "55477647471",  # Toadstool Hoodoos, April
        "55477764188",  # Toadstool Hoodoos, April
        "55477822669",  # Toadstool Hoodoos, April
        # Vermilion Cliffs National Monument
        "55477198311",  # Coyote Buttes North, April
        "55478039260",  # Buckskin Gulch, April
        "55477822184",  # Buckskin Gulch, April
        "55477763578",  # Buckskin Gulch, April
        "55478038810",  # Buckskin Gulch, April
        "55477763423",  # Coyote Buttes, April
        "55478038370",  # Coyote Buttes, April
        "55478038300",  # Coyote Buttes South, April
        "55478038230",  # Coyote Buttes South, April
        "55478037835",  # Coyote Buttes South, April
        "55477645546",  # Coyote Buttes South, April
        "55476653397",  # Coyote Buttes North, April
        "55477762398",  # Coyote Buttes North, April
        "55478037290",  # Coyote Buttes North, April
        "55477761903",  # Coyote Buttes North, April
        "55477761778",  # Coyote Buttes South, April
        "55476652302",  # Coyote Buttes North, April
        "55477761268",  # Coyote Buttes North, April
        "55477761098",  # Vermilion Cliffs National Monument, April
        # Cane Beds
        "55476657432",  # Cane Beds, April
        "55477825109",  # Cane Beds, April
        "55477824749",  # Cane Beds, April
        "55476656982",  # Cane Beds, April
        "55478041005",  # Cane Beds, April
        "55477649181",  # Cane Beds, April
    ],
}
