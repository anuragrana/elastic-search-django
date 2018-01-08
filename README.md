# **Django와 ELK STACK을 이용한 빅데이터 분석을 해보자**

저의 환경이 Mac os이기 때문에 Mac을 기준으로 개발하겠습니다.

## **준비해야 할 것들**

### 가상환경(virtualenv) 생성
~~~
python3 -m venv myvenv
~~~

python3 버전이 있다면 간단히 생성이 가능합니다.

### 가상환경 사용
~~~
source myvenv/bin/activate
~~~

### 가상환경이 실행이 됬다면 커맨드라인이
~~~~
(myvenv) ~$
~~~~
이런 식으로 나와있을 겁니다.


### 장고를 설치기 전 pip를 최신으로 업그레이드 해줍니다.
~~~
pip install --upgrade pip
~~~

### django(virtualenv) 설치
~~~
pip install django
~~~

Django 설치 완료~~~

### elasticsearch 설치

https://www.elastic.co/downloads/elasticsearch

위 사이트에서 tar 파일을 다운 받으시고 아래처럼 압축을 풀어주세요

~~~
tar -xzvf elasticsearch-5.x.x.tar
~~~

### elasticsearch 실행

압축이 풀린 파일에 들어가 아래의 커맨드라인에 아래의 명령어를 입력하면

~~~
./bin/elasticsearch
~~~

실행이 됩니다.

~~~
http://localhost:9200/
~~~
위의 주소로 들어갔을떄 

http://thepythondjango.com/wp/wp-content/uploads/2017/11/elastic-search-UI.png

이런 화면이 뜬다면 실행이 된 것입니다.

### kibana 설치

https://www.elastic.co/kr/downloads/kibana

위 사이트에서 elasticsearch와 마찬가지로 tar 파일을 다운 받으시고 아래처럼 압축을 풀어주세요

~~~
tar -xzvf kibana-5.x.x.tar
~~~

### kibana 실행

압축이 풀린 파일에 들어가 아래의 커맨드라인에 아래의 명령어를 입력하면

~~~
./bin/kibana
~~~

실행이 됩니다.


~~~
http://localhost:5601
~~~

위의 주소로 들어갔을떄 

http://thepythondjango.com/wp/wp-content/uploads/2017/11/kibana-elastic-search-error.png

위와 같은 화면이 나온다면 성공입니다.

이제 장고 프로젝트를 생성해야 합니다.

~~~
git clone https://github.com/kl4314/elastic-search-django
~~~

### elasticsearch python 패키지 설치

python과 elasticsearch를 연동 해주는 패키지를 다운받아 봅시다.
아래 명령어를 입력해주세요.

~~~
pip install elasticsearch-dsl
~~~

자이제 기본적인 환경 설정은 끝이 났으니 본격적으로 만들어 봅시다.