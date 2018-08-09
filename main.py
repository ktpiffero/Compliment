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
        accomplishments = ["You should be proud of yourself.",
                            "You are making a difference.",
                            "You deserve a hug right now.",
                            "You're a great example to others.",
                            "Actions speak louder than words, and yours tell an incredible story.",
                            "You are a gritty person."]
        
        random_acp = random.choice(accomplishments)
        new_dict = {
            "acc":random_acp,
            
        }
        
        self.response.write(results_template.render(new_dict))
        

class appearance(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/appearance.html')
        appearance = ["Your eyes are breathtaking.",
                      "How is it that you always look so great?",
                      "That color looks great on you.",
                      "You have a beautiful smile."]
        
        random_acp1 = random.choice(appearance)
        new_dict1 = {
            "acc1":random_acp1,
        }
        self.response.write(results_template.render(new_dict1))



class for_her(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/for_her.html')
        for_her = ["You look stunning",
                    "You're beautiful",
                    "You're gorgeous",
                    "You look pretty",
                    "You're awesome",
                    "You look spectacular",
                    "You are amazing"]
    
        random_acp2 = random.choice(for_her)
        new_dict3 = {
            "acc2":random_acp2,
        }
    
        self.response.write(results_template.render(new_dict3))


class for_him(webapp2.RequestHandler):
    def get(self):  
        results_template = the_jinja_env.get_template('templates/for_him.html')
        for_him = ["You are really smart.", 
                    "You're a great listener.",
                    "You're so strong.", 
                    "You are a great brother.",
                    "You are such a hard worker.", 
                    "You are very talented.", 
                    "You're a great friend.", 
                     "You're handsome."]
        
        random_acp3 = random.choice(for_him)
        new_dict4 = {
            "acc3":random_acp3,
            
        }
        
        self.response.write(results_template.render(new_dict4))


class personal_traits(webapp2.RequestHandler):
    def get(self):
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
        
        random_acp4 = random.choice(personal_traits)
        new_dict5 = {
            "acc4":random_acp4
            
        }
        
        self.response.write(results_template.render(new_dict5))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/accomplishments', accomplishments),
    ('/appearance', appearance),
    ('/for_her', for_her),
    ('/for_him', for_him),
    ('/personal_traits', personal_traits),
   
], debug=True)