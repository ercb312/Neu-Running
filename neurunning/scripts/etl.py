import pandas as pd
from hrv_calc import compute_rmssd

df_wearable = pd.read_csv("data/raw/wearable_sample.csv")
df_survey = pd.read_csv("data/raw/survey_sample.csv")

summary_list = []

for session_id in df_wearable['session_id'].unique():
    df_session = df_wearable[df_wearable['session_id']==session_id]
    hr_avg = df_session['hr'].mean()
    hr_max = df_session['hr'].max()
    rr_series = df_session['rr_interval_ms'].dropna()
    hrv_value = compute_rmssd(rr_series)

    df_sess_survey = df_survey[df_survey['session_id']==session_id]
    pre_stress = df_sess_survey[df_sess_survey['timepoint']=='pre']['stress_vas'].values[0]
    post_stress = df_sess_survey[df_sess_survey['timepoint']=='post']['stress_vas'].values[0]

    duration = df_session['duration_min'].iloc[0]
    distance = df_session['distance_km'].iloc[0]
    tempo = distance / (duration / 60)

    summary_list.append({
        'session_id': session_id,
        'pre_stress': pre_stress,
        'post_stress': post_stress,
        'stress_reduction': pre_stress - post_stress,
        'avg_hr': hr_avg,
        'max_hr': hr_max,
        'tempo': tempo
    })

df_summary = pd.DataFrame(summary_list)
df_summary.to_csv("data/processed/session_summary.csv", index=False)
print("✅ ETL 완료 → data/processed/session_summary.csv 저장됨")
