import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Stíl uppsetning (til að passa við fyrri gröf) ---
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'Arial'

# ==============================================================================
# --- Nýtt, bjartsýnna gagnasett ---
# ==============================================================================
years = np.arange(1, 11)

# Ný gögn með hraðari vexti á Íslandi og Norðurlöndum
data_growth_optimistic = {
    'Ár': years,
    'Ísland': [0, 5, 20, 40, 60, 80, 100, 120, 140, 150],
    'Norðurlönd': [0, 0, 10, 40, 80, 120, 160, 200, 240, 280],
    'Enskumælandi': [0, 0, 0, 20, 80, 200, 400, 650, 900, 1200]
}
df_growth = pd.DataFrame(data_growth_optimistic)
df_growth['Heildartekjur'] = df_growth.drop('Ár', axis=1).sum(axis=1)

# Gögn fyrir notendafjölda (samsvarar tekjuvexti)
data_users = {
    'Ár': years,
    'Ísland': [0, 1000, 4000, 8000, 12000, 20000, 30000, 40000, 45000, 50000],
    'Norðurlönd': [0, 0, 2000, 8000, 16000, 25000, 35000, 45000, 55000, 65000],
    'Enskumælandi': [0, 0, 0, 4000, 16000, 40000, 80000, 130000, 180000, 240000]
}
df_users = pd.DataFrame(data_users)

# ==============================================================================
# Graf 1: Tekjuáætlun
# ==============================================================================
fig1, ax1 = plt.subplots(figsize=(12, 7))

colors = {
    'Ísland': '#27ae60',
    'Norðurlönd': '#e67e22',
    'Enskumælandi': '#3498db',
    'Heildartekjur': '#34495e'
}

# Sýnum tekjur fyrir hvern markað
for column in ['Ísland', 'Norðurlönd', 'Enskumælandi', 'Heildartekjur']:
    ax1.plot(df_growth['Ár'], df_growth[column], marker='o', linestyle='-', color=colors[column], label=column)

# --- Fínpússun á útliti ---
ax1.set_title('Tekjuáætlun eftir mörkuðum (10 ár)', fontsize=16, pad=20)
ax1.set_xlabel('Ár', fontsize=12)
ax1.set_ylabel('Árlegar Tekjur (millj. ISK)', fontsize=12)
ax1.set_xticks(years)
ax1.set_ylim(0) # Byrjar í 0
ax1.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f} m.kr.'))
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

fig1.tight_layout()
plt.show()


# ==============================================================================
# Graf 2: Notendaþróun (Stacked Area Chart)
# ==============================================================================
fig2, ax2 = plt.subplots(figsize=(12, 7))

# Nota "stackplot" til að sýna hvernig notendahópurinn stækkar
labels = ['Ísland', 'Norðurlönd', 'Enskumælandi']
colors_stack = ['#27ae60', '#e67e22', '#3498db']
ax2.stackplot(df_users['Ár'],
              df_users['Ísland'], df_users['Norðurlönd'], df_users['Enskumælandi'],
              labels=labels,
              colors=colors_stack,
              alpha=0.8)

# --- Fínpússun á útliti ---
ax2.set_title('Áætluð Notendaþróun (10 ár)', fontsize=16, pad=20)
ax2.set_xlabel('Ár', fontsize=12)
ax2.set_ylabel('Uppsafnaður Fjöldi Notenda', fontsize=12)
ax2.set_xticks(years)
ax2.set_ylim(0)
ax2.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
ax2.legend(loc='upper left', fontsize=12)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)

fig2.tight_layout()
plt.show()