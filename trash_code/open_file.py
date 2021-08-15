def open_file():
    values=[]
    with open('charachetrs.json') as f:
    for entry in data:
        values.append(entry['character'])
    return values
    
def random_characters():
    all_values=open_file
    
