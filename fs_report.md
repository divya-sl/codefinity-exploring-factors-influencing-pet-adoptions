This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
pet_adoption_data.csv
````

# Files

## File: pet_adoption_data.csv
````
PetID,PetType,Breed,AgeMonths,Color,Size,WeightKg,Vaccinated,HealthCondition,TimeInShelterDays,AdoptionFee,PreviousOwner,AdoptionLikelihood
500,Bird,Parakeet,131,Orange,Large,5.039767822529515,1,0,27,140,0,0
501,Rabbit,Rabbit,73,White,Large,16.086726854616735,0,0,8,235,0,0
````

## File: main.py
````
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

adoption_rates_TimeInShelterDays = df.groupby('AdoptionLikelihood')['TimeInShelterDays'].mean()
print("Adoption rates by TimeInShelterDays:")
print({
    "Mean Time In Shelter Average for unlikely adopted": round(adoption_rates_TimeInShelterDays.loc[0], 3),
    "Mean Time In Shelter Average for likely adopted": round(adoption_rates_TimeInShelterDays.loc[1], 3)
})

adoption_rates_TimeInShelterDays.plot(kind = 'bar')
plt.title("Adoption Rate based on Time in Shelter")
plt.xticks(rotation=0)
#df.plot(x = 'AdoptionLikelihood', y='TimeInShelterDays', kind='bar')
plt.show()

      ````
