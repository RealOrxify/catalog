import requests
import json
import subprocess

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

def clone_repository(url):
    result = subprocess.run(["git", "clone", url], capture_output=True)
    output = result.stdout.decode("utf-8")

    if result.returncode == 0:
        print("Repository cloned successfully")
    else:
        print("Failed to clone repository. Error message:\n", output)

def main():
    title_art = """
    ░█████╗░██████╗░██╗░░██╗██╗███████╗██╗░░░██╗  ░█████╗░░█████╗░████████╗░█████╗░██╗░░░░░░█████╗░░██████╗░
    ██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝╚██╗░██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗██╔════╝░
    ██║░░██║██████╔╝░╚███╔╝░██║█████╗░░░╚████╔╝░  ██║░░╚═╝███████║░░░██║░░░███████║██║░░░░░██║░░██║██║░░██╗░
    ██║░░██║██╔══██╗░██╔██╗░██║██╔══╝░░░░╚██╔╝░░  ██║░░██╗██╔══██║░░░██║░░░██╔══██║██║░░░░░██║░░██║██║░░╚██╗
    ╚█████╔╝██║░░██║██╔╝╚██╗██║██║░░░░░░░░██║░░░  ╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗╚█████╔╝╚██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░
    """

    print(title_art)
    title_id = input("TITLE ID: ")
    token = input("Enter your PlayFab developer secret key: ")

    catalog = get_catalog(token, title_id)

    if catalog:
        print("Catalog items:")
        for item in catalog:
            print(item)

        url = input("Enter the repository URL to clone: ")
        clone_repository(url)

if __name__ == "__main__":
    main()
