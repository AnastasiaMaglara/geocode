import requests 
import json 


def send_request(locationArray, adminAreaArray):
  KEY = 'BoLshMW41NYbEfbvVeHHXp0cwnGvyDqL'
  
  ##defining a params dict for the parameters to be sent to the API 
  PARAMS = {'key': KEY, 'location': locationArray, 'maxResults': 1}
  
  ##api-endpoint 
  URL = 'http://open.mapquestapi.com/geocoding/v1/batch'
  
  ##sending get request and saving the response as response object 
  r = requests.get(url = URL, params = PARAMS)

  ##extracting data in json format 
  results = r.json() 
  
  ##extracting latitude, longitude and formatted address  
  ##of the first matching location
  for n in  results['results']:
    v = n['locations'][0]
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
results= []
for index, value in enumerate(_list):
  authorLocation = value['AuthorLocation']
  if authorLocation != "":
    locations.append(authorLocation)
  ##limit of 100 at a time
  if index % 99 ==0 and index!=0 or value ==_list[-1]:
    send_request(locations,results)
    locations=[]


for v in _list:
    authorLocation = v['AuthorLocation']
    if authorLocation != "":
      tmp= []
      for x in range(0, 4):
        tmp.append(results.pop(0))
      v['AuthorLocation'] = tmp


##Save our changes to JSON file
jsonFile = open('C:/Users/Αναστασία/Desktop/72572.json', 'w+')
jsonFile.write(json.dumps(data))
jsonFile.close()
