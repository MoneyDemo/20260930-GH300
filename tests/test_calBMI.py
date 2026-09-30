"""測試 calBMI 依 BMI 數值回傳正確的體重分類。"""

import math

from assertpy import assert_that

from app import calBMI


def test_calBMI_returns_underweight_below_18_5():
    """驗證 BMI 低於 18.5 時分類為體重過輕。"""
    # 準備（Arrange）
    bmi = 18.49
    expected_category = "Underweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_healthy_weight_at_18_5():
    """驗證 BMI 等於 18.5 時分類為健康體重。"""
    # 準備（Arrange）
    bmi = 18.5
    expected_category = "Healthy weight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_healthy_weight_below_24():
    """驗證 BMI 低於 24 且不低於 18.5 時分類為健康體重。"""
    # 準備（Arrange）
    bmi = 23.99
    expected_category = "Healthy weight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_overweight_at_24():
    """驗證 BMI 等於 24 時分類為過重。"""
    # 準備（Arrange）
    bmi = 24
    expected_category = "Overweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_overweight_below_27():
    """驗證 BMI 低於 27 且不低於 24 時分類為過重。"""
    # 準備（Arrange）
    bmi = 26.99
    expected_category = "Overweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_obesity_at_27():
    """驗證 BMI 等於 27 時分類為肥胖。"""
    # 準備（Arrange）
    bmi = 27
    expected_category = "Obesity"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_underweight_immediately_below_18_5():
    """驗證緊鄰 18.5 下方的 BMI 分類為體重過輕。"""
    # 準備（Arrange）
    bmi = math.nextafter(18.5, -math.inf)
    expected_category = "Underweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_healthy_weight_immediately_above_18_5():
    """驗證緊鄰 18.5 上方的 BMI 分類為健康體重。"""
    # 準備（Arrange）
    bmi = math.nextafter(18.5, math.inf)
    expected_category = "Healthy weight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_healthy_weight_immediately_below_24():
    """驗證緊鄰 24 下方的 BMI 分類為健康體重。"""
    # 準備（Arrange）
    bmi = math.nextafter(24, -math.inf)
    expected_category = "Healthy weight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_overweight_immediately_above_24():
    """驗證緊鄰 24 上方的 BMI 分類為過重。"""
    # 準備（Arrange）
    bmi = math.nextafter(24, math.inf)
    expected_category = "Overweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_overweight_immediately_below_27():
    """驗證緊鄰 27 下方的 BMI 分類為過重。"""
    # 準備（Arrange）
    bmi = math.nextafter(27, -math.inf)
    expected_category = "Overweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_obesity_immediately_above_27():
    """驗證緊鄰 27 上方的 BMI 分類為肥胖。"""
    # 準備（Arrange）
    bmi = math.nextafter(27, math.inf)
    expected_category = "Obesity"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_underweight_for_zero_bmi():
    """驗證 BMI 為零時分類為體重過輕。"""
    # 準備（Arrange）
    bmi = 0
    expected_category = "Underweight"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)


def test_calBMI_returns_obesity_for_extremely_high_bmi():
    """驗證極大的正 BMI 分類為肥胖。"""
    # 準備（Arrange）
    bmi = 1_000_000
    expected_category = "Obesity"

    # 執行（Act）
    actual_category = calBMI(bmi)

    # 驗證（Assert）
    assert_that(actual_category).is_equal_to(expected_category)