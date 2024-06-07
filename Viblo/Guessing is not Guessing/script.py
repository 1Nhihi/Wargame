from pwn import *

# Đặt IP và cổng
host = '172.104.49.143'
port = 9234

# Tạo kết nối tới máy chủ
conn = remote(host, port)

# Gửi dữ liệu (chuyển chuỗi thành bytes)
# conn.sendline(b'Hello, server!')

# Đọc dữ liệu phản hồi từ máy chủ (nếu cần)
response = conn.recvline()
print(response.decode())
response = conn.recvline()

conn.sendline(str('0'))
response = conn.recvline()


low = 0
high = 18446744073709551616
tries = 70

for _ in range(tries):
    guess = (low + high) // 2
    print(guess, low, high)
    conn.sendline(str(guess))  # nhập guess về  server
    
    # Receive and process the response
    response = conn.recvline().decode().strip()
    if response[:22] == 'Your guess is too high':
        high = guess - 1
    elif response[:21] == 'Your guess is too low':
        low = guess + 1
    else:
        print(response)
        response = conn.recvline()
        print(response)
        break

# Đóng kết nối
conn.close()
