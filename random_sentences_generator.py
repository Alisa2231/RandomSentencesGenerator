import random


def random_word(list_of_words: list):
    return random.choice(list_of_words)


names = ["Asya", "Preslav", "Elizabeth", "Todor", "Rosen", "Navdeep", "Rafael", "Sergio", "Ewald", \
         "Felix", "Catalin", "Stefan", "Metodi", "Victoria", "Laurence", "Paola", \
         "Gabriela", "Judith", "Deborah", "Brenda", "Leonid", "Cristina", "Marcio", "Miguel", "Mariana", \
         "Anna", "Rita", "Antonio", "Jennifer", "Naomi", "Rachel", "Monika"]
places = ["Sofia", "London", "Madrid", "Barcelona", "Lisbon", "Porto", "Aveiro", "Berlin", \
          "Bucharest", "Paris", "San Jose", "Grenoble", "New Zealand", "Dominican Republic", "Nessebar", \
          "Brazil", "Japan", "Portugal", "Australia", "Vienna", "Valencia", "UK"]
adverbs = ["slowly", "quickly", "gently", "warmly", "sadly", "happily", "thoroughly", "carefully", \
           "calmly", "freely", "strongly", "passionately", "positively", "intentionally", \
           "unintentionally", "fairly", "rapidly", "bravely", "unexpectedly", "suddenly", \
           "carefully", "loudly", "silently", "accidentally", "kindly", "softly"]
verbs = ["eats", "sees", "holds", "plays with", "brings", "takes", "loves", "likes", "puts", \
         "sells", "drinks", "buys", "wants", "knows", "gets", "gives", "thinks of", "cooks", "hugs", \
         "builds", "plays with", "draws", "invents", "assembles", "analyzes", "creates", "fixes", "repairs"]
nouns = ["tree", "eggs", "coffee", "beer", "wine", "cat", "dog", "drinks", "laptop", "headset", "chips", \
         "bird", "animal", "cinnamon gum", "dress", "bag", "steak", "tea", "truck", "juice", "table", \
         "window", "wall", "computer", "server", "book", "car", "train", "bus", "airplane"]
details = ["near the river", "at home", "in the park", "at work", "in the air", "on the bus", \
           "in the car", "on the plane", "with friends", "with love", "upstairs", "downstairs", \
           "outside", "inside", "with care", "tonight", "today", "in the morning", "alone", "constantly", \
           "regularly", "weekly", "daily", "annually", "in the office"]

command = input("Hit enter to generate a random sentence or any other key to quit: ")
while command == "":
    name = random_word(names)
    place = random_word(places)
    adverb = random_word(adverbs)
    verb = random_word(verbs)
    noun = random_word(nouns)
    detail = random_word(details)
    random_sentence = f"{name} from {place} {adverb} {verb} {noun} {detail}."
    print(random_sentence)
    command = input("Hit enter to generate a random sentence or any other key to quit: ")

print("Goodbye!")
