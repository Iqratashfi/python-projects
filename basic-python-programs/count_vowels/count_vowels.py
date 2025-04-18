def count_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    new_list = []
    count = 0

    for x in sentence:
        if x in vowels:
            count += 1
            new_list.append(x)

    print ("Number of vowels: ", +count)
    print(f"The new list is {new_list}")
sentence = input("Enter a sentence: ")

count_vowels(sentence)

