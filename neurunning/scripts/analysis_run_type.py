import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/session_summary.csv")

# run_type 병합하려면 survey 또는 wearable에 포함되어 있어야 함
df_sessions = pd.read_csv("data/raw/wearable_sample.csv")[['session_id','run_type']]
df = df.merge(df_sessions, on="session_id")

print(df.groupby("run_type")[['stress_reduction','tempo']].mean())

sns.boxplot(x='run_type', y='stress_reduction', data=df)
plt.title("Stress Reduction by Run Type")
plt.show()

sns.scatterplot(x='tempo', y='stress_reduction', hue='run_type', data=df, s=100)
plt.title("Stress Reduction vs Tempo by Run Type")
plt.xlabel("Tempo (km/h)")
plt.ylabel("Stress Reduction (VAS)")
plt.show()
