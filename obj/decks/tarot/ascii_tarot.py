cards = [
    "ar01", "ar02", "ar03", "ar04", "ar05", "ar06", "ar07", "ar08", "ar09", "ar10", "ar11", "ar12", "ar13",
    "ar14", "ar15", "ar16", "ar17", "ar18", "ar19", "ar20", "ar00", "ar21", "wapa", "wakn", "waqu", "waki",
    "waac", "wa02", "wa03", "wa04", "wa05", "wa06", "wa07", "wa08", "wa09", "wa10", "cupa", "cukn", "cuqu",
    "cuki", "cuac", "cu02", "cu03", "cu04", "cu05", "cu06", "cu07", "cu08", "cu09", "cu10", "pepa", "pekn",
    "pequ", "peki", "peac", "pe02", "pe03", "pe04", "pe05", "pe06", "pe07", "pe08", "pe09", "pe10", "swpa",
    "swkn", "swqu", "swki", "swac", "sw02", "sw03", "sw04", "sw05", "sw06", "sw07", "sw08", "sw09", "sw10"
]

# mono_deck = ' '.join(' '.join(card) for card in cards)
# cols = 27
# rows = 27
# padded = mono_deck.ljust(cols * rows)[:cols * rows]


# for r in range(rows):
#     print(padded[r * cols:(r + 1) * cols])
    


char_stream = ' '.join((card) for card in cards)

cols = 26


for i in range(0, len(char_stream), cols):
    print(char_stream[i:i+cols])


    
    
# ar01ar02ar03ar04ar05ar06
# ar07ar08ar09ar10ar11ar12
# ar13ar14ar15ar16ar17ar18
# ar19ar20ar00ar21wapawakn
# waquwakiwaacwa02wa03wa04
# wa05wa06wa07wa08wa09wa10
# cupacukncuqucukicuaccu02
# cu03cu04cu05cu06cu07cu08
# cu09cu10pepapeknpequpeki
# peacpe02pe03pe04pe05pe06
# pe07pe08pe09pe10swpaswkn
# swquswkiswacsw02sw03sw04
# sw05sw06sw07sw08sw09sw10


# ar01ar02ar03ar04ar05ar06ar07ar08ar09ar10ar11ar12ar13ar14ar15ar16ar17ar18ar19ar20ar00ar21wapawaknwaquwakiwaacwa02wa03wa04wa05wa06wa07wa08wa09wa10cupacukncuqucukicuaccu02cu03cu04cu05cu06cu07cu08cu09cu10pepapeknpequpekipeacpe02pe03pe04pe05pe06pe07pe08pe09pe10swpaswknswquswkiswacsw02sw03sw04sw05sw06sw07sw08sw09sw10