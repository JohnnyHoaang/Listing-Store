def encode_image(image):
    import base64
    image_base64 = base64.b64encode(image.image).decode()
    return image_base64

def image_to_binary(image_file):
    import io
    from PIL import Image
    image = Image.open(image_file)
    byte_arr = io.BytesIO()
    image.save(byte_arr, format=image.format)
    return byte_arr.getvalue()
