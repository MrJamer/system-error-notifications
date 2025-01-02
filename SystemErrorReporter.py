def calculate_error_rate(errors: int, total_requests: int) -> float:
    """
    Обчислює відсоток помилок у загальній кількості запитів.

    Args:
        errors (int): Кількість помилок.
        total_requests (int): Загальна кількість запитів.

    Returns:
        float: Відсоток помилок.
    """
    if total_requests == 0:
        return 0.0
    return (errors / total_requests) * 100

import pytest
from system.analysis import calculate_error_rate

def test_calculate_error_rate():
    assert calculate_error_rate(10, 100) == 10.0
    assert calculate_error_rate(0, 100) == 0.0
    assert calculate_error_rate(10, 0) == 0.0

from system.data_collector import DataCollector
from system.analysis import ErrorAnalyzer

def test_data_to_analysis_integration():
    collector = DataCollector()
    analyzer = ErrorAnalyzer()

    # Збір тестових даних
    test_data = collector.collect_errors()
    
    # Аналіз зібраних даних
    results = analyzer.analyze(test_data)
    
    # Перевірка результатів
    assert len(results) > 0

