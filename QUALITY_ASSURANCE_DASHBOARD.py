import sys
import vs

class FeedbackPortal:
    sd = {"vinay": "viay0000", "rakesh": "rash0000", "vasudendra": "vara0000", "dinesh": "dish0000"}
    rat = [1.0, 2.0, 3.0, 4.0, 5.0]
    ru = []
    ch = 0
    cho = 0
    crs = {"vinay": False, "rakesh": False, "vasudendra": False, "dinesh": False}

    def login(self, user):
        user = user.lower()
        if user in self.sd:
            return self.sd[user]
        return None

    def rating_input(self, field):
        while True:
            try:
                rating = float(input(f"Rating for {field} (1.0-5.0): "))
                if 1.0 <= rating <= 5.0:
                    return rating
                else:
                    print("Please enter a rating between 1.0 and 5.0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def give_ratings(self, user):
        if self.crs[user]:
            print("You have already submitted your ratings.")
            return
        
        print("\n---Start Giving Ratings---")
        fields = ["Academic", "Ground Maintainability", "Kits Availability", "Students Achievement in Sports", "Environment"]
        ratings = {}
        
        for field in fields:
            rating = self.rating_input(field)
            ratings[field] = rating
        
        vs.pr1[user] = ratings
        self.crs[user] = True
        print("Ratings submitted successfully.")

    def analyze_ratings(self):
        if not all(self.crs.values()):
            print("All ratings must be completed by all users before analysis.")
            return
        
        print("---Analysis of Ratings---")
        fields = ["Academic", "Ground Maintainability", "Kits Availability", "Students Achievement in Sports", "Environment"]
        averages = {field: sum(vs.pr1[name][field] for name in vs.pr1) / len(vs.pr1) for field in fields}
        
        for field, avg in averages.items():
            print(f"Average {field} Rating: {avg}")
        
        overall_avg = sum(averages.values()) / len(averages)
        print(f"Overall Average Rating for NAAC: {overall_avg}")

        if overall_avg <= 1.0:
            print("---B Grade---")
        elif overall_avg <= 2.5:
            print("---B++ Grade---")
        elif overall_avg <= 3.5:
            print("---A Grade---")
        else:
            print("---A++ Grade---")

    def start(self):
        while self.ch != 2:
            print("\n---Welcome to RVVV institution official portal---")
            choice = input("\n1. To login\n2. Exit\nSelect your choice: ")
            if not choice.isdigit():
                print("Enter only numbers.")
                continue
            choice = int(choice)

            if choice == 1:
                print("---Login---")
                username = input("Enter username: ")
                password = self.login(username)

                if password:
                    entered_password = input("Enter password: ")
                    if entered_password == password:
                        print(f"Welcome to RVVV portal, {username.title()}!")

                        while True:
                            action = input("\n1. To give ratings\n2. To analyze\n3. To return back\nSelect one: ")
                            if not action.isdigit():
                                print("Enter only numbers.")
                                continue
                            action = int(action)

                            if action == 1:
                                self.give_ratings(username)
                            elif action == 2:
                                self.analyze_ratings()
                            elif action == 3:
                                break
                            else:
                                print("Enter correct option.")
                    else:
                        print("Incorrect password.")
                else:
                    print("User not found.")

            elif choice == 2:
                print("Exiting...")
                sys.exit()
            else:
                print("Enter a valid choice.")

if _name_ == "_main_":
    portal = FeedbackPortal()
    portal.start()