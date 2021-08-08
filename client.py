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

    def __init__(self, jid, password, jid_receiver, message):
        # ClientXMPP.__init__(self, jid, password)
        super().__init__(jid, password)
        self.jid = jid
        self.password = password
        self.jid_receiver = jid_receiver
        self.message = message

        self.add_event_handler('session_start', self.start)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()

        self.send_message(mto=self.jid_receiver, mbody=self.message, mtype='chat')
        self.disconnect()

    def register(self):
        # Registrar una nueva cuenta en el servidor
        pass

    def login(self):
        # Iniciar sesión con una cuenta
        pass

    def logout(self):
        # Cerrar sesión con una cuenta
        pass

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
        pass

    def group_chat(self):
        # Participar en conversaciones grupales
        pass

    def set_presence_message(self):
        # Definir mensaje de presencia
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



if __name__ == '__main__':
    client = Client('test@alumchat.xyz', '12345', 'echobot@alumchat.xyz', 'Test message')
    client.register_plugin('xep_0030') # Service Discovery
    client.register_plugin('xep_0199') # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    client.connect()
    client.process(forever=False)
