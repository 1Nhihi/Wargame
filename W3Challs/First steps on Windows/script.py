byte_B586A8 = [0xb9, 0xb2, 0x6a, 0xe, 0xcb, 0xa4, 0x7a, 0x97, 0xea, 0x6e, 0xed, 0xd8, 0x82, 0xc9, 0xe1, 0x71, 0x2f, 0x38, 0x7d, 0x7b, 0xc8, 0x69, 0xb8, 0xb0, 0x86, 0xf3, 0x57, 0x2f, 0xeb, 0xcc, 0xc5, 0xe2, 0x7b]
byte_B58684 = [0xee, 0x81, 0x29, 0x75, 0x9c, 0x97, 0x16, 0xf4, 0xda, 0x3, 0xde, 0xf8, 0xd5, 0xf8, 0xd6, 0x19, 0xf, 0x6f, 0x4c, 0x15, 0xac, 0x59, 0xcf, 0x85, 0xa6, 0xb0, 0x25, 0x1b, 0x88, 0xa7, 0xa8, 0xd1, 0x6]

print("".join(chr(byte_B58684[i] ^ byte_B586A8[i]) for i in range(len(byte_B58684))))

# W3C{W3lc0m3 W17h W1nd0w5 Cr4ckm3}