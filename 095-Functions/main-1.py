# Pętla while sterowana inputem - proste menu tak/nie.
motivational_videos = True

while motivational_videos:
    print("thanks")
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() == "no":
        motivational_videos = False
