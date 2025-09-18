import pandas as pd
import numpy as np
import json
from faker import Faker

fake = Faker()

# Available column types
COLUMN_TYPES = {
    "int": "Random integers (0–1000)",
    "float": "Random floats (0–1000)",
    "label": "Random categorical labels (A, B, C, D)",
    "string": "Random words",
    "name": "Fake full names",
    "email": "Fake email addresses",
    "date": "Random dates",
    "text": "Random short text"
}

def banner_top():
    print("\n" + "="*70)
    print(" RYO DATASET FORGE ".center(70))
    print("="*70)
    print("Generate any dataset you imagine — CSV, Excel, JSON, JSONL".center(70))
    print("Synthetic. Predictive. Scalable. Ryo-powered. 🔥".center(70))
    print("="*70 + "\n")

def banner_bottom():
    print("\n" + "="*70)
    print("✅ Dataset creation completed successfully!".center(70))
    print("💾 Your synthetic data is ready to rule the future ⚡".center(70))
    print("Keep forging. Keep predicting. Keep building. 🚀".center(70))
    print("="*70 + "\n")

def generate_column(col_type, n):
    """Generate column data based on type"""
    if col_type == "int":
        return np.random.randint(0, 1000, n)
    elif col_type == "float":
        return np.round(np.random.uniform(0, 1000, n), 2)
    elif col_type == "label":
        return np.random.choice(["A", "B", "C", "D"], n)
    elif col_type == "string":
        return [fake.word() for _ in range(n)]
    elif col_type == "name":
        return [fake.name() for _ in range(n)]
    elif col_type == "email":
        return [fake.email() for _ in range(n)]
    elif col_type == "date":
        return [fake.date() for _ in range(n)]
    elif col_type == "text":
        return [fake.text(max_nb_chars=50) for _ in range(n)]
    else:
        raise ValueError(f"Unsupported column type: {col_type}")

def generate_dataset(columns, n_rows, file_format, filename):
    """Generate and save dataset"""
    data = {}
    for col_name, col_type in columns.items():
        data[col_name] = generate_column(col_type, n_rows)

    df = pd.DataFrame(data)

    if file_format == "csv":
        df.to_csv(filename + ".csv", index=False)
    elif file_format == "xlsx":
        df.to_excel(filename + ".xlsx", index=False)
    elif file_format == "json":
        df.to_json(filename + ".json", orient="records", indent=4)
    elif file_format == "jsonl":
        with open(filename + ".jsonl", "w") as f:
            for record in df.to_dict(orient="records"):
                f.write(json.dumps(record) + "\n")
    else:
        raise ValueError("Unsupported format!")

    print(f"\n🔥 File saved: {filename}.{file_format}")

def user_input_workflow():
    banner_top()

    # Number of rows
    while True:
        try:
            n_rows = int(input("👉 Enter number of rows: "))
            if n_rows > 0:
                break
            else:
                print("❌ Please enter a positive number.")
        except ValueError:
            print("❌ Invalid input. Enter an integer.")

    # Number of columns
    while True:
        try:
            n_cols = int(input("👉 Enter number of columns: "))
            if n_cols > 0:
                break
            else:
                print("❌ Please enter a positive number.")
        except ValueError:
            print("❌ Invalid input. Enter an integer.")

    columns = {}
    print("\n📊 Available column types:")
    for k, v in COLUMN_TYPES.items():
        print(f" - {k}: {v}")

    for i in range(n_cols):
        col_name = input(f"\n🔹 Enter name for column {i+1}: ")

        while True:
            col_type = input(f"   🔸 Enter type for '{col_name}': ").strip().lower()
            if col_type in COLUMN_TYPES:
                break
            else:
                print("❌ Invalid type. Choose from:", ", ".join(COLUMN_TYPES.keys()))

        columns[col_name] = col_type

    # File format
    supported_formats = ["csv", "xlsx", "json", "jsonl"]
    while True:
        file_format = input(f"\n💾 Choose output format {supported_formats}: ").strip().lower()
        if file_format in supported_formats:
            break
        else:
            print("❌ Unsupported format.")

    filename = input("📂 Enter output filename (without extension): ").strip()

    # Generate dataset
    generate_dataset(columns, n_rows, file_format, filename)

    banner_bottom()

if __name__ == "__main__":
    user_input_workflow()