from koslab.messengerbot.bot import BaseMessengerBot

#bot implementation
class ElizDoc(BaseMessengerBot):

    GREETING_TEXT = 'Hi I\'m Eliz, I\'ll be assessing your health today!'
    STARTUP_MESSAGE = {'text':'Point me to your symptom'}

    PERSISTENT_MENU = [{
        'type': 'postback',
        'title': 'Start Assessment',
        'payload': 'messengerbot.get_started'
    }]

    def message_hook(self, event):
        text = event['message'].get('text', '')
        if text.upper() == 'headache'.upper():
            self.send(recipient=event['sender'], message={'text': 'http://google.com/headache'})
        elif text.upper() == 'nausea'.upper():
            self.send(recipient=event['sender'], message={'text': 'http://google.com/nausea'})
        else:
            self.send(recipient=event['sender'], message={'text': 'errno'})

