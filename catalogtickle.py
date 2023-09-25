import requests
import json

def get_catalog(title_id):
    url = f"https://<your_title_id>.playfabapi.com/Admin/GetCatalogItems"
    headers = {
        "Content-Type": "application/json",
        "X-SecretKey": title_id
    }
    request_data = {
        "CatalogVersion": "main"
    }

    response = requests.post(url, headers=headers, data=json.dumps(request_data))

    if response.status_code == 200:
        catalog_items = response.json()["Catalog"]
        return catalog_items
    else:
        print(f"Failed to retrieve catalog items. Error code: {response.status_code}")
        return None

def print_title():
    title_message = """
░█████╗░██████╗░██╗░░██╗██╗███████╗██╗░░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝╚██╗░██╔╝╚█║██╔════╝
██║░░██║██████╔╝░╚███╔╝░██║█████╗░░░╚████╔╝░░╚╝╚█████╗░
██║░░██║██╔══██╗░██╔██╗░██║██╔══╝░░░░╚██╔╝░░░░░░╚═══██╗
╚█████╔╝██║░░██║██╔╝╚██╗██║██║░░░░░░░░██║░░░░░░██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░░░╚═════╝░ 
████████╗██╗░█████╗░██╗░░██╗██╗░░░░░███████╗██████╗░
╚══██╔══╝██║██╔══██╗██║░██╔╝██║░░░░░██╔════╝██╔══██╗
░░░██║░░░██║██║░░╚═╝█████═╝░██║░░░░░█████╗░░██████╔╝
░░░██║░░░██║██║░░██╗██╔═██╗░██║░░░░░██╔══╝░░██╔══██╗
░░░██║░░░██║╚█████╔╝██║░╚██╗███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
    """

    print("*" * len(title_message))
    print(title_message)
    print("*" * len(title_message))

def main():
    print_title
