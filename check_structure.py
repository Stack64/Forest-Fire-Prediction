#!/usr/bin/env python3
"""
Quick script to verify repository structure for Streamlit Cloud
"""
import os

print("Repository Structure Check for Streamlit Cloud")
print("=" * 50)

# Check root requirements.txt
root_requirements = "requirements.txt"
if os.path.exists(root_requirements):
    print(f"✅ {root_requirements} found at root")
    with open(root_requirements, 'r') as f:
        print(f"   Contents ({len(f.readlines())} lines)")
else:
    print(f"❌ {root_requirements} NOT found at root")

# Check packages.txt
packages_file = "packages.txt"
if os.path.exists(packages_file):
    print(f"✅ {packages_file} found at root")
else:
    print(f"❌ {packages_file} NOT found at root")

# Check app directory
app_dir = "Forest FIre Prediction"
if os.path.exists(app_dir):
    print(f"✅ App directory '{app_dir}' exists")
    app_file = os.path.join(app_dir, "app.py")
    model_file = os.path.join(app_dir, "model.pkl")
    if os.path.exists(app_file):
        print(f"✅ app.py found in '{app_dir}'")
    else:
        print(f"❌ app.py NOT found in '{app_dir}'")
    if os.path.exists(model_file):
        print(f"✅ model.pkl found in '{app_dir}'")
    else:
        print(f"❌ model.pkl NOT found in '{app_dir}'")
else:
    print(f"❌ App directory '{app_dir}' NOT found")

print("\n" + "=" * 50)
print("If deployment still fails, consider:")
print("1. Removing spaces from directory name")
print("2. Moving app.py to root directory")
print("3. Checking Streamlit Cloud logs for exact error")
