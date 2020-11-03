#
# sa https://www.python.ambitious-engineer.com/archives/2066
# sa https://note.nkmk.me/python-textwrap-wrap-fill-shorten/
#
import base64
import textwrap

file_path = r"C:\Users\User01\Sources\GitHub\PatchWorks\Sample\Text_Binary"
image_file = file_path + "\\" + "python-logo.png"
encode_file = file_path + "\\" + "encode.txt"
decode_file = file_path + "\\" + "python-logo2.png"

with open(image_file, 'br') as f:
    base64_image = base64.b64encode(f.read())
# print(base64_image) # この時点ではまだ、b'iVBOrw...'というバイナリデータ

wrapped_text = textwrap.fill(base64_image.decode(), 70) # decode()でテキスト化
print(wrapped_text)
print("-" * 70)

with open(encode_file, 'w') as f:
    #f.write(base64_image.decode())  # decode()でテキスト化される
    f.write(wrapped_text) # 折り曲げたまま出力... CRLF出力でした

with open(encode_file, 'r') as f:
    file_contents = f.readlines() # 行単位で配列で取得する EOFはLFだけ
# \nで改行されたままのstr変数をそのままエンコードしても問題ないようだが...
base64_text = '\n'.join(file_contents)
print(base64_text)
print("-" * 70)

# encode()でテキスト→バイナリ、decode()で復号化
image = base64.b64decode(base64_text.encode())
with open(decode_file, 'bw') as f:
    f.write(image)
