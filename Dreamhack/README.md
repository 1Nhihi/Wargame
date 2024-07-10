# Derange
## [rev-basic-0](https://dreamhack.io/wargame/challenges/14)

check IDA: 

![image](https://github.com/1Nhihi/Wargame/assets/127366803/71f7e9e9-eff2-439c-9116-679d7e04b84a)

chương chình check input nhập vào qua `sub_140001000`, nhảy vào `sub_140001000` thì biết được nó so sánh input với "Compar3_the_str1ng"
> 🚩flag: `DH{Compar3_the_str1ng}`

## [rev-basic-1](https://dreamhack.io/wargame/challenges/15)
check IDA:
![image](https://github.com/1Nhihi/Wargame/assets/127366803/7ea0ebf2-eacb-4923-ad80-52998eb30796)

biết được chương trình check input nhập vào qua `sub_140001000` nhảy vào `sub_140001000` thì thấy chương trình so sánh từng ký tự của input với giá trị cho trước

![image](https://github.com/1Nhihi/Wargame/assets/127366803/4e5259e5-687c-455c-ae10-6ea430e5f3a8)

nhìn sơ thì biết được địa chỉ của mỗi lần so sánh cách đều nhau nên sửa dụng idapython để in ra cho nhanh nè (ở đây mình thay ký tự `h` băng `0x` luôn để tí dùng python chon nhanh

```py
for i in range(0x0000000140001017, 0x0000000140001230, 0x1e):
    print("0x"+ idc.print_operand(i,1)[:-1], end  = ", ")

for i in range(0x0000000140001230, 0x0000000140001269, 0x1b):
    print("0x" + idc.print_operand(i,1)[:-1], end  = ", ")
```
được chuỗi a:
ném vào py:
```
a = [0x43, 0x6F, 0x6D, 0x70, 0x61, 0x72, 0x33, 0x5F, 0x74, 0x68, 0x65, 0x5F, 0x63, 0x68, 0x34, 0x72, 0x61, 0x63, 0x74, 0x33, 0x72]
print("".join(chr(i) for i in a))
#Compar3_the_ch4ract3r
```
> 🚩flag:  `Compar3_the_ch4ract3r`
## [rev-basic-2](https://dreamhack.io/wargame/challenges/16)

check IDA:

