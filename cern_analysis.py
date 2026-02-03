import pandas as pd
import matplotlib.pyplot as plt

# --- Load the CSV file ---
df = pd.read_csv("cern_sample.csv")

print("\n=== RAW DATA ===")
print(df)

# --- Basic Summary Statistics ---
print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

# --- Line Plot: Energy per Event ---
plt.figure(figsize=(6,4))
plt.plot(df["EventID"], df["Energy_GeV"], marker="o")
plt.title("Energy Per Event")
plt.xlabel("Event ID")
plt.ylabel("Energy (GeV)")
plt.grid(True)
plt.show()

# --- Histogram: Energy Distribution ---
plt.figure(figsize=(6,4))
plt.hist(df["Energy_GeV"], bins=5)
plt.title("Energy Distribution")
plt.xlabel("Energy (GeV)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# --- Scatter Plot: Energy vs Momentum ---
plt.figure(figsize=(6,4))
plt.scatter(df["Energy_GeV"], df["Momentum_GeV_c"])
plt.title("Energy vs Momentum")
plt.xlabel("Energy (GeV)")
plt.ylabel("Momentum (GeV/c)")
plt.grid(True)
plt.show()

# --- Filtering Example ---
higgs_events = df[df["Particle"] == "Higgs"]

print("\n=== FILTERED DATA: HIGGS EVENTS ONLY ===")
print(higgs_events)

# --- Save one graph as image ---
plt.figure(figsize=(6,4))
plt.bar(df["EventID"], df["Energy_GeV"])
plt.title("Energy Bar Chart (Saved Image)")
plt.xlabel("Event ID")
plt.ylabel("Energy (GeV)")
plt.savefig("energy_chart.png")
plt.close()