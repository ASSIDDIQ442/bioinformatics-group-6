# ------------------- BIOINFORMATICS SCRIPT -------------------
def display_profile():
    # User information variables
    name = "Abdullahi Auwal Garba"
    email = "abdullahiauwal796@gmail.com"
    slack_username = "@apdoulahae_Mr_Bee"
    area_of_interest = "Proteomics 🧬🔍"
    
    # Formatting constants
    border = "-" * 40
    tab = "\t"
    
    # Display header
    print(f"\n{border}\n\tBIOINFORMATICS PROFILE\n{border}\n")
    print(f"{tab}Hello {name}, below are your information details:\n")
    
    print(f"{tab}Name: {tab*2}{name}")
    print(f"{tab}Email: {tab*2}{email}")
    print(f"{tab}Slack Username: {tab}{slack_username}")
    print(f"{tab}Area of Interest: {tab}{area_of_interest}💻🧪")
    
    print(f"\n{border}\n")

# Run the profile display
if __name__ == "__main__":
    display_profile()