"""
    Author: Francisco Rosal
"""

import logging

from slixmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout

class Client(ClientXMPP):

    def __init__(self, jid, password):
        super().__init__(jid, password)
        # self.jid = jid
        self.password = password

        self.authenticated = True
        self.authenticated_options = ["Logout",  "Chat", "Presence"]

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("register", self.register)
        # Event triggered: connected


    # def start(self, event):
    async def start(self, event):
        self.presence('chat')
        # self.get_roster()
        await self.get_roster()

        while self.authenticated:
            self.authenticated_menu()

            option = input("> ")

            if self.authenticated and option.lower() in [i.lower() for i in self.authenticated_options]:
                exec("self.{}()".format(option.lower()))
                await self.get_roster()
            else:
                print("Command not found: {}".format(option))


    def authenticated_menu(self):
        print("=" * 20)
        print("\tAuthenticated Menu:")
        print("-" * 20)
        for option in self.authenticated_options:
            print("· ", option)
        print("=" * 20)


    async def register(self, iq):
        # Registrar una nueva cuenta en el servidor
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            await resp.send()
            logging.info("Account created for %s!" % self.boundjid)
        except IqError as e:
            logging.error("Could not register account: %s" %
                    e.iq['error']['text'])
            self.disconnect()
        except IqTimeout:
            logging.error("No response from server.")
            self.disconnect()


    def logout(self):
        self.authenticated = False
        self.disconnect()


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


    def chat(self):
        # Comunicación 1 a 1 con cualquier usuario/contacto
        jid_receiver = input("receiver: [testw@alumchat.xyz] ")

        if not jid_receiver:
            jid_receiver = "testw@alumchat.xyz"

        message = input("message: ")

        self.send_message(mto=jid_receiver, mbody=message, mtype="chat")


    def group_chat(self):
        # Participar en conversaciones grupales
        pass


    def presence(self, show=None):
        # Definir mensaje de presencia
        if not show:
            show = input("show: [chat, away, xa, dnd, custom] ")

        if show not in ["chat", "away", "xa", "dnd", "custom"]:
            show = "chat"

        if show == "chat":
            status = "Available"
        elif show == "away":
            status = "Unavailable"
        elif show == "xa":
            status = "Bye"
        elif show == "dnd":
            status = "Do not Disturb"
        elif show == "custom":
            show = input("show: ")
            status = input("status: ")

        if show not in ["chat", "away", "xa", "dnd"]:
            show = "chat"
            status = "Available"

        self.send_presence(pshow=show, pstatus=status)


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
