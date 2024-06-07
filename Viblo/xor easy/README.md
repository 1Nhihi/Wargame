# XOR easy
chall: [XOR easy](https://ctf.viblo.asia/puzzles/xor-easy-jisqsheiied)

với format của flag là `Flag{}` nên xor với ord('F') để tìm số xor thôi 
```py
a = "321815130f0c44062b1d072b07441911001c451a4d09"
a = [f"0x{a[i:i+2]}" for i in range(0, len(a), 2)]
a = [int(i,16) for i in a]

int_xor = a[0] ^ ord('F')
print(''.join(chr(int_xor ^ i) for i in a))

# Flag{x0r_is_s0meth1n9}
```

> 🚩: `Flag{x0r_is_s0meth1n9}`