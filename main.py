import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("pet_adoption_data.csv")

# Your code starts here
print(df.describe())
print(df.sample())

# Calculate adoption rates by previous ownership
adoption_rates = df.groupby('PreviousOwner')['AdoptionLikelihood'].mean()

# Text-based representation of the data values
print("Adoption rates by PreviousOwner:")
print({
    "No Previous Owner (0)": round(adoption_rates.loc[0], 3),
    "Has Previous Owner (1)": round(adoption_rates.loc[1], 3)
})

# Bar chart comparing adoption rates
adoption_rates.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Adoption Rate by Previous Ownership")
plt.xlabel("PreviousOwner (0 = No, 1 = Yes)")
plt.ylabel("Mean Adoption Likelihood")
plt.xticks(rotation=0)
plt.ylim(0, 1)
plt.show()

adoption_rates_pet_type = df.groupby('PetType')['AdoptionLikelihood'].mean()
#print(adoption_rates_pet_type)
adoption_rates_pet_type.plot(kind='bar')
plt.title("Adoption Rate by Pet Type")
plt.xlabel("Pet Type")
plt.ylabel("Mean Adoption Likelihood")
plt.ylim(0,1)
plt.show()

print(f"Pet Type with highest adoption rate : {adoption_rates_pet_type.sort_values(ascending=False).head(1)}")

adoption_rates_vaccination = df.groupby('Vaccinated')['AdoptionLikelihood'].mean()
print(f"Does vaccination status affect adoption rates : {adoption_rates_vaccination.loc[0] < adoption_rates_vaccination.loc[1]}")

# Boxplot for distributions
plt.figure(figsize=(8, 6))
sns.boxplot(
    x='AdoptionLikelihood',
    y='TimeInShelterDays',
    data=df,
    palette=['lightcoral', 'lightseagreen']
)
plt.title("Distribution of Shelter Stay Durations\nby Adoption Likelihood")
plt.xlabel("Adoption Likelihood (0 = Unlikely, 1 = Likely)")
plt.ylabel("Time in Shelter (Days)")
plt.xticks([0, 1], ['Unlikely Adopted', 'Likely Adopted'])
plt.show()