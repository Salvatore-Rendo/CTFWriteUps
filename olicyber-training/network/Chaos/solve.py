import json

# Load the JSON file
with open('olicyber-training/network/Chaos/artifacts/packets.json', 'r') as file:
    data = json.load(file)

# Extract tcp.payload from each packet, handling the case where the key might not exist
payload_list = [packet['_source']['layers']['tcp'].get('tcp.payload', '') for packet in data]

# Convert hex values to decimal and then to ASCII characters
ascii_characters = ''.join([chr(int(data, 16)) for data in payload_list if data])

# Print or process the ascii_characters as needed
print(ascii_characters)