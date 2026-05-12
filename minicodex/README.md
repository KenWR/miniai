# minicodex

작은 Codex 스타일 Python CLI를 직접 만들어보는 학습 프로젝트입니다.

## Current Status

현재까지 진행한 내용:

- `miniai/minicodex` 하위 프로젝트 생성
- `src` layout 기반 Python 패키지 구조 생성
- `cli.py`에 기본 CLI 루프 구현
- `pyproject.toml` 추가
- `pip install -e .`를 통한 editable install 설정
- `minicodex` 명령어로 CLI를 실행할 수 있도록 entry point 설정

현재 구조:

```text
minicodex/
  README.md
  pyproject.toml
  src/
    minicodex/
      __init__.py
      cli.py
```

## How to Run

프로젝트 폴더로 이동합니다.

```powershell
cd C:\Users\skyqk\Desktop\ALL\works\OLD\Study\AI\miniai\minicodex
```

개발 모드로 설치합니다.

```powershell
python -m pip install -e .
```

CLI를 실행합니다.

```powershell
minicodex
```

또는:

```powershell
python -m minicodex.cli
```

종료하려면 CLI에서 다음을 입력합니다.

```text
quit
```

## Note

`pyproject.toml`의 다음 설정 때문에 `minicodex` 명령어가 생깁니다.

```toml
[project.scripts]
minicodex = "minicodex.cli:main"
```

터미널에서 `minicodex`를 입력하면 `src/minicodex/cli.py` 파일의 `main()` 함수가 실행됩니다.

다음 단계는 CLI와 모델 역할을 분리하는 것입니다.
