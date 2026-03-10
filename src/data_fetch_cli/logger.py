# import logging
# from pythonjsonlogger import jsonlogger

# def get_logger():
#     logger = logging.getLogger("app") #Tạo một logger với tên "app"
#     logger.setLevel(logging.INFO) #Đặt mức độ log là INFO, có nghĩa là sẽ ghi lại các thông tin quan trọng và các sự kiện bình thường

#     handler = logging.StreamHandler() #Tạo một handler để ghi log ra console
    
#     formatter = jsonlogger.JsonFormatter() #Tạo một formatter để định dạng log dưới dạng JSON
#     handler.setFormatter(formatter) #Gán formatter cho handler

#     logger.addHandler(handler) #Gán handler cho logger

#     return logger
