1. 데이터 불러오기
2. DataFrame 전처리, Label 부분과 Pixel 부분 나누기
3. DataFrame을 28*28 사이즈로 리사이징 후, 흑/백으로 바꿔주기
4. 모델 작성
  a. CNN (input:(28,28), filter:50, kernel_size:(3,3), activation=relu func)
  b. CNN (input:(28,28), filterL50, kernel_size:(3,3), activation=relu func)
  c. Dropout (33%)
  d. MaxPooling 3*3
  e. CNN (input:(9,9), filter:50, kernel_size:(3,3), activation=relu func)
  f. Dropout (33%)
  g. MaxPooling 3*3
  h. CNN (input:(3,3), filter:50, kernel_size:(3,3), activation=relu func)
  i. Dropout (33%)
  j. MaxPooling 3*3
  k. Flatten
  l. Dense (units:50, activation=relu func)
  m. Dense (units:10, activation=softmax func)
5. 데이터 시각화 및 submission DataFrame 작성
6. 제출
