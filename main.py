import webapp2
import jinja2
import os

env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/start.html")
        self.response.write(template.render())

class RunHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class TJayHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/tjay.html")
        self.response.write(template.render())

class HideHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/hide.html")
        self.response.write(template.render())

class RunFasterHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/runFaster.html")
        self.response.write(template.render())

class EnterHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/enter.html")
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/run', RunHandler),
    ('/tjay', TJayHandler),
    ('/hide', HideHandler),
    ('/runFaster', RunFasterHandler),
    ('/enter', EnterHandler),


], debug = True)
