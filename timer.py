import time
def second_func():
            while True:
                print("\nThe second_function game")
                print("1. Start")
                print("2. Exit")
                choose = input("Choose your number (1 or 2)")
                if choose == '1':
                    start_time = time.time()
                    input("You are started a game,please click the 'Enter' butoon for the end!")

                    end_time = time.time()
                    duration = end_time - start_time
                    print(f"Elapsed time {duration.2f} seconds!")
                elif choose == '2':
                    print("The programm is ending")
                    break
                else:
                    print("Invalid choice.Please enter 1 or 2!")
second_func()
