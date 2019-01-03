from random import sample

decks_base = ['пираты', 'зомби', 'роботы', 'маги', 'динозавры', 'ниндзя', 'лепреконы', 'пришельцы']
decks_ktulhu = ['старцы', 'учёные', 'ктулху', 'местные']
decks_plants = ['растения', 'медведи', 'механики', 'призраки']
decks_mimimi = ['принцессы' ,'котики', 'феи', 'пони']
decks = decks_base + decks_ktulhu + decks_plants + decks_mimimi
chosen = sample(decks, 4)
#print("Ваня: " + chosen[0] + "-" + chosen[1] + "; Лера: " + chosen[2] + "-" + chosen[3])

chosen = sample(decks_ktulhu + decks_plants + decks_base, 2)
chosen_mimimi = sample(decks_mimimi, 2)
print("Ваня: " + chosen[0] + "-" + chosen_mimimi[0] + "; Лера: " + chosen[1] + "-" + chosen_mimimi[1])
