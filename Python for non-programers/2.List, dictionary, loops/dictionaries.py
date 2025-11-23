nexus = {
    'name': 'Nexus 5',
    'manufacturer': 'LG',
    'os': 'Android',
    'version': 4.4  
}



nexus['hardware'] = "Samsung"

del(nexus['manufacturer'])

print(len(nexus))

print(nexus["name"])

print(nexus)

truth_or_date = {'handsome': True,
                 'Ugly': False}

print(truth_or_date['Ugly'])