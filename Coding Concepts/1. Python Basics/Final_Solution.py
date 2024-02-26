def calculate_age(birth_year):
    """Calculate age based on a fixed current year, to avoid using datetime library."""
    return 2024 - birth_year  # Assuming current year is 2024 for simplicity

def add_to_list(item_list, item):
    """Adds an item to a list."""
    item_list.append(item)

def create_education_dict(school, subject):
    """Creates a dictionary for education information."""
    return {"school": school, "subject": subject}

def display_dashboard(info):
    """Prints out the stored information in a user-friendly format."""
    print("\n--- Personal Information Dashboard ---")
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("Favorite Colors:")
    for color in info["favorite colors"]:
        print("- " + color)
    print("Hobbies:")
    for hobby in info["hobbies"]:
        print("- " + hobby)
    print("Education:")
    print("  School:", info["education"]["school"])
    print("  Favorite Subject:", info["education"]["subject"])

def main():
    """Main function that runs the dashboard application."""
    info = {}
    
    # Basic information
    info["name"] = input("What is your name? ")
    birth_year = int(input("What year were you born? "))
    info["age"] = calculate_age(birth_year)
    
    # Favorite colors
    info["favorite colors"] = []
    print("Enter your favorite colors (type 'done' to finish):")
    while True:
        color = input()
        if color == "done":
            break
        add_to_list(info["favorite colors"], color)
    
    # Hobbies
    info["hobbies"] = []
    print("Enter your hobbies (type 'done' to finish):")
    while True:
        hobby = input()
        if hobby == "done":
            break
        add_to_list(info["hobbies"], hobby)
    
    # Education information
    school = input("What is the name of your school? ")
    subject = input("What is your favorite subject? ")
    info["education"] = create_education_dict(school, subject)
    
    # Display the collected information
    display_dashboard(info)

if __name__ == "__main__":
    main()
