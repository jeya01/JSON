
"""Retrive unique state form open brewerie"""

def func2(file):
    with open(file, 'r') as f:
        data = json.load(f)
        s = []
        new_list = []

        for i in data:
            s.append(i['state'])
        print(s,"\n")

        for j in s:
            if j not in new_list:
                new_list.append(j)
        print("Unique list:", new_list)





func2('opem_breweries.json')
