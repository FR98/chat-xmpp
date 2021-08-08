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
        self.authenticated = False

        self.authenticated_options = ["Logout"]
        self.unauthenticated_options = ["Close", "Register", "Login"]

        self.app()


    def app(self):
        while self.running:
            if self.authenticated:
                self.authenticated_menu()
            else:
                self.unauthenticated_menu()

            option = input("> ")

            if not self.authenticated and option.lower() in [i.lower() for i in self.unauthenticated_options]:
                exec("self.{}()".format(option.lower()))
            elif self.authenticated and option.lower() in [i.lower() for i in self.authenticated_options]:
                exec("self.{}()".format(option.lower()))
            else:
                log.error("Command not found: {}".format(option))


    def unauthenticated_menu(self):
        print("=" * 20)
        print("\tMenu:")
        print("-" * 20)
        for option in self.unauthenticated_options:
            print("· ", option)
        print("=" * 20)


    def authenticated_menu(self):
        print("=" * 20)
        print("\tMenu:")
        print("-" * 20)
        for option in self.authenticated_options:
            print("· ", option)
        print("=" * 20)


    async def start(self, event):
        # await self.get_roster()
        # self.private_chat()
        pass


    def register(self):
        # Registrar una nueva cuenta en el servidor
        pass


    def login(self):
        # Iniciar sesión con una cuenta
        if not self.current_user_jid:
            self.current_user_jid = input("jid: [test@alumchat.xyz] ")

        if not self.current_user_jid:
            self.current_user_jid = "test@alumchat.xyz"
        
        if not self.password:
            self.password = input("password: [12345] ")

        if not self.password:
            self.password = "12345"

        # Connect to the XMPP server and start processing XMPP stanzas.
        self.client = Client(self.current_user_jid, self.password)
        self.client.register_plugin("xep_0030") # Service Discovery
        self.client.register_plugin("xep_0199") # XMPP Ping
        self.client.connect()
        self.client.process(forever=False)
        self.authenticated = True


    def logout(self):
        # Cerrar sesión con una cuenta
        self.authenticated = False
        self.client.disconnect()


    def close(self):
        self.running = False


    def destroy_account(self):
        # Eliminar la cuenta del servidor
        pass


    def list_users(self):
        # Mostrar todos los usuarios y su estado
        pass


    def list_contacts(self):
        # Mostrar todos los contactos y su estado
        pass


    def add_user_to_contacts(self):
        # Agregar un usuario a los contactos
        pass


    def show_user_detail(self):
        # Mostrar detalles de contacto de un usuario
        pass


    def private_chat(self):
        # Comunicación 1 a 1 con cualquier usuario/contacto
        receiver_jid = "echobot@alumchat.xyz"
        message = input("Message")
        # self.send_message(mto=receiver_jid, mbody=message, mtype="chat")
        pass


    def group_chat(self):
        # Participar en conversaciones grupales
        pass


    def set_presence_message(self):
        # Definir mensaje de presencia
        # self.send_presence()
        pass


    def send_notifications(self):
        # Enviar/recibir notificaciones
        pass


    def receive_notifications(self):
        # Recibir notificaciones
        pass


    def send_files(self):
        # Enviar/recibir archivos
        pass


    def receive_files(self):
        # Recibir archivos
        pass



if __name__ == "__main__":
    App()
