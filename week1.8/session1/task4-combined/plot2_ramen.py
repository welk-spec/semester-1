'''
This will combine some basic data handling, plotting, and writing functions.
You will probably want to have the docs/help open to support you!

The base code is provided at the bottom - you can add to this, change it, or remove it and write your own if you prefer!

You are welcome to add more options to the menu and create your own graphs - think of how you can use the different styles of graph.

For example - you could add box and whisker diagrams to show averages, or scatter plots to show outliers.

The data set 'ramen-ratings.csv' draws from a popular blog rating instant ramen products.
'''
import pandas as pd
import matplotlib.pyplot as plt
import random



def show_histogram_of_ramen_scores(data):
    '''
    Create a histogram to show the distribution of numbers of stars given to ramen.
    '''
    ratings = pd.to_numeric(data["Stars"], errors="coerce").dropna().round(1)
    plt.figure(figsize=(10, 6))
    plt.hist(ratings, bins=10, color="#eff542")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.title("Distribution of Ramen Ratings")
    plt.show()
    pass

def show_bar_chart_stars_per_country(data):
    '''
    Create a bar chart showing the average rating per country
    '''
    stats = data.groupby("Country")["Stars"].agg(["mean", "count"])
    avg_ratings = stats[stats["count"] >= 10]["mean"].sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    plt.bar(avg_ratings.index, avg_ratings.values, color="#eff542")
    plt.xlabel("Country")
    plt.ylabel("Average Rating")
    plt.title("Average Ramen Ratings by Country (10+ reviews)")
    plt.xticks(rotation=45, ha="right")
    plt.show()

def show_bar_chart_stars_per_manufacturer(data):
    '''
    Create a bar chart showing the average rating per manufacturer
    '''
    stats = data.groupby("Brand")["Stars"].agg(["mean", "count"])
    avg_ratings = stats[stats["count"] >= 10]["mean"].sort_values(ascending=False).head(15)
    plt.figure(figsize=(10, 6))
    plt.bar(avg_ratings.index, avg_ratings.values, color="#eff542")
    plt.xlabel("Brand")
    plt.ylabel("Average Rating")
    plt.title("Average Ramen Ratings by Brand (10+ reviews)")
    plt.xticks(rotation=45, ha="right")
    plt.show()

def _in_country(data, country):
    return data[data["Country"].str.lower() == country.lower()]

def find_best_per_country(data, country):
    '''
    Find and return the index of the row with the highest rating per country.
    '''
    return _in_country(data, country)["Stars"].idxmax()

def find_worst_per_country(data, country):
    '''
    Find and return the index of the row with the lowest rating per country.
    '''
    return _in_country(data, country)["Stars"].idxmin()

def show_piechart_of_manufacturers_by_country(data, country):
    '''
    Create a pie chart showing the percentage of each manufacturer in the country
    '''
    counts = _in_country(data, country)["Brand"].value_counts()
    if len(counts) > 8:  # Japan has loads of brands, 100 slices is unreadable
        counts = pd.concat([counts.head(8), pd.Series({"Other": counts.iloc[8:].sum()})])
    plt.figure(figsize=(8, 8))
    plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
    plt.title(f"Ramen brands in {country}")
    plt.show()

def print_ramen_rating(rating):
    '''
    Print out a row from the dataframe in a more human-readable format
    '''
    print(f"Name: {rating['Variety']}")
    print(f"Type of ramen: {rating['Style']}")
    print(f"Manufacturer: {rating['Brand']}")
    print(f"Country of Origin: {rating['Country']}")
    print(f"Stars: {rating['Stars']}\n")

def show_top_ten(data):
    '''
    Select the top-ten ramen and print them out in order of lowest rating to highest
    '''
    for _, row in data.nlargest(10, "Stars").iloc[::-1].iterrows():
        print_ramen_rating(row)

def random_ramen_review(data):
    '''
    Pick a random ramen and give its basic information plus how it compares to averages.
    '''
    row = data.sample(1).iloc[0]
    print_ramen_rating(row)
    print(f"Brand average: {data[data['Brand'] == row['Brand']]['Stars'].mean():.2f}")
    print(f"Country average: {data[data['Country'] == row['Country']]['Stars'].mean():.2f}")


def menu():
    ''' Displays menu and allows user to enter choice to be returned to main - if you add more, remember to add them to the 'while choice not in' line! '''
    print("~ ramen rating database ~")
    print("1 - See distribution of scores")
    print("2 - see average score per country")
    print("3 - see average score per manufacturer")
    print("4 - Get a breakdown of a specific country")
    print("5 - See the top ten ramens")
    print("6 - See a random Ramen")
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6", "Q"]:
        choice = input("Pick an option: ").upper()
    return choice

# the main program is below - complete the functions one at a time and test them!

ramen_data = pd.read_csv("ramen-ratings.csv")
ramen_data["Stars"] = pd.to_numeric(ramen_data["Stars"], errors="coerce")

while True:
    choice = menu()
    match choice:
        case "1":
            show_histogram_of_ramen_scores(ramen_data)
        case "2":
            show_bar_chart_stars_per_country(ramen_data)
        case "3":
            show_bar_chart_stars_per_manufacturer(ramen_data)
        case "4":
            country = input("Enter country: ").strip()
            if _in_country(ramen_data, country).empty:
                print("No ramen found for that country.")
            else:
                print("BEST:")
                print_ramen_rating(ramen_data.loc[find_best_per_country(ramen_data, country)])
                print("WORST:")
                print_ramen_rating(ramen_data.loc[find_worst_per_country(ramen_data, country)])
                show_piechart_of_manufacturers_by_country(ramen_data, country)
        case "5":
            show_top_ten(ramen_data)
        case "6":
            random_ramen_review(ramen_data)
        case "Q":
            break