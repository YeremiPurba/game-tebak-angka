import random

print("=== GAME TEBAK ANGKA ===")

nama = input("Siapa Namamu? ")
print("Selamat Datang", nama)

try_again = 'y'
while try_again == 'y':
    # fitur: pilihan level kesulitan
    level = input("\nPilih Level Kesulitan (Easy/Medium/Hard): ").lower()

    if level == "easy":
        max_num = 10
        opportunity = 5
        print(f"\nKamu memilih level {level.capitalize()}")
        print(f"Tebak Angka dari 1 hingga {max_num}")
        print(f"Kesempatan : {opportunity} \n")
    elif level == "medium":
        max_num = 50
        opportunity = 7
        print(f"\nKamu memilih level {level.capitalize()}")
        print(f"Tebak Angka dari 1 hingga {max_num}")
        print(f"Kesempatan : {opportunity} \n")
    elif level == "hard":
        max_num = 100
        opportunity = 5
        print(f"\nKamu memilih level {level.capitalize()}")
        print(f"Tebak Angka dari 1 hingga {max_num}")
        print(f"Kesempatan : {opportunity} \n")
    else:
        print("Input tidak valid!")
        print("Silahkan masukkan pilihan 'easy/medium/hard'")
        continue

    secret_num = random.randint(1, max_num)
    while opportunity > 0:
        # input validation : bukan angka
        try:
            # input tebakan user
            guess_num = int(input("Masukkan Tebakanmu : "))
        except ValueError:
            print("Input Harus Berupa Angka!\n")
            continue

        # input validaton : diluar rentang
        if guess_num < 1 or guess_num > max_num:
            print(f"Angka harus berada di antara 1 dan {max_num}\n")
            continue

        # logic game
        if guess_num == secret_num:
            print("Selamat! Tebakanmu Benar")
            break
        elif guess_num > secret_num:
            print("Maaf! Tebakanmu Masih Terlalu Besar")
        else:
            print("Maaf! Tebakanmu Masih Terlalu Kecil")

        opportunity = opportunity - 1
        print("Sisa Kesempatan : ", opportunity, "\n")

    else:
        print("Kesempatan Habis!!")
        print("Angka Rahasia adalah", secret_num)

    # fitur: coba lagi/try again
    try_again = input("Ingin Bermain lagi?(y/n) ")

else:
    print("Terima Kasih telah bermain :)")