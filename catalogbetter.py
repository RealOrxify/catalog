import requests
import json
from termcolor import colored

def get_catalog(token, title_id):
    url = f"https://<your_title_id>.playfabapi.com/Admin/GetCatalogItems"
    headers = {
        "Content-Type": "application/json",
        "X-SecretKey": token
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

def main():
    title = colored("""
    ░█████╗░██████╗░██╗░░██╗██╗███████╗██╗░░░██╗  ░█████╗░░█████╗░████████╗░█████╗░██╗░░░░░░█████╗░░██████╗░
    ██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗██╔════╝░
    ██║░░██║██████╔╝░╚███╔╝░██║█████╗░░░╚████╔╝░  ██║░░╚═╝███████║░░░██║░░░███████║██║░░░░░██║░░██║██║░░██╗░
    ██║░░██║██╔══██╗░██╔██╗░██║██╔══╝░░░░╚██╔╝░░  ██║░░██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██║░░██║██║░░╚██╗
    ╚█████╔╝██║░░██║██╔╝╚██╗██║██║░░░░░░░░██║░░░  ╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗╚█████╔╝╚██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░
    """, "blue")

    print(title)
    
    title_id = input("Enter your PlayFab Title ID: ")
    token = input("Enter your PlayFab developer secret key: ")
    
    catalog = get_catalog(token, title_id)
    
    if catalog:
        print("Catalog items:")
        for item in catalog:
            print(item)

if __name__ == "__main__":
    main()
