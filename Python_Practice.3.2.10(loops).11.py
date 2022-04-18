x = 0
while x <= 5:
    print(x)
    x = x + 1


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I recieved" + str(percentage_votes)+"% + of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the number of the total votes in the election? "))
message_to_candidate = (
    f"You recieved {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}"
    f"You recieved {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

