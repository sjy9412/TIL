# HTML

## 1. 시작하기

```html
<!DOCTYPE html>
<html lang = "ko">
    <head>
        <meta charest = 'utf-8'>
        <title>
        <!-- 타이틀은 위에 뜨는 이름 -->
        </title>
        <style>
        /* 기본적으로 값을 설정해 줌 */
        </style>
    </head>
    <body>
        
    </body>
</html>
```



# 2. 내용 추가하기

* style

  ```html
  <style>
  	h1 {
          color: red;
          text-align: center;
          }
      p {
          color: blue;
          text-align: right;
     		}
          /* 태그 선택자 */
      h2 {
          color: black;
          }
           
          /* 클래스 선택자 */
      .red {
  		color: red;
  		}
          /* 아이디 선택자 */
      #pink {
  		color: pink;
  		}
          /* 우선순위
          id > class > 태그
          id는 문서에서 하나만 존재할 수 있다.
          class는 무서에서 여러개 존재할 수 있다.
          태그는 그냥 기본이다. */
  </style>
  ```

  

* body

  ```html
  <body>
      <h1>제목 1</h1>
      <h2 id="pink" class="red">제목 2</h2>
      <!-- <h2> 안에 id나 class를 설정해줄 수 있다-->
      <h6>가장 작은 제목(heading)입니다.</h6>
      <p>내용내용. <br> 문단의 내용을 작성합니다.</p>
      <p class="red">나는 빨간색이 좋아</p>
      <a href="http://google.com">구글로 가자!</a>
      <!-- a 태그는 href 속성으로 해당하는 링크를 설정한다. -->
      <br>
      <img src="data:image/jpeg;base64,/9j/"> 
      <!--img 태그는 닫는 태그가 없다.
          scr 속성값은 이미지의 경로이다.
          -->
      <br>
      <iframe width="300" height="200" src="https://youtu.be/cWc12iU0odk"></iframe>
  </body>
  ```

  * `h1` : 제목 입력 (h6까지 가능)
  * `<br>` : 줄 바꿈
  * `<p>` : 내용 입력
  * `<a herf=" ">` : 링크 삽입
  * `<img src=" ">` : 이미지 삽입
  * `<iframe src=" ">` : 동영상 삽입