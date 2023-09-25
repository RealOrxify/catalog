import playfab
from playfab.PlayFabSettings import PlayFabSettings
from playfab.PlayFabAdminApi import PlayFabAdminAPI

title_id = "YOUR_TITLE_ID"
secret_key = "YOUR_SECRET_KEY"

PlayFabSettings.static_settings.title_id = title_id
PlayFabSettings.static_settings.developer_secret_key = secret_key

playfab_id = "PLAYER_PLAYFAB_ID"

catalog_item_id = "YOUR_CATALOG_ITEM_ID"

def grant_item_to_player(playfab_id, catalog_item_id):
    try:
        result = PlayFabAdminAPI.GrantItemsToUsers(
            {
                "CatalogVersion": "YOUR_CATALOG_VERSION",
                "PlayFabIds": [playfab_id],
                "ItemIds": [catalog_item_id],
            }
        )

        if "ItemGrantResults" in result:
            item_grant_result = result["ItemGrantResults"][0]
            if item_grant_result.get("Result") == "Granted":
                print(f"Item {catalog_item_id} granted to player {playfab_id}")
            else:
                print(f"Failed to grant item {catalog_item_id} to player {playfab_id}")
        else:
            print(f"Failed to grant item {catalog_item_id} to player {playfab_id}")

    except playfab.PlayFabException as e:
        print(f"PlayFab Error: {e}")

grant_item_to_player(playfab_id, catalog_item_id)
