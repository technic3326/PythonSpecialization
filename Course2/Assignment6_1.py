
# Assignment 6.1
text = "X-DSPAM-Confidence:    0.8475";
position = text.find('0')
number = text[position:]
print float(number)