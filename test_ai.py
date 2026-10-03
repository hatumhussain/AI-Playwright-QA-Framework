from ai.failure_analyzer import analyze_failure

result = analyze_failure(
    "test_invalid_login",
    "AssertionError: Expected error message was not found"
)

print("===== AI ANALYSIS =====")
print(result)
