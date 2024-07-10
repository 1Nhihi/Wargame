# Derange
Chall: [Derange](https://ctf.viblo.asia/puzzles/derange-qmwigmmdxks)

từ code của bài mình viết được code để reverse flag ban đầu là `RmxhZ3tIYTRoNGFoNDRfZnVubnlfajBrM19Zb3VfZ090X20zIX0=`
nhìn thấy thấy quen quen biết đc nó đã base 64 rồi nên decode tiếp thì có được flag đúng với format rồi nè:

script:

```py
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
# RmxhZ3tIYTRoNGFoNDRfZnVubnlfajBrM19Zb3VfZ090X20zIX0=
# Flag{Ha4h4ah44_funny_j0k3_You_gOt_m3!} 
```

> 🚩:` Flag{Ha4h4ah44_funny_j0k3_You_gOt_m3!} `