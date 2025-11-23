import json
import requests

url = "sbx-nxos-mgmt.cisco.com"

username = 'admin'
password = 'Admin_1234!'

myheaders = {'content-type': 'application/json-rpc'}
payload = {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
        "cmd": "show version",
        "version": 1.2
    },
    "id": 1
}   

response = requests.post(f"https://{url}/ins",
                          auth=(username, password),
                          headers=myheaders, 
                          data=json.dumps(payload), 
                          verify=False).json()


#create a file and write the output to a file
response = response['result']['body']['kickstart_ver_str']
with open('show_version_output1.txt', 'w') as f:
    f.write(json.dumps(response, indent=4))

