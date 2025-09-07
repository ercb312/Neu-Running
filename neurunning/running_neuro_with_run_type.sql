
---

## 2️⃣ SQL 스키마 (`running_neuro_with_run_type.sql`)

```sql
CREATE DATABASE running_neuro;
USE running_neuro;

CREATE TABLE participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender ENUM('M','F'),
    notes TEXT
);

CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50)
);

CREATE TABLE running_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    participant_id INT NOT NULL,
    device_id INT,
    session_start DATETIME NOT NULL,
    session_end DATETIME NOT NULL,
    duration_min INT,
    distance_km DECIMAL(6,2),
    tempo DECIMAL(5,2), -- km/h
    avg_hr INT,
    peak_hr INT,
    run_type ENUM('Interval','Fartlek','LSD','TimeTrial','BuildUp') NOT NULL,
    notes TEXT,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id),
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

CREATE TABLE surveys (
    survey_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT,
    timepoint ENUM('pre','post'),
    stress_vas INT, -- 0~10
    mood_score INT,
    FOREIGN KEY (session_id) REFERENCES running_sessions(session_id)
);

CREATE TABLE session_summary (
    summary_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT,
    pre_stress INT,
    post_stress INT,
    stress_reduction INT,
    avg_hr INT,
    max_hr INT,
    tempo DECIMAL(5,2),
    FOREIGN KEY (session_id) REFERENCES running_sessions(session_id)
);
