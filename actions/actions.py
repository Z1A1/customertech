# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import email
from typing import Any, Text, Dict, List

#from database import DataUpdate
#
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import mysql.connector
#
# class ValidateNameForm(FormValidationAction):
class Actionsubmit(Action):
    def name(self) -> Text:

      return "action_submit"
   # async def run(
      #  self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
   # ) -> List[Dict[Text, Any]]:
    #  DataUpdate(tracker.get_slot("name"),    
     # tracker.get_slot("amt"),tracker.get_slot("account"),
      #tracker.get_slot("time"),tracker.get_slot("transfer")) 
      #dispatcher.utter_message(" Your funds transfer is now completed")
      #return()
    
    

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
      def  Dts(name,email,phone_number):
        mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="schoolqa",
    auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name CHAR(255), amt  VARCHAR(255), account  VARCHAR(255), time VARCHAR(255),transfer VARCHAR(255) )") 
        sql='INSERT INTO customercare (name,email,phone_number) VALUES ("{0}","{1}", "{2}");'.format(name,email,phone_number)
        mycursor.execute(sql)
        mydb.commit()  
      Dts(tracker.get_slot("name"),    
      tracker.get_slot("email"),
      tracker.get_slot("phone_number")) 
      #dispatcher.utter_message(" Your funds transfer is now completed")
      return()
      
class Actionresult(Action):
    def name(self) -> Text:

      return "action_result"
    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) ->List[Dict[Text, Any]]:
       mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="schoolqa",
    auth_plugin='mysql_native_password')
       sql_select_Query = "select * from customercare"  
       cursor = mydb.cursor()
       cursor.execute(sql_select_Query)
       records = cursor.fetchall() 
       for row in records:
          name = row[0]
          email = row[1]
          phone_number  = row[2]
          #time  = row[3]
          #ransfer =row[4]  
          dispatcher.utter_message(f"name : {name}, email address: {email},phonenumber:{phone_number}")
class ValidateName(FormValidationAction):

    def name(self) -> Text:

        return "validate_techincal_form"
    def validate_breakdwon(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate breakdwon."""
        #print(f"First name given = {slot_value} length = {len(slot_value)}")
        if slot_value == "Breakdown visit":
            
            print("Here are your appointment details:\r 1)Repair Visit 18 June 2021 2)Installation 06 July 2021   View	3)Maintenance Visi15June 2021	 View")
            dispatcher.utter_message(text=f"Here are your breakdown visit details:\
Order Id		ORD-0015326750\
  Type & Activity	Installation & Installation\
  Date & Time		06 July 2021, 14:00\
  Location		New Delhi, 110001\
  CustomerName & City	Life line Hospital & Delhi\
  Instrument		cobas c 111 with ISE")                               
    #return()

                             
          

          


