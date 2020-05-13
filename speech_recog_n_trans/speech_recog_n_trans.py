
import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 

from googletrans import Translator
  
authenticator = IAMAuthenticator('6YHih4cHeLCDQW42QP4j2KtppqjB9NLTT7HxNUn4RFQe')  
service = SpeechToTextV1(authenticator = authenticator) 
   
service.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/58397bfd-794b-4856-a691-aedcfd50311a') 
   

with open(join(dirname('__file__'), r'sample-audio.mp3'),  
          'rb') as audio_file: 
      
        dic = json.loads( 
                json.dumps( 
                    service.recognize( 
                        audio=audio_file, 
                        content_type='audio/mp3',    
                        model='en-US_NarrowbandModel', 
                    continuous=True).get_result(), indent=2)) 
  
str = "" 

      
while bool(dic.get('results')): 
    print(dic.get('results'))
    str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:] 
       
print(str)

str = Translator().translate(str,dest = 'ja')
print (str) 
