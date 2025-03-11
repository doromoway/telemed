import hashlib
import string
import time
import itertools

password = 'abba'  
res = hashlib.md5(password.encode())  
print(res.hexdigest())

target_hash = "47bce5c74f589f4867dbd57e9ca9f808"
alphabet = string.ascii_letters
start_time = time.time()

for combination in itertools.product(alphabet, repeat=5):
    password = ''.join(combination)  
    test_hash = hashlib.md5(password.encode()).hexdigest() 
    
    if test_hash == target_hash:
        print(f"Пароль найден: {password}")
        break

finish_time = time.time()
print(f"Время подбора: {finish_time - start_time:.6f} сек")