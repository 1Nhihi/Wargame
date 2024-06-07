# Validatingggg
Chall: [Validatingggg](https://ctf.viblo.asia/puzzles/validatingggg-tviggg89q8z)

sau khi chạy thử file và ném vào IDA check thì mình biết được hàm check input nhập vào là đúng hay không là hàm này 


![image](https://github.com/1Nhihi/nhap/assets/127366803/66672199-f6f8-437f-b800-44b356b2dc28)


để tìm flag bài này thì mình brute force  kí tự đầu và tìm các ký tự tiếp theo theo quy luật hehe

```py
v3  = [0x65, 0x48, 0x41, 0x57, 0x6f, 0x5c, 0x6c, 0x66, 0x57, 0x48, 0x3b, 0x75, 0x68, 0x4e, 0x56, 0x50, 0x58, 0x3b, 0x3b, 0x68, 0x75, 0x3c, 0x3e, 0x3d, 0x75, 0x44, 0x5a, 0x46, 0x49, 0x3e, 0x6d]

arr = []
for bf in range(0x20, 0x7f):
	
	arr = []
	arr.append(chr(bf)) 
	for i in range(30):
		nx = chr((v3[i] - 59) ^ ord(arr[i]))
		arr.append(nx)
	print(''.join(k for k in arr))
# Flag{On_thee_razorrr_edge_VIBLO}
```

> 🚩:   `Flag{On_thee_razorrr_edge_VIBLO}`