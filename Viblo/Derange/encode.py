# def f(t):
#     c = list(t)
#     for i in range(len(t)):
#         for j in range(i, len(t) - 1):
#             c[j], c[j+1] = c[j+1], c[j]
#     return "".join(c)
    
# if __name__ == "__main__":
#     flag = open("flag.txt", "r").read()
#     open("ciphertext.txt", "w").write(f(flag))


# --------------------------
import base64

flag = open("ciphertext.txt", "r").read()
a = list(flag)

for i in range(len(a)-1, -1,-1):
    for j in range(len(a)-2, i-1, -1):
        a[j], a[j+1] = a[j+1], a[j]
    
print("".join(i for i in a))
a  = ''.join(a)

decoded_bytes = base64.b64decode(a)
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)

