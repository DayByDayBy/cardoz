[{
    "type": "major",
    "suit": None,
    "value": None,
    "nameShort": "ar01",
    "name": "The Magician",
    "position": 1,
    "meaningUp": "Skill, diplomacy, address, subtlety; sickness, pain, loss, disaster, snares of enemies; self-confidence, will; the Querent, if male.",
    "meaningRev": "Physician, Magus, mental disease, disgrace, disquiet.",
    "description": "A youthful figure in the robe of a magician, having the countenance of divine Apollo, with smile of confidence and shining eyes. Above his head is the mysterious sign of the Holy Spirit, the sign of life, like an endless cord, forming the figure 8 in a horizontal position . About his waist is a serpent-cincture, the serpent appearing to devour its own tail. This is familiar to most as a conventional symbol of eternity, but here it indicates more especially the eternity of attainment in the spirit. In the Magician's right hand is a wand raised towards heaven, while the left hand is pointing to the earth. This dual sign is known in very high grades of the Instituted Mysteries; it shews the descriptionent of grace, virtue and light, drawn from things above and derived to things below. The suggestion throughout is therefore the possession and communication of the Powers and Gifts of the Spirit. On the table in front of the Magician are the symbols of the four Tarot suits, signifying the elements of natural life, which lie like counters before the adept, and he adapts them as he wills. Beneath are roses and lilies, the flos campi and lilium convallium, changed into garden flowers, to shew the culture of aspiration. This card signifies the divine motive in man, reflecting God, the will in the liberation of its union with that which is above. It is also the unity of individual being on all planes, and in a very high sense it is thought, in the fixation thereof. With further reference to what I have called the sign of life and its connexion with the number 8, it may be remembered that Christian Gnosticism speaks of rebirth in Christ as a change \"unto the Ogdoad.\" The mystic number is termed Jerusalem above, the Land flowing with Milk and Honey, the Holy Spirit and the Land of the Lord. According to Martinism, 8 is the number of Christ."
    },
#   etc
 {
    "type": "minor",
    "suit": "wands",
    "value": 4,
    "nameShort": "wa04",
    "name": "Four of Wands",
    "position": 25,
    "meaningUp": "They are for once almost on the surface--country life, haven of refuge, a species of domestic harvest-home, repose, concord, harmony, prosperity, peace, and the perfected work of these.",
    "meaningRev": "The meaning remains unaltered; it is prosperity, increase, felicity, beauty, embellishment.",
    "description": "From the four great staves planted in the foreground there is a great garland suspended; two female figures uplift nosegays; at their side is a bridge over a moat, leading to an old manorial house."
    },
#   etc
 ]


#  added 'suit' to major, streamlined and simplified very slightly, 
#  but tbh the design could still do with work

# wondering if there's any sense in making a more generic card list 
# schema - playing cards don't really need it, suit and number is enough but maybe some 
# depth could be added. eg could add 'colour', even tho it's 1:1 with suit, could allow for 
# different sorts/shuffles/etc to be done, or where you want an even split of the deck; could 
# also add weights and values from various games, but that seems better left to the game mechanics 
# themselves, could get complicated otherwise


# thought: could also maybe add other frameworks/relationships people ascribe to tarot




# some SQL thoughts...


# readings (
#   id INTEGER PRIMARY KEY,
#   user_id INTEGER REFERENCES users(id),
#   question TEXT,
#   spread_type TEXT,
#   deck_id TEXT,
#   prompt_version TEXT,
#   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#   output_text TEXT,
#   user_notes TEXT
# )

# and

# reading_cards (
#   id INTEGER PRIMARY KEY,
#   reading_id INTEGER REFERENCES readings(id),
#   position INTEGER,
#   name_short TEXT,
#   name TEXT,
#   meaning_up TEXT,
#   meaning_rev TEXT,
#   is_reversed BOOLEAN,
#   notes TEXT
# )
or
# CREATE TABLE reading_cards (
#     id INTEGER PRIMARY KEY,
#     reading_id INTEGER NOT NULL,     -- foreign key to readings
#     position_index INTEGER NOT NULL, -- e.g. 0, 1, 2 (spread len)
#     card_id TEXT NOT NULL,           -- e.g. 'ar01' or similar, short name
#     reversed BOOLEAN DEFAULT FALSE,  -- whether the card is reversed
#     FOREIGN KEY (reading_id) REFERENCES readings(id),
#     FOREIGN KEY (card_id) REFERENCES cards(nameShort)
# );

# and obvs for all that, will need cards:   

# cards (
#   id INTEGER PRIMARY KEY,
#   name_short TEXT UNIQUE,
#   name TEXT,
#   type TEXT,
#   suit TEXT,
#   value INTEGER,
#   position INTEGER,
#   meaning_up TEXT,
#   meaning_rev TEXT,
#   description TEXT,
#   keywords TEXT[], -- or TEXT if serialized
#   deck_id TEXT,
#   image_url TEXT
# )

#  with

# SELECT rc.position_index, sp.label, c.name, c.meaningUp, c.meaningRev, rc.reversed
# FROM reading_cards rc
# JOIN cards c ON rc.card_id = c.nameShort
# JOIN readings r ON rc.reading_id = r.id
# JOIN spread_positions sp ON sp.spread_id = r.spread_id AND sp.position = rc.position_index
# WHERE rc.reading_id = 1
# ORDER BY rc.position_index;