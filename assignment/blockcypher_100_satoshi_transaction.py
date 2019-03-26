import blockcypher


# address = blockcypher.generate_new_address(coin_symbol='btc-testnet', api_key='0d7ace0138a0460baa3600a486dd7df8')

address = 'n1WMvqdsXvpMyQDxXd1XzpeY38XtZoSocm'
private = '489ebfb64928e90510bc9a05626ca60e0bbe8c3816e19673cf4aa9fb1f02a3c2'
public = '03768717a1baedf1b7a13de38be56eaecefca6c427e834327636bdde2655c7b472'

#Specify the inputs and outputs below
#For convenince you can specify an address, and the backend will work out what transaction output that address has available to spend
#You do not need to list a change address, by default the transaction will be created with all change (minus the fees) going to the first input address
inputs = [{'address': 'mrVMhtH74sbB46qVJ8Ty6DRErJULKvv8SE'}]
outputs = [{'address': address, 'value': 100}]
#The next line creates the transaction shell, which is as yet unsigned
unsigned_tx = blockcypher.create_unsigned_tx(inputs=inputs, outputs=outputs, coin_symbol='btc-testnet', api_key='0d7ace0138a0460baa3600a486dd7df8')

#You can edit the transaction fields at this stage, before signing it.


#Now list the private and public keys corresponding to the inputs
private_keys=[private]
public_keys=[public]
#Next create the signatures
tx_signatures = blockcypher.make_tx_signatures(txs_to_sign=unsigned_tx['tosign'], privkey_list=private_keys, pubkey_list=public_keys)
#Finally push the transaction and signatures onto the network
blockcypher.broadcast_signed_transaction(unsigned_tx=unsigned_tx, signatures=tx_signatures, pubkeys=public_keys, coin_symbol='btc-testnet', api_key='0d7ace0138a0460baa3600a486dd7df8')
