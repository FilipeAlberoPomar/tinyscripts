import requests, simplejson, operator

class School:
    def __init__(self, name, postcode, type):
        self.name = name
        self.postcode = postcode
        self.type = type

primary_schools = []
secondary_schools = []

primary_schools.append(School("Holy Family", "W3 0DY", "primary"))
primary_schools.append(School("Larmenier & Sacred Heart", "W6 7BL", "primary"))
primary_schools.append(School("Oratory", "SW3 6QH", "primary"))
primary_schools.append(School("Our Lady of Lourdes", "N12 0JP", "primary"))
primary_schools.append(School("Our Lady of Muswell", "N10 1PS", "primary"))
primary_schools.append(School("Our Lady of Victories", "SW7 5AQ", "primary"))
primary_schools.append(School("Sacred Heart", "HA4 6EZ", "primary"))
primary_schools.append(School("St Agnes", "E3 3ER", "primary"))
primary_schools.append(School("St Anselm's", "HA1 3BE", "primary"))
primary_schools.append(School("St Anthony's", "WD18 6BW", "primary"))
primary_schools.append(School("St Augustine's", "W6 8QE", "primary"))
primary_schools.append(School("St Catherine's", "EN5 2ED", "primary"))
primary_schools.append(School("St Dominic", "AL5 1PF", "primary"))
primary_schools.append(School("St Eugene de Mazenod", "NW6 4LS", "primary"))
primary_schools.append(School("St George's", "EN2 0QA", "primary"))
primary_schools.append(School("St James's", "TW2 5NP", "primary"))
primary_schools.append(School("St John Fisher", "HA5 5RA", "primary"))
primary_schools.append(School("St John XXIII", "W12 7QT", "primary"))
primary_schools.append(School("St Joseph's", "CM23 2NL", "primary"))
primary_schools.append(School("St Josephs", "WC2B 5NA", "primary"))
primary_schools.append(School("St Joseph", "WD19 7DW", "primary"))
primary_schools.append(School("St Joseph's ", "NW10 9LS", "primary"))
primary_schools.append(School("St Joseph's", "N19 5NE", "primary"))
primary_schools.append(School("St Joseph's", "SW3 2QT", "primary"))
primary_schools.append(School("St Joseph's", "HA3 7LP", "primary"))
primary_schools.append(School("St Margaret Clitherow", "SG2 8QJ", "primary"))
primary_schools.append(School("St Mary's", "UB8 2UA", "primary"))
primary_schools.append(School("St Mary", "SG8 7DB", "primary"))
primary_schools.append(School("St Michael", "TW15 2DG ", "primary"))
primary_schools.append(School("St Richard Reynolds", "TW1 4LT", "primary"))
primary_schools.append(School("St Swithun Wells", "HA4 9HS", "primary"))
primary_schools.append(School("St Thomas of Canterbury", "SG11 1RZ", "primary"))
primary_schools.append(School("St Vincent's", "W1U 4DF", "primary"))
primary_schools.append(School("St Vincent's", "NW7 1EJ", "primary"))
primary_schools.append(School("Good Shepherd", "W12 9BY", "primary"))
primary_schools.append(School("Holy Rood", "WD17 4FS", "primary"))
primary_schools.append(School("St Thomas More", "HP4 3LF", "primary"))
primary_schools.append(School("Servite", "SW10 9NA", "primary"))

secondary_schools.append(School("Bishop Challoner (girls)", "E1 0LB", "secondary"))
secondary_schools.append(School("Sacred Heart", "W6 7DG", "secondary"))
secondary_schools.append(School("St Anne's (Girls)", "N13 5TY", "secondary"))
secondary_schools.append(School("St George's", "W9 1RB", "secondary"))
secondary_schools.append(School("St Mary's", "CM23 2NQ", "secondary"))
secondary_schools.append(School("St Michael's (Grammar)", "N12 7NJ", "secondary"))
secondary_schools.append(School("Saint Michael's", "WD25 0SS ", "secondary"))
secondary_schools.append(School("St Thomas More", "N22 5HN", "secondary"))

distances = dict()

for primary in primary_schools:
    for secondary in secondary_schools:
        print(primary.name + " > " + secondary.name)
        # Brace! Brace! Google Maps now needs an API key to work. This needs tweaking.
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&mode=walking&origins=%s&destinations=%s" % (primary.postcode, secondary.postcode)
        json = simplejson.loads(requests.get(url).content)
        meters = json['rows'][0]["elements"][0]["distance"]["value"]
        schools = primary.name + " (" + primary.postcode + ") > " +secondary.name + " (" + secondary.postcode +")"
        distances[schools] = meters

sorted_distances = sorted(distances.items(), key=operator.itemgetter(1))

for entry in sorted_distances:
    print(entry)