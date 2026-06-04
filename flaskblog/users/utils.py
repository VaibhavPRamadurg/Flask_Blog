import os
import secrets
from PIL import Image
from flask import url_for, current_app
import resend

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext= os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(current_app.root_path, 'static/profile', picture_fn)
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    url = url_for('users.reset_token', token=token, _external=True) 
    
    
    resend.api_key = current_app.config.get('RESEND_API_KEY')
    
    params = {
        "from": 'onboarding@resend.dev',
        "to": [user.email],
        "subject": "Password Reset Request",
        "html": f"""
            <p>To reset your password, click the link below:</p>
            <a href="{url}">Reset Password</a>
            <p>If you did not make this request, simply ignore this email.</p>
        """
    }

    try:
        resend.Emails.send(params)
    except Exception as e:
        print(f"Error sending email: {e}")