import sys
import qrcode

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from stellar_base.keypair import Keypair
from stellar_base.utils import DecodeError

# Determine what kind of design user wants
d = sys.argv[1]

if d == "d1":
    design = Image.open("d1.png")
elif d == "d2":
    design = Image.open("d2.png")
elif d == "d3":
    design = Image.open("d3.png")
else:
    print("Invalid design parameter")
    exit()

# If random design
if len(sys.argv) == 2:
    # Make public/private keypair
    kp = Keypair.random()
elif len(sys.argv) == 3:
    # Get keypair from seed
    try:
        kp = Keypair.from_seed(sys.argv[2])
    except DecodeError:
        print("Unable to generate public key from private key. Is your private key correct?")
        exit()

pub = kp.address().decode()
priv = kp.seed().decode()    
pubqr = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=7,border=0)
pubqr.add_data(pub)
pubqr.make(fit=True)
pubqr = pubqr.make_image()

privqr = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=7,border=0)
privqr.add_data(priv)
privqr.make(fit=True)
privqr = privqr.make_image()

design.paste(pubqr,(56,370))
design.paste(privqr,(1448,44))
draw = ImageDraw.Draw(design)
font = ImageFont.truetype("ClearSans-Light.ttf",18)
draw.text((332,542),pub,(0,0,0),font=font)
design.save(pub+".png")
