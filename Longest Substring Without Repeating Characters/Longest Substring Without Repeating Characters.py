def lswrc(s):
    t = set(s)
    t = list(t)
    print(t)
    a = ""
    for i in range(len(t)):
        w = t[i]
        a = a + w
    print(f"The answer is {a}, with the length of {len(a)}.")

def main():
    s = "aabbbcccc"
    lswrc(s)

if __name__ == "__main__":
    main()
