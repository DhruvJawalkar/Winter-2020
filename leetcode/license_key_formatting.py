class Solution:
def licenseKeyFormatting(self, S: str, K: int) -> str:
    S = S.replace('-','')
    reversed_s = S[::-1]
    arr = [reversed_s[i:i+K] for i in range(0,len(reversed_s), K)]
    res = '-'.join([str(i).upper() for i in arr])
    res = res[::-1]
    return res
