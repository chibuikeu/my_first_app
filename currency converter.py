def main():
    print("This program converts Naira to dollar")
    print()

    naira = eval(input("Enter amount in naira: "))

    dollar = convert_to_dollar(naira)

    print("That is" , dollar, "dollar. ")

convert_to_dollar = lambda naira: naira * 0.0013
main()