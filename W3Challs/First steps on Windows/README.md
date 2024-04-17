# First steps on Windows
Chall: [First steps on Windows](https://w3challs.com/challenges/reversing/first_steps_on_windows)


bài này bài khá đơn giản 

có 1 antidebug ở đây 
![image](https://github.com/1Nhihi/nhap/assets/127366803/63d89fb9-f2cc-4cb7-ae76-5c20b6c9451c)

Debug xuống dưới thì biết được nó xor giá trị của từng ký tự mình nhập vào, mảng `byte_B58684` và `byte_B586A8`
rồi or kết quả với 0 để check giá trị nhập vào có đúng hay không nè 
![image](https://github.com/1Nhihi/nhap/assets/127366803/86d5b60d-1976-413c-b024-43baf66b76ff)

> 🚩: `W3C{W3lc0m3 W17h W1nd0w5 Cr4ckm3}`
