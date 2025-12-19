import sys
from pathlib import Path

def test_smoke_import_app():
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root))

    import app 
    assert hasattr(app, "app")
