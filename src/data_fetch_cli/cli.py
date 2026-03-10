#Lợi ích của typer:Mạnh cho xây CLI nhanh chóng
import typer
from data_fetch_cli.downloader import download_data

#Đại diện cho ứng dụng CLI
#App quản lý các command và tham số của chương trình
app = typer.Typer()

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
    data = download_data(url) #Gọi hàm download_data với URL được cung cấp từ dòng lệnh
    print(f"Data fetched successfully from {url}") #In thông báo thành công sau khi dữ liệu được tải về
    print(data) #In dữ liệu đã tải về, có thể là nội dung của URL hoặc thông tin liên quan tùy thuộc vào cách download_data được triển khai

if __name__ == "__main__":
    app() #Khởi chạy ứng dụng CLI, cho phép người dùng tương tác với các lệnh đã định nghĩa


