import json
import gzip
import io
import binascii
import tarfile

json_path = 'olicyber-training/network/08-ByteExtraction/solve/extraction.json'

with open(json_path) as f:
    json_data = json.load(f)

# Extract the data.data field from each packet and store in a list
extracted_data = []

for packet in json_data:
    source_data = packet.get('_source', {})
    layers_data = source_data.get('layers', {})
    
    if 'data' in layers_data:
        data = layers_data.get('data', None)
        data_data = data.get('data.data', None)

        if data_data is not None:
            # Remove colons and convert hex string to bytes
            data_data = data_data.replace(":", "")
            extracted_data.append(data_data)

# Concatenate the extracted data into a single string
compressed_data = ''.join(extracted_data)

# Convert the hex string to bytes
compressed_bytes = binascii.unhexlify(compressed_data)

# Create a decompression object for gzip
with gzip.GzipFile(fileobj=io.BytesIO(compressed_bytes), mode='rb') as f:
    uncompressed_data = f.read()

# Check if the uncompressed data is a tar archive
try:
    with tarfile.open(fileobj=io.BytesIO(uncompressed_data), mode='r') as tar:
        # Extract all members of the tar archive
        tar.extractall('.')
        print("Tar archive extracted successfully.")
except tarfile.TarError:
    # If it's not a tar archive, assume it's a regular text file
    decoded_data = uncompressed_data.decode('utf-8')
    print(f"Decoded data:\n{decoded_data}")
