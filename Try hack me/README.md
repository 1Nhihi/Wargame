#  [Try hack me](https://tryhackme.com/r/room/reverselfiles)
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
## Crackme5
## Crackme6
## Crackme7
## Crackme8
