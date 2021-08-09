"""
    Author: Francisco Rosal
"""

import logging

from slixmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout

class Client(ClientXMPP):

    def __init__(self, jid, password):
        try:
            super().__init__(jid, password)
        except IqError:
            logging.error("Something went wrong.")
            self.logout()
        except IqTimeout:
            logging.error("No response from server.")
            self.logout()

        self.password = password

        self.contacts = []

        self.authenticated = True
        self.authenticated_options = ["Logout",  "Chat", "Presence", "List Contacts", "Add Contact"]

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("register", self.register)


    async def start(self, event):
        self.presence('chat')
        roster = await self.get_roster()
        self.update_contacts(roster)

        while self.authenticated:
            self.authenticated_menu()

            option = input("> ")

            if self.authenticated and option.lower() in [i.lower() for i in self.authenticated_options]:
                exec("self.{}()".format(option.replace(" ", "_").lower()))
                roster = await self.get_roster()
                self.update_contacts(roster)
            else:
                print("Command not found: {}".format(option))


    def authenticated_menu(self):
        print("=" * 25)
        print("\tAuthenticated Menu:")
        print("-" * 25)
        for option in self.authenticated_options:
            print("· ", option)
        print("=" * 25)


    async def register(self, iq):
        # Registrar una nueva cuenta en el servidor
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            await resp.send()
            logging.info("Account created for %s!" % self.boundjid)
        except IqError:
            logging.error("Something went wrong.")
            self.logout()
        except IqTimeout:
            logging.error("No response from server.")
            self.logout()


    def logout(self):
        self.authenticated = False
        self.disconnect()


    def list_contacts(self):
        # Mostrar todos los contactos y su estado
        # TODO: Falta mostrar su estado
        print("\n\nCONTACTS:")
        for contact in self.contacts:
            print("· ", contact)
        print("-" * 25)
        print("\n\n")


    def update_contacts(self, roster):
        for contact in roster['roster']['items'].keys():
            if contact not in self.contacts:
                self.contacts.append(contact)


    def add_contact(self):
        # Agregar un usuario a los contactos
        try:
            contact_jid = input("Contact JID: ")

            self.send_presence_subscription(pto = contact_jid)

            self.send_message(
                mto = contact_jid,
                mbody = "Hi! I added you to my roster",
                mtype = "chat",
                mfrom = self.boundjid.bare
            )

        except IqError:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")


    def list_users(self):
        # Mostrar todos los usuarios y su estado
        # TODO
        pass


    def show_user(self):
        # Mostrar detalles de contacto de un usuario
        # TODO
        pass


    def chat(self):
        # Comunicación 1 a 1 con cualquier usuario/contacto
        try:
            jid_receiver = input("receiver: [testw@alumchat.xyz] ")

            if not jid_receiver:
                jid_receiver = "testw@alumchat.xyz"

            message = input("message: ")

            self.send_message(mto=jid_receiver, mbody=message, mtype="chat")

            logging.info("Message sent.")
        except IqError:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")


    def group_chat(self):
        # Participar en conversaciones grupales
        # TODO
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

        try:
            self.send_presence(pshow=show, pstatus=status)
            logging.info("Presence setted.")
        except IqError:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")


    def send_notifications(self):
        # Enviar/recibir notificaciones
        # TODO
        pass


    def receive_notifications(self):
        # Recibir notificaciones
        # TODO
        pass


    def send_files(self):
        # Enviar/recibir archivos
        # TODO
        pass


    def receive_files(self):
        # Recibir archivos
        # TODO
        pass


    def destroy_account(self):
        # Eliminar la cuenta del servidor
        # TODO
        pass
