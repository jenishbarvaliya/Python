population = {
    "chaina" : 143,
    "india" : 136,
    "usa" : 32,
    "pakistan" : 21
}

def add():
    country = input("enter the name of country which you want to add in dictionary : ")
    country = country.lower()
    if country in population:
        print("Country already exist in our dataset. Terminating")
        return
    p = float(input(f"enter the population of the company{country}"))
    population[country]=p
    print_all()

def remove():
    country = input("enter the name of country which you want to remove from dictionary : ")
    country = country.lower()
    if country not in population:
        print("Country does not exist in our dataset. Terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("enter the name of country which you want to query from dictionary : ")
    country = country.lower()
    if country not in population:
        print("Country does not exist in our dataset. Terminating")
        return
    print(f"population of {country} is {population[country]}")


def print_all():
    for country,p in population.items():
        print(f"{country} ==> {p}")

def main():
    op=input("Enter the operation(add,remove,query or print)")
    if op.lower() == "add":
        add()
    elif op.lower() == "remove":
        remove()
    elif op.lower() == "query":
        query()
    elif op.lower() == "print":
        print_all()
    else:
        print("Invalid operation. Terminating")

if __name__ == '__main__':
    main()



