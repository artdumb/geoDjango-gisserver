# geoDjango-gisserver

- DB MODEL

  - Post
    - title
    - content
    - geom(point)
    - created, update_at
  - Review
    - comment
    - Post(FK)

- API
  - GET : 전체 데이터 목록 GeoJSON형식으로
    - url/api/listpost
  - POST : 하나의 GeoJSON point형식을 올릴 수 있다
    - url/api/post
    - featureCollection타입의 객체들 읽는 거 아직 못함

