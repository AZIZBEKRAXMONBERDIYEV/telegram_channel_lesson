from read_data import fromJson

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    s=0
    data=data["messages"]
    for i in data:
        if i["type"]=="message":
            s+=1    
    return s

f="data/result.json"
data = fromJson(f)
print(get_number_of_posts(data))