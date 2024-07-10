![image](https://github.com/1Nhihi/Wargame/assets/127366803/d7f5c18a-2f75-43e9-8462-007155d5f8b7)![image](https://github.com/1Nhihi/Wargame/assets/127366803/74c0c54c-1c4e-424b-910c-09320d28fb38)#  [Try hack me](https://tryhackme.com/r/room/reverselfiles)
## Crackme1
`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/99bb359a-5cee-44a9-815a-abbe4530e898)

> 🚩: `flag{not_that_kind_of_elf}`

## Crackme2
check IDA:

![image](https://github.com/1Nhihi/Wargame/assets/127366803/42ecd302-5683-4c37-8068-fc5a117be753)

biết được password cần tìm là `super_secret_password`

![image](https://github.com/1Nhihi/Wargame/assets/127366803/0596b36b-3edc-46b1-ac84-ce920eac4eb9)

> 🚩super secret password: `super_secret_password`
> 
> 🚩flag: `flag{if_i_submit_this_flag_then_i_will_get_points}`



## Crackme3
Check IDA biết được password được thay đổi qua `sub_80486B0` và so sánh với `a2`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/b857aa26-8cc8-41a3-a52a-905865723b07)

check `sub_80486B0` thì biết được nó là encode base64

=> password = decode Base64 của `s2`
>🚩: `f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5`
## Crackme4
check IDA: thì thấy nó check paramater của mình với giá trá trị cố định được tạo ra vậy nên đặt breakpoint tại chỗ so sánh  và biết được chuỗi so sánh đó là `my_m0r3_secur3_pwd`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/2cea8d6e-0d92-454d-a325-bb74569339b0)

>🚩: `my_m0r3_secur3_pwd`

## Crackme5
Check IDA:
![image](https://github.com/1Nhihi/Wargame/assets/127366803/3012ff34-6ea1-4e8d-9179-382ab0424167)

input được so sánh với `OfdlDSA|3tXb32~X3tX@sX`4tXtz`
>🚩input: `OfdlDSA|3tXb32~X3tX@sX`4tXtz` 
## Crackme6
Check IDA thì thấy từng ký tự của input được so sánh với ký tự có sẵn
![image](https://github.com/1Nhihi/Wargame/assets/127366803/79756241-0ae4-4576-bf41-5ca8fc43f47a)
vì mỗi lần so sánh cách không cách đều nhau nên không dùng idapython được nhưng tại chỉ có 8 ký tự nên cũng dễ để biết đc password cần tìm là `1337_pwd`
![image](https://github.com/1Nhihi/Wargame/assets/127366803/beb63dcc-5926-445d-9cf1-979800f8fb75)

>🚩: `1337_pwd` 
## Crackme7
Check IDA: 

chương trình cho mình các option mà nếu như nhập đúng thì nó hiện flag ra màn hình
![image](https://github.com/1Nhihi/Wargame/assets/127366803/11009420-3f59-4e6c-a495-788d91353044)



tại target của mình là tới `giveFlag` để lấy flag thôi nên mình không cần quan tâm cái mớ trên làm gì vậy nên mình đặt 2 breakpoint tại 2 chỗ so sánh và thay đổi ZF để tới thẳng `giveFlag` luôn 
![image](https://github.com/1Nhihi/Wargame/assets/127366803/e877e977-8e42-404e-b9ee-fc0d6ff0cb70)
>🚩: `flag{much_reversing_very_ida_wow}`

## Crackme8
check IDA:
![image](https://github.com/1Nhihi/Wargame/assets/127366803/a7d9250d-a395-4b37-a1f4-389e502fa998)
bài này thì chỉ cần hiểu được cách cách tính số trong  hệ binary là ra rồi 
giá trị của của của input được lưu vào eax mà eax có độ lớn là 32 bit vì thế nên lớn nếu muốn giá trị nhập vào = 0x0CAFEF00D như ở trên đề bài thì chắc chắn nó là số âm (> 0x80000000) ==> giá trị cần tìm là bù 2 của 0x0CAFEF00D ( = -889262067)
check password

![image](https://github.com/1Nhihi/Wargame/assets/127366803/1ca777c3-d00d-464c-bc4d-fa3a14bece51)

>🚩 Flag:  `flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}`


-----------Cờ Lia-----------
