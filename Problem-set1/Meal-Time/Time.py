def main():
    expression = input("What time is it ? ")
    expression = convert(expression)
    
    if 7<= expression <= 8:
        print("breakfast time")
    elif 12 <= expression <= 13:
        print("lunch time")
    elif 18 <= expression <= 19:
        print("dinner time")


def convert(time):
    h1,h2 = time.split(":")
    h1 = float(h1)
    h2 = float(h2) / 60
    return h1+h2

if __name__ == "__main__":
    main()