# Old Computer
Chall: [Old Computer](https://ctf.viblo.asia/puzzles/old-computer-xolsw8q1cb0)

run file:

![image](https://github.com/1Nhihi/Wargame/assets/127366803/a8d05548-dd5b-42e4-b589-aef268548924)
sau khi run file và tên của challenge thì mình nghĩ file phải chạy với hệ điều hành bé hơn cái win11 mình đang sài rồi vì thế ném vào ida để check luôn 

check hàm `main`, `sub_4005F6` và `sub_40061F`
==> sờ cờ ríp của bài là:
```python
v7 = [0] * 21
v7[0] = 217;
v7[1] = 254;
v7[2] = 197;
v7[3] = 244;
v7[4] = 158;
v7[5] = 199;
v7[6] = 155;
v7[7] = 220;
v7[8] = 231;
v7[9] = 210;
v7[10] = 244;
v7[11] = 147;
v7[12] = 254;
v7[13] = 255;
v7[14] = 244;
v7[15] = 158;
v7[16] = 222;
v7[17] = 249;
v7[18] = 206;
v7[19] = 231;
v7[20] = 210; 
print("".join(chr(i^ 171) for i in v7))
# rUn_5l0wLy_8UT_5uReLy
```

> 🚩:   `Flag{rUn_5l0wLy_8UT_5uReLy}`