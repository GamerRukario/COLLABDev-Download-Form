import pandas
import requests
import os 


#Download list of forms in server
def download_form_all(token):
    print("Status Codes")
    print("200 - Successful")
    print("201 - Resource successfully created")
    print("204 - Resource successfully deleted")
    print("403 - Permission denied to resource")
    print("404 - Resource was not found")
    down_form = requests.get('https://kc.humanitarianresponse.info/api/v1/forms.csv', headers={'Authorization': 'Token {}'.format(token)})
    print("Downloading Forms List | Status Code: {}".format(down_form))
    open('Download_all.csv','wb').write(down_form.content)
    print("Downloading complete!")

#get all urls from the list
def read():
    i = 0
    csv_file = []
    df = pandas.read_csv('download_all.csv')
    for url,formid,description in zip(df.url,df.formid,df.description):
        csv_file.append([url,formid,description])
        i = i + 1
    return csv_file, i

#Iterate over each url and download, also output to folder 
def download_form_list(links,token):
    i = 0
    if not os.path.exists('COLLABdev'):
        os.makedirs('COLLABdev')
    for link in links:
        down_form = requests.get(link[0], headers={'Authorization': 'Token {}'.format(token)})
        print("Downloading {} Form | Status Code {}".format(link[2],down_form))
        open('COLLABdev/COLLABDev_{}_{}.csv'.format('PLACEHOLDER',link[2]),'wb').write(down_form.content)
    print("All Forms Downloaded")

token = "" # insert kobotoolbox access token
if not token:
    print("No token")
else:
    download_form_all(token)
    links,i = read()
    print("URL List count: {}".format(i))
    download_form_list(links,token)