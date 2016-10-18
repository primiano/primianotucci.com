import re
import webapp2

REDIRECTS_ = {
  '^/blog/(.*)': r'https://www.bitleaks.net/blog/\1/',
  '^/os/portable-pgp': 'http://ppgp.sourceforge.net/',
  '^/os/smartcard-explorer': 'https://www.sourceforge.net/projects/jsmartcard/',
  '^/os/wake-my-subnet': 'https://github.com/primiano/wake-my-subnet',
  '^/os/openpgp-card-driver': 'https://www.sourceforge.net/projects/jopenpgpcard/',
  '^/os/fourier-rocks': 'https://www.sourceforge.net/projects/fourierrocks/',
  '^/os/netcross-ip-over-dns-tunneling': 'https://www.sourceforge.net/projects/netcross/',
  '^/os/linux-network-load-balancing': 'http://lnlb.sourceforge.net/',
  '^/os/mc2-multicast-chat': 'https://www.sourceforge.net/projects/mc2/',
  '^/os/ssg-generator': 'https://www.sourceforge.net/projects/ssg-generator/',
  '^/os/smart-asm-editor': 'https://www.sourceforge.net/projects/sasme/',
  '^/os/codek': 'https://www.sourceforge.net/projects/codek/',
  '^/os/spotlite-desktop-search': 'https://www.sourceforge.net/projects/spotlite/',
  '^/os/tetris-vhdl': 'https://github.com/primiano/tetris-vhdl',
  '^/os/lgtm-hid ': 'https://github.com/primiano/lgtm-hid',
  '^/os/i2s-to-parallel': 'http://opencores.org/project,i2s_to_parallel',
  '/os/cobalt-raq-panel': 'https://www.sourceforge.net/projects/altcobaltfp/',

}

class RedirectHandler(webapp2.RequestHandler):
    def get(self, uri):
      for k,v in REDIRECTS_.itervalues():
        m = re.match(k, uri)
        if not m:
          continue
        redirect_url = m.expand(v)
        self.response.set_status(301)
        self.response.headers['Location'] = redirect_url
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(redirect_url)
        return;
      self.response.set_status(200)
      self.response.write('Redirect not found for: ' + redirect_url)


app = webapp2.WSGIApplication([
    ('(.*)', RedirectHandler),
], debug=True)
