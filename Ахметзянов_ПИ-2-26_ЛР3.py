# 1
C = (input("1. Введите символ C: ").strip() or "A")[0]
print(ord(C))

# 2
N_str = input("2. Введите целое число N (1-26): ").strip()
N = int(N_str) if N_str.isdigit() and 1 <= int(N_str) <= 26 else 5
print(''.join(chr(ord('z') - i) for i in range(N)))

# 3
C = (input("3. Введите символ C: ").strip() or "B")[0]
print(chr(ord(C) - 1), chr(ord(C) + 1))

# 4
N_str = input("4. Введите целое число N (> 0): ").strip()
N = int(N_str) if N_str.isdigit() and int(N_str) > 0 else 5
C = (input("4. Введите символ C: ").strip() or "*")[0]
print(C * N)

# 5
S = input("5. Введите непустую строку S: ") or "Python"
print(' '.join(S))

# 6
S = input("6. Введите непустую строку S: ") or "Python"
N_str = input("6. Введите целое число N (> 0): ").strip()
N = int(N_str) if N_str.isdigit() and int(N_str) > 0 else 1
print(('*' * N).join(S))

# 7
S = input("7. Введите непустую строку: ") or "Python"
print(ord(S[0]), ord(S[-1]))

# 8
S = input("8. Введите строку: ")
print(S[::-1])

# 9
S = input("9. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
S_copy = S[:]
print(S_copy)

# 10
S = input("10. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[4])

# 11
S = input("11. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[-1])

# 12
S = input("12. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[:5])

# 13
S = input("13. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[-5:])

# 14
S = input("14. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[3:8])

# 15
S = input("15. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[-9:-4])

# 16
S = input("16. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[1::2])

# 17
S = input("17. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[1::2][::-1])

# 18
S = input("18. Введите строку (> 10 символов): ")
S = S if len(S) > 10 else S.ljust(11, '_')
print(S[-4:-9:-1])

# 19
S = input("19. Введите строку: ")
print(sum(c.isdigit() for c in S))

# 20
S = input("20. Введите строку: ")
print(sum('A' <= c <= 'Z' for c in S))

# 21
S = input("21. Введите строку: ")
print(''.join(c.lower() if 'A' <= c <= 'Z' else c for c in S))

# 22
S = input("22. Введите строку: ")
print(S.swapcase())

# 23
S = input("23. Введите целое положительное число: ").strip()
print(sum(int(c) for c in S if c.isdigit()))

# 24
S = input("24. Введите целое положительное число: ").strip()
print(sum(int(c) for c in S if c.isdigit()))

# 25
S = ''.join(c for c in input("25. Введите двоичное число: ") if c in '01') or '0'
print(str(int(S, 2)))