import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Order ID": [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],
    "Food Item": ["Pizza","Burger","Biryani","Pizza","Momos","Burger","Pizza","Biryani","Momos","Pizza","Burger","Biryani","Pizza","Momos","Burger"],
    "Order Time": ["7:00 PM","8:00 PM","1:00 PM","9:00 PM","6:00 PM","7:00 PM","8:00 PM","2:00 PM","5:00 PM","10:00 PM","9:00 PM","1:00 PM","7:00 PM","6:00 PM","8:00 PM"],
    "Delivery Time": [30,25,40,35,20,28,32,45,22,38,27,41,29,21,26]
}

df = pd.DataFrame(data)

print("📊 Dataset:\n", df)

avg_time = df["Delivery Time"].mean()
print("\n⏱ Average Delivery Time:", avg_time)


food_count = df["Food Item"].value_counts()
print("\n🍕 Popular Food:\n", food_count)

def categorize_time(time):
    hour = int(time.split(":")[0])
    if 1 <= hour <= 3:
        return "Afternoon"
    elif 6 <= hour <= 8:
        return "Evening"
    else:
        return "Night"

df["Time Slot"] = df["Order Time"].apply(categorize_time)

peak_hours = df["Time Slot"].value_counts()
print("\n⏰ Peak Hours:\n", peak_hours)

food_count.plot(kind='bar')
plt.title("Popular Food Items")
plt.xlabel("Food Item")
plt.ylabel("Number of Orders")
plt.show()

peak_hours.plot(kind='pie', autopct='%1.1f%%')
plt.title("Peak Hours Distribution")
plt.ylabel("")
plt.show()