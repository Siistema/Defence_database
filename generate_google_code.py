import time
import hmac
import hashlib
import base64


def google_auth(code, google_code):
    if code == genCode(google_code):
        return True


def genCode(code):
    ### TOTP-key (get it from Google)
    secret = base64.b32decode(code)
    #       MZXW633PN5XW6MZX
    ### Calc counter from UNIX time (see RFC6238)
    counter = int(time.time() / 30)

    ### Use counter as 8 byte array
    bytes = bytearray()
    for i in reversed(range(0, 8)):
        bytes.insert(0, counter & 0xff)
        counter >>= 8

    ### Calculate HMAC-SHA1(secret, counter)
    hs = bytearray(hmac.new(secret, bytes, hashlib.sha1).digest())

    ### Truncate result (see RFC4226)
    n = hs[-1] & 0xF
    result = (hs[n] << 24 | hs[n + 1] << 16 | hs[n + 2] << 8 | hs[n + 3]) & 0x7fffffff

    ### Print last 6 digits
    print(str(result)[-6:])
    return str(result)[-6:]
