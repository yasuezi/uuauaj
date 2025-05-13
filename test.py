import requests

# URL endpoint untuk registrasi
url = "https://tmtunnels.tech/execsignup.php"  # Ganti dengan URL API registrasi yang sesuai

# Data yang akan dikirim dalam form
data = {
    'username': 'your_username',  # Ganti dengan username yang diinginkan
    'password': 'your_password',    # Ganti dengan password yang diinginkan
    'email': 'your_email@example.com',  # Ganti dengan email yang valid
    'password1': 'your_password',  # Pastikan password1 cocok dengan password
}

# Header yang akan digunakan
headers = {
    "accept": "*/*",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"89\", \"Google Chrome\";v=\"89\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "PHPSESSID=6bda3581df99ed6e0f39c02ef79bb1a3",  # Ganti dengan cookie yang sesuai
    "Referer": "https://tmtunnels.tech/signup"  # Ganti dengan URL referer yang sesuai
}

# Mengirim request POST
response = requests.post(url, headers=headers, data=data)

# Menampilkan hasil response
print(response.status_code)
print(response.text)
