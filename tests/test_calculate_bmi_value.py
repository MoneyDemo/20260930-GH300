"""測試 calculate_bmi_value 的 BMI 計算結果。"""

from assertpy import assert_that

from app import calculate_bmi_value


def test_calculate_bmi_value_converts_inches_to_meters_and_calculates_bmi():
    """驗證函式會將英吋換算為公尺後計算 BMI。"""
    # 準備（Arrange）
    weight_in_kilograms = 70
    height_in_inches = 70
    expected_bmi = 22.14

    # 執行（Act）
    actual_bmi = calculate_bmi_value(weight_in_kilograms, height_in_inches)

    # 驗證（Assert）
    assert_that(actual_bmi).is_close_to(expected_bmi, 0.01)


def test_calculate_bmi_value_returns_zero_for_zero_weight():
    """驗證體重為零且身高有效時，BMI 為零。"""
    # 準備（Arrange）
    weight_in_kilograms = 0
    height_in_inches = 70

    # 執行（Act）
    actual_bmi = calculate_bmi_value(weight_in_kilograms, height_in_inches)

    # 驗證（Assert）
    assert_that(actual_bmi).is_zero()


def test_calculate_bmi_value_returns_large_bmi_for_one_inch_height():
    """驗證極小但大於零的身高會產生很大的有限 BMI。"""
    # 準備（Arrange）
    weight_in_kilograms = 70
    height_in_inches = 1
    expected_bmi = 108500.22

    # 執行（Act）
    actual_bmi = calculate_bmi_value(weight_in_kilograms, height_in_inches)

    # 驗證（Assert）
    assert_that(actual_bmi).is_close_to(expected_bmi, 0.01)


def test_calculate_bmi_value_returns_small_bmi_for_very_tall_height():
    """驗證極大的正身高會產生較小但大於零的 BMI。"""
    # 準備（Arrange）
    weight_in_kilograms = 70
    height_in_inches = 100
    expected_bmi = 10.85

    # 執行（Act）
    actual_bmi = calculate_bmi_value(weight_in_kilograms, height_in_inches)

    # 驗證（Assert）
    assert_that(actual_bmi).is_close_to(expected_bmi, 0.01)


def test_calculate_bmi_value_raises_for_zero_height():
    """驗證身高為零時，BMI 計算會引發除以零例外。"""
    # 準備（Arrange）
    weight_in_kilograms = 70
    height_in_inches = 0

    # 執行與驗證（Act and Assert）
    assert_that(calculate_bmi_value).raises(ZeroDivisionError).when_called_with(
        weight_in_kilograms,
        height_in_inches,
    )