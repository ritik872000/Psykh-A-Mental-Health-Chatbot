# # This files contains your custom actions which can be used to run
# # custom Python code.

# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/core/actions/#custom-actions/


# # This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from database_conn import GetData



class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text =tracker.latest_message['text']
        dispatcher.utter_message(text=f"That's a nice name {text}!")
        return [SlotSet("name",text)]

class ActionReceiveDelight(Action):
    def name(self) -> Text:
        return "action_receive_delight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text =tracker.latest_message['text']
        dispatcher.utter_message(text=f"Great!")
        return [SlotSet("user_delight",text)]

class Actionreceivemood(Action):
    def name(self) -> Text:
        return "action_receive_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(template="utter_submit")
        return [SlotSet("journal",tracker.latest_message['text'])]


        

class ActionGetData(Action):
    def name(self) -> Text:
        return "action_get_data"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text=" Your Name is {0}\n Your Feedback is {1}".format(tracker.get_slot("name"),tracker.get_slot("journal")))
        GetData( tracker.get_slot("name"),tracker.get_slot("journal"))
        dispatcher.utter_message('Thanks for the feedback!')
        return[]
# keeps track of every conversation
class ActionSessionId(Action):
    def name(self) -> Text:
        return "action_session_id"
    
    async def run(
        self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            conversation_id=tracker.sender_id

            dispatcher.utter_message("The conversation id is {}".format(conversation_id))

            return []