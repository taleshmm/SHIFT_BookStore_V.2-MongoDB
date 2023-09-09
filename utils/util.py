import re
from bson import ObjectId

def showPhone(phone: str) -> str:
    phone_format = ''
    if len(phone) == 9:
        peace1 = phone[:5]
        peace2 = phone[5:]
        phone_format = f'{peace1}-{peace2}'
    elif len(phone) == 11:
        peace1 = phone[:2]
        peace2 = phone[2:6]
        peace3 = phone[6:]
        phone_format = f'({peace1}) {peace2}-{peace3}'
    elif len(phone) == 13:
        peace1 = phone[:2]
        peace2 = phone[2:4]
        peace3 = phone[4:8]
        peace4 = phone[8:]
        phone_format = f'+{peace1} ({peace2}) {peace3}-{peace4}'
    else:
      return phone
    return phone_format


def clearPhone(phone: str) -> str:
    phone_format  = re.sub(r'[-() ]', '', phone)
    return phone_format

def searchToName(method_search, name) -> ObjectId:
    element = method_search.getByName(name)
    id = None
    if element:
        id = ObjectId(element.id)
    return id

def searchToId(method_search, id) -> str:
    element = method_search.getById(id)
    name = None
    if element:
        name = element.name
    return name