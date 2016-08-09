from koslab.messengerbot.bot import BaseMessengerBot

#bot implementation
class ElizDoc(BaseMessengerBot):

    GREETING_TEXT = 'Hi I\'m Eliz, do you suspect to have dengue?'
    STARTUP_MESSAGE = {
            'text':'Do you have sudden high fever?',
            'quick_replies':[
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'get_fever'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'get_fever'
                }
            ] 
    }

    POSTBACK_HANDLERS = {
        'get_fever': 'get_fever',
    }

    PERSISTENT_MENU = [{
        'type': 'postback',
        'title': 'Start Assessment',
        'payload': 'messengerbot.get_started'
    }]

    def get_fever(self, event):
        print event['message'].get('text','')

    """
    def set_fever(self, event, text, session):
        if 'yes' in text:
            session.set('fever','true')
        else:
            session.set('fever','false')
        
        headache = { 
            'text':'Do you have severe headaches?',
            'quick_replies':[ 
                {
                    'content_type': 'text',
                    'title': 'yes severe headache',
                    'payload': 'get_severe_headache'
                },
                {
                    'content_type': 'text',
                    'title': 'no headache',
                    'payload': 'get_no_headache'
                }
            ]
        }
        self.send(recipient=event['sender'], message=headache)
     
    def set_headache(self, event, text, session):
        if 'yes' in text:
            session.set('headache','true')
        else:
            session.set('headache','false')

        eyes = {
            'text':'Pain behind the eyes?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes eyes pain',
                    'payload': 'get_eyes_pain'
                },
                {
                    'content_type': 'text',
                    'title': 'no eyes pain',
                    'payload': 'get_no_pain'
                }
            ]
        }
            
        self.send(recipient=event['sender'], message=eyes)

    def set_eyes(self, event, text, session):
        if 'yes' in text:
            session.set('eyes','true')
        else:
            session.set('eyes','false')
        
        joint_muscle = {
            'text':'Experiencing severe joint and muscle pain?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes joint and muscle pain',
                    'payload': 'get_yes_joint_muscle'
                },
                {
                    'content_type': 'text',
                    'title': 'no joint and muscle pain',
                    'payload': 'get_no_joint_muscle'
                }
            ]
        }      
            
        self.send(recipient=event['sender'], message=joint_muscle)

    def set_joint_muscle(self, event, text, session):
        if 'yes' in text:
            session.set('muscle','true')
        else:
            session.set('muscle','false')
            
        fatigue = {
            'text':'Do you feel fatigue?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes fatigue',
                    'payload': 'get_yes_fatigue'
                },
                {
                    'content_type': 'text',
                    'title': 'no fatigue',
                    'payload': 'get_no_fatigue'
                }
            ]
        }
            
        self.send(recipient=event['sender'], message=fatigue)

    def set_fatigue(self, event, text, session):
        if 'yes' in text:
            session.set('fatigue','true')
        else:
            session.set('fatigue','false')
            
        nausea = {
            'text':'How about nausea?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes nausea',
                    'payload': 'get_yes_nausea'
                },
                {
                    'content_type': 'text',
                    'title': 'no nausea',
                    'payload': 'get_no_nausea'
                }
            ]
        }

        self.send(recipient=event['sender'], message=fatigue)

    def set_nausea(self, event, text, session):
        if 'yes' in text:
            session.set('nausea','true')
        else:
            session.set('nausea','false')
        
        vomitting = {
            'text':'Do you experience vomitting?',
            'quick_replies': [
                {   
                    'content_type': 'text',
                    'title': 'yes vomitting',
                    'payload': 'get_yes_vomitting'
                },
                {
                    'content_type': 'text',
                    'title': 'no vomitting',
                    'payload': 'get_no_vomitting'
                }
            ]
        }

        self.send(recipient=event['sender'], message=vomitting)

    def set_vomitting(self, event, text, session):
        if 'yes' in text:
            session.set('vomitting','true')
        else:
            session.set('vomitting','false')
        
        rash = {
            'text':'Do you notice any skin rash?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes skin rash',
                    'payload': 'get_yes_rash'
                },
                {
                    'content_type': 'text',
                    'title': 'no skin rash',
                    'payload': 'get_no_rash'
                }
            ]
        }   

        self.send(recipient=event['sender'], message=rash)

    def set_rash(self, text, session):
        if 'yes' in text:
            session.set('rash','true')
        else:
            session.set('rash','false')
        
        response = { 'text': 'You are suspected to have dengue\nWe are setting up appointment for you' }

        self.send(recipient=evet['sender'], message=response)
    """
    def message_hook(self, event):

        session = self.get_session(event)
        text = event['message'].get('text','')
        """
        if 'fever' in text:
            self.set_fever(event, text, session)

        if 'headache' in text:
            self.set_headache(event, text, session)

        if 'eyes' in text:
            self.set_eyes(event, text, session)

        if 'joint' in text:
            self.set_joint_muscle(event, text, session)

        if 'fatigue' in text:
            self.set_fatigue(event, text, session)

        if 'nausea' in text:
            self.set_nausea(event, text, session)

        if 'vomitting' in text:
            self.set_vomitting(event, text, session)

        if 'rash' in text:
            self.set_rash(event, text, session)
        """
