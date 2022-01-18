


from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('game', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Games(BaseModel):
    name = CharField()
    sales = IntegerField()
    release = CharField()
    genre = CharField()
    developer = CharField()
    publisher = CharField()
    


db.connect()
db.drop_tables([Games])
db.create_tables([Games])

GAMES1 = Games(name="PlayerUnknown's Battlegrounds", sales=42, release="Dec-17", genre="Battle royale", developer="PUBG Studios", publisher="Krafton").save()
GAMES2 = Games(name="Minecraft", sales=33, release="Nov-11", genre="Sandbox, survival", developer="Mojang Studios", publisher="Mojang Studios").save()
GAMES3 = Games(name="Diablo III", sales=20, release="May-12", genre="Action role-playing", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES4 = Games(name="Garry's Mod", sales=20, release="Nov-06", genre="Sandbox", developer="Facepunch Studios", publisher="Valve").save()
GAMES5 = Games(name="Terraria", sales=17.2, release="May-11", genre="Action-adventure", developer="Re-Logic", publisher="Re-Logic").save()
GAMES6 = Games(name="World of Warcraft", sales=14, release="Nov-04", genre="MMORPG", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES7 = Games(name="Half-Life 2", sales=12, release="Nov-04", genre="First-person shooter", developer="Valve", publisher="Valve (digital)").save()
GAMES8 = Games(name="The Witcher 3: Wild Hunt", sales=12, release="May-15", genre="Action role-playing", developer="CD Projekt Red", publisher="CD Projekt").save()
GAMES9 = Games(name="StarCraft", sales=11, release="Mar-98", genre="Real-time strategy", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES10 = Games(name="The Sims", sales=11, release="Feb-00", genre="Life simulation", developer="Maxis", publisher="Electronic Arts").save()
GAMES11 = Games(name="Fall Guys", sales=10, release="Aug-20", genre="Battle royale", developer="Mediatonic", publisher="Devolver Digital").save()
GAMES12 = Games(name="RollerCoaster Tycoon 3", sales=10, release="Oct-04", genre="Construction and management simulation", developer="Frontier Developments", publisher="Atari, Inc. (Windows)").save()
GAMES13 = Games(name="Half-Life", sales=9, release="Nov-98", genre="First-person shooter", developer="Valve", publisher="Sierra Entertainment").save()
GAMES14 = Games(name="Rust", sales=9, release="Feb-18", genre="Survival", developer="Facepunch Studios", publisher="Facepunch Studios").save()
GAMES15 = Games(name="Civilization V", sales=8, release="Sep-10", genre="Turn-based strategy, 4X", developer="Firaxis Games", publisher="2K Games & Aspyr").save()
GAMES16 = Games(name="The Sims 3", sales=7, release="Jun-09", genre="Life simulation", developer="Maxis", publisher="Electronic Arts").save()
GAMES17 = Games(name="Euro Truck Simulator 2", sales=6.5, release="Oct-12", genre="Vehicle simulation", developer="SCS Software", publisher="SCS Software").save()
GAMES18 = Games(name="Guild Wars", sales=6, release="Apr-05", genre="MMORPG", developer="ArenaNet", publisher="NCsoft").save()
GAMES19 = Games(name="StarCraft II: Wings of Liberty", sales=6, release="Jul-10", genre="Real-time strategy", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES20 = Games(name="The Sims 2", sales=6, release="Sep-04", genre="Life simulation", developer="Maxis", publisher="Electronic Arts").save()
GAMES21 = Games(name="Valheim", sales=6, release="Feb-21", genre="Survival", developer="Iron Gate", publisher="Coffee Stain Publishing").save()
GAMES22 = Games(name="ARMA 3", sales=5.5, release="Sep-13", genre="Tactical shooter", developer="Bohemia Interactive", publisher="Bohemia Interactive").save()
GAMES23 = Games(name="Last Ninja 2", sales=5.5, release="Aug-88", genre="Action-adventure", developer="System 3", publisher="Activision").save()
GAMES24 = Games(name="Cities: Skylines", sales=5, release="Mar-15", genre="City-building", developer="Colossal Order", publisher="Paradox Interactive").save()
GAMES25 = Games(name="Guild Wars 2", sales=5, release="Aug-12", genre="MMORPG", developer="ArenaNet", publisher="NCsoft").save()
GAMES26 = Games(name="SimCity 3000", sales=5, release="Jan-99", genre="City-building", developer="Maxis", publisher="Electronic Arts").save()
GAMES27 = Games(name="The Forest", sales=5, release="Apr-18", genre="Survival", developer="Endnight Games", publisher="Endnight Games").save()
GAMES28 = Games(name="Cyberpunk 2077", sales=4.5, release="Dec-20", genre="Action role-playing", developer="CD Projekt Red", publisher="CD Projekt").save()
GAMES29 = Games(name="DayZ", sales=4, release="Dec-13", genre="Survival", developer="Bohemia Interactive", publisher="Bohemia Interactive").save()
GAMES30 = Games(name="Diablo II", sales=4, release="Jun-00", genre="Action role-playing", developer="Blizzard North", publisher="Blizzard Entertainment").save()
GAMES31 = Games(name="Populous", sales=4, release="Jun-89", genre="God game", developer="Bullfrog Productions", publisher="Electronic Arts").save()
GAMES32 = Games(name="RollerCoaster Tycoon", sales=4, release="Mar-99", genre="Construction and management simulation", developer="Chris Sawyer", publisher="MicroProse Software").save()
GAMES33 = Games(name="The Last Ninja", sales=4, release="Jun-05", genre="Action-adventure", developer="System 3", publisher="Activision").save()
GAMES34 = Games(name="Warhammer 40,000: Dawn of War (including expansions)", sales=4, release="Sep-04", genre="Real-time strategy", developer="Relic Entertainment", publisher="THQ").save()
GAMES35 = Games(name="Where in the World Is Carmen Sandiego?", sales=4, release="Jun-85", genre="Educational", developer="Broderbund", publisher="Broderbund").save()
GAMES36 = Games(name="Dark Souls", sales=3.6, release="Aug-12", genre="Action role-playing", developer="FromSoftware", publisher="Namco Bandai Games").save()
GAMES37 = Games(name="Dark Souls III", sales=3.3, release="Apr-16", genre="Action role-playing", developer="FromSoftware", publisher="Bandai Namco Entertainment").save()
GAMES38 = Games(name="Age of Empires", sales=3, release="Oct-97", genre="Real-time strategy", developer="Ensemble Studios", publisher="Microsoft").save()
GAMES39 = Games(name="Civilization IV", sales=3, release="Oct-05", genre="Turn-based strategy, 4X", developer="Firaxis Games", publisher="2K Games & Aspyr").save()
GAMES40 = Games(name="Command & Conquer", sales=3, release="Aug-95", genre="Real-time strategy", developer="Westwood Studios", publisher="Virgin Interactive").save()
GAMES41 = Games(name="Command & Conquer: Red Alert", sales=3, release="Oct-96", genre="Real-time strategy", developer="Westwood Studios", publisher="Virgin Interactive").save()
GAMES42 = Games(name="Crysis", sales=3, release="Nov-07", genre="First-person shooter", developer="Crytek", publisher="Electronic Arts").save()
GAMES43 = Games(name="EverQuest", sales=3, release="Mar-99", genre="MMORPG", developer="Verant Interactive", publisher="Sony Online Entertainment").save()
GAMES44 = Games(name="Life Is Strange", sales=3, release="Jan-15", genre="Graphic adventure", developer="Dontnod Entertainment", publisher="Square Enix").save()
GAMES45 = Games(name="Theme Park", sales=3, release="Jun-05", genre="Construction and management simulation", developer="Bullfrog Productions", publisher="Electronic Arts").save()
GAMES46 = Games(name="Warcraft III: Reign of Chaos", sales=3, release="Jul-02", genre="Real-time strategy", developer="Blizzard Entertainment", publisher="Blizzard Entertainment (North America)").save()
GAMES47 = Games(name="Dark Souls II", sales=2.7, release="Apr-14", genre="Action role-playing", developer="FromSoftware", publisher="Bandai Namco Games").save()
GAMES48 = Games(name="Caesar II", sales=2.5, release="Sep-95", genre="City-building game", developer="Impressions Game", publisher="Sierra On-Line").save()
GAMES49 = Games(name="Caesar III", sales=2.5, release="May-99", genre="City-building game", developer="Impressions Game", publisher="Sierra Studios").save()
GAMES50 = Games(name="Factorio", sales=2.5, release="Feb-16", genre="Construction and management simulation", developer="Wube Software", publisher="Wube Software").save()
GAMES51 = Games(name="Lords of the Realm II", sales=2.5, release="Oct-96", genre="Turn-based strategy", developer="Impressions Game", publisher="Impressions Game").save()
GAMES52 = Games(name="Myst", sales=2.5, release="Sep-93", genre="Adventure, puzzle", developer="Cyan", publisher="Brøderbund").save()
GAMES53 = Games(name="Final Fantasy VII", sales=2.1, release="Jun-98", genre="Role-playing game", developer="Square", publisher="Eidos Interactive").save()
GAMES54 = Games(name="7 Days to Die", sales=2, release="Jun-16", genre="Survival horror", developer="The Fun Pimps", publisher="The Fun Pimps").save()
GAMES55 = Games(name="Age of Empires II: The Age of Kings", sales=2, release="Sep-99", genre="Real-time strategy", developer="Ensemble Studios", publisher="Microsoft").save()
GAMES56 = Games(name="Age of Empires III", sales=2, release="Oct-05", genre="Real-time strategy", developer="Ensemble Studios", publisher="Microsoft").save()
GAMES57 = Games(name="Anno 1503", sales=2, release="Mar-03", genre="City-building", developer="Max Design", publisher="Sunflowers").save()
GAMES58 = Games(name="Anno 1602", sales=2, release="Sep-98", genre="City-building", developer="Max Design", publisher="Sunflowers").save()
GAMES59 = Games(name="Baldur's Gate", sales=2, release="Dec-98", genre="Role-playing game", developer="BioWare", publisher="Interplay Entertainment").save()
GAMES60 = Games(name="Baldur's Gate II: Shadows of Amn", sales=2, release="Sep-00", genre="Computer role-playing game", developer="BioWare", publisher="Interplay Entertainment").save()
GAMES61 = Games(name="Battlefield 1942", sales=2, release="Sep-02", genre="First-person shooter", developer="EA DICE", publisher="Electronic Arts").save()
GAMES62 = Games(name="Black & White", sales=2, release="Mar-01", genre="God game", developer="Lionhead Studios", publisher="EA Games").save()
GAMES63 = Games(name="Civilization III", sales=2, release="Oct-01", genre="Turn-based strategy, 4X", developer="Firaxis Games", publisher="Infogrames").save()
GAMES64 = Games(name="Cossacks II: Napoleonic Wars", sales=2, release="Apr-05", genre="Real-time strategy", developer="GSC Game World", publisher="CDV Software").save()
GAMES65 = Games(name="Counter-Strike: Condition Zero", sales=2, release="Mar-04", genre="First-person shooter", developer="Valve", publisher="Valve (digital)").save()
GAMES66 = Games(name="Counter-Strike: Source", sales=2, release="Nov-04", genre="First-person shooter", developer="Valve", publisher="Electronic Arts (retail)").save()
GAMES67 = Games(name="Diablo", sales=2, release="Dec-96", genre="Action role-playing", developer="Blizzard North", publisher="Blizzard Entertainment (North America)").save()
GAMES68 = Games(name="Doom", sales=2, release="Dec-93", genre="First-person shooter", developer="id Software", publisher="id Software").save()
GAMES69 = Games(name="Doom II: Hell on Earth", sales=2, release="Sep-94", genre="First-person shooter", developer="id Software", publisher="GT Interactive").save()
GAMES70 = Games(name="Far Cry", sales=2, release="Mar-04", genre="First-person shooter", developer="Crytek", publisher="Ubisoft").save()
GAMES71 = Games(name="Grand Theft Auto V", sales=2, release="Apr-15", genre="Action-adventure", developer="Rockstar North", publisher="Rockstar Games").save()
GAMES72 = Games(name="Mafia: The City of Lost Heaven", sales=2, release="Aug-02", genre="Third-person shooter", developer="Illusion Softworks", publisher="Gathering of Developers").save()
GAMES73 = Games(name="Magicka", sales=2, release="Jan-11", genre="Action-adventure", developer="Arrowhead Game Studios", publisher="Paradox Interactive").save()
GAMES74 = Games(name="Neverwinter Nights", sales=2, release="Jun-02", genre="Role-playing game", developer="BioWare", publisher="Infogrames / Atari").save()
GAMES75 = Games(name="Planet Coaster", sales=2, release="Nov-16", genre="Construction and management simulation", developer="Frontier Developments", publisher="Frontier Developments").save()
GAMES76 = Games(name="POD", sales=2, release="Feb-97", genre="Racing game", developer="Ubisoft", publisher="Ubisoft").save()
GAMES77 = Games(name="SimCity", sales=2, release="Mar-13", genre="City-building", developer="Electronic Arts", publisher="Electronic Arts").save()
GAMES78 = Games(name="SimCity 4", sales=2, release="Jan-03", genre="City-building", developer="Maxis", publisher="Electronic Arts (Windows)").save()
GAMES79 = Games(name="Space Engineers", sales=2, release="Oct-13", genre="Simulation", developer="Keen Software House", publisher="Keen Software House").save()
GAMES80 = Games(name="Spore", sales=2, release="Sep-08", genre="God game", developer="Maxis", publisher="Electronic Arts").save()
GAMES81 = Games(name="Stickfight: The Game", sales=2, release="Sep-17", genre="Fighting", developer="Landfall Games", publisher="Landfall Games").save()
GAMES82 = Games(name="Stronghold: Crusader", sales=2, release="Jul-02", genre="Real-time strategy", developer="Firefly Studios", publisher="Take-Two Interactive / Gathering of Developers").save()
GAMES83 = Games(name="The Binding of Isaac", sales=2, release="Sep-11", genre="Action-adventure, roguelike", developer="Edmund McMillen & Florian Himsl", publisher="Headup Games").save()
GAMES84 = Games(name="The Witcher", sales=2, release="Oct-07", genre="Action role-playing", developer="CD Projekt Red", publisher="Atari, Inc").save()
GAMES85 = Games(name="The Witcher 2: Assassins of Kings", sales=2, release="May-11", genre="Action role-playing", developer="CD Projekt Red", publisher="CD Projekt").save()
GAMES86 = Games(name="Warcraft II: Tides of Darkness", sales=2, release="Dec-95", genre="Real-time strategy", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES87 = Games(name="Metal Gear Solid V: The Phantom Pain", sales=1.8, release="Sep-15", genre="Action-adventure, stealth", developer="Kojima Productions", publisher="Konami").save()
GAMES88 = Games(name="American Truck Simulator", sales=1.5, release="Oct-12", genre="Vehicle simulation", developer="SCS Software", publisher="SCS Software").save()
GAMES89 = Games(name="International Karate", sales=1.5, release="Nov-85", genre="Fighting", developer="System 3", publisher="Epyx").save()
GAMES90 = Games(name="Sega Mega Drive and Genesis Classics", sales=1.5, release="Jun-10", genre="Compilation", developer="Sega", publisher="Sega").save()
GAMES91 = Games(name="Stellaris", sales=1.5, release="May-16", genre="RTS, 4X, Grand Strategy", developer="Paradox Development Studio", publisher="Paradox Interactive").save()
GAMES92 = Games(name="Resident Evil 6", sales=1.3, release="Mar-13", genre="Third-person shooter, survival horror", developer="Capcom", publisher="Capcom").save()
GAMES93 = Games(name="Satisfactory", sales=1.3, release="Mar-19", genre="Construction and management simulation", developer="Coffee Stain Studios", publisher="Coffee Stain Publishing").save()
GAMES94 = Games(name="Ultra Street Fighter IV", sales=1.3, release="Jul-09", genre="Fighting", developer="Capcom", publisher="Capcom").save()
GAMES95 = Games(name="Nier: Automata", sales=1.2, release="Mar-17", genre="Action role-playing, hack and slash", developer="PlatinumGames", publisher="Square Enix").save()
GAMES96 = Games(name="Resident Evil 4: Ultimate HD Edition", sales=1.2, release="Feb-14", genre="Third-person shooter, survival horror", developer="Capcom", publisher="Capcom").save()
GAMES97 = Games(name="Kingdom Come: Deliverance", sales=1.1, release="Feb-18", genre="Action role-playing game", developer="Warhorse Studios", publisher="Warhorse Studios").save()
GAMES98 = Games(name="Pac-Man Championship Edition DX+", sales=1.1, release="Sep-13", genre="Maze, arcade", developer="Namco Bandai Games", publisher="Namco Bandai Games").save()
GAMES99 = Games(name="Age of Mythology", sales=1, release="Oct-02", genre="Real-time strategy", developer="Ensemble Studios", publisher="Microsoft").save()
GAMES100 = Games(name="American McGee's Alice", sales=1, release="Oct-00", genre="Action-adventure, platformer", developer="Rogue Entertainment", publisher="Electronic Arts").save()
GAMES101 = Games(name="Ark: Survival Evolved", sales=1, release="Jun-15", genre="Action-adventure, Survival", developer="Studio Wildcard", publisher="Studio Wildcard").save()
GAMES102 = Games(name="Battlefield Vietnam", sales=1, release="Mar-04", genre="First-person shooter", developer="EA DICE", publisher="Electronic Arts").save()
GAMES103 = Games(name="BioShock", sales=1, release="Aug-07", genre="First-person shooter", developer="Irrational Games", publisher="2K Games").save()
GAMES104 = Games(name="Blade Runner", sales=1, release="Nov-97", genre="Point-and-click", developer="Westwood Studios", publisher="Virgin Interactive").save()
GAMES105 = Games(name="Civilization II", sales=1, release="Feb-96", genre="Turn-based strategy, 4X", developer="MicroProse", publisher="MicroProse").save()
GAMES106 = Games(name="Command & Conquer 3: Tiberium Wars", sales=1, release="Mar-07", genre="Real-time strategy", developer="EA Los Angeles", publisher="Electronic Arts").save()
GAMES107 = Games(name="Command & Conquer: Red Alert 2", sales=1, release="Oct-00", genre="Real-time strategy", developer="Westwood Pacific", publisher="Electronic Arts").save()
GAMES108 = Games(name="Command & Conquer: Tiberian Sun", sales=1, release="Aug-99", genre="Real-time strategy", developer="Westwood Studios", publisher="Electronic Arts").save()
GAMES109 = Games(name="Commandos: Behind Enemy Lines", sales=1, release="Jun-98", genre="Real-time tactics", developer="Pyro Studios", publisher="Eidos Interactive").save()
GAMES110 = Games(name="Crusader Kings II", sales=1, release="Feb-12", genre="Grand strategy", developer="Paradox Development Studio", publisher="Paradox Interactive").save()
GAMES111 = Games(name="Crusader Kings III", sales=1, release="Sep-20", genre="Grand strategy", developer="Paradox Development Studio", publisher="Paradox Interactive").save()
GAMES112 = Games(name="Crysis Warhead", sales=1, release="Sep-08", genre="First-person shooter", developer="Crytek Budapest", publisher="Electronic Arts").save()
GAMES113 = Games(name="Cuphead", sales=1, release="Sep-17", genre="Run and gun", developer="StudioMDHR", publisher="StudioMDHR").save()
GAMES114 = Games(name="Danganronpa 2: Goodbye Despair", sales=1, release="Apr-16", genre="Visual novel, adventure", developer="Spike Chunsoft", publisher="Spike Chunsoft").save()
GAMES115 = Games(name="Danganronpa: Trigger Happy Havoc", sales=1, release="Feb-16", genre="Visual novel, adventure", developer="Spike Chunsoft", publisher="Spike Chunsoft").save()
GAMES116 = Games(name="Daryl F. Gates' Police Quest: SWAT", sales=1, release="Sep-95", genre="Interactive movie", developer="Sierra Online", publisher="Sierra Online").save()
GAMES117 = Games(name="Deer Hunter", sales=1, release="Nov-97", genre="Sports", developer="Sunstorm Interactive", publisher="WizardWorks").save()
GAMES118 = Games(name="Divinity: Original Sin II", sales=1, release="Sep-17", genre="Role-playing game", developer="Larian Studios", publisher="Larian Studios").save()
GAMES119 = Games(name="Duke Nukem 3D", sales=1, release="Jan-96", genre="First-person shooter", developer="3D Realms", publisher="GT Interactive Software").save()
GAMES120 = Games(name="Dungeon Lords", sales=1, release="May-05", genre="Role-playing game", developer="Heuristic Park", publisher="DreamCatcher Interactive").save()
GAMES121 = Games(name="Dungeon Siege", sales=1, release="Apr-02", genre="Role-playing game", developer="Gas Powered Games", publisher="Microsoft Game Studios").save()
GAMES122 = Games(name="Empire Earth", sales=1, release="Nov-01", genre="Real-time strategy", developer="Stainless Steel Studios", publisher="Sierra Entertainment").save()
GAMES123 = Games(name="Europa Universalis IV", sales=1, release="Aug-13", genre="Grand strategy", developer="Paradox Development Studio", publisher="Paradox Interactive").save()
GAMES124 = Games(name="Frogger", sales=1, release="Nov-97", genre="Action", developer="SCE Cambridge Studio", publisher="Hasbro Interactive").save()
GAMES125 = Games(name="Full Throttle", sales=1, release="Apr-95", genre="Graphic adventure", developer="LucasArts", publisher="LucasArts").save()
GAMES126 = Games(name="Glory of the Roman Empire", sales=1, release="Jun-06", genre="City-building game", developer="Haemimont Games", publisher="CDV Software").save()
GAMES127 = Games(name="Grand Prix 2", sales=1, release="Aug-96", genre="Sim racing", developer="MicroProse", publisher="MicroProse").save()
GAMES128 = Games(name="Harry Potter and the Philosopher's Stone", sales=1, release="Nov-01", genre="Action-adventure", developer="KnowWonder", publisher="Electronic Arts").save()
GAMES129 = Games(name="Hearts of Iron IV", sales=1, release="Jun-16", genre="Real-time strategy, grand strategy wargame", developer="Paradox Development Studio", publisher="Paradox Interactive").save()
GAMES130 = Games(name="Hidden & Dangerous", sales=1, release="Jul-99", genre="Action", developer="Illusion Softworks", publisher="Take-Two Interactive").save()
GAMES131 = Games(name="Hidden & Dangerous 2", sales=1, release="Oct-03", genre="Action", developer="Illusion Softworks", publisher="Take-Two Interactive").save()
GAMES132 = Games(name="Hollow Knight", sales=1, release="Feb-17", genre="Metroidvania", developer="Team Cherry", publisher="Team Cherry").save()
GAMES133 = Games(name="Hotel Giant", sales=1, release="May-02", genre="Business simulation", developer="Enlight Software", publisher="JoWood Productions").save()
GAMES134 = Games(name="Hydlide", sales=1, release="Dec-84", genre="Action role-playing", developer="Technology and Entertainment Software", publisher="Technology and Entertainment Software").save()
GAMES135 = Games(name="Imperivm: Great Battles of Rome", sales=1, release="May-05", genre="Real-time strategy", developer="Haemimont Games", publisher="FX Interactive").save()
GAMES136 = Games(name="Just Survive[e]", sales=1, release="Jan-15", genre="Survival", developer="Daybreak Game Company", publisher="Daybreak Game Company").save()
GAMES137 = Games(name="Killing Floor", sales=1, release="May-09", genre="First-person shooter", developer="Tripwire Interactive", publisher="Tripwire Interactive").save()
GAMES138 = Games(name="Machinarium", sales=1, release="Oct-09", genre="Graphic adventure, puzzle", developer="Amanita Design", publisher="Amanita Design").save()
GAMES139 = Games(name="Microsoft Flight Simulator X", sales=1, release="Oct-06", genre="Amateur flight simulation", developer="Microsoft Game Studios", publisher="Microsoft Game Studios").save()
GAMES140 = Games(name="Mordhau", sales=1, release="Apr-19", genre="Action", developer="Triternion", publisher="Triternion").save()
GAMES141 = Games(name="Operation Flashpoint: Cold War Crisis", sales=1, release="Jun-01", genre="Tactical shooter", developer="Bohemia Interactive Studio", publisher="Codemasters").save()
GAMES142 = Games(name="Patrician III: Rise of the Hanse", sales=1, release="Oct-03", genre="Business simulation", developer="Ascaron", publisher="Encore").save()
GAMES143 = Games(name="Phantasmagoria", sales=1, release="Jul-95", genre="Interactive movie", developer="Sierra Online", publisher="Sierra Online").save()
GAMES144 = Games(name="Prison Architect", sales=1, release="Sep-12", genre="Construction and management simulation", developer="Introversion Software", publisher="Introversion Software").save()
GAMES145 = Games(name="Psychonauts", sales=1, release="Apr-05", genre="Platform", developer="Double Fine Productions", publisher="THQ").save()
GAMES146 = Games(name="Quake", sales=1, release="Jun-96", genre="First-person shooter", developer="id Software", publisher="GT Interactive").save()
GAMES147 = Games(name="Quake II", sales=1, release="Dec-97", genre="First-person shooter", developer="id Software", publisher="Activision").save()
GAMES148 = Games(name="Railroad Tycoon II", sales=1, release="Nov-98", genre="Construction and management simulation", developer="PopTop Software", publisher="Gathering of Developers").save()
GAMES149 = Games(name="Resident Evil 5", sales=1, release="Sep-09", genre="Third-person shooter, survival horror", developer="Capcom", publisher="Capcom").save()
GAMES150 = Games(name="Return to Castle Wolfenstein", sales=1, release="Nov-01", genre="First-person shooter", developer="Gray Matter Interactive", publisher="Activision").save()
GAMES151 = Games(name="Return to Zork", sales=1, release="Aug-93", genre="Adventure", developer="Infocom", publisher="Activision").save()
GAMES152 = Games(name="RoboCop", sales=1, release="Dec-88", genre="Beat 'em up, run-and-gun", developer="Data East", publisher="Data East, Ocean Software").save()
GAMES153 = Games(name="Rome: Total War", sales=1, release="Sep-04", genre="Real-time strategy", developer="The Creative Assembly", publisher="Activision").save()
GAMES154 = Games(name="Runaway: A Road Adventure", sales=1, release="Jul-01", genre="Adventure", developer="Péndulo Studios, S.L.", publisher="Dinamic Multimedia").save()
GAMES155 = Games(name="Sacred", sales=1, release="Mar-04", genre="Action role-playing", developer="Ascaron", publisher="Encore").save()
GAMES156 = Games(name="Star Wars Galaxies", sales=1, release="Jun-03", genre="MMORPG", developer="Sony Online Entertainment", publisher="LucasArts").save()
GAMES157 = Games(name="Star Wars: Rebel Assault", sales=1, release="Nov-93", genre="Rail shooter", developer="LucasArts", publisher="LucasArts").save()
GAMES158 = Games(name="StarCraft II: Heart of the Swarm", sales=1, release="Mar-13", genre="Real-time strategy", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES159 = Games(name="StarCraft II: Legacy of the Void", sales=1, release="Nov-15", genre="Real-time strategy", developer="Blizzard Entertainment", publisher="Blizzard Entertainment").save()
GAMES160 = Games(name="Stardew Valley", sales=1, release="Feb-16", genre="Simulation, role-playing game", developer="ConcernedApe", publisher="ConcernedApe[f]").save()
GAMES161 = Games(name="Stronghold", sales=1, release="Oct-01", genre="Real-time strategy", developer="Firefly Studios", publisher="Take-Two Interactive / Gathering of Developers").save()
GAMES162 = Games(name="Supreme Commander", sales=1, release="Feb-07", genre="Real-time strategy", developer="Gas Powered Games", publisher="THQ").save()
GAMES163 = Games(name="Tetris", sales=1, release="Jan-88", genre="Puzzle", developer="Spectrum HoloByte", publisher="Spectrum HoloByte").save()
GAMES164 = Games(name="The Legend of Sword and Fairy 3", sales=1, release="Jul-03", genre="Role-playing game", developer="Softstar Entertainment", publisher="Softstar Entertainment").save()
GAMES165 = Games(name="The Legend of Sword and Fairy 5", sales=1, release="Jul-11", genre="Role-playing game", developer="Softstar", publisher="Softstar").save()
GAMES166 = Games(name="The Stanley Parable", sales=1, release="Oct-13", genre="Interactive fiction", developer="Galactic Cafe", publisher="Galactic Cafe").save()
GAMES167 = Games(name="Total Annihilation", sales=1, release="Sep-97", genre="Real-time strategy", developer="Cavedog Entertainment", publisher="GT Interactive").save()
GAMES168 = Games(name="Tropico", sales=1, release="Apr-01", genre="Construction and management simulation", developer="PopTop Software", publisher="Gathering of Developers").save()
GAMES169 = Games(name="Unreal", sales=1, release="May-98", genre="First-person shooter", developer="Epic Games", publisher="GT Interactive").save()
GAMES170 = Games(name="Unreal Tournament", sales=1, release="Nov-99", genre="First-person shooter", developer="Epic Games", publisher="GT Interactive").save()
GAMES171 = Games(name="Vietcong", sales=1, release="Mar-03", genre="Tactical shooter", developer="Pterodon", publisher="Gathering of Developers").save()
GAMES172 = Games(name="Warhammer Online: Age of Reckoning", sales=1, release="Sep-08", genre="MMORPG", developer="Mythic Entertainment", publisher="Electronic Arts").save()
GAMES173 = Games(name="Who Wants to Be a Millionaire?", sales=1, release="Nov-99", genre="Trivia game", developer="Jellyvision", publisher="Disney Interactive Studios").save()
GAMES174 = Games(name="Wing Commander 3: Heart of the Tiger", sales=1, release="Dec-94", genre="Space combat simulation", developer="Origin Systems", publisher="Electronic Arts").save()
GAMES175 = Games(name="Zoo Tycoon", sales=1, release="Oct-01", genre="Business simulation", developer="Microsoft", publisher="Blue Fang Games").save()


app = Flask(__name__)


@app.route('/')
def index():
    
    return 'Welcome to my games API'
@app.route('/games', methods=['GET'])
@app.route('/games/<id>', methods=['GET'])


def games(id=None, game=None):
  if request.method == 'GET':
    while id:
        games = Games.get(Games.id == id)
        games = model_to_dict(games)
        return jsonify(games)
    else:
        game = []
        for games in Games.select():
            game.append(model_to_dict(games))
        return jsonify(game)

@app.route('/games/names/<name>', methods=['GET'])
def name(name=None):
    if name:
        name = Games.get(Games.name == name)
        name = model_to_dict(name)
        return jsonify(name) 

@app.route('/games/genre/<genre>', methods=['GET'])
def genre(genre=None):
    if genre:
        genrer = []
        for gen in Games.select().where(Games.genre == genre):
            genrer.append(model_to_dict(gen))
        while genre:    
            return jsonify(genrer)

@app.route('/games/developer/<developer>', methods=['GET'])
def developer(developer=None):
    if developer:
        developerr = []
        for dev in Games.select().where(Games.developer == developer):
            developerr.append(model_to_dict(dev))
        while developer:    
            return jsonify(developerr)

app.run(port=9020, debug=True)

