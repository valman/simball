from helpers.functions import choose_action
from collections import defaultdict

class Team:
    # Represents a basketball team with basic stats
    def __init__(self, name, FGA, ThPA, ThPct, PF, FTPct, ORB):
        self.name = name
        self.FGA = FGA
        self.ThPA = ThPA
        self.ThPct = ThPct * 100
        self.PF = PF
        self.FTPct = FTPct * 100
        self.ORB = ORB
        self.stats = defaultdict(float)
        self.log ={}

    # Run a play
    def play(self):

        # Shoot or Pass
        actions = [("shoot" , self.FGA), ("pass" , 100-self.FGA)]
        action = choose_action(actions)
        match action:
            # If a shot attempt was made
            case "shoot":
                actions = [("3", self.ThPA), ("2", 100 - self.ThPA)]
                shot_type = choose_action(actions)

                # Is it blocked?



                # If it's a 3PT shot
                match shot_type:
                    case "3":
                        self.stats["FGA"] += 1
                        self.stats["3PA"] += 1
                        print("🏀 3PT shot attempted → " , end="")
                        # In or out
                        actions = [("In", self.ThPct), ("Out", 100 - self.ThPct)]
                        basket = choose_action(actions)
                        match basket:
                            case "In":
                                self.stats["3PM"] += 1
                                self.stats["FGM"] += 1
                                print("✔️  made → ", end="")

                                # Fouled?
                                if self.is_fouled(self.PF):
                                    print("✊🏻 fouled ")
                                    if self.shoot_freethrow(1, self.FTPct) == 0:
                                        # Determine who rebounds the ball
                                        if self.rebound(self.ORB):
                                            self.stats["ORB"] += 1
                                            print("👋  offensive rebound ")
                                            return "reset"
                                        else:
                                            print("Defensive rebound → End")
                                            return "over"
                                else:
                                    print("End.")
                                    return "over"

                            case "Out":
                                print("⭕ missed → ", end="")

                                if self.is_fouled(self.PF):
                                    print("✊🏻 fouled!")
                                    if self.shoot_freethrow(3, self.FTPct) == 0:
                                        # Determine who rebounds the ball
                                        if self.rebound(self.ORB):
                                            self.stats["ORB"] += 1
                                            print("👋  offensive rebound ")
                                            return "reset"
                                        else:
                                            print("Defensive rebound → End")
                                            return "over"
                                else:
                                    # Determine who rebounds the ball
                                    if self.rebound(self.ORB):
                                        self.stats["ORB"] += 1
                                        print("👋  offensive rebound ")
                                        return "reset"
                                    else:
                                        print("Defensive rebound → End")
                                        return "over"



                    case "2":
                        self.stats["FGA"] += 1
                        self.stats["2PA"] += 1
                        print("🏀 2PT shot attempted → ", end="")

                        # In or out
                        actions = [("In", self.ThPct), ("Out", 100 - self.ThPct)]
                        basket = choose_action(actions)
                        match basket:
                            case "In":
                                self.stats["3PM"] += 1
                                self.stats["FGM"] += 1
                                print("✔️  made → " , end="")

                                # Fouled?
                                if self.is_fouled(self.PF):
                                    print("✊🏻 fouled!")

                                    if self.shoot_freethrow(1, self.FTPct) == 0:
                                        # Determine who rebounds the ball
                                        if self.rebound(self.ORB):
                                            self.stats["ORB"] += 1
                                            print("👋  offensive rebound ")
                                            return "reset"
                                        else:
                                            print("Defensive rebound → End")
                                            return "over"

                                else:
                                    print("End.")
                                    return "over"

                            case "Out":
                                print("⭕ missed → ", end="")

                                if self.is_fouled(self.PF):
                                    print("✊🏻 fouled ")

                                    if self.shoot_freethrow(2, self.FTPct) == 0:
                                        # Determine who rebounds the ball
                                        if self.rebound(self.ORB):
                                            self.stats["ORB"] += 1
                                            print("👋  offensive rebound ")
                                            return "reset"
                                        else:
                                            print("Defensive rebound → End.")
                                            return "over"

                                else:
                                    # Determine who rebounds the ball
                                    if self.rebound(self.ORB):
                                        self.stats["ORB"] += 1
                                        print("👋  offensive rebound ")
                                        return "reset"
                                    else:
                                        print("Defensive rebound → End.")
                                        return "over"

            case "pass":
                print("A pass is made ...")

        print("End.")
        return "over"

    # Print stats
    def summary(self):
        print(self.stats)

    # Append safely
    def add_log(self, level, message):
        if level not in self.log:
            self.log[level] = []  # create list if it doesn't exist
        self.log[level].append(message)

    # Shoot free throws
    def shoot_freethrow(self, count, ftp):
        goal_ft = 0  # No FT shot made yet
        for i in range(count):
            print(f"Shooting {i+1} of {count} ... ", end="")
            self.stats["FTA"] += 1
            actions = [(1, ftp), (0 , 100 - ftp)]
            goal_ft = choose_action(actions)
            if goal_ft:
                print("✔️ made")
                self.stats["FTM"] += 1
            else:
                print("❌ missed")

        # Return status of last shot
        return goal_ft

    def is_fouled(self, pf):
        # Fouled?
        actions = [(1, pf), (0, 100 - pf)]
        return choose_action(actions)

    def rebound(self, reb):
        # Offensive rebound?
        actions = [(1, reb), (0, 100 - reb)]
        return choose_action(actions)