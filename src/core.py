import pandas as pd
from typing import Dict, List, Any

class SchemaGuard:
    """Lightweight schema validation and synthetic data generator."""
    def __init__(self, schema: Dict[str, str]):
        self.schema = schema

    def validate_dataframe(self, df: pd.DataFrame) -> List[str]:
        errors = []
        for column, expected_type in self.schema.items():
            if column not in df.columns:
                errors.append(f"Missing column: {column}")
                continue
            actual_type = str(df[column].dtype)
            if expected_type == "int" and not actual_type.startswith("int"):
                errors.append(f"Type mismatch for {column}: expected int, got {actual_type}")
            elif expected_type == "float" and not actual_type.startswith("float"):
                errors.append(f"Type mismatch for {column}: expected float, got {actual_type}")
        return errors

    def generate_synthetic_sample(self, rows: int = 5) -> pd.DataFrame:
        data: Dict[str, List[Any]] = {}
        for col, col_type in self.schema.items():
            if col_type == "int":
                data[col] = list(range(1, rows + 1))
            elif col_type == "float":
                data[col] = [float(i) * 1.5 for i in range(1, rows + 1)]
            else:
                data[col] = [f"sample_{i}" for i in range(1, rows + 1)]
        return pd.DataFrame(data)
