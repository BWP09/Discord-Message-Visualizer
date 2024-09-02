import requests
from html.parser import HTMLParser

class __hrefParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = True) -> None:
        self.result = ""
        
        super().__init__(convert_charrefs=convert_charrefs)
    
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attributes = dict(attrs)
            
            if attributes.get("title") == "Click here to go to the original source of the profile picture.":
                self.result = attributes.get("href")

def get_pfp(user_id: int):
    parser = __hrefParser()
    parser.feed(requests.get(f"https://discord-avatar.com/en/user/?id={user_id}").text)

    return parser.result

if __name__ == "__main__":
    print(get_pfp(666778774934781982))