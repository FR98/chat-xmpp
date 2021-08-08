"""
    Author: Francisco Rosal
"""

from slixmpp import ClientXMPP

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
