import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self): 
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        
        self.response.write(welcome_template.render())



class accomplishments(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/accomplishments.html')
        accomplishments = { "accomplishment1":"You should be proud of yourself.",
                            "accomplishment2":"You are making a difference.",
                            "accomplishment3":"You deserve a hug right now.",
                            "accomplishment4":"You're a great example to others.",
                            "accomolishment5":"Actions speak louder than words, and yours tell an incredible story.",
                            "accomolishment6":"You are a gritty person."}
        self.response.write(results_template.render(accomplishments))
              

class appearance(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/appearance.html')
        appearance = {"appearance1":"Your eyes are breathtaking.",
                      "appearance2":"How is it that you always look so great?",
                      "appearance3":"That color looks great on you.",
                      "appearance4":"You have a beautiful smile."}
        self.response.write(results_template.render(appearance))


for_her_noun1 = ["hair", "shirt", "makeup"]
for_her_adj1 = ["great", "nice", "stunning"]

class for_her2(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/for_her2.html')
        for_her2 = {"for_her1":"stunning",
                    "for_her2":"beautiful",
                    "for_her3":"gorgeous",
                    "for_her4":"pretty",
                    "for_her5":"great",
                    "for_her6":"spectacular",
                    "for_her7":"amazing"
                    
        }
        self.response.write("You look " + results_template.render(for_her))

class for_him(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/for_him.html')
        for_him =  {"for_him1":"smart.", 
           "for_him2":"a great listener.",
           "for_him3":"very strong.", 
           "for_him4":"a great brother.", 
           "for_him5":"a hard worker.", 
           "for_him6":"very talented.", 
           "for_him7":"a great friend.", 
           "for_him8":"handsome."
            
        }
        self.response.write("You're " +  str(results_template.render(random.choice(for_him))))

class personal_traits(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/personal_traits.html')
        personal_traits = {"trait1":"You have impeccable manners.",
                             "trait2":"I like your style.",
                             "trait3":"You're strong.",
                             "trait4":"Your kindness is a balm to all who encounter it.",
                             "trait5":"You are brave.",
                             "trait6":"You have the courage of your convictions.",
                             "trait7":"You're a great listener.",
                             "trait8":"You were cool way before hipsters were cool.",
                             "trait9":"That thing you don't like about yourself is what makes you really interesting.",
                             "trait10":"You're inspiring.",
                             "trait11":"You're so thoughtful."}
        self.response.write(results_template.render(personal_traits))
        self.response.write("personal_traits handled request")

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/accomplishments', accomplishments),
    ('/appearance', appearance),
    ('/for_her', for_her2),
    ('/for_him', for_him),
    ('/personal_traits', personal_traits),
   
], debug=True)