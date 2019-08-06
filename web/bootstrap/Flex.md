# Flex

## flex

### 1. flex 선언

* flex 선언

```html
/* head */
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
/* head */
.container {
  ...
  display: flex;
  flex-direction: column;
}
```

* item들이 쌓이는 방향을 설정
* row(기본값) / column / row-reverse / column-reverse



### 3. wrap

```html
/* head */
.container {
  ...
  display: flex;
  flex-wrap: wrap;
}
```

* container 내부에 item 배치
* no-wrap(기본값) / wrap / wrap-reverse