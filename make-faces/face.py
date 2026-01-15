#implement a concert function
def convert(str):
    str = str.replace(":(", "🙁")
    str = str.replace(":)", "🙂")
    return str

#implement main that asks input and converts it then outputs it
def main():
    answer = input("Type away:")
    answer = convert(answer)
    print(answer)

main()