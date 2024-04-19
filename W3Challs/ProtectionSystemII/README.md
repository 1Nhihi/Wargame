# ProtectionSystem II
Chall: [ProtectionSystem II](https://w3challs.com/challenges/reversing/protectionsystem_ii)

chạy challange thì biết đc chương trình bảo login và nhập password

![image](https://github.com/1Nhihi/nhap/assets/127366803/8d74badf-0586-4366-b53f-f52a2fc61b2a)

load vào ida 

trong `main_0`
hàm này check độ dài và ký tự của chuỗi mình nhập có thỏa mãn là độ dài có nằm trong đoạn [5,8] và các ký tự có phải là chữ thường không

![image](https://github.com/1Nhihi/nhap/assets/127366803/4890d759-8554-4c8e-9752-d49a74ea8015)


sau khi check chiều dài và ký tự thương, chương trình tính giá trị của `login` quan `cal0` và so sánh giá trị với `password` qua `cal1`
![image](https://github.com/1Nhihi/nhap/assets/127366803/6a7dddc4-bec6-47e1-a98f-c46efb460c23)

và chuỗi cùng chạy hàm `sub_40101E` để in ra kết quả thôi nè
![image](https://github.com/1Nhihi/nhap/assets/127366803/527b0159-382c-4d5a-a4d1-5acdc3704c5e)


mà trong hàm `sub_40101E` :
- tổng ký tự của `login` = tổng của `password`
- yêu cầu các ký tự của `login` và `password` không được giống nhau
- các ký tự của của `login` cũng không đc giống ký tự cúa `password`
- và có thêm một hàm là điều kiện của `password` nữa 

==> có được code của bài là [chall](chall.py)

bài này có quá trời điều kiện mình ngồi nghĩ quá trời và rồi mình dùng `z3` luôn cho nhanh :v 
thì có được [script](script.py) mình bay vào web đề để submit và có được flag rồi nè hihi


![image](https://github.com/1Nhihi/nhap/assets/127366803/f12fea36-8765-4061-bdfd-d4f6fea6b980)

> 🚩: `W3C{IalwaysLovedCrackmes}`
