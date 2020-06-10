import requests 
import json 



def send_request(location):
  KEY = 'BoLshMW41NYbEfbvVeHHXp0cwnGvyDqL'
  
  ##defining a params dict for the parameters to be sent to the API 
  PARAMS = {'key': KEY, 'location': location}
  
  ##api-endpoint 
  URL = 'http://open.mapquestapi.com/geocoding/v1/address'
  
  ##sending get request and saving the response as response object 
  r = requests.get(url = URL, params = PARAMS)
  
  ##extracting data in json format 
  results = r.json() 
  
##extracting latitude, longitude and formatted address  
##of the first matching location
  adminAreaArray= []
  v = results['results'][0]['locations'][0]
  adminAreaArray.append(v['adminArea5'])
  adminAreaArray.append(v['adminArea4'])
  adminAreaArray.append(v['adminArea3'])
  adminAreaArray.append(v['adminArea1'])
  return(adminAreaArray)


##forOneJsonFile
jsonFile = open('C:/Users/Αναστασία/Desktop/72572.json', 'r') 
data = json.load(jsonFile)
jsonFile.close()
	
##forMoreJsonFiles
#data= []
#pathOfJsonFiles
#path_to_json = 'C:/Users/Αναστασία/Desktop/json/'
#for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
#  json_file=open('C:/Users/Αναστασία/Desktop/72572.json', 'r') 
#  data = json.load(json_file)
#  json_file.close()


##location given here 
#locations = ['Boston', 'Denver,CO']
locations= []
_list = data['Reviews']

for v in _list:
    authorLocation = v['AuthorLocation']
    if authorLocation != "":
      v['AuthorLocation'] = send_request(authorLocation)

## Save our changes to JSON file
jsonFile = open('C:/Users/Αναστασία/Desktop/72572.json', 'w+')
jsonFile.write(json.dumps(data))
jsonFile.close()
