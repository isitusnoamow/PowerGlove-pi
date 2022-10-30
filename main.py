from gpiozero import Button

NULL_CHAR = chr(0)

zButton = Button(2)
zCode = NULL_CHAR
xButton = Button(3)
xCode = NULL_CHAR
wButton = Button(4)
wCode = NULL_CHAR
aButton = Button(14)
aCode = NULL_CHAR
sButton = Button(15)
sCode = NULL_CHAR
dButton = Button(18)
dCode = NULL_CHAR


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

while True:
    if zButton.is_pressed:
        zCode = chr(29)
    else:
        zCode = NULL_CHAR

    if xButton.is_pressed:
        xCode = chr(27)
    else:
        xCode = NULL_CHAR

    if wButton.is_pressed:
        wCode = chr(26)
    else:
        wCode = NULL_CHAR

    if aButton.is_pressed:
        aCode = chr(4)
    else:
        aCode = NULL_CHAR

    if sButton.is_pressed:
        sCode = chr(22)
    else:
        sCode = NULL_CHAR

    if dButton.is_pressed:
        dCode = chr(7)
    else:
        dCode = NULL_CHAR

    write_report(NULL_CHAR*2+zCode+xCode+wCode+aCode+sCode+dCode)