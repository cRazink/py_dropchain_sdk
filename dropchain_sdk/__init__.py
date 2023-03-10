import requests

class DropChainSDK:
    def __init__(self, rapidapi_key, app_id):
        self.rapidapi_key = rapidapi_key
        self.app_id = app_id
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": rapidapi_key,
            "X-RapidAPI-Host": "dropchain1.p.rapidapi.com"
        }

    def asset_mint_testnet(self, created_asset_amount_int, created_asset_decimals, created_asset_name, created_asset_unit_name, created_asset_url, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/asset_mint_testnet"

        payload = {
            "app_id": self.app_id,
            "created_asset_amount_int": created_asset_amount_int,
            "created_asset_decimals": created_asset_decimals,
            "created_asset_name": created_asset_name,
            "created_asset_unit_name": created_asset_unit_name,
            "created_asset_url": created_asset_url,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def asset_mint_dropnet(self, created_asset_amount_int, created_asset_decimals, created_asset_name, created_asset_unit_name, created_asset_url, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/asset_mint_dropnet"

        payload = {
            "app_id": self.app_id,
            "created_asset_amount_int": created_asset_amount_int,
            "created_asset_decimals": created_asset_decimals,
            "created_asset_name": created_asset_name,
            "created_asset_unit_name": created_asset_unit_name,
            "created_asset_url": created_asset_url,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_algo_address_from_uid(self, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_algo_address_from_uid"

        payload = {
            "app_id": self.app_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def freeze_asset_testnet(self, asset1_id, receiver1_uid, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/freeze_asset_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_id": asset1_id,
            "receiver1_uid": receiver1_uid,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def freeze_asset_dropnet(self, asset1_id, receiver1_uid, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/freeze_asset_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_id": asset1_id,
            "receiver1_uid": receiver1_uid,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_transaction_info_dropnet(self, transaction1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_transaction_info_dropnet"

        payload = {
            "app_id": self.app_id,
            "transaction1_id": transaction1_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_transaction_info_testnet(self, transaction1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_transaction_info_testnet"

        payload = {
            "app_id": self.app_id,
            "transaction1_id": transaction1_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_note_from_txid_testnet(self, transaction1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_note_from_txid_testnet"

        payload = {
            "app_id": self.app_id,
            "transaction1_id": transaction1_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_note_from_txid_dropnet(self, transaction1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_note_from_txid_dropnet"

        payload = {
            "app_id": self.app_id,
            "transaction1_id": transaction1_id,
            "user1_uid": user1_uid
        }
        
        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_asset_info_testnet(self, asset1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_asset_info_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_id": asset1_id,
            "user1_uid": user1_uid
        }
        
        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_asset_info_dropnet(self, asset1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_asset_info_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_id": asset1_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()


    def send_asset_dropnet(self, asset1_amount_int, asset1_id, receiver1_uid, transaction1_note, session1_token, user1_uid): 
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/send_asset_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "asset1_id": asset1_id,
            "receiver1_uid": receiver1_uid,
            "transaction1_note": transaction1_note,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()
       
    def send_asset_testnet(self, asset1_amount_int, asset1_id, receiver1_uid, transaction1_note, session1_token, user1_uid): 
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/send_asset_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "asset1_id": asset1_id,
            "receiver1_uid": receiver1_uid,
            "transaction1_note": transaction1_note,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()


    def send_algo_testnet(self, asset1_amount_int, receiver1_uid, transaction1_note, session1_token, user1_uid): 
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/send_algo_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "receiver1_uid": receiver1_uid,
            "transaction1_note": transaction1_note,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def send_drop_dropnet(self, asset1_amount_int, receiver1_uid, transaction1_note, session1_token, user1_uid): 
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/send_drop_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "receiver1_uid": receiver1_uid,
            "transaction1_note": transaction1_note,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def atomic_swap_algo_testnet(self, asset1_amount_int, asset2_amount_int, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/atomic_swap_algo_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "asset2_amount_int": asset2_amount_int,
            "receiver1_uid": receiver1_uid,
            "receiver2_uid": receiver2_uid,
            "transaction1_note": transaction1_note,
            "transaction2_note": transaction2_note,
            "user1_uid": user1_uid,
            "user2_uid": user2_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        if session2_token is not None:
            payload["session2_token"] = session2_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def atomic_swap_drop_dropnet(self, asset1_amount_int, asset2_amount_int, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/atomic_swap_drop_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "asset2_amount_int": asset2_amount_int,
            "receiver1_uid": receiver1_uid,
            "receiver2_uid": receiver2_uid,
            "transaction1_note": transaction1_note,
            "transaction2_note": transaction2_note,
            "user1_uid": user1_uid,
            "user2_uid": user2_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        if session2_token is not None:
            payload["session2_token"] = session2_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def get_metadata_from_hash(self, asset_metadata_hash, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/get_metadata_from_hash"

        payload = {
            "app_id": self.app_id,
            "asset_metadata_hash": asset_metadata_hash,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def asset_indexer_testnet(self, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/asset_indexer_testnet"

        payload = {
            "app_id": self.app_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def asset_indexer_dropnet(self, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/asset_indexer_dropnet"

        payload = {
            "app_id": self.app_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def atomic_swap_testnet(self, asset1_amount_int, asset1_id, asset2_amount_int, asset2_id, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/atomic_swap_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "asset1_id": asset1_id,
            "asset2_amount_int": asset2_amount_int,
            "asset2_id": asset2_id,
            "receiver1_uid": receiver1_uid,
            "receiver2_uid": receiver2_uid,
            "transaction1_note": transaction1_note,
            "transaction2_note": transaction2_note,
            "user1_uid": user1_uid,
            "user2_uid": user2_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        if session2_token is not None:
            payload["session2_token"] = session2_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def atomic_swap_dropnet(self, asset1_amount_int, asset1_id, asset2_amount_int, asset2_id, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/atomic_swap_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_amount_int": asset1_amount_int,
            "asset1_id": asset1_id,
            "asset2_amount_int": asset2_amount_int,
            "asset2_id": asset2_id,
            "receiver1_uid": receiver1_uid,
            "receiver2_uid": receiver2_uid,
            "transaction1_note": transaction1_note,
            "transaction2_note": transaction2_note,
            "user1_uid": user1_uid,
            "user2_uid": user2_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        if session2_token is not None:
            payload["session2_token"] = session2_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def asset_optin_dropnet(self, asset1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/asset_optin_dropnet"

        payload = {
            "app_id": self.app_id,
            "asset1_id": asset1_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def asset_optin_testnet(self, asset1_id, session1_token, user1_uid):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/asset_optin_testnet"

        payload = {
            "app_id": self.app_id,
            "asset1_id": asset1_id,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def redeem_session_token(self, session1_token):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/redeem_session_token"

        payload = {
            "app_id": self.app_id,
            "session1_token": session1_token
        }

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()

    def create_asset_metadata(self, asset_metadata_description, asset_metadata_external_url, asset_metadata_has_traits, asset_metadata_image_url, asset_metadata_name, asset_metadata_trait_type1, asset_metadata_trait_type2, asset_metadata_trait_type3, asset_metadata_trait_type4, asset_metadata_trait_type5, asset_metadata_trait_type6,asset_metadata_trait_type7, asset_metadata_trait_type8, asset_metadata_value1, asset_metadata_value2, asset_metadata_value3, asset_metadata_value4, asset_metadata_value5, asset_metadata_value6, asset_metadata_value7, asset_metadata_value8, user1_uid, session1_token):
        url = "https://dropchain1.p.rapidapi.com/dropchain/v1/create_asset_metadata"

        payload = {
            "app_id": self.app_id,
            "asset_metadata_description": asset_metadata_description,
            "asset_metadata_external_url": asset_metadata_external_url,
            "asset_metadata_has_traits": asset_metadata_has_traits,
            "asset_metadata_image_url": asset_metadata_image_url,
            "asset_metadata_name": asset_metadata_name,
            "asset_metadata_trait_type1": asset_metadata_trait_type1,
            "asset_metadata_trait_type2": asset_metadata_trait_type2,
            "asset_metadata_trait_type3": asset_metadata_trait_type3,
            "asset_metadata_trait_type4": asset_metadata_trait_type4,
            "asset_metadata_trait_type5": asset_metadata_trait_type5,
            "asset_metadata_trait_type6": asset_metadata_trait_type6,
            "asset_metadata_trait_type7": asset_metadata_trait_type7,
            "asset_metadata_trait_type8": asset_metadata_trait_type8,
            "asset_metadata_value1": asset_metadata_value1,
            "asset_metadata_value2": asset_metadata_value2,
            "asset_metadata_value3": asset_metadata_value3,
            "asset_metadata_value4": asset_metadata_value4,
            "asset_metadata_value5": asset_metadata_value5,
            "asset_metadata_value6": asset_metadata_value6,
            "asset_metadata_value7": asset_metadata_value7,
            "asset_metadata_value8": asset_metadata_value8,
            "user1_uid": user1_uid
        }

        if session1_token is not None:
            payload["session1_token"] = session1_token

        response = requests.post(url, json=payload, headers=self.headers, timeout=30)

        return response.json()


