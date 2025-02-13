def greet_with(name, location):
    print(f"\nHello {name}")
    print(f"What is it like in {location}?")


def main():

    # Calling Function with Positional Argument
    greet_with("Shikhor", "Kolkata")

    # Calling Function with Keyword Argument
    greet_with(location="New York City", name="Emma")

if __name__ == '__main__':
    main()