from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    s=0
    data=data["messages"]
    for i in data:
        if i["type"]=="message":
            a = i["date"]
            x=a[5:7]
            if int(x)==int(month):
                s+=1

    return x
f="data/result.json"
data=fromJson(f)
print(get_post_month(data, 10))