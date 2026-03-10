#Lợi ích của typer:Mạnh cho xây CLI nhanh chóng
import typer
from data_fetch_cli.downloader import download_data
from data_fetch_cli.validator import validate_url
from logger import get_logger

#Đại diện cho ứng dụng CLI
#App quản lý các command và tham số của chương trình
app = typer.Typer()
logger = get_logger()

#Định nghĩa callback chính cho ứng dụng CLI
#Callback này sẽ được gọi
#khi người dùng chạy ứng dụng mà không chỉ định lệnh cụ thể nào
@app.callback()
def main() -> None:
    """Entry point cho CLI group."""
    return None

# @app.command() Đăng ký hàm thành lệnh
#decorator @app.command() cho hàm bên dưới
#báo cho typer biết fetch là lệnh trong CLI
#Khi người dùng chạy script với tham số dòng lệnh
#Typer sẽ dựa vào các decorator này để xác định lệnh nào được gọi và ánh xạ tham số.

#Hàm chứa logic xử lý lệnh fetch
#Hint "str" cho tham số url giúp typer hiểu rằng url là một chuỗi
@app.command()
def fetch(url: str = typer.Argument(..., help="URL để lấy dữ liệu")):
    # logger.info(f"download_started, extra = {{'url': '{url}'}}") #Ghi log thông tin về việc tải và xác thực dữ liệu thành công
    
    data = download_data(url) #Gọi hàm download_data với URL được cung cấp từ dòng lệnh

    # logger.info(f"download_completed, extra = {{'record': {len(data)}}}") #Ghi log thông tin về việc tải và xác thực dữ liệu thành công
    
    users = validate_url(data) #Gọi hàm validate_url để kiểm tra tính hợp lệ của data đã tải về
    
    # logger.info(f"validation_completed, extra = {{'valid_users': {len(users)}}}") #Ghi log thông tin về việc tải và xác thực dữ liệu thành công

    print(users) #In dữ liệu đã tải về, có thể là nội dung của URL hoặc thông tin liên quan tùy thuộc vào cách download_data được triển khai

if __name__ == "__main__":
    app() #Khởi chạy ứng dụng CLI, cho phép người dùng tương tác với các lệnh đã định nghĩa


