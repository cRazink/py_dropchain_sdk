from dropchain_sdk import DropChainSDK

dropchain_sdk = DropChainSDK("<Your RapidAPI Key>", "<Your App ID>")

# [ Start Example Usage Snippets ]
# for each of the example snippets below, you must replace the parameters with your own test credentials on your dropchain.network developer dashboard

response = dropchain_sdk.asset_mint_testnet(created_asset_amount_int, created_asset_decimals, created_asset_name, created_asset_unit_name, created_asset_url, session1_token, user1_uid)
response = dropchain_sdk.asset_mint_dropnet(created_asset_amount_int, created_asset_decimals, created_asset_name, created_asset_unit_name, created_asset_url, session1_token, user1_uid)
response = dropchain_sdk.get_algo_address_from_uid(session1_token, user1_uid)
response = dropchain_sdk.get_transaction_info_dropnet(transaction1_id, session1_token, user1_uid)
response = dropchain_sdk.get_transaction_info_testnet(transaction1_id, session1_token, user1_uid)
response = dropchain_sdk.get_note_from_txid_testnet(transaction1_id, session1_token, user1_uid)
response = dropchain_sdk.get_note_from_txid_dropnet(transaction1_id, session1_token, user1_uid)
response = dropchain_sdk.get_asset_info_testnet(asset1_id, session1_token, user1_uid)
response = dropchain_sdk.get_asset_info_dropnet(asset1_id, session1_token, user1_uid)
response = dropchain_sdk.send_asset_dropnet(asset1_amount_int, asset1_id, receiver1_uid, transaction1_note, session1_token, user1_uid)
response = dropchain_sdk.send_asset_testnet(asset1_amount_int, asset1_id, receiver1_uid, transaction1_note, session1_token, user1_uid)
response = dropchain_sdk.send_algo_testnet(asset1_amount_int, receiver1_uid, transaction1_note, session1_token, user1_uid)
response = dropchain_sdk.send_drop_dropnet(asset1_amount_int, receiver1_uid, transaction1_note, session1_token, user1_uid)
response = dropchain_sdk.asset_optin_testnet(asset1_id, session1_token, user1_uid)
response = dropchain_sdk.asset_optin_dropnet(asset1_id, session1_token, user1_uid)
response = dropchain_sdk.atomic_swap_algo_testnet(asset1_amount_int, asset2_amount_int, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid)
response = dropchain_sdk.atomic_swap_drop_dropnet(asset1_amount_int, asset2_amount_int, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid)
response = dropchain_sdk.get_metadata_from_hash(asset_metadata_hash, session1_token, user1_uid)
response = dropchain_sdk.create_asset_metadata(asset_metadata_description, asset_metadata_external_url, asset_metadata_has_traits, asset_metadata_image_url, asset_metadata_name, asset_metadata_trait_type1, asset_metadata_trait_type2, asset_metadata_trait_type3, asset_metadata_trait_type4, asset_metadata_trait_type5, asset_metadata_trait_type6,asset_metadata_trait_type7, asset_metadata_trait_type8, asset_metadata_value1, asset_metadata_value2, asset_metadata_value3, asset_metadata_value4, asset_metadata_value5, asset_metadata_value6, asset_metadata_value7, asset_metadata_value8, user1_uid, session1_token)
response = dropchain_sdk.asset_indexer_testnet(session1_token, user1_uid)
response = dropchain_sdk.asset_indexer_dropnet(session1_token, user1_uid)
response = dropchain_sdk.atomic_swap_testnet(asset1_amount_int, asset1_id, asset2_amount_int, asset2_id, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid)
response = dropchain_sdk.atomic_swap_dropnet(asset1_amount_int, asset1_id, asset2_amount_int, asset2_id, receiver1_uid, receiver2_uid, transaction1_note, transaction2_note, session1_token, session2_token, user1_uid, user2_uid)
response = dropchain_sdk.redeem_session_token(session1_token)
response = dropchain_sdk.freeze_asset_testnet(asset1_id, receiver1_uid, session1_token, user1_uid)
response = dropchain_sdk.freeze_asset_dropnet(asset1_id, receiver1_uid, session1_token, user1_uid)

# if you are still testing dropchain and have not yet started using the DropChain SSO, you do not need to include the session1_token parameter. For this parameter, simply include None within the session1_token field for your calls in order to use the SDK 
# [ End Example Usage Snippets ]

print(response)

