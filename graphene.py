import cv2

def analyze(filename):
    image = cv2.imread(filename)
    return


def main():
    filenames = ["./Photos/DSL30002.TIF"]
    for filename in filenames:
        analyze(filename)


if __name__ == "__main__":
    main()
