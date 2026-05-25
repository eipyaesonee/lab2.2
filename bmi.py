def calculate_bmi(height,weight):
    print("Height="+ str(height))
    print("Weight="+ str(weight))

    bmi = weight / height**2
    print(f"calculated BMI:  {bmi:.2f}")
    if bmi < 18.5:
        print("Under Weight")
        return -1

    elif (bmi >= 18.5) & (bmi <= 25.0):
        print("Normal Weight")
        return 0

    else:
         print("Over weight")
         return 1

if __name__ == "__main__":
    result = calculate_bmi(1.73, 57)
    print("Return value =", result)