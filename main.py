import random

accomplishments = ["You should be proud of yourself.",
                   "You are making a difference.",
                   "You deserve a hug right now.",
                   "You're a great example to others.",
                   "Actions speak louder than words, and yours tell an incredible story."
                   "You are a gritty person"]
                   
print(random.choice(accomplishments))


appearance = ["Your eyes are breathtaking.",
              "How is it that you always look so great?",
              "That color looks great on you.",
              "You have a beautiful smile."]

print(random.choice(appearance))




for_her_noun1 = ["hair", "shirt", "makeup"]
for_her_adj1 = ["great", "nice", "stunning"]

for_her2 = ["stunning",
            "beautiful",
            "gorgeous",
            "pretty",
            "great"]

print("Your " + random.choice(for_her_noun1) + " looks " + random.choice(for_her_adj1) + ".") 


for_him1 = ["smart.", 
           "a great listener.",
           "very strong.", 
           "a great brother.", 
           "a hard worker.", 
           "very talented.", 
           "a great friend.", 
           "handsome."]
print("You're " + for_him1)

for_him2 = ["a great heart.",
            "an awesome personality.",
            "a great personality."
            "a great attitude."
            "a positive personality."
            "a great heart"]

print("You have " + for_him2)

personal_traits = ["You have impeccable manners.",
                   "I like your style.",
                   "You're strong.",
                   "Your kindness is a balm to all who encounter it.",
                   "You are brave.",
                   "You have the courage of your convictions.",
                   "You're a great listener.",
                   "You were cool way before hipsters were cool.",
                   "That thing you don't like about yourself is what makes you really interesting.",
                   "You're inspiring.",
                   "You're so thoughtful."]

print(random.choice(personal_traits))