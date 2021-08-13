# XMPP Chat
## UVG Redes Proyecto 1 - XMPP
---

This project is a chat client that implements the XMPP Protocol. This client is based on the python library [slixmpp](https://slixmpp.readthedocs.io/en/latest/). Consist of two files, app.py, which is the main file and is in charge of showing the unauthenticated menu options to the user; and client.py, which is the XMPP Client custom implementation. The client make use of the following XEP Plugins:

- [XEP-0004 - Data forms](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0004.html)
- [XEP-0030 - Service Discovery](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0030.html)
- [XEP-0066 - Out-of-band Data](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0066.html)
- [XEP-0071 - XHTML-IM](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0071.html)
- [XEP-0077 - In-band Registration](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0077.html)
- [XEP-0085 - Chat State Notifications](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0085.html)
- [XEP-0128 - Service Discovery Extensions](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0128.html)
- [XEP-0199 - XMPP Ping](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0199.html)
- [XEP-0363 - HTPP File Upload](https://slixmpp.readthedocs.io/en/latest/api/plugins/xep_0363.html)


## Specifications and Features of the Client
---
### The client has the following event listeners:
---
- Event: session_start
    - This event is triggered when the client is connected and the user is logged in.

- Event: register
    - This event is triggered when the user is on registration process.

- Event: message
    - This event is triggered when the user receive a message of any type.

- Event: chatstate_active
    - This event is triggered when some user that we are chatting with set its chat state as active.

- Event: chatstate_inactive
    - This event is triggered when some user that we are chatting with set its chat state as inactive.

- Event: chatstate_composing
    - This event is triggered when some user that we are chatting with set its chat state as composing.

- Event: chatstate_paused
    - This event is triggered when some user that we are chatting with set its chat state as paused.

- Event: chatstate_gone
    - This event is triggered when some user that we are chatting with set its chat state as gone.


### Client class methods
---
- init: class initializer, loads the event handlers.
- start: set initial presence status, update the user contacts, and show the menu options.
- load: update the state of the client, is usefull to know is there is new messages.
- authenticated_menu: print the menu.
- register: send the xmpp petition to register a new user.
- logout: disconnect the client and ends the authenticated flow.
- list_contacts: list all the user contacts.
- update_contacts: temporaly store of the user contacts extracted from the roster
- add_contacts: add a user to my roster (contact list)
- show_contact: show info of a specific contact
- chat: send a message to a specific user
- group_chat: send a message to a group chat
- receive_message: get the messages and files received
- presence: set and send presence
- send_chat_status: send chat status
- receive_chatstate_active: receive chat state active
- receive_chatstate_inactive: receive chat state inactive
- receive_chatstate_composing: receive chat state composing
- receive_chatstate_paused: receive chat state paused
- receive_chatstate_gone: receive chat state gone
- send_file: upload and send a file
- destroy_account: destroy the current user account on the server


## How to install and use
---
### How to install
---
    * Important: USE PYTHON 3.7
    pip3 install -r requirements.txt
    python app.py -q

### How to use
---
Available menu options:
- Registration
- Login
- Logout
- Chat
- Presence
- List Contacts
- Show Contact
- Add Contanct
- Send File
- Destroy Account


- Características implementadas
- Dificultades
- Lecciones aprendidas
- Video max 5 minutos

