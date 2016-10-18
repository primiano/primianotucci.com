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
  '^/os/cobalt-raq-panel': 'https://www.sourceforge.net/projects/altcobaltfp/',
  '^/go/about': '/#about',
  '^/go/gallery': '/#photography',
  '^/go/computing': '/#projects',
  '^/go/ip_cores': '/#projects',
  '^/go/electronics': '/#projects',
  '^/go/mechanics': '/#projects',
  '^/go/music': '/#projects',
  '^/go/BestShotsOfLondon': '/#photography',
  '^/go/dizionario': 'https://github.com/primiano/misc/tree/master/yamaha-tt60re-cheat-sheet',
  '^/go/diyspeakers': 'https://www.hackster.io/primiano/my-hifi-diy-amplifier-lm3886-gainclone-3bab33',
  '^/go/diystrat': 'https://www.hackster.io/primiano/my-diy-stratocaster-clone-8135c3',
  '^/go/tt600re': 'https://github.com/primiano/misc/tree/master/yamaha-tt60re-cheat-sheet',
  '^/go/mc35hack': 'https://www.bitleaks.net/blog/siemens-mc35-gsm-modem-hacking/',
  '^/go/diyampli': 'https://www.hackster.io/primiano/my-hifi-diy-amplifier-lm3886-gainclone-3bab33',
  '^/go/mc2': '/os/mc2-multicast-chat',
  '^/go/multimac': '/os/mc2-multicast-chat',
  '^/go/altcobaltfp': '/os/cobalt-raq-panel',
  '^/go/cobaltfp': '/os/cobalt-raq-panel',
  '^/go/netcross': '/os/netcross-ip-over-dns-tunneling',
  '^/go/fourierrocks': 'os/fourier-rocks',
  '^/go/lnlb': '/os/linux-network-load-balancing',
  '^/go/spotlite': '/os/spotlite-desktop-search',
  '^/go/ssg': '/os/ssg-generator',
  '^/go/sasme': '/os/smart-asm-editor',
  '^/go/codek': '/os/codek',
  '^/go/ppgp': '/os/portable-pgp',
  '^/go/jsmartcardexplorer': '/os/smartcard-explorer',
  '^/go/jopenpgpcard': '/os/openpgp-card-driver',
}

class RedirectHandler(webapp2.RequestHandler):
    def get(self, uri):
      for k,v in REDIRECTS_.iteritems():
        m = re.match(k, uri)
        if not m:
          continue
        redirect_url = m.expand(v)
        self.response.set_status(301)
        self.response.headers['Location'] = redirect_url
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(redirect_url)
        return;
      self.response.set_status(404)
      self.response.write('Redirect not found for: ' + uri)


app = webapp2.WSGIApplication([
    ('(.*)', RedirectHandler),
], debug=True)
