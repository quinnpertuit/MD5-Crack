# *****************************************************************************
# *                                                                           *
# *  Title        : MD5 Crack                                                 *
# *                                                                           *
# *  Deskripsi    : Script to crack MD5 type hashes automatically             *
# *                 by trying all character combinations.                     *
# *                                                                           *
# *  Author       : msverse                                                   *
# *                                                                           *
# *  Tanggal      : 16/25/2024                                                *
# *                                                                           *
# *  Copyright © 2024 msverse                                                 *
# *                                                                           *
# *  Duplication, publication or distribution                                 *
# *  without permission from the author is prohibited.                        *
# *                                                                           *
# *****************************************************************************

import hashlib
import itertools
import string
import time

def crack_md5_hash(hash_to_crack, max_length):
    all_chars = string.printable.strip() # Mengambil semua karakter yang dapat dicetak
    start_time = time.time()

    for length in range(1, min(max_length, 101)):  # Batasi panjang maksimum menjadi 100
        for combination in itertools.product(all_chars, repeat=length):
            candidate = ''.join(combination)
            hashed_candidate = hashlib.md5(candidate.encode()).hexdigest()
            if hashed_candidate == hash_to_crack:
                return candidate, time.time() - start_time

    return None, time.time() - start_time

def main():
    hash_to_crack = input("Input hash MD5 ~# ")
    max_length = 100  # Set Maximum Length to 100
    found = False

    print("Start Cracking...")

    while not found:
        password, elapsed_time = crack_md5_hash(hash_to_crack, max_length)
        if password:
            print("Keyword Results ~#", password)
            print("Time required ~#", round(elapsed_time, 2), "Second")
            found = True
        else:
            max_length += 1

if __name__ == "__main__":
    main()
