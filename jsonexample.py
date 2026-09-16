def main():
    data = {
    "Names" : ["Alice", "Bob", "Charlie"],
    "Phones Numbers" : ["123-456-7890", "987-654-3210", "555-555-5555"],
    "Ages" : [25, 30, 35],
    "Occupations" : ["Engineer", "Doctor", "Artist"],
    "Addresses" : ["123 Main St", "456 Elm St", "789 Oak St"],
    "Money Owed to Me" : [125.50, 290.75, 301.00]
    }

    #Exporting the data to a JSON file
    import json
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        #print(data)
        Name = input("Who do you want to look up? ")
        if Name in data["Names"]:
            index = data["Names"].index(Name)
            print(f"Phone Number: {data['Phones Numbers'][index]}")
            print(f"Age: {data['Ages'][index]}")
            print(f"Occupation: {data['Occupations'][index]}")
            print(f"Address: {data['Addresses'][index]}")
            print(f"Money Owed to Me: ${data['Money Owed to Me'][index]}")
main()