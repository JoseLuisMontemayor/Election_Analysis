
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[3])


temperature = int(input("What is the temperature outside?"))

if temperature > 80:
            print("Turn on the AC")

else:
            print("Open the windows.")


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


for county in counties:
    print(county)


numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

numbers = [0, 1, 2, 3, 4, 5]
for num in range(5)
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
