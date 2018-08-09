import webapp2
import jinja2
import os
import random

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self)
        welcome_template = the_jinja_env.get_template('template/welcome.html')
        
        self.response.write(welcome_template.render())

class accomplishments(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/accomplishments.html')
        accomplishments = [ "You should be proud of yourself.",
                            "You are making a difference.",
                            "You deserve a hug right now.",
                            "You're a great example to others.",
                            "Actions speak louder than words, and yours tell an incredible story.",
                            "You are a gritty person."]
                            
        random_acp = random.choice(accomplishments)
        
        new_dict = {"acc":random_accomplishment

        }
                            
        self.response.write(results_template.render(random.choice(random_acp)))
             
class appearance(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/appearance.html')
        appearance = ["Your eyes are breathtaking.",
                      "How is it that you always look so great?",
                      "That color looks great on you.",
                      "You have a beautiful smile."]
         
        random_appearance = random.choice(appearance)
        
        new_dict = {"appearance":random_appearance
        
        }
        self.response.write(results_template.render(random.choice(appearance)))


class for_her2(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/for_her2.html')
        for_her2 = ["You look stunning",
                    "You're beautiful",
                    "You're gorgeous",
                    "You look pretty",
                    "You're awesome",
                    "You look spectacular",
                    "You are amazing"
                    
        ]
        
        random_for_her2 = random.choice(for_her2)
        
        new_dict = {"for_her":for_her}
        self.response.write(results_template.render(for_her))

class for_him(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/for_him.html')
        for_him =  ["You are really smart.", 
           "You're a great listener.",
           "You're so strong.", 
           "You are a great brother.",
           "You are such a hard worker.", 
           "You are very talented.", 
           "You're a great friend.", 
           "You're handsome."]
           
        random_for_him = random.choice(for_him)
        
        new_dict = {"for_him":random_for_him}
        
        self.response.write(str(results_template.render(random.choice(for_him)))

class personal_traits(webapp2.RequestHandler):
    def get(self):  # for a get request
        results_template = the_jinja_env.get_template('templates/personal_traits.html')
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
        
         random_pt = random.choice(personal_traits)
        
        new_dict = {"random_pt":random_personal_traits}
        self.response.write(results_template.render(personal_traits))



app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler)
    ('/personal_traits', personal_traits),
    ('/accomplishments', accomplishments),
    ('/appearance', appearance,
    ('/for_him', for_him),
    ('/for_her', for_her),
   
], debug=True)