"""
    Author: Francisco Rosal
"""

import logging
from argparse import ArgumentParser

from slixmpp import ClientXMPP

# Setup the command line arguments and logging.
parser = ArgumentParser()
parser.add_argument("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
parser.add_argument("-d", "--debug", help="set logging to DEBUG", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
args = parser.parse_args()

# logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')
logging.basicConfig(level=args.loglevel, format='%(levelname)-8s %(message)s')
# log = logging.getLogger(__name__)
# log.warning('You should catch IqTimeout exceptions')





class Client(ClientXMPP):

    def __init__(self):
        self.jid = None
        self.password = None
        self.running = True
        self.authenticated = False

        client.register_plugin('xep_0030') # Service Discovery
        client.register_plugin('xep_0199') # XMPP Ping

    def app(self):
        while self.running:
            if self.authenticated:
                self.unauthenticated_menu()
            else:
                self.authenticated_menu()

            input("NEXT")

    def unauthenticated_menu(self):
        print("""
-----------------
        Menu:
    1. Register
    2. Login
-----------------
        """)

    def authenticated_menu(self):
        print("""
-----------------
        Menu:
    1. Logout
-----------------
        """)

    async def start(self, event):
        await self.get_roster()
        self.private_chat()

    def register(self):
        # Registrar una nueva cuenta en el servidor
        pass

    def login(self):
        # Iniciar sesión con una cuenta
        self.jid = 'test@alumchat.xyz'
        self.password = '12345'

        super().__init__(self.jid, self.password)
        client.connect()
        client.process(forever=False)

        self.add_event_handler('session_start', self.start)

    def logout(self):
        # Cerrar sesión con una cuenta
        self.disconnect()

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
        receiver_jid = 'echobot@alumchat.xyz'
        message = input("Message")
        self.send_message(mto=receiver_jid, mbody=message, mtype='chat')
        pass

    def group_chat(self):
        # Participar en conversaciones grupales
        pass

    def set_presence_message(self):
        # Definir mensaje de presencia
        self.send_presence()

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



if __name__ == '__main__':
    client = Client()
