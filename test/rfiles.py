from pathlib import Path

def test_path():
    current_path=Path('.').resolve()
    return current_path

path=test_path()
current_file=Path(__file__).resolve()
for path in path.iterdir():
    if path.name == current_file.name:
        continue
    else:
        content=path.read_text(encoding='utf-8')
        print(f'Content of {path.name}:{content}')
    