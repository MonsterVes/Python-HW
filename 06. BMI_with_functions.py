def get_user_data():
    """retrieves user data from the command line
    
    Returns:
        [dictionary] of the form:
            {
                "name" : "user_name",
                "height": "user heigth in meters",
                "weight": "user weight in kilograms"
            }
    """
    input_data = {} 
    while True:  
        name = input("Name: ")
        if validate_name(name):
            input_data["name"] = name
            break
    while True:
        height = cm_to_meters(int(input("Height in centimeters: ")))
        if validate_height(height):
            input_data["height"] = height
            break
    while True:
        weight = float(input("Weight in kilograms: "))
        if validate_weight(weight):
            input_data["weight"] = weight 
            break
    return input_data

    
def validate_name(name_check):
    while True:
        if len(name_check) > 2 :
            return True
        else:
            return False
        
    
def validate_height(height_check):
    while True:
        if 50 <= height_check*100 <= 250 :
            return True   
        else:
            return False
        

def validate_weight(weight_check):
    while True:
        if 5 <= weight_check <= 300 :
            return True 
        else:
            return False
        

def calc_BMI(w,h):
    """calculates the BMI

    Arguments:
        w {[float]} -- [weight]
        h {[float]} -- [height]

    Returns:
        [float] -- [calculated BMI = w / (h*h)]
    """
    return w / (h*h)


def calc_BMI_category(bmi):
    """Calculates the BMI category

    Arguments:
        bmi {[float]} -- [the bmi number index]

    Returns:
        [string] -- [bmi category]
    """
    if bmi < 16:
        return "Underweight (Severe thinness)"
    elif bmi < 17:
        return "Underweight (Moderate thinness)"
    elif bmi < 18.5:
        return "Underweight (Mild thinness)"
    elif bmi < 25:
        return "Normal range"
    elif bmi < 30:
        return "Overweight (Pre-obese)"
    elif bmi < 35:
        return "Obese (Class I)"
    elif bmi < 40:
        return "Obese (Class II)"
    else:
        return "Obese (Class III)"


def print_results(bmi_category):
    """[Prints the BMI category to the user ]

    Arguments:
        bmi_category {[string]} -- []
    """
    print(f"Category: {bmi_category}")


def cm_to_meters(cm):
    """converts centimetres to meters

    Arguments:
        cm {[int]}

    Returns:
        [float]
    """
    return cm/100

user_data = get_user_data()
bmi = calc_BMI(user_data["weight"],user_data["height"] )
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)