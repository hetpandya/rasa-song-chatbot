
#happy path
* greet
  - utter_greet

#happy path
* play_song
  - slot{"song_name": "liggi"}
  - utter_play_song
   - action_play_song

#happy path
* greet
  - utter_greet
* play_song
  - slot{"song_name": "senorita"}
  - utter_play_song
  - action_play_song

#happy path
* greet
  - utter_greet
* play_song
  - slot{"song_name": "maula mere maula"}
  - utter_play_song
  - action_play_song
* goodbye
  - utter_goodbye

#happy path
* play_song
  - slot{"song_name": "matarghasti"}
  - utter_play_song
  - action_play_song
* goodbye
  - utter_goodbye

#sad path 2
* greet
  - utter_greet
* goodbye
  - utter_goodbye

#say goodbye
* goodbye
  - utter_goodbye
  
#bot_functions 
* greet
  - utter_greet
* bot_functions
  - utter_bot_functions

##story_form
* greet
    - utter_greet
* bot_functions
    - utter_bot_functions
* play_song
  - slot{"song_name": "ghoonghroo"}
  - utter_play_song
  - action_play_song

##story_form
* greet
    - utter_greet
* bot_functions
    - utter_bot_functions
* play_song
  - slot{"song_name": "Khwabon Ke Parindey"}
  - utter_play_song
  - action_play_song
* goodbye
  - utter_goodbye

#Generated Story 3183310183320455154
* greet
    - utter_greet
* bot_functions
    - utter_bot_functions
* play_song
  - slot{"song_name": "saibo"}
  - utter_play_song
  - action_play_song
* play_song
  - slot{"song_name": "muqabala"}
  - utter_play_song
  - action_play_song
* goodbye
    - utter_goodbye
* stop
    - utter_goodbye

#Generated Story 3183310183320455154
* greet
    - utter_greet
* bot_functions
    - utter_bot_functions
* play_song
  - slot{"song_name": "gulabi ankhein"}
  - utter_play_song
  - action_play_song
* goodbye
    - utter_goodbye
* stop
    - utter_goodbye

#interactive_story_1
* play_song
  - slot{"song_name": "Iktara"}
  - utter_play_song
  - action_play_song
* play_song
  - slot{"song_name": "Sawaar loon"}
  - utter_play_song
  - action_play_song

#interactive_story_1
* play_song
  - slot{"song_name": "Raabta"}
  - utter_play_song
  - action_play_song
* goodbye
    - utter_goodbye

#interactive_story_1
* play_song
  - slot{"song_name": "kabira"}
  - utter_play_song
  - action_play_song
* play_song
  - slot{"song_name": "Moh Moh Ke Dhaage"}
  - utter_play_song
  - action_play_song
* play_song
  - slot{"song_name": "sapna jahan"}
  - utter_play_song
  - action_play_song
* goodbye
    - utter_goodbye