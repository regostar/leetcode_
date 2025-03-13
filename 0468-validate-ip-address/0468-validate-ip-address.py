class Solution:
    def validateIPv4(self, queryIP):
        nums = queryIP.split('.')
        for x in nums:
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            if x[0] == '0' and len(x) != 1:
                # no leading 0s
                return "Neither"
            if not x.isdigit():
                # only digits allowed
                return "Neither"
            if int(x) > 255:
                # <= 255
                return "Neither"
        return "IPv4"
    
    def validateIPv6(self, IP):
        nums = IP.split(":")
        hexdigits = "0123456789abcdefABCDEF"
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexsigits in one chunk
            if len(x) == 0 or len(x) > 4:
                return "Neither"
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            for ch in x:
                if ch not in hexdigits:
                    return "Neither"
        return "IPv6"



    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(".") == 3:
            return self.validateIPv4(queryIP)
        elif queryIP.count(":") == 7:
            return self.validateIPv6(queryIP)
        else:
            return "Neither"