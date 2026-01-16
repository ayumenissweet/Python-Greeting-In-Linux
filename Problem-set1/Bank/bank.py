def main():
    answer = input("Greeting: ").lower().strip()
    check_answer(answer)

def check_answer(d):
    if d.startswith("hello"):
        print("$0")
    elif d.startswith("h"):
        print("$20")
    else:
        print("$100")

main()