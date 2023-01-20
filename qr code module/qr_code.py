import qrcode
code = "shivansh "
img  = qrcode.make(code)
img.save("your_message.png")
