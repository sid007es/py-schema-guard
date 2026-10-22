import pytest
import pandas as pd
from src.core import SchemaGuard

def test_schema_guard_validation():
    schema = {"id": "int", "value": "float"}
    guard = SchemaGuard(schema)
    
    # Valid sample
    df_valid = pd.DataFrame({"id": [1, 2], "value": [10.5, 20.0]})
    assert len(guard.validate_dataframe(df_valid)) == 0
    
    # Missing column
    df_invalid = pd.DataFrame({"id": [1, 2]})
    errors = guard.validate_dataframe(df_invalid)
    assert any("Missing column: value" in err for err in errors)

def test_synthetic_generation():
    schema = {"user_id": "int", "name": "str"}
    guard = SchemaGuard(schema)
    synthetic = guard.generate_synthetic_sample(rows=3)
    assert len(synthetic) == 3
    assert list(synthetic.columns) == ["user_id", "name"]
