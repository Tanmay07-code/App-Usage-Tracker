from tracker import start_tracker
from display import get_top_five,get_todays_data,get_usage_on

def main():
    """User menu interface."""

    while True:
        print("""
================ APP USAGE TRACKER ================
1. Start live tracking
2. Show today's summary
3. Show top 5 apps today
4. View usage for a past date
5. Exit
===================================================
""")

        choice = input("Select option: ").strip()

        if not choice.isdigit():
            print("\n❌ Enter a number 1 to 5.\n")
            continue
        choice = int(choice)

        match choice:
            case 1:
                print("\n🔴 Tracking started... (Press CTRL+C to stop)\n")
                start_tracker()
            case 2:
                print("\n📊 Today's Usage: \n")
                todays_data()
            case 3:
                print("\n🏆 Top 5 Apps Today: \n")
                top_five()
            case 4:
                d = input("Enter date (YYYY-MM-DD): ").strip()
                print("\n📅 Usage for", d)
                usage_on(d)
            case 5:
                print("\nExiting... Goodbye 👋")
                break
            case _:
                print("\n❌ Invalid input. Try again.\n")


def top_five():
    """Returns top 5 most used apps """
    top5 = get_top_five()
    for key,val in top5:
        print(f'{key}: {format_time(val)}')

def todays_data():
    """Returns today's usage data as a dictionary """
    data = get_todays_data()
    for key,val in data:
        print(f'{key}: {format_time(val)}')

def usage_on(this_date):
    """Returns usage dictionary for a given date 'YYYY-MM-DD'"""
    data = get_usage_on(this_date)
    for key,val in data:
        print(f'{key}: {format_time(val)}')

def format_time(seconds):
    """makes the the time readable """
    hours = int(seconds // 3600)
    mins = int((seconds % 3600)//60)
    sec = int(seconds % 60)
    return f'{hours}h {mins}m {sec}s'

if __name__=="__main__":
    main()
    
