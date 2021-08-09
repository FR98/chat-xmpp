"""
    Author: Francisco Rosal
"""

import logging
from argparse import ArgumentParser

from client import Client

# Setup the command line arguments and logging.
parser = ArgumentParser()
parser.add_argument("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
parser.add_argument("-d", "--debug", help="set logging to DEBUG", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
args = parser.parse_args()

# logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")
logging.basicConfig(level=args.loglevel, format="%(levelname)-8s %(message)s")
log = logging.getLogger(__name__)
# log.error("Command not found 1")
# log.warning("Command not found 2")
# log.critical("Command not found 3")
# log.debug("Command not found 4")
# log.exception("Command not found 5")
# log.info("Command not found 6")





class App(object):

    def __init__(self):
        self.client = None
        self.current_user_jid = None
        self.password = None
        self.running = True
        self.unauthenticated_options = ["Close", "Register", "Login"]

        self.app()


    def app(self):
        while self.running:
            self.unauthenticated_menu()

            option = input("> ")

            if option.lower() in [i.lower() for i in self.unauthenticated_options]:
                exec("self.{}()".format(option.lower()))
            else:
                log.error("Command not found: {}".format(option))


    def unauthenticated_menu(self):
        print("=" * 20)
        print("\tUnauthenticated Menu:")
        print("-" * 20)
        for option in self.unauthenticated_options:
            print("· ", option)
        print("=" * 20)


    def login(self):
        # Iniciar sesión con una cuenta
        if not self.current_user_jid:
            self.current_user_jid = input("jid: [ros18676@alumchat.xyz] ")

        if not self.current_user_jid:
            self.current_user_jid = "ros18676@alumchat.xyz"

        if not self.password:
            self.password = input("password: [123456] ")

        if not self.password:
            self.password = "123456"

        # Connect to the XMPP server and start processing XMPP stanzas.
        self.client = Client(self.current_user_jid, self.password)
        self.client.register_plugin("xep_0030") # Service Discovery
        self.client.register_plugin("xep_0199") # XMPP Ping

        self.client.connect()
        self.client.process()


    def register(self):
        # Iniciar sesión con una cuenta
        if not self.current_user_jid:
            self.current_user_jid = input("jid: [ros18676@alumchat.xyz] ")

        if not self.current_user_jid:
            self.current_user_jid = "ros18676@alumchat.xyz"

        if not self.password:
            self.password = input("password: [123456] ")

        if not self.password:
            self.password = "123456"

        # Connect to the XMPP server and start processing XMPP stanzas.
        self.client = Client(self.current_user_jid, self.password)
        self.client.register_plugin("xep_0030") # Service Discovery
        self.client.register_plugin("xep_0004") # Data forms
        self.client.register_plugin("xep_0199") # XMPP Ping
        self.client.register_plugin("xep_0066") # Out-of-band Data
        self.client.register_plugin("xep_0077") # In-band Registration

        # Some servers don't advertise support for inband registration, even
        # though they allow it. If this applies to your server, use:
        self.client["xep_0077"].force_registration = True

        self.client.connect()
        self.client.process()


    def close(self):
        self.running = False



if __name__ == "__main__":
    App()
