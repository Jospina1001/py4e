text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find('0')
host=text[atpos:100]
numero=float(host)
print(numero)
