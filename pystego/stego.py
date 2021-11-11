from PIL import Image
import numpy as np

def encode(src, msg, delimiter = '!@#$%'):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4    
    
    total_pixels = array.size//n

    msg +=  delimiter
    b_message = ''.join([format(ord(i), '08b') for i in msg])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print('ERROR: Need larger file size')

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(src)
        print(f'SUCCESS: Image Encoded Successfully @ {src}')

def decode(src, delimiter = '!@#$%'):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4    
        
    total_pixels = array.size//n

    hidden_bits = ''
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ''
    for i in range(len(hidden_bits)):
        if message[-5:] == delimiter:
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if delimiter in message:
        print(f"SUCCESS: Image Decoded Successfully @ {src}", message[:-5], sep='\n→ ')
        return message[:-5]
    else:
        print("FAILURE: No Hidden Message Found")