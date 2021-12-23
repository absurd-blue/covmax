import sys
import qrcode

if len(sys.argv) < 2:
  exit(-1);

code = sys.argv[1];
link = f'https://covax-morph.pages.dev/impactmobile/vaccine/certificate?code={code}';

script = [];
with open('assets/impactmobile.js') as f:
  script = f.readlines();

# modify the script
script.insert(-2, f'  {code}: new Profile("ID", "name", "birthdate", [\n');
script.insert(-2, f'    new Vaccine("date : time", "site", "type", "lotnumber"),\n')
script.insert(-2, f'    new Vaccine("date : time", "site", "type", "lotnumber"),\n')
script.insert(-2, '  ]),\n')

# create qr code
qr = qrcode.QRCode(version=1, box_size=10, border=2)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

#save qr code
img.save(f'assets/images/qr/{code}.png')
print(f'wrote /assets/images/qr/{code}.png')

#save the script
with open('assets/impactmobile.js', 'w') as f:
  f.write(''.join(script));

print(f'wrote /assets/impactmobile.js')

print(" ______      ___   ____  _____  ________ ") 
print("|_   _ `.  .'   `.|_   \|_   _||_   __  |") 
print("  | | `. \/  .-.  \ |   \ | |    | |_ \_|") 
print("  | |  | || |   | | | |\ \| |    |  _| _ ") 
print(" _| |_.' /\  `-'  /_| |_\   |_  _| |__/ |") 
print("|______.'  `.___.'|_____|\____||________|") 
print("                                         ") 