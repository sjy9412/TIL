* npm

  ```bash
  $ npm init
  ```

  * 비어있는 `package.json` 생성

* vue, webpack 설치

  ```bash
  $ npm install vue
  ```

  ```bash
  $ npm install webpack webpack-cli -D
  ```

  * webpack은 개발환경에서 모듈 번들러로써 활용하기 위한 것이므로 `-D` 옵션을 통해 `packge.json`에서 `devDependencies`에 추가



## Vue 개발환경

### 1 . vue 파일

```bash
$ npm install vue-loader vue-template-compiler -D
```


* `vue-loader` : vue 파일을 불러오는 역할
* `vue-template-compiler` : 해석하는 역할



## 2. style

```bash
$ npm install vue-style-loader css-loader -D
```

* vue-style-loader : vue의 style
* css-loader : webpack css 불러오는 로더



#  npm install -g @vue/cli

```bash
$ vue create {프로젝트 이름}
```

* default(babel, eslint) -> enter