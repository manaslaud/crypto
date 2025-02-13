import hmac
import hashlib
def md5_mac(key:bytes, message:bytes)->str:
    return hmac.new(key, message, hashlib.md5).hexdigest()
key=b'Manas'
message=b'this is a test message'
mac=md5_mac(key,message)
print("md5-mac",mac)
print(message)
