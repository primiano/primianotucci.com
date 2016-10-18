import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self, challenge):
        app = webapp2.get_app()
        response = app.registry.get(challenge)
        if not response:
          self.response.set_status(404)
          return
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(response)

    def post(self, challenge):
        self.response.headers['Content-Type'] = 'text/plain'
        app = webapp2.get_app()
        app.registry[challenge] = self.request.body
        self.response.write('OK')

app = webapp2.WSGIApplication([
    ('/.well-known/acme-challenge/(.*)', MainPage),
], debug=True)
