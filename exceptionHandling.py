try:
    number = int(input("Enter a number please: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by 0 idiot!")
except ValueError:
    print("We are expecting numbers only.")
except Exception:
    print("something weird happen. we are investigating.")
finally:
    print("Now cleaning up your mess.")

