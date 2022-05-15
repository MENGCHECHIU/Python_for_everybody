text = "X-DSPAM-Confidence:    0.8475"
bgn=text.find("0")
last=text.find("5",bgn)
print(float(text[bgn:last+1]))