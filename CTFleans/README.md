# [CTFLeans](https://ctflearn.com/)
## [Basic Android RE 1 ](https://ctflearn.com/challenge/962)

Check apk với jadx 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/346fb8a6-1771-49e8-8459-3b4c12924ebc)


và sử dụng [tool ](https://hashes.com/en/decrypt/hash) để tim đoạn bị mã hóa md5 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/c9c8d1e4-a542-4a56-b7a5-2e85a2b2f6d8)


> 🚩flag là: `CTFlearn{Spring2019_is_not_secure!}`

## [Pin](https://ctflearn.com/challenge/379)
Check IDA biết được hàm check `Masukan PIN` là `cek`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/a0a10af7-5655-41a8-a252-fbc7d14de4d3)


nhảy vào hàm `cek` thì biết hàm check `Masukan Pin ` với `333333`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/e3b21aec-4e2c-4d67-a1ff-ac42c7a5be89)

> 🚩: `333333`


## [RE_verseDIS](https://ctflearn.com/challenge/188)

khi chạy file thì chương trình bảo nhập vào password và out là trả về "Good job dude !!!" hay  "Wrong password" 
vì thế nên nhảy vào ida để check 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/e1219aa6-6ca4-408f-aaa2-f27496338d6e)


nhìn sơ qua thì tìm được password đúng thì `stat`  phải = 1  nhìn lên tại `0x00055555540081C` giá trị của `input == msg`
và giá trị của `msg` lại được khởi tạo tại `loc_55555540077A` vì thế nên đặt 1 BP sao khi khởi tạo xong `msg` và debug vì biết được giá trị của `msg` là `'AbCTF{r3vers1ng_dud3}'`

> 🚩: `AbCTF{r3vers1ng_dud3}`


## [Reykjavik](https://ctflearn.com/challenge/990)
chạy thử chương trình 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/b049abc9-96e3-43cc-adec-4a2aa7c3ec82)


vậy nên ném vào IDA và debug với một para

