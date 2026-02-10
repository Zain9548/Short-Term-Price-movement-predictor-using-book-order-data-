import os

print("1. Train Model")
print("2. Run Live Prediction")
choice = input("Enter choice: ")

if choice == "1":
    os.system("python src/train.py")

elif choice == "2":
    os.system("python realtime/run_live.py")

else:
    print("Invalid choice")

