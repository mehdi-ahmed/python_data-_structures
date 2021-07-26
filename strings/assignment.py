text = "X-DSPAM-Confidence:    0.8475"

first_section = text.find(":")
second_section = text[first_section + 1:]  # '    0.8475'
print(float(second_section.lstrip()))
