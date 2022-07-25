import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
a= data['company']['employee']['payable']['salary']
print(a)

data['company']['employee']['birth_name']='02/06/05'

print(data)

with open('sampleJson.json', 'w') as f:
    json.dump(data, f, indent = 2, sort_keys=True)