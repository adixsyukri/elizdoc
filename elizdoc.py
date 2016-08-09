from koslab.messengerbot.bot import BaseMessengerBot

#bot implementation
class ElizDoc(BaseMessengerBot):

    GREETING_TEXT = 'Hi I\'m Eliz, do you suspect to have dengue?'
    STARTUP_MESSAGE = {
            'text':'Do you have sudden high fever?',
            'quick_replies':[
                {
                    'content_type': 'text',
                    'title': 'yes high fever',
                    'payload': 'get_yes_fever'
                },
                {
                    'content_type': 'text',
                    'title': 'no high fever',
                    'payload': 'get_no_fever'
                }
            ] 
    }

    POSTBACK_HANDLERS = {
        'get_yes_fever': 'get_yes_fever',
        'get_no_fever': 'get_no_fever'
    }

    PERSISTENT_MENU = [{
        'type': 'postback',
        'title': 'Start Assessment',
        'payload': 'messengerbot.get_started'
    }]

    def message_hook(self, event):

        session = self.get_session(event)
 
        text = event['message'].get('text','')

        self.send(recipient=event['sender'], message={'text': 'errno'})

    def get_nausea(self, event):
        text = "holly nausea"
        self.send(recipient=event['sender'], message={'text':text})

    def get_headache(self, event):
        text = "shit headache"
        self.send(recipient=event['sender'], message={'text': text})
