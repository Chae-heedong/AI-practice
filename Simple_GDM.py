import numpy as np
# 데이터 입력
data = np.array([
    [0.0, 0.0],
    [1.0, 1.0],
    [1.0, 2.0],
    [2.0, 1.0]
])
# 학습률 설정
학습률 = float(input("학습률 알파를 실수로 입력해주세요"))
# 반복 횟수 설정
반복횟수 = int(input("반복 횟수를 정수로 입력해주세요"))
#목표 오차 설정
목표오차=float(input("목표하는 오차(mse)를 실수로 입력해주세요"))
# 파라미터 설정
print("w0+w1x+w1x^2로 식을 근사하기 위한 파라미터를 입력해주세요.")
w0=float(input("w0을 입력해주세요"))
w1=float(input("w1을 입력해주세요"))
w2=float(input("w2을 입력해주세요"))
mse=0
# 경사하강법 실행
for i in range(반복횟수 ):
    # 예측 값 계산
    예측값 = w2 * data[:, 0] ** 2 + w1 * data[:, 0] + w0
    # 오차 계산
    오차 = data[:, 1] - 예측값
    #기존오차 기록
    beforemse = mse
    # 평균 제곱 오차 계산
    mse = np.mean(오차 ** 2)
    # 그래디언트 계산
    dw0 = -2 * np.mean(오차)
    dw1 = -2 * np.mean(오차 * data[:, 0])
    dw2 = -2 * np.mean(오차 * data[:, 0] ** 2)
    # 파라미터 업데이트
    w0 -= 학습률 * dw0
    w1 -= 학습률 * dw1
    w2 -= 학습률 * dw2
    # 중간 결과 출력
    print(f"계산 횟수 {i+1}, 평균제곱오차: {mse} w0:{w0} w1:{w1} w2:{w2}")
    #오차가 일정 미만인 경우
    if mse<목표오차:
        print("목표하던 mse까지 도달하여 계산을 종료합니다.")
        break
    if mse==beforemse:
        print("mse가 변하지 않아서 종료합니다.")
        break
    k=i #반복횟수 확인용
# 최종 파라미터 출력
if k+1==반복횟수:
    print("반복 횟수를 넘어서 종료합니다.")
print(f"계산 횟수 {i+1}, 평균제곱오차: {mse}  w0: {w0}, w1: {w1}, w2: {w2}")
