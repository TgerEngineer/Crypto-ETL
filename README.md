# Crypto Data Pipeline với Airflow, PostgreSQL và Docker

🚀 **Giới thiệu**  
Dự án này xây dựng một data pipeline tự động để thu thập, lưu trữ và phân tích dữ liệu tiền mã hóa.  
Pipeline sử dụng Apache Airflow để orchestration, PostgreSQL để lưu trữ, và phân tích dữ liệu bằng Jupyter Notebook và Power BI.

**Mục tiêu:**  
- Thực hành xây dựng ETL pipeline chuẩn cho vị trí Data Engineer.  
- Làm quen với Docker, Airflow, PostgreSQL và công cụ phân tích dữ liệu.

---

🛠️ **Công nghệ sử dụng:**  
- Apache Airflow: Orchestration ETL pipeline  
- PostgreSQL: Cơ sở dữ liệu lưu trữ  
- Docker & Docker Compose: Đóng gói hệ thống  
- Python: Xử lý dữ liệu (psycopg2, pandas, matplotlib)  
- Jupyter Notebook: Truy vấn và trực quan hóa dữ liệu  
- Power BI: Visualization dashboard (tuỳ chọn)

---

🧩 **Kiến trúc hệ thống:**  
CoinGecko API 
   -> 
Airflow DAG (Extract → Load → Transform) 
   ->
PostgreSQL Database (raw, dim, fact) 
   ->
Phân tích dữ liệu (Jupyter Notebook, Power BI)

---

📂 **Cấu trúc thư mục:**  
![image](https://github.com/user-attachments/assets/93f7b7fc-64b1-49a7-9126-06de71c25613)

---

🗄️ **Các bảng dữ liệu:**  
- `raw_crypto_prices`: Bảng lưu dữ liệu thô từ API  
- `dim_crypto`: Bảng dimension lưu thông tin các đồng coin  
- `fact_crypto_price`: Bảng fact lưu giá, market cap, volume theo thời gian

---

🎯 **Các bước triển khai:**  
1. **Clone dự án:**
   ```bash
   git clone https://github.com/TgerEngineer/Crypto-ETL
   cd crypto-data-pipeline
Khởi động Docker Compose:

bash
docker-compose up -d
Truy cập Airflow UI:

Mở trình duyệt tại: http://localhost:8080

Đăng nhập với:

Username: admin

Password: admin

Trigger DAG: crypto_etl_dag

Phân tích dữ liệu:

Kết nối PostgreSQL từ Jupyter Notebook (analysis.ipynb)

Một số phân tích mẫu:

Top 5 đồng coin có market cap cao nhất

Biểu đồ biến động giá Bitcoin theo thời gian

📑 Ghi chú:

Pipeline hiện tại mang tính học thuật, mô phỏng quy trình Data Engineering thực tế.

Một số dữ liệu mẫu được lấy từ CoinGecko API.
