import cv2

# 이미지 읽기 (파일 경로와 확장자 확인)
image = cv2.imread(r'C:\Users\s\Desktop\New Folder\a.jpg')

# 이미지가 제대로 읽혔는지 확인
if image is None:
    print("이미지를 읽을 수 없습니다. 경로를 확인하세요.")
else:
    # 이미지를 그레이스케일로 변환
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지 크기 조정 (8분의 1로 줄이기)
    resized_image = cv2.resize(image, (image.shape[1] // 8, image.shape[0] // 8))
    resized_gray_image = cv2.resize(gray_image, (image.shape[1] // 8, image.shape[0] // 8))

    # 원본 이미지와 그레이스케일 이미지 표시
    cv2.imshow('Original Image', resized_image)
    cv2.imshow('Grayscale Image', resized_gray_image)

    # 키 입력 대기
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()