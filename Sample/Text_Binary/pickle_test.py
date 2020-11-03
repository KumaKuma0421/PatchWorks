import pickle
import base64

file_path = r"C:\Users\User01\Sources\GitHub\PatchWorks\Sample\Text_Binary"
image_file = file_path + "\\" + "python-logo.png"
encode_file = file_path + "\\" + "serialize.txt"
decode_file = file_path + "\\" + "python-logo3.png"

with open(image_file, 'br') as f:
    binary_image = f.read()

serialized_image = pickle.dumps(binary_image)
encoded_image = base64.b64encode(serialized_image)
decoded_text = encoded_image.decode()

with open(encode_file, 'w') as f:
    f.write(decoded_text)

with open(encode_file, 'r') as f:
    file_contents = f.read()

decoded_image = base64.b64decode(file_contents.encode())
image = pickle.loads(decoded_image)
with open(decode_file, 'bw') as f:
    f.write(image)