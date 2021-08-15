import json

# FIND THE USER'S CODE


def find_code():
    appli = input("Entrez pour quelle application"
                  " vous recherchez votre mdp : ")
    with open('generator_mdp\modules\data_mdp.json', "r+") as json_data:
        mdp_dict = json.loads(json_data.read())
        print(mdp_dict[appli])


find_code()
