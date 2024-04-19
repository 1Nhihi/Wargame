# Wargame


```
Random number: 0x5c49cfd0
Input? 559252698
Result: a0b4c1d7
Congrats!
DH{cc0017076ad93f32c8aaa21bea38af5588d95d2cdc9cf48760381cc84df4668e}
```
![image](https://github.com/1Nhihi/Wargame/assets/127366803/49ea7f3a-4bc8-4caf-8486-6471940b8a72)

![image](https://github.com/1Nhihi/Wargame/assets/127366803/1f1de2fb-4a5a-477a-900c-334be3536add)



write up: 
# rev-basic-2

như thường lệ thì kiểm tra file và chạy thử file nè
![image](https://github.com/1Nhihi/Wargame/assets/127366803/8396626a-f60a-47ad-acee-46704ce96ccb)
thầy file yêu cầu nhập vào input và hiểu thị là cái input mình nhập vào đã đúng chưa nè 
vì thế nên ném vào ida 
đề nó như thế này

![image](https://github.com/1Nhihi/Wargame/assets/127366803/b4de6e90-84cb-4ef6-af68-57bf424df214)
biết được là chương trình kiểm tra file mình nhập qua hàm `sub_140001000` 
nhảy vào vào xem thì biết được nó so sánh với giá trị của một mảng có sẵn
![image](https://github.com/1Nhihi/Wargame/assets/127366803/02fd281f-6b1a-49ae-8587-ebd9861d7960)

vì thế nên các ký tự của `*aC` là pass cần tìm rồi nè hihi
dùng idapython để tìm nhanh hơn (shift f2)
```
print("hihi")
for i in range(0x12):
    print(chr(idc.get_wide_byte(0x0000000140003000 +i*4)), end = "")
#Comp4re_the_arr4y
```
kết hợp với format của dreamhack nữa là có được flag rồi nè:
>🚩 flag là: "DH{Comp4re_the_arr4y}" 

# Simple Crack Me
`DH{322376503}`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/5de58756-a7aa-4246-bc83-a785b182bd39)


# ProtectionSystem II
![image](https://github.com/1Nhihi/Wargame/assets/127366803/1b343e66-e18a-4c46-8559-2f6360344fee)
