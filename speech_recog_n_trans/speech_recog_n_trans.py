#ibm-watson-speech-to-text
import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 

#googletrans api
from googletrans import Translator
  
authenticator = IAMAuthenticator('6YHih4cHeLCDQW42QP4j2KtppqjB9NLTT7HxNUn4RFQe')  #API key generated for my IBM account only (free version allows 500 minutes per month)
service = SpeechToTextV1(authenticator = authenticator) 
   
service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/58397bfd-794b-4856-a691-aedcfd50311a') 
   

with open(join(dirname('__file__'), r'sample-audio.mp3'),       #sample-audio.mp3 - audio file needed to be translated
          'rb') as audio_file: 
      
        dic = json.loads( 
                json.dumps( 
                    service.recognize( 
                        audio=audio_file, 
                        content_type='audio/mp3',    
                        model='en-GB_BroadbandModel',  #for english(UK) model, models need to be specified for different languages
                    continuous=True).get_result(), indent=2)) 
  
str = "" 
  
while bool(dic.get('results')): 
    str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:] 
       
print(str)

str = Translator().translate(str,dest = 'ja') #dest - destination language text has to be translated in.
print (str) 
