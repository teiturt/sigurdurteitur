import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Style Setup ---
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'Arial'

# ==============================================================================
# --- NEW DATA BASED ON MARKET ANALYSIS & PENETRATION GOALS ---
# ==============================================================================

# --- Assumptions ---
PRICE_PER_USER_PER_YEAR_ISK = 15000
ICELAND_MARKET_SIZE = 60000
NORDICS_MARKET_SIZE = 2500000 # (Denmark, Norway, Sweden etc.)
ENGLISH_MARKET_SIZE = 50000000 # (A fraction of UK, US, international schools)

# --- Penetration Goals over 10 Years (%) ---
years = np.arange(1, 11)
penetration_iceland = np.array([0.01, 0.05, 0.15, 0.30, 0.50, 0.60, 0.70, 0.75, 0.80, 0.83]) # Ends at ~50k users
penetration_nordics = np.array([0, 0, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07])
penetration_english = np.array([0, 0, 0, 0.001, 0.002, 0.004, 0.006, 0.008, 0.01, 0.012])

# --- Calculate Users and Revenue ---
df_proj = pd.DataFrame({'Ár': years})
df_proj['Ísland Notendur'] = penetration_iceland * ICELAND_MARKET_SIZE
df_proj['Norðurlönd Notendur'] = penetration_nordics * NORDICS_MARKET_SIZE
df_proj['Enskumælandi Notendur'] = penetration_english * ENGLISH_MARKET_SIZE

# Convert users to revenue (and millions)
df_proj['Ísland Tekjur'] = (df_proj['Ísland Notendur'] * PRICE_PER_USER_PER_YEAR_ISK) / 1000000
df_proj['Norðurlönd Tekjur'] = (df_proj['Norðurlönd Notendur'] * PRICE_PER_USER_PER_YEAR_ISK) / 1000000
df_proj['Enskumælandi Tekjur'] = (df_proj['Enskumælandi Notendur'] * PRICE_PER_USER_PER_YEAR_ISK) / 1000000
df_proj['Heildartekjur'] = df_proj['Ísland Tekjur'] + df_proj['Norðurlönd Tekjur'] + df_proj['Enskumælandi Tekjur']

# ==============================================================================
# Graph 1: Revenue Projection
# ==============================================================================
fig1, ax1 = plt.subplots(figsize=(12, 7))

colors = {'Ísland Tekjur': '#27ae60', 'Norðurlönd Tekjur': '#e67e22', 'Enskumælandi Tekjur': '#3498db', 'Heildartekjur': '#34495e'}
for column, color in colors.items():
    ax1.plot(df_proj['Ár'], df_proj[column], marker='o', linestyle='-', color=color, label=column.replace(' Tekjur', ''))

ax1.set_title('Tekjuspá byggð á markmiðum um markaðshlutdeild', fontsize=16, pad=20)
ax1.set_xlabel('Ár', fontsize=12)
ax1.set_ylabel('Árlegar Tekjur (millj. ISK)', fontsize=12)
ax1.set_xticks(years)
ax1.set_ylim(0)
ax1.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f} m.kr.'))
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
fig1.tight_layout()
plt.show()

# ==============================================================================
# Graph 2: User Projection (Stacked Area Chart)
# ==============================================================================
fig2, ax2 = plt.subplots(figsize=(12, 7))

labels = ['Ísland', 'Norðurlönd', 'Enskumælandi']
colors_stack = ['#27ae60', '#e67e22', '#3498db']
ax2.stackplot(df_proj['Ár'],
              df_proj['Ísland Notendur'], df_proj['Norðurlönd Notendur'], df_proj['Enskumælandi Notendur'],
              labels=labels, colors=colors_stack, alpha=0.8)

ax2.set_title('Spá um fjölda notenda eftir mörkuðum', fontsize=16, pad=20)
ax2.set_xlabel('Ár', fontsize=12)
ax2.set_ylabel('Uppsafnaður Fjöldi Notenda', fontsize=12)
ax2.set_xticks(years)
ax2.set_ylim(0)
ax2.yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
ax2.legend(loc='upper left', fontsize=12)
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
fig2.tight_layout()
plt.show()