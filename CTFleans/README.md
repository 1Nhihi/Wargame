# [CTFLeans](https://ctflearn.com/)
## [Basic Android RE 1 ](https://ctflearn.com/challenge/962)

Check apk với jadx 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/346fb8a6-1771-49e8-8459-3b4c12924ebc)


và sử dụng [tool ](https://hashes.com/en/decrypt/hash) để tim đoạn bị mã hóa md5 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/c9c8d1e4-a542-4a56-b7a5-2e85a2b2f6d8)


> 🚩flag là: `CTFlearn{Spring2019_is_not_secure!}`

## [Pin](https://ctflearn.com/challenge/379)
Check IDA biết được hàm check `Masukan PIN` là `cek`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/4647b5bd-a093-4c7c-b53c-1f8961fe89ff)

nhảy vào hàm `cek` thì biết hàm check `Masukan Pin ` với `333333`
![image](https://hackmd.io/_uploads/ByEX_-aw0.png)
> 🚩: `333333`


## [RE_verseDIS](https://ctflearn.com/challenge/188)

khi chạy file thì chương trình bảo nhập vào password và out là trả về "Good job dude !!!" hay  "Wrong password" 
vì thế nên nhảy vào ida để check 
![image](https://hackmd.io/_uploads/rJrmyMTwA.png)

nhìn sơ qua thì tìm được password đúng thì `stat`  phải = 1  nhìn lên tại `0x00055555540081C` giá trị của `input == msg`
và giá trị của `msg` lại được khởi tạo tại `loc_55555540077A` vì thế nên đặt 1 BP sao khi khởi tạo xong `msg` và debug vì biết được giá trị của `msg` là `'AbCTF{r3vers1ng_dud3}'`

> 🚩: `AbCTF{r3vers1ng_dud3}`


## [Reykjavik](https://ctflearn.com/challenge/990)
chạy thử chương trình 
![image](https://hackmd.io/_uploads/ryHL5bavC.png)

vậy nên ném vào IDA và debug với một para

thì thấy nó so sành từng ký tự của para và 1 ký tự có sẵn thế nên đặt 1 BP tại cmp và xem chuỗi đó luôn nè
![image](https://hackmd.io/_uploads/BkgysW6PC.png)
 >🚩: `CTFlearn{Eye_L0ve_Iceland_}`


## [Riyadh](https://ctflearn.com/challenge/991) 

chương trình cũng bắt nhập vào 1 para là flag giống bài "Reykjavik"
nhảy vào IDA 
nhìn sơ qua thì thấy được tại `00005555555551FB test    r12d, r12d` (điểm đặt BP) check xem flag của mình đã đúng chưa 
flag đúng khi r12 = 0 <- tại `00005555555551B4 add     r12d, edx` edx phải luôn = 0  <- `00005555555551AD setnz   dl` cờ ZF luôn = 1 <- `00005555555551A8 cmp     [rbp+rax+0], sil` 
- `sil` là flag nhập vào 
- `[rbp+rax+0]` là giá trị có thể check bằng cách đặt BP 
- cộng với điều kiện chuỗi nhập vào có len = 0x1E (ô màu trắng)
![image](https://hackmd.io/_uploads/B1P0dM6v0.png)



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



