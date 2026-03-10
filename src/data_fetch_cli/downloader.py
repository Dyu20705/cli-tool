import requests

#Hàm để tải dữ liệu từ một URL cụ thể
def download_data(url: str) -> dict:
    request = requests.get(url) #Gửi yêu cầu GET đến URL đã cung cấp
    request.raise_for_status() #Kiểm tra nếu yêu cầu không thành công, sẽ ném ra lỗi HTTP tương ứng
    return request.json() #Trả về dữ liệu đã tải về dưới dạng JSON, nếu có thể phân tích được