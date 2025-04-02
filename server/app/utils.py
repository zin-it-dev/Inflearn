import hashlib, cloudinary.uploader, pyotp, qrcode, base64, os, random

from io import BytesIO
from urllib.parse import urlencode
from flask import request, session


def gravatar_url(email, size=40, default="identicon", rating="g"):
    digest = hashlib.sha256(email.lower().encode("utf-8")).hexdigest()
    params = urlencode({"d": default, "s": str(size), "r": rating})
    return f"https://www.gravatar.com/avatar/{digest}?{params}"


def upload_image(file_data):
    result = cloudinary.uploader.upload(file_data)
    return result.get("secure_url")


def handle_verify_totp(secret_key, totp_code):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(totp_code)


def generate_totp(user_id):
    secret_key = pyotp.random_base32()

    totp = pyotp.TOTP(secret_key)

    provisioning_uri = totp.provisioning_uri(
        name=f"user_{user_id}@gmail.com",
        issuer_name="Inflearn 인프런 🎓",
    )

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(provisioning_uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return secret_key, provisioning_uri, img_str


def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "en")


def generate_color_palette(amount):
    return [
        f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)"
        for _ in range(amount)
    ]
