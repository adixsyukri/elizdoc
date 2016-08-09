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

    def set_fever(text, session):
        if 'yes' in text:
            session.set('fever','true')
        else:
            session.set('fever','false')
        
    def set_headache(text, session):
        if 'yes' in text:
            session.set('headache','true')
        else:
            session.set('headache','false')

    def set_eyes(text, session):
        if 'yes' in text:
            session.set('eyes','true')
        else:
            session.set('eyes','false')

    def set_joint_muscle(text, session):
        if 'yes' in text:
            session.set('muscle','true')
        else:
            session.set('muscle','false')

    def message_hook(self, event):

        session = self.get_session(event)
        text = event['message'].get('text','')
        if 'fever' in text:
            set_fever(text,session)
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

        if 'headache' in text:
            set_headache(text,session)
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

        if 'eyes' in text:
            set_eyes(text,session)
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

        if 'joint' in text:
            set_joint_muscle(text,session)
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

        if 'fatigue' in text:
            set_fatigue(text, session)
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

        if 'nausea' in text:
            set_nausea(text, session)
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

        if 'vomitting' in text:
            set_vomitting(text, session)
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

        if 'rash' in text:
            set_rash(text, session)
            response = { 'text': 'You are suspected to have dengue\nWe are setting up appointment for you' }

            self.send(recipient=evet['sender'], message=response)
