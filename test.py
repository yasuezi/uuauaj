#!/bin/bash

# Ganti dengan detail pendaftaran
USERNAME="your_username" # Ganti dengan username
PASSWORD="your_password"  # Ganti dengan password
EMAIL="your_email@example.com" # Ganti dengan email
PASSWORD1="$PASSWORD" # Konfirmasi password, sama dengan password

# URL endpoint untuk pendaftaran
URL="https://tmtunnels.tech/execsignup.php" # Ganti dengan URL API yang sesuai

# Menyusun data yang akan dikirim
DATA="username=$USERNAME&password=$PASSWORD&email=$EMAIL&password1=$PASSWORD1" # Pastikan field sesuai yang dibutuhkan

# Kirim permintaan POST menggunakan curl
response=$(curl -s -X POST "$URL" \
  -H "Accept: */*" \
  -H "Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "Sec-CH-UA: \"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"89\", \"Google Chrome\";v=\"89\"" \
  -H "Sec-CH-UA-Mobile: ?1" \
  -H "Sec-CH-UA-Platform: \"Android\"" \
  -H "Sec-Fetch-Dest: empty" \
  -H "Sec-Fetch-Mode: cors" \
  -H "Sec-Fetch-Site: same-origin" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: PHPSESSID=6bda3581df99ed6e0f39c02ef79bb1a3" \
  -H "Referer: https://tmtunnels.tech/signup" \ # Ganti dengan referer yang sesuai
  -d "$DATA")

# Menampilkan respon
echo "Response: $response"
