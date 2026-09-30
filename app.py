"""提供互動式 BMI 計算與體重分類。"""


def calculate_bmi():
    """讀取體重與身高，並顯示 BMI 和對應的體重分類。"""
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in inches: "))
    bmi = calculate_bmi_value(weight, height)
    category = calBMI(bmi)
    print(f"Your BMI is {bmi:.2f} and you are categorized as {category}.")

def calculate_bmi_value(weight, height):
    """根據公斤體重與英吋身高計算 BMI。

    Args:
        weight: 體重，單位為公斤。
        height: 身高，單位為英吋。

    Returns:
        計算出的 BMI 數值。
    """
    # 將英吋換算為公尺後，套用 BMI 公式。
    height_in_meters = height * 0.0254
    bmi = weight / (height_in_meters ** 2)
    return bmi

def calBMI(bmi):
    """依 BMI 數值回傳對應的體重分類。

    Args:
        bmi: 待分類的 BMI 數值。

    Returns:
        體重分類的英文名稱。
    """
    if bmi < 18.5:
            category = "Underweight"
    elif 18.5 <= bmi < 24:
        category = "Healthy weight"
    elif 24 <= bmi < 27:
        category = "Overweight"
    else:
        category = "Obesity"
    return category

if __name__ == "__main__":
    # 直接執行本檔案時啟動互動流程。
    calculate_bmi()