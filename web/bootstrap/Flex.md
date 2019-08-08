# Flex

## flex

### 1. flex 선언

* flex 선언

```html
/* style */
.container {
  ...
  display: flex;
  ...
}
```

* flex container : 감싸고 있는 부모 요소
* flex itmes : 구성하고 있는 아이템 요소

```html
/* body */
<div class="container">
    <div>item</div>
    <div>item</div>
    <div>item</div>
</div>
```



###  2. flex 방향 설정

```html
/* style */
.container {
  ...
  display: flex;
  flex-direction: column;
}
```

* item들이 쌓이는 방향을 설정
* `row`(기본값) / `column` /` row-reverse` / `column-reverse`



### 3. wrap

```html
/* style */
.container {
  ...
  display: flex;
  flex-wrap: wrap;
}
```

* container 내부에 item 배치
* `no-wrap`(기본값) / `wrap` / `wrap-reverse`



## flex 정렬

### 1. flex-grow

* 기존에 배치되었을 때 있었던 여백이 flex-forw를 사용하면 남은 여백을 나눠 가진다. (기본값은 0이고 값이 클수록 많은 영역을 차지)

```html
/* style */
.item {
  flex-grow: 1;
}
```



### 2.  *justify-content (x축)*

* `flex-direction`이 row일 때 : 가로 정렬
* `flex-direction`이 column일 때 : 세로 정렬

```html
/* style */
.container {
  display: flex;
  justify-content: flex-start;
}
```

* `flex-start`(방향 시작) / `center`(가운데) / `flex-end`(방향 끝)
* `space-between`(사이에 균등한 여백)  / `space-around`(item 좌우에 동일 여백) / `space-evenly`(item 및 외곽 여백 동일)
* `flex-direction`에서 `reverse`를 설정해주면 `start`와 `end`의 위치가 바뀜



### 3. align-items (y축)

```html
/* style */
.container {
  display: flex;
  align-items: baseline;
}
```

* 