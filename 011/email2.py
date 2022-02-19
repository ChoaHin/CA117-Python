test = "chee.choa2@g=mail.dcu.ie"

def email(s):
    [left, _] = s.split('@')
    left = left.strip('0123456789')
    [fname, sname] = left.split('.')
    return ' '.join([fname.capitalize(), sname.capitalize()])

print(email(test)) 