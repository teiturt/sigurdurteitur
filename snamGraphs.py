import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    'Year': [2003, 2003, 2003, 2003, 2003, 2003, 2006, 2006, 2006, 2006, 2006, 2006, 2009, 2009, 2009, 2009, 2009, 2009, 2012, 2012, 2012, 2012, 2012, 2012, 2015, 2015, 2015, 2015, 2015, 2015, 2018, 2018, 2018, 2018, 2018, 2018, 2022, 2022, 2022, 2022, 2022, 2022],
    'Kyn': ['Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl', 'Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl', 'Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl', 'Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl', 'Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl', 'Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl', 'Heild', 'Heild', 'Kona', 'Kona', 'Karl', 'Karl'],
    'Tegund': ['Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Stærðfræði', 'Lestur', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði', 'Lestur', 'Stærðfræði'],
    'Value': [85, 81.5, 88.5, 90.5, 81.7, 73.1, 79.5, 83.2, 87.5, 84.7, 71.1, 81.7, 83.2, 83.1, 90.1, 84, 76.2, 82.2, 79, 78.5, 88, 80.3, 70.2, 76.8, 77.9, 76.4, 84.3, 77.2, 71.1, 75.6, 80, 81.3, 82, 82, 65.6, 77, 60, 66, 68, 66, 53, 65]
}
df = pd.DataFrame(data)

# --- Graph 1: Reading Skills (Lestur) ---
plt.style.use('seaborn-v0_8-whitegrid')
fig1, ax1 = plt.subplots(figsize=(12, 7))

# Filter data for Reading
df_lestur = df[df['Tegund'] == 'Lestur']
df_lestur_kona = df_lestur[df_lestur['Kyn'] == 'Kona']
df_lestur_karl = df_lestur[df_lestur['Kyn'] == 'Karl']

# Plotting
ax1.plot(df_lestur_kona['Year'], df_lestur_kona['Value'], marker='o', linestyle='-', color='#8e44ad', label='Lestur, Kona')
ax1.plot(df_lestur_karl['Year'], df_lestur_karl['Value'], marker='o', linestyle='-', color='#3498db', label='Lestur, Karl')

# Formatting
ax1.set_title('Þróun lágmarksfærni í lesskilningi (PISA 2003-2022)', fontsize=16)
ax1.set_ylabel('Hlutfall nemenda (%)', fontsize=12)
ax1.set_ylim(45, 100)
ax1.set_xticks(df['Year'].unique())
ax1.legend(fontsize=12)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()

# --- Graph 2: Math Skills (Stærðfræði) ---
fig2, ax2 = plt.subplots(figsize=(12, 7))

# Filter data for Math
df_staerdfraedi = df[df['Tegund'] == 'Stærðfræði']
df_staerdfraedi_kona = df_staerdfraedi[df_staerdfraedi['Kyn'] == 'Kona']
df_staerdfraedi_karl = df_staerdfraedi[df_staerdfraedi['Kyn'] == 'Karl']

# Plotting
ax2.plot(df_staerdfraedi_kona['Year'], df_staerdfraedi_kona['Value'], marker='o', linestyle='-', color='#8e44ad', label='Stærðfræði, Kona')
ax2.plot(df_staerdfraedi_karl['Year'], df_staerdfraedi_karl['Value'], marker='o', linestyle='-', color='#3498db', label='Stærðfræði, Karl')

# Formatting
ax2.set_title('Þróun lágmarksfærni í stærðfræði (PISA 2003-2022)', fontsize=16)
ax2.set_ylabel('Hlutfall nemenda (%)', fontsize=12)
ax2.set_ylim(45, 100)
ax2.set_xticks(df['Year'].unique())
ax2.legend(fontsize=12)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()