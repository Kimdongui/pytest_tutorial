## Description
[`pytest`](https://docs.pytest.org/en/7.1.x/index.html)는 쉽고 작은 단위의 가독성 높은 테스트를 만들어주는 python framework이다.

## install
[PyPI](https://pypi.org/project/pytest/)에 사용 가능한 버전이 있다.
글을 작성하는 2022-07-14 기준으로는 `7.1.2`버전이 최신 버전이다.
```bash
pip install pytest
```

## CLI 테스트 방법
- 디렉토리 단위 : `tests/`라는 이름으로 directory를 만들거나, 특정 경로를 지정하면 된다
```bash
$ pytest # If tests/ directory exists

$ pytest <DIR_PATH> 
```
- 파일 단위
`test_`로 시작하거나 `_test`로 끝나는 `.py` 스크립트 만들기
```bash
$ "print(hello)" > test_print.py
$ pytest
```

- 함수 단위
`test_`로 시작하는 python function(def ...) 만들기
```python
def test_function_name():
    ...
    return ...
```

## 설정 파일 만들기
python project의 표준이 된 `pyproject.toml`파일 또는 `pytest.ini`라는 파일을 통해서 configuration이 가능하며, 두 가지 정도의 옵션이 더 존재한다.
- [reference](https://docs.pytest.org/en/7.1.x/reference/customize.html#configuration)


## 참고 문서
- [공식 홈페이지](https://docs.pytest.org/en/7.1.x/index.html)