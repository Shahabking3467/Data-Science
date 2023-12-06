import matplotlib.pyplot as plt
import numpy as np


flag = True
# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize BMI

def categorize_bmi(bmi):
    if bmi > 30:
        category = "خیلی چاق"
        #explode = (0.1, 0, 0, 0, 0)
    elif 25 <= bmi <= 30:
        category = "چاق"
        #explode = (0, 0.1, 0, 0, 0)
    elif 18.5 <= bmi < 25:
        category = "معمولی"
        #explode = (0, 0, 0.1, 0, 0)
    elif 17 <= bmi < 18.5:
        category = "لاغر"
        #explode = (0, 0, 0, 0.1, 0)
    else:
        category = '' "خیلی لاغر"
        #explode = (0, 0, 0, 0, 0.1)
    return category

# Input from the user
name = input("اسمت را وارد کن: ")
age = int(input("سنت را وارد کن: "))
weight = float(input("وزنت را وارد کن (به کیلوگرم): "))
height = float(input("قدت را وارد کن (به متر): "))

# Calculate BMI and categorize
bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)

# Display BMI category
print(f"بی ام ای تو {bmi:.2f},و شما به عنوان دسته بندی می شوید {category}.")

# Calculate the target BMI for the "Normal" category
target_bmi = 22.5  # You can adjust this value as needed for your definition of "Normal" BMI

# Caculate Normal Weight
Normal_Weight = target_bmi * (height ** 2)

# Calculate extra Weight
if weight > Normal_Weight:
    Extra_Weight = weight - Normal_Weight
else:
    Extra_Weight = Normal_Weight - weight

# Display the recommendation
if category =='Overfat' or category =='Fat' :
    print(f"برای قرار گرفتن در دسته BMI «عادی»، ممکن است لازم باشد وزن خود را کاهش دهید{abs(Extra_Weight):.2f} کیلوگرم.")
elif category =='OverThin' or category =='Thin' :
    flag = False
    print(f"برای قرار گرفتن در دسته BMI «عادی»، ممکن است لازم باشد وزن خود را افزایش دهید {abs(Extra_Weight):.2f} کیلوگرم.")
else:
    print("شما در حال حاضر در دسته BMI عادی هستید.")
# Pie chart  
labels = ['خیلی چاق', 'چاق', 'معمولی', 'لاغر', 'خیلی لاغر']
sizes = [10, 20, 40, 20, 10]
if category == "خیلی چاق":
        explode = (0.1, 0, 0, 0, 0)
elif category == "چاق":
    explode = (0, 0.1, 0, 0, 0)
elif category == "معمولی":
        explode = (0, 0, 0.1, 0, 0)
elif category == "لاغر":
    explode = (0, 0, 0, 0.1, 0)
else:
    explode = (0, 0, 0, 0, 0.1)

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
plt.title('توزیع BMI')
plt.show()


# Bar plot for user's information
user_info = [height*100, weight, bmi]
labels_user = ['قد', 'وزن', 'BMI']

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # Subplot for user's information

plt.bar(labels_user, user_info, color=['#66b3ff', '#66b3ff', '#ffcc99'])
plt.xlabel('اطلاعات کاربر')
plt.ylabel('ارزش های')
plt.title('اطلاعات کاربر')

# Bar plot for normal person's information
if flag:
    normal_person_info = [height*100, weight - Extra_Weight , target_bmi]
    labels_normal = ['قد', 'ن_وزن', 'N_BMI']
else :
    normal_person_info = [height*100, weight + Extra_Weight , target_bmi]
    labels_normal = ['قد', 'ن_وزن', 'N_BMI']

plt.subplot(1, 2, 2)  # Subplot for normal person's information

plt.bar(labels_normal, normal_person_info, color=['#66b3ff', '#66b3ff', '#ffcc99'])
plt.xlabel('اطلاعات افراد عادی')
plt.ylabel('ارزش های')
plt.title('اطلاعات افراد عادی')

plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# Linear diagram for fitness progress
months = ['ازر', 'دی', 'بهمن', 'اسفند', 'فروردین']
piece_bmi_difference = Extra_Weight / 4

plt.figure()
plt.ylim(weight - 30, weight + 30)

if flag:
    fitness_progress = [weight, weight - piece_bmi_difference, weight - 2 * (piece_bmi_difference),
                        weight - 3 * (piece_bmi_difference), weight - 4 * (piece_bmi_difference)]

    plt.plot(months, fitness_progress, marker='s', linestyle='--', color='orange')
    plt.xlabel('ماه ها')
    plt.ylabel('بهبود BMI')
    plt.title('پیشرفت تناسب اندام بیش از 4 ماه')

    # Customize y-axis ticks and labels for more detail
    plt.yticks(np.arange(weight - 30, weight + 31, 2.5))  

    plt.show()
else:
    fitness_progress = [weight, piece_bmi_difference + weight, 2 * (piece_bmi_difference) + weight,
                        3 * (piece_bmi_difference) + weight, 4 * (piece_bmi_difference) + weight]

    plt.plot(months, fitness_progress, marker='s', linestyle='--', color='orange')
    plt.xlabel('ماه ها')
    plt.ylabel('وزن شما')
    plt.title('پیشرفت تناسب اندام بیش از 4 ماهs')

    # Customize y-axis ticks and labels for more detail
    plt.yticks(np.arange(weight - 30, weight + 31, 2.5))  

    plt.show()