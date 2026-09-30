# BMI 單元測試

本專案使用 `pytest` 執行測試、使用 `AssertPy` 撰寫 fluent assertions，並由 `uv` 管理測試依賴。

## 測試範圍

- `tests/test_calculate_bmi_value.py`：驗證公斤與英吋輸入的 BMI 計算，使用 `is_close_to()` 比較浮點數。
- `tests/test_calBMI.py`：逐一驗證各分類及目前程式使用的 18.5、24、27 邊界。

分類測試刻意依照 `app.py` 現有門檻撰寫；這些測試不代表對醫療分類標準的確認，也不會更改程式邏輯。

## 執行測試

先安裝 [uv](https://docs.astral.sh/uv/getting-started/installation/)，再於專案根目錄執行：

```powershell
uv run pytest
```

第一次執行時，uv 會依 `pyproject.toml` 和 `uv.lock` 建立或同步虛擬環境及測試依賴。專案已設定工作站使用的 Microsoft Python package proxy。

## 查看詳細結果

以下指令會逐項列出測試名稱，並在失敗時顯示完整 traceback 與測試摘要：

```powershell
uv run pytest -vv -ra --tb=long
```

常用選項：

- `-vv`：列出每個測試案例的名稱與結果。
- `-ra`：在摘要中列出失敗、錯誤及其他非通過項目。
- `--tb=long`：顯示較完整的失敗 traceback。
- `--showlocals`：發生失敗時一併顯示區域變數。

只執行其中一個函式的測試檔：

```powershell
uv run pytest -vv tests/test_calculate_bmi_value.py
uv run pytest -vv tests/test_calBMI.py
```

## Fluent assertion 套件

[AssertPy](https://pypi.org/project/assertpy/) 是 Python 專用 fluent assertion 套件，語法如 `assert_that(value).is_equal_to(expected)`；對浮點數則使用 `is_close_to(expected, tolerance)`。本專案選它來滿足 fluent assertion 需求，並由 [pytest](https://pypi.org/project/pytest/) 提供成熟的測試探索、執行與詳細失敗輸出。

採用前需留意：截至 2026-09-30，AssertPy 的 PyPI 最新發佈為 1.1（2020-07-19），雖然 GitHub 顯示有 529 stars 及約 2,650 個使用者專案，更新頻率不如 pytest 活躍。因此本專案只使用其基本數值 fluent assertions；若未來優先考慮維護活躍度，可改用 pytest 原生 `assert`，但那就不再是 fluent assertion。