import hashlib
def encode_base62(num):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321"

    str = ''
    num = int(num)
    while int(num)>0:
        str = key[int(num%62)]+str
        num=num/62
    print(str)
    # return str

encode_base62(50000000000)

# str="1"
# result = hashlib.sha256(str.encode())
# print(result.hexdigest())




