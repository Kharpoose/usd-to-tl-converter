def main():
    print("This program conver usd to tl ")
    print()

    dollars = eval(input("enter amount in dolars: "))

    tl = convert_to_tl(dollars)

    print(f"that is {tl} turkish lira")
    
convert_to_tl = lambda dollars: dollars * 26.5

main()