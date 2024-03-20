import itertools
from threading import Thread, Lock

def single_guess(real, look_for, debug=False):
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(look_for, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return attempts
            if debug:
                print(guess, attempts)
    return attempts

found_password = False
guess_attempts = 0

def guess_split(real, look_for, password_length, guess_lock, debug=False):
    global found_password
    global guess_attempts
    for guess in itertools.product(look_for, repeat=password_length):
        if found_password:  # If another thread found the password, stop
            return
        with guess_lock:
            guess_attempts += 1
            guess = ''.join(guess)
            if guess == real:
                found_password = True
                return
            if debug:
                print("Thread", password_length, guess, guess_attempts)
    return

def multi_guess(real, look_for, debug=False):
    threads = []
    guess_lock = Lock()
    for i in range(9):
        t = Thread(target=guess_split, args=(real, look_for, i + 1, guess_lock, debug))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    return guess_attempts