# What is Package
**패키지(package)** 란, 각각의 모듈들을 묶어놓은 하나의 단위이며, **모듈(module)** 이란, 함수(function)들과 클래스(class)들의 집합을 의미합니다. 경우에 따라 패키지와 모듈을 같은 의미로써 사용하는 경우도 존재합니다.

## pip
[PyPI](https://pypi.org/)에 업로드 된 별도의 패키지들을 설치합니다.

### help
`pip` 명령어 사용법은 콘솔창을 열고 아래와 같이 명령어를 입력하면 알 수 있습니다.
```console
pip help
```

### install
패키지를 다운로드 받을 때는 콘솔창에 아래와 같이 `pip` 명령어를 입력합니다.
```console
pip install 다운받을_패키지
```

### list
다운받은 패키지 목록을 확인하려면 콘솔창에 아래와 같이 `pip` 명령어를 입력합니다.
```console
pip list
```

### show
패키지에 대한 세부적인 정보를 알고 싶을 때 콘솔창에 아래와 같이 `pip` 명령어를 입력합니다. 
```console
pip show 다운받은_패키지
```

### freeze
`다운받은_패키지==버전` 형식으로 패키지의 현재 버전과 함께 목록을 출력합니다. 콘솔창에 아래와 같이 `pip` 명령어를 입력합니다. 
```console
pip freeze
```

### update
패키지가 업데이트 시키기 위해서는 콘솔창에 아래와 같이 `pip` 명령어를 입력합니다.
```console
pip install --upgrade 다운받은_패키지
```

### delete
다운받은 패키지를 삭제하려면 콘솔창에 아래와 같이 `pip` 명령어를 입력합니다.
```console
pip uninstall 다운받은_패키지
```
