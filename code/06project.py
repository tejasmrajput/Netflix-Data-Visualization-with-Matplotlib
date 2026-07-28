import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and store it in a DataFrame
df = pd.read_csv(r"C:\Users\tejas\Downloads\The-Ultimate-Python-Course-main\DATA ANALYSIS\matplotilb\netflix_titles.csv")

# Display the first 5 rows to check if data loaded correctly
print(df.head())


# --------------------------------------------------
# Data Cleaning
# --------------------------------------------------

# Remove rows that have missing values in important columns.
# We use this because missing values can cause errors while plotting graphs.
df = df.dropna(subset=["type", "release_year", "rating", "country", "duration"])


# ==================================================
# 1. Movies vs TV Shows Count (Bar Chart)
# ==================================================

# Count how many Movies and TV Shows exist.
# value_counts() counts the frequency of each unique value.
type_counts = df["type"].value_counts()

# Create a new figure of size 6x4 inches.
# figsize makes the graph larger or smaller.
plt.figure(figsize=(6, 4))

# Create a Bar Chart.
# index = category names (Movie, TV Show)
# values = total count of each category
plt.bar(type_counts.index,
        type_counts.values,
        color=["#E50914", "#221F1F"])

# Add title to the graph
plt.title("Movies vs TV Shows on Netflix")

# Label X-axis
plt.xlabel("Type")

# Label Y-axis
plt.ylabel("Count")

# Add horizontal grid lines to make comparison easier
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display the graph
plt.show()


# ==================================================
# 2. Content Type Distribution (Pie Chart)
# ==================================================

# Create a square figure for Pie Chart
plt.figure(figsize=(6, 6))

# Draw Pie Chart
# labels -> category names
# autopct -> shows percentage
# startangle -> rotate chart for better appearance
plt.pie(type_counts.values,
        labels=type_counts.index,
        autopct="%1.1f%%",
        colors=["#E50914", "#221F1F"],
        startangle=90)

# Add title
plt.title("Distribution of Movies & TV Shows")

# Display graph
plt.show()


# ==================================================
# 3. Content Releases Over the Years (Line Plot)
# ==================================================

# Count titles released every year.
# sort_index() arranges years in ascending order.
release_counts = df["release_year"].value_counts().sort_index()

# Create figure
plt.figure(figsize=(10, 5))

# Plot Line Graph
# marker='o' shows circles on each data point
# linewidth controls line thickness
plt.plot(release_counts.index,
         release_counts.values,
         color="#E50914",
         marker="o",
         linewidth=2)

# Graph title
plt.title("Content Released Over the Years")

# X-axis label
plt.xlabel("Release Year")

# Y-axis label
plt.ylabel("Number of Titles")

# Show grid for easier reading
plt.grid(True, linestyle="--", alpha=0.6)

# Display graph
plt.show()


# ==================================================
# 4. Top Content Ratings Distribution (Bar Chart)
# ==================================================

# Count ratings and select the top 10 most common ones.
# head(10) returns only the first 10 rows.
rating_counts = df["rating"].value_counts().head(10)

# Create figure
plt.figure(figsize=(10, 5))

# Plot Bar Chart
plt.bar(rating_counts.index,
        rating_counts.values,
        color="skyblue")

# Graph title
plt.title("Top 10 Ratings on Netflix")

# X-axis label
plt.xlabel("Rating Category")

# Y-axis label
plt.ylabel("Count")

# Rotate X-axis labels so they don't overlap
plt.xticks(rotation=45)

# Add horizontal grid lines
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display graph
plt.show()


# ==================================================
# 5. Movie Duration Distribution (Histogram)
# ==================================================

# Select only Movie rows.
# copy() creates a separate DataFrame to avoid warnings while editing.
movies_df = df[df["type"] == "Movie"].copy()

# Remove the word " min" from duration values.
# Example:
# "90 min" → "90"
movies_df["duration_min"] = movies_df["duration"].str.replace(" min", "").astype(int)

# Create figure
plt.figure(figsize=(8, 5))

# Histogram shows how movie durations are distributed.
# bins=20 divides data into 20 intervals.
# edgecolor adds black borders around bars.
plt.hist(movies_df["duration_min"],
         bins=20,
         color="#E50914",
         edgecolor="black")

# Graph title
plt.title("Distribution of Movie Durations (in Minutes)")

# X-axis label
plt.xlabel("Duration (Minutes)")

# Y-axis label
plt.ylabel("Number of Movies")

# Add grid for easier analysis
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display graph
plt.show()