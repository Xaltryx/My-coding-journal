str = 'X-DSPAM-Confidence: 0.8475'
colon_index = str.find(":")
number = float(str[colon_index+1:].strip())
print(number)