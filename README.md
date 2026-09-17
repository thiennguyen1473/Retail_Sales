# Phân tích doanh số Chuỗi cung ứng và bán hàng
Dự án phân tích dữ liệu toàn diện sử dụng Python, MySQL Workbench trực quan hóa dữ liệu để trích xuất những thông tin kinh doanh hữu ích từ chuỗi cung ứng và bán hàng, 
phản ánh vòng đời của đơn hàng trong hoạt động thương mại điện tử và bán lẻ đa danh mục.

## Tổng quan dự án:
Dự án này phân tích dữ liệu trong có trụ sở tại Hoa Kỳ để trả lời các câu hỏi kinh doanh quan trọng:
Những loại sản phẩm nào tạo ra doanh thu và lợi nhuận cao nhất?

Những **khách hàng** nào tạo ra **doanh thu** nhiều nhất?

**Doanh thu và lợi nhuận** thay đổi như thế nào theo **khu vực và thời điểm**?

Những **sản phẩm** nào gây ra **thua lỗ hoặc rất kén người mua**?

## Sơ đồ ERD

## Kiến trúc kỹ thuật

## Công nghệ sử dụng

| Tools | Mục đích |
|---|---|
| Python 3.14.0 | Kiểm tra và làm sạch dữ liệu |
| MySQL Workbench | Thao tác và phân tích dữ liệu |
| Pandas | Thao tác với DataFrame |
| Matplotlib | Trực quan hóa dữ liệu |
| Visual Studio Code	| Môi trường tương tác với python | 
| Excel | Thay đổi định dạng ngày |

## Tập dữ liệu:
Nguồn: https://www.kaggle.com/datasets/nhatthuaunguyen/supply-chain-and-sales

**Thời gian**: bộ dữ liệu bắt đầu từ 1/2014 cho đến 12/2017

**Số lượng giao dịch**: 9.994 lượt giao dịch

**Các bảng**: Calendar, Category, SubCate, Product, Customer, Customer Segment, FactRetaild, Retail Sales People, Location, ShipMode.

Trong đó FactRetaild là bảng trung tâm, chứa các thông tin như doanh số, lợi nhuận, chi phí, số lượng, ngày đặt hàng, ngày giao hàng và các mã liên kết đến các bảng khác.
### 1.Kiểm tra dữ liệu
- Số dòng, số cột, kiểu dữ liệu
- Missing value
- Duplicate
- Primary Key
- Foreign Key
- Phân bố dữ liệu
- Các giá trị bất thường
### 2.Làm sạch dữ liệu bằng Python với thư viện pandas
- Chuẩn hóa kiểu dữ liệu
- Xóa các dòng bất thường, thiếu dữ liệu
- Xóa các dòng trùng lặp
- Chuẩn hóa tên cột
### 3.Phân tích dữ liệu từ SQL
Đã tải dữ liệu đã được làm sạch vào MySQL Workbench và viết các truy vấn để trả lời các câu hỏi kinh doanh cụ thể. Dưới đây là một số ví dụ:

**Doanh thu theo Customer**
```sql
-- Top 10 khách hàng theo doanh thu
select c.`customer name`, f.`customer id`, sum(f.sales) as tong from factretaild f 
join customer c on f.`customer id` = c.`customer id`
group by c.`customer name`, f.`customer id`
order by sum(f.sales) desc
limit 10;
```

**Doanh thu thay đổi như thế nào theo địa điểm?**
```sql
-- Top 10 địa điểm có doanh thu cao nhất
	select l.`postal code`, l.`country`, sum(f.sales) as tong from factretaild f 
join location l on f.`postal Code` = l.`postal code` 
group by l.`country`, l.`postal Code`
order by tong desc
limit 10;
```

**Doanh thu thay đổi như thế nào theo năm, liệu có sự tăng dần ổn định hay bức phá tại năm nào đó?**
```sql
-- Tổng doanh thu theo năm
select c.year, sum(f.sales) as tong from factretaild f join calendar c
on f.`order date` = c.`date`
group by c.year;
```

**Doanh thu theo tháng trong từng năm riêng lẻ thay đổi như thế nào?**
```sql
-- Tổng doanh thu theo tháng
select c.month,c .year, sum(f.sales) as tong_month from factretaild f join calendar c
on f.`order date` = c.`date`
group by c.month,c.year
order by c.year, c.month;
```

**Có danh mục Category nào tạo ra doanh thu và lợi nhuận vượt trội so với còn lại?**
```sql
-- Doanh thu và lợi nhuận theo từng danh mục Category
select c.`category`, sum(f.sales) as total_sales,(sum(f.sales) - sum(f.cost)) as total_profit from factretaild f join product p
on f.`product id` = p.`product id`
join subcate s on p.`sub-Cate id` = s.`sub-Cate id`
join category c on s.`category id` = c.`category id`
group by c.`category`
order by total_profit desc;
```
