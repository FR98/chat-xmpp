"""
    Author: Francisco Rosal
"""

import logging
from client import Client
from argparse import ArgumentParser


# Setup the command line arguments and logging.
parser = ArgumentParser()
parser.add_argument("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
parser.add_argument("-d", "--debug", help="set logging to DEBUG", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
args = parser.parse_args()

logging.basicConfig(level=args.loglevel, format="%(levelname)-8s %(message)s")


# Log methods
# logging.error("Command not found 1")
# logging.warning("Command not found 2")
# logging.critical("Command not found 3")
# logging.debug("Command not found 4")
# logging.exception("Command not found 5")
# logging.info("Command not found 6")




class App(object):

    """
        Main app, this is going to define the behavior since introduce
        the user to the initials options of the menu.
    """

    def __init__(self):
        # Client refers to the xmpp client.
        self.client = None

        self.current_user_jid = None
        self.password = None
        self.running = True

        # Registered options of the menu
        self.unauthenticated_options = ["Close", "Register", "Login"]

        # Executing the app
        self.app()


    def app(self):
        # First interaction with the user. Shows the menu and read the option
        # executing the proper function.
        while self.running:
            self.unauthenticated_menu()

            option = input("> ")

            # Execute the user option
            if option.lower() in [i.lower() for i in self.unauthenticated_options]:
                exec("self.{}()".format(option.lower()))
            else:
                logging.error("Command not found: {}".format(option))


    def unauthenticated_menu(self):
        # Unauthenticated menu
        print("=" * 40)
        print("\tUnauthenticated Menu:")
        print("-" * 40)
        for option in self.unauthenticated_options:
            print("· ", option)
        print("=" * 40)


    def login(self):
        # Use the xmpp client to login the user to the server with the registered plugin
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
        self.client.register_plugin("xep_0004") # Data forms
        self.client.register_plugin("xep_0030") # Service Discovery
        self.client.register_plugin("xep_0045") # Multi-User Chat
        self.client.register_plugin("xep_0066") # Out-of-band Data
        self.client.register_plugin('xep_0071') # XHTML-IM
        self.client.register_plugin("xep_0085") # Chat State Notifications
        self.client.register_plugin('xep_0128') # Service Discovery Extensions
        self.client.register_plugin("xep_0199") # XMPP Ping
        self.client.register_plugin('xep_0363') # HTPP File Upload

        self.client.connect()
        self.client.process()


    def register(self):
        # Use the xmpp client to register a new user to the server with the registered plugin

        if not self.current_user_jid:
            self.current_user_jid = input("jid: [delete18676@alumchat.xyz] ")

        if not self.current_user_jid:
            self.current_user_jid = "delete18676@alumchat.xyz"

        if not self.password:
            self.password = input("password: [123456] ")

        if not self.password:
            self.password = "123456"

        # Connect to the XMPP server and start processing XMPP stanzas.
        self.client = Client(self.current_user_jid, self.password)
        self.client.register_plugin("xep_0004") # Data forms
        self.client.register_plugin("xep_0030") # Service Discovery
        self.client.register_plugin("xep_0045") # Multi-User Chat
        self.client.register_plugin("xep_0066") # Out-of-band Data
        self.client.register_plugin('xep_0071') # XHTML-IM
        self.client.register_plugin("xep_0077") # In-band Registration
        self.client.register_plugin("xep_0085") # Chat State Notifications
        self.client.register_plugin('xep_0128') # Service Discovery Extensions
        self.client.register_plugin("xep_0199") # XMPP Ping
        self.client.register_plugin('xep_0363') # HTPP File Upload

        # Some servers don't advertise support for inband registration, even
        # though they allow it. If this applies to your server, use:
        self.client["xep_0077"].force_registration = True

        self.client.connect()
        self.client.process()


    def close(self):
        self.running = False



if __name__ == "__main__":
    App()
