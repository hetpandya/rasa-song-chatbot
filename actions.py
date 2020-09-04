
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import logging
import soundcloud
from pyDes import *
import base64

logger = logging.getLogger(__name__)


class SongMachine(object):
    def __init__(self):
      self.client_id = 'xxxxxxxxxxxx'

    def decrypt_url(self,url):
      des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",pad=None, padmode=PAD_PKCS5)
      enc_url = base64.b64decode(url.strip())
      dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
      return dec_url
    
    def fetchSong(self,song):
        try:
          req = requests.get('https://www.jiosaavn.com/api.php?__call=autocomplete.get&_marker=0&query='+song+'&ctx=android&_format=json&_marker=0')
          resonse = req.json()
          songs_data = resonse['songs']['data']

          if songs_data != []:
            song_id = songs_data[0]['id']
            title = songs_data[0]['title']
            data = requests.get('https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids='+song_id)
            data = data.json()
            encrypted_url = data[song_id]['encrypted_media_url']
            return {'url':self.decrypt_url(encrypted_url),'title':title}
          
          else:
            client = soundcloud.Client(client_id=self.client_id)
            tracks = client.get('/tracks', q=song,limit=1)
            stream_url = client.get(tracks[0].stream_url, allow_redirects=False)
            return {'url':stream_url.location,'title':tracks[0].title}
            
        except:
          return {'url':'','title':''}

class ActionFetchSong(Action):

    def name(self) -> Text:
        return "action_play_song"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        song_name = tracker.get_slot('song_name')
        if song_name is not None:
          machine = SongMachine()
          data = machine.fetchSong(song_name)
          if data['url'] is not '':
            dispatcher.utter_custom_json({"payload":'audio',"url":data['url'],'title':data['title']})
          else:
            dispatcher.utter_message("I couldn't find the song you asked for.")
        else:
          dispatcher.utter_message("What song should I play?")
        
        return []