# ============================================================
# 🔥 RyoAI Model Testing Script (Colab + Kaggle Ready)
# ============================================================

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ============================================================
# 1. Create Synthetic Ryo Model Test Dataset
# ============================================================

n_rows = 10000  # you can increase if you want bigger dataset

np.random.seed(42)

data = {
    "Company Name": np.random.randint(100, 999, size=n_rows),
    "Model Name": np.arange(1000, 1000 + n_rows),
    "Mobile Weight": np.random.randint(120, 250, size=n_rows),
    "RAM": np.random.choice([4, 6, 8, 12, 16], size=n_rows),
    "Front Camera": np.random.choice([8, 12, 16, 32], size=n_rows),
    "Back Camera": np.random.choice([32, 48, 64, 108], size=n_rows),
    "Processor": np.random.randint(4, 10, size=n_rows),
    "Battery Capacity": np.random.randint(3000, 6000, size=n_rows),
    "Screen Size": np.round(np.random.uniform(5.5, 7.5, size=n_rows), 2),
    "Launched Price (Pakistan)": np.random.randint(200, 300, size=n_rows),
    "Launched Price (India)": np.random.randint(150, 280, size=n_rows),
    "Launched Price (China)": np.random.randint(180, 290, size=n_rows),
    "Launched Price (USA)": np.random.randint(250, 500, size=n_rows),
    "Launched Price (Dubai)": np.random.randint(240, 450, size=n_rows),
    "Launched Year": np.random.choice([2022, 2023, 2024, 2025], size=n_rows),
}

df = pd.DataFrame(data)
df.to_csv("Ryo-model-test-dataset.csv", index=False)
print("✅ Dataset created and saved: Ryo-model-test-dataset.csv")

# ============================================================
# 2. Load Dataset + Prepare Features/Labels
# ============================================================

df = pd.read_csv("Ryo-model-test-dataset.csv")

# Predict USA Price from other features
X = df.drop(columns=["Launched Price (USA)"])
y = df["Launched Price (USA)"]

# Convert categorical-ish columns to numeric
X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(
    X.values, y.values, test_size=0.2, random_state=42
)

# ============================================================
# 3. Define Model Skeleton (Load from .pt if available)
# ============================================================

class RyoModel(nn.Module):
    def __init__(self, input_dim, hidden_dim=128, output_dim=1):
        super(RyoModel, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim//2),
            nn.ReLU(),
            nn.Linear(hidden_dim//2, output_dim)
        )

    def forward(self, x):
        return self.net(x)

model = RyoModel(input_dim=X_train.shape[1])

# Try loading your pretrained model if exists
try:
    model.load_state_dict(torch.load("C:/Projects/RyoAI/src/data/processed/Ryo-model-001.pt"))
    print("✅ Loaded pretrained Ryo-model-001.pt")
except:
    print("⚠️ Could not load pretrained model, training from scratch.")

# ============================================================
# 4. Train Model (if not pretrained)
# ============================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

X_train_t = torch.tensor(X_train, dtype=torch.float32).to(device)
y_train_t = torch.tensor(y_train, dtype=torch.float32).view(-1,1).to(device)

X_test_t = torch.tensor(X_test, dtype=torch.float32).to(device)
y_test_t = torch.tensor(y_test, dtype=torch.float32).view(-1,1).to(device)

loss_fn = nn.MSELoss()
opt = optim.Adam(model.parameters(), lr=1e-3)

epochs = 10
for epoch in range(epochs):
    model.train()
    opt.zero_grad()
    preds = model(X_train_t)
    loss = loss_fn(preds, y_train_t)
    loss.backward()
    opt.step()
    print(f"Epoch {epoch+1}/{epochs} | Loss = {loss.item():.4f}")

# ============================================================
# 5. Evaluation
# ============================================================

model.eval()
with torch.no_grad():
    preds = model(X_test_t).cpu().numpy().flatten()

mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))

print(f"✅ Model Evaluation:")
print(f"MAE  = {mae:.2f}")
print(f"RMSE = {rmse:.2f}")

# Save model weights for Kaggle
torch.save(model.state_dict(), "Ryo-model-test-trained.pt")
print("✅ Trained model saved: Ryo-model-test-trained.pt")
