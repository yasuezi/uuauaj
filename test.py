import requests

def auto_sign_up(username, password, email, password1):
    # URL endpoint signup TMTunnel
    url = "https://tmtunnels.tech/execsignup.php"  # Ganti dengan URL endpoint signup yang benar

    # Data yang akan dikirim
    data = {
        'username': username,
        'password': password,
        'email': email,
        'password1': password1
    }

    # Header yang diperlukan
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
        "x-requested-with": "XMLHttpRequest"
    }

    try:
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()  # Meningkatkan pengecualian untuk status kesalahan HTTP
        print("Pendaftaran berhasil:", response.json())  # Output hasil berhasil
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan:", e)  # Menangani kesalahan

if __name__ == "__main__":
    # Mengambil input dari pengguna
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    email = input("Masukkan email: ")
    password1 = input("Masukkan ulang password: ")

    auto_sign_up(username, password, email, password1)
