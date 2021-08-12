"""
    Author: Francisco Rosal
"""

import logging
from slixmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout


class Client(ClientXMPP):

    """
        XMPP Client
    """

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

        # Registered authenticated menu options
        self.authenticated_options = ["", "Logout", "Chat", "Presence", "List Contacts", "Show Contact", "Add Contact", "Send File", "Destroy Account"]

        # Defining listeners to events
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("register", self.register)
        self.add_event_handler("message", self.receive_message)
        self.add_event_handler("chatstate_active", self.receive_chatstate_active)
        self.add_event_handler("chatstate_inactive", self.receive_chatstate_inactive)
        self.add_event_handler("chatstate_composing", self.receive_chatstate_composing)
        self.add_event_handler("chatstate_paused", self.receive_chatstate_paused)
        self.add_event_handler("chatstate_gone", self.receive_chatstate_gone)


    async def start(self, event):
        # Setting initial presence on login
        self.presence("chat")
        # Getting contacts
        roster = await self.get_roster()
        self.update_contacts(roster)

        while self.authenticated:
            self.authenticated_menu()

            option = input("> ")

            # Execute the selected user option
            if option.replace(" ", "_").lower() == "":
                await self.load()
            elif option.replace(" ", "_").lower() == "send_file":
                await self.send_file()
            elif self.authenticated and option.lower() in [i.lower() for i in self.authenticated_options]:
                exec("self.{}()".format(option.replace(" ", "_").lower()))
                roster = await self.get_roster()
                self.update_contacts(roster)
            else:
                print("Command not found: {}".format(option))


    async def load(self):
        # This methods is useful to load the data
        await self.get_roster()


    def authenticated_menu(self):
        print("=" * 40)
        print("\tAuthenticated Menu:")
        print("-" * 40)
        for option in self.authenticated_options:
            print("· ", option)
        print("=" * 40)


    async def register(self, iq):
        # Register a new user on the server
        resp = self.Iq()
        resp["type"] = "set"
        resp["register"]["username"] = self.boundjid.user
        resp["register"]["password"] = self.password

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
        # List all the contacts
        print("\nCONTACTS:")
        for contact in self.contacts:
            print("· ", contact)
        print("-" * 40)
        print("\n")


    def update_contacts(self, roster):
        # Get the contacts from the roster
        for contact in roster["roster"]["items"].keys():
            if contact not in self.contacts:
                self.contacts.append(contact)


    def add_contact(self):
        # Add contact to my roster
        try:
            contact_jid = input("Contact JID: ")

            # This is actually the add contact to roster
            self.send_presence_subscription(pto = contact_jid)

            # Send friendly message
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


    def show_contact(self):
        # Show contact presence
        self.get_roster()

        contact_jid = input("JID: ")
        print("\n", contact_jid)
        connections = self.client_roster.presence(contact_jid)

        if connections == {}:
            print("No recent session")
        else:
            for device, presence in connections.items():
                print(device, " - ", presence["show"])


    def chat(self):
        # Chat
        try:
            jid_receiver = input("receiver: [testw@alumchat.xyz] ")

            if not jid_receiver:
                jid_receiver = "testw@alumchat.xyz"

            # Set "is typing..." status
            self.send_chat_status(jid_receiver, "composing")

            message = input("message: ")
            self.send_message(mto=jid_receiver, mbody=message, mtype="chat")

            # Remove "is typing..." status
            self.send_chat_status(jid_receiver, "paused")

            logging.info("Message sent.")
        except IqError:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")


    def group_chat(self):
        # Participar en conversaciones grupales
        # TODO
        pass


    def receive_message(self, msg):
        # Get messages and files
        logging.info(msg)
        print("{} > {}".format(str(msg["from"]).split("@")[0], msg["body"]))


    def presence(self, show=None):
        # Set presence messages
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


    def send_chat_status(self, to, state):
        # Send chat state notifications
        try:
            msg = self.Message()
            msg["chat_state"] = state
            msg["to"] = to

            msg.send()
            logging.info("Notification sent!")
        except IqError:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")


    def receive_chatstate_active(self, chatstate):
        # Receive chat state notifications
        logging.info(chatstate)
        print("{} > [{}]".format(str(chatstate["from"]).split("@")[0], "Is active"))


    def receive_chatstate_inactive(self, chatstate):
        # Receive chat state notifications
        logging.info(chatstate)
        print("{} > [{}]".format(str(chatstate["from"]).split("@")[0], "Is inactive"))


    def receive_chatstate_composing(self, chatstate):
        # Receive chat state notifications
        logging.info(chatstate)
        print("{} > [{}]".format(str(chatstate["from"]).split("@")[0], "Is typing..."))


    def receive_chatstate_paused(self, chatstate):
        # Receive chat state notifications
        logging.info(chatstate)
        print("{} > [{}]".format(str(chatstate["from"]).split("@")[0], "Stop typing"))


    def receive_chatstate_gone(self, chatstate):
        # Receive chat state notifications
        logging.info(chatstate)
        print("{} > [{}]".format(str(chatstate["from"]).split("@")[0], "Is gone"))


    async def send_file(self):
        # Send file
        filename = "proyecto1.pdf"
        receiver = "testw@alumchat.xyz"
        # domain = "httpfileupload.alumchat.xyz"
        # domain = "httpfileupload.alumchat.xyz"
        domain = None

        try:
            logging.info("Uploading file %s...", filename)

            url = await self["xep_0363"].upload_file(filename, domain=domain, timeout=10)

            logging.info("Upload success!")
            logging.info("Sending file to %s", receiver)

            html = (
                f"<body xmlns='http://www.w3.org/1999/xhtml'>"
                f"<a href='{url}'>{url}</a></body>"
            )

            message = self.make_message(mto=receiver, mbody=url, mhtml=html)
            message["oob"]["url"] = url
            message.send()
        except IqError as e:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")


    def destroy_account(self):
        # Destroy user account
        try:
            if input("Are you sure you want to delete? [yes/no]: ") == "yes":
                self.register_plugin("xep_0077") # In-band Registration

                resp = self.Iq()
                resp["type"] = "set"
                resp["from"] = self.boundjid.user
                resp["register"]["remove"] = True

                resp.send()
                logging.info("Account deleted succesfully.")
                self.logout()
        except IqError:
            logging.error("Something went wrong.")
        except IqTimeout:
            logging.error("No response from server.")