thì thấy nó so sánh từng ký tự của para và 1 ký tự có sẵn thế nên đặt 1 BP tại cmp và xem chuỗi đó luôn nè
![image](https://github.com/1Nhihi/Wargame/assets/127366803/dfa3b538-ff06-4a10-9ac4-7c243b99da04)

 >🚩: `CTFlearn{Eye_L0ve_Iceland_}`


## [Riyadh](https://ctflearn.com/challenge/991) 

chương trình cũng bắt nhập vào 1 para là flag giống bài "Reykjavik"
nhảy vào IDA 
nhìn sơ qua thì thấy được tại `00005555555551FB test    r12d, r12d` (điểm đặt BP) check xem flag của mình đã đúng chưa 
flag đúng khi r12 = 0 <- tại `00005555555551B4 add     r12d, edx` edx phải luôn = 0  <- `00005555555551AD setnz   dl` cờ ZF luôn = 1 <- `00005555555551A8 cmp     [rbp+rax+0], sil` 
- `sil` là flag nhập vào 
- `[rbp+rax+0]` là giá trị có thể check bằng cách đặt BP 
- cộng với điều kiện chuỗi nhập vào có len = 0x1E (ô màu trắng)
![image](https://github.com/1Nhihi/Wargame/assets/127366803/61c8bf27-affd-4385-bbb6-1db39efdec7a)




>🚩flag là: `CTFlearn{Masmak_Fortress_1865}`

## [Time to Eat](https://ctflearn.com/challenge/743)
bài này tác giả cố tình để mình khó nhìn bằng cách đổi các hàm hay dùng của python = `eat` 
```
EAT = int
eAT = len
EaT = print
ATE = str
EATEATEATEATEATEAT = ATE.isdigit
```
nhìn đơn giản thì chỉ cần quan tâm tới hàm `Eat` để "absolutely EATEN!!!" thì input nhập vào có
- độ dài = 9 
- 3 tự tự đầu, 3 tứ tự cuối là số 
- và eateat == "E10a23t9090t9ae0140"


vì thế nên chỉ cần tập trung vào điều kiện cuối cùng thôi
eateat = EAt(eaT(eat), Ate(aTE(aten(eat))))

- hàm eaT trả về chuỗi: "int(3 ký tự đầu) * 3" + chuỗi eat đảo ngược (eat[::-1])
- và hàm EAt chỉ là xếp cách ký tự 2 para trả về chuỗi 1 ký tự của para2 + 2 ký tự của para1 thôi

==> chuỗi cần tìm là: `341eat009`
nhập nó vào chương trình là lấy flag thôi 😁

>🚩: `CTFlearn{ eaten_341eat009 }`



## [Riga ](https://ctflearn.com/challenge/996) 

tương tự những bài trên chương trình bảo nhập vào một parameter là flag và kiểm tra xem flag mình nhập vào đã đúng chưa

![image](https://github.com/user-attachments/assets/633d65d8-cc2a-4836-b861-acc9ab213bd4)



nhập đại một chuỗi làm param và chạy chương trình thì biết được hàm chương trình xor các ký tự của chuỗi vừa nhập với 0xDE và nhảy vào hàm `_Z13BlackRyeBreadv` trong hàm này có 1 antidebug ta pass qua nó bằng cách thay đổi `ZF` khi đó giá trị của `beerEmbassy == 2`  vì vậy nên khi xuống dưới nó nhảy vào hàm `_Z10HerbalTea2Pc`
 để flag nhập vào đúng thì hàm vừa rồi phải return về 1 nhảy vào hàm    `_Z10HerbalTea2Pc` kiểm tra
![image](https://github.com/user-attachments/assets/1979fe24-482d-434d-a7a4-d99db0f37d47)


mới vào chương trình gặp thêm 1 antidebug `_gettimeofday` pass qua nó thì chương trình xor các ký tự ngược lại với 0xDE để trả về chuỗi ban đầu sau đố tính tính với mỗi ký tự và đem so sánh với mảng `pickles0` để print ra  `aCongratulation` hay `aSorryYouDidNot`

đề bài sau khi viết lại:
```py

inp = input('flag: ')
pickles2 =[0x9d, 0xac, 0x92, 0xeb, 0xb3, 0xbf, 0xed, 0xe9, 0xe4, 0x97, 0xb9, 0x94, 0xe8, 0xe1, 0xb3, 0xb9, 0x94, 0xbf, 0xe3, 0xe1, 0xb7, 0xbf, 0xff, 0xfa]

result = 1

if len(inp) != 24:
    print('a')
    result = 0

inp = [ord(i) for i in inp]
for i in range(len(inp)):
    if (inp[i] + 19) > 0x7e:
        if (inp[i] - 76) ^ 0xCB != pickles2[i]:
            print('b')
            result = 0
    elif (inp[i] + 19) < 0x20:
        if ((inp[i] + 114)^ 0xCB ) != pickles2[i]:
            result = 0
            print('c')
    else:
        if ((inp[i] + 19)^ 0xCB ) != pickles2[i]:
            result = 0
            print(i)


if result:
    print("Congratulations!! You found the flag")
else:
    print( "Sorry, you did not find the flag ")

print(''.join(chr(i) for i in inp))

```

script của bài là:
```py
pickles2 =[0x9d, 0xac, 0x92, 0xeb, 0xb3, 0xbf, 0xed, 0xe9, 0xe4, 0x97, 0xb9, 0x94, 0xe8, 0xe1, 0xb3, 0xb9, 0x94, 0xbf, 0xe3, 0xe1, 0xb7, 0xbf, 0xff, 0xfa]

for i in pickles2:
    x = ((i ^ 0xCB) - 19 )
    if x <  0x20:
        x += 114
        x -= 19
    print(chr(x), end = '')

#CTFlearn{I_Love_Latvia!}
```
>🚩: `CTFlearn{I_Love_Latvia!} `

## [Reverse Me](https://ctflearn.com/challenge/989) 

chạy chương trình thì nó bảo nhập vào flag và in ra `Incorrect` hoặc `Correct` nhảy vào IDA  kiểm tra thì biết được đề bài viết ngắn lại như sau:
```py
inp = input('enter the flag: ')
v5 = [1,3,3,7,222,173,190, 239,]
inp = [ord(i) for i in inp]
for i in range(len(inp)):
    inp[i] ^= v5[i % 8]


b = []
for i in range(1, len(inp), 2):
    b.append(inp[i])
    b.append(inp[i-1])

target = [0x57, 0x42, 0x4b, 0x45, 0xcc, 0xbb, 0x81, 0xcc, 0x71, 0x7a, 0x71, 0x66, 0xdf, 0xbb, 0x86, 0xcd, 0x64, 0x6f, 0x6e, 0x5c, 0xf2, 0xad, 0x9a, 0xd8, 0x7e, 0x6f]
if b == target:
    print('Correct')
else:
    print('Incorrect')

```

từ đó viết được sờ cờ ríp

```py

target = [0x57, 0x42, 0x4b, 0x45, 0xcc, 0xbb, 0x81, 0xcc, 0x71, 0x7a, 0x71, 0x66, 0xdf, 0xbb, 0x86, 0xcd, 0x64, 0x6f, 0x6e, 0x5c, 0xf2, 0xad, 0x9a, 0xd8, 0x7e, 0x6f]

b = []
for i in range(1, len(target), 2):
    b.append(target[i])
    b.append(target[i-1])

v5 = [1,3,3,7,222,173,190, 239,]
# a = [ord(i) for i in a]
for i in range(len(b)):
    b[i] ^= v5[i % 8]
print(''.join(chr(i) for i in b))

# CTFLearn{reversing_is_fun}
```
>🚩:`CTFLearn{reversing_is_fun}`


