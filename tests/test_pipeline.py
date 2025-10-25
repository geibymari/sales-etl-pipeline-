# tests/test_pipeline.py
import pytest
import pandas as pd
from src.transform import clean_sales_data

def test_remove_duplicates():
    """Test que duplicados son removidos correctamente"""
    # Arrange
    df = pd.DataFrame({
        'id': [1, 1, 2],
        'value': [100, 100, 200]
    })
    
    # Act
    result = clean_sales_data(df)
    
    # Assert
    assert len(result) == 2
    assert result['id'].is_unique

def test_handle_missing_values():
    """Test que valores nulos son manejados"""
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'value': [100, None, 200]
    })
    
    result = clean_sales_data(df)
    
    assert result['value'].isna().sum() == 0
