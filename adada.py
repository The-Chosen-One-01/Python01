


scores= []


while True:
    try:
        score = input("Enter a score, or type 'done' to exit: ")
        if score == "done":
            break
        score = int(score)
        if score > 0:
            scores.append(score)
        else:
            print("Please type a postivie number.")
    except ValueError:
        print('It is wrong')

print('done')