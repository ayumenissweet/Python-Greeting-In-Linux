answer = input("What is the Answer to the Great Question of Life, The universe, and Everything? ")

match answer.lower().strip():
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")