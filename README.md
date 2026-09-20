# Phân tích doanh số Chuỗi cung ứng và bán hàng
Dự án phân tích dữ liệu toàn diện sử dụng Python, MySQL Workbench trực quan hóa dữ liệu để trích xuất những thông tin kinh doanh hữu ích từ chuỗi cung ứng và bán hàng, 
phản ánh vòng đời của đơn hàng trong hoạt động thương mại điện tử và bán lẻ đa danh mục.

## Tổng quan dự án:
Dự án này phân tích dữ liệu trong có trụ sở tại Hoa Kỳ để trả lời các câu hỏi kinh doanh quan trọng:
Những loại sản phẩm nào tạo ra doanh thu và lợi nhuận cao nhất?

Những **khách hàng** nào tạo ra **doanh thu** nhiều nhất?

**Doanh thu và lợi nhuận** thay đổi như thế nào theo **khu vực và thời điểm**?

Những **sản phẩm** nào gây ra **thua lỗ hoặc rất kén người mua**?

## Diagram
![Diagram](https://github.com/thiennguyen1473/Retail_Sales/blob/442d861ed361f04f40bf34c3d7ae7a15d6f5187c/Diagram.png)

## Kiến trúc kỹ thuật
## Cấu trúc Project

```text
Retail_Sales/
│
├── kaggle/
│   ├── dataset.csv
│   ├── cleaned/              # Các file CSV sau khi làm sạch
│   └── sql_query/            # Kết quả các truy vấn SQL dưới dạng CSV
│
├── py/
│   ├── cleaning.py           # Làm sạch dữ liệu bằng Python
│   └── visualization/        # Các file Python dùng để vẽ biểu đồ
│
├── sql/
│   └── create_table.sql      # Tạo database, bảng và các quan hệ
│
├── dashboard.png            
└── diagram.png
```               


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

## Project Workflow
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
### 4 POWER BI DASHBOARD
**Tổng quan**
Các thẻ KPI hiển thị các số liệu chính, cùng với xu hướng doanh thu hàng tháng, khách hàng hàng đầu,  doanh thu sản phẩm theo category,phân tích theo địa điểm — tất cả trên một trang tương tác duy nhất.

**Các chỉ số chính**
|số liệu| giá trị|
|---|---|
| Tổng doanh thu | 2.300.000 usd |
|tổng khách hàng| 793 người |
| tổng order | 9.994 lượt giao dịch| 
| phần trăm lợi nhuận | 12% |



![DashBoard](https://github.com/thiennguyen1473/Retail_Sales/blob/092bdeb1e149b0b195f6b08ce7f1c4ac39050e0f/DashBoard.PNG)

**Phân tích kinh doanh và xu hướng**

Doanh thu **tăng cao rõ rệt** vào các tháng cuối năm, đạt mức **cao nhất ở tháng 11** và hạ nhiệt dần đến tháng 12.

Doanh thu có xu hướng tăng trong giai đoạn 2014–2017. giảm nhẹ trong năm 2015, sau đó tăng dần đến và đạt mức cao nhất năm 2017. Điều này cho thấy doanh thu có sự cải thiện về tổng thể qua các năm.
<img width="732" height="307" alt="image" src="https://github.com/user-attachments/assets/777b4d26-893a-4b62-bc12-a8ca72105671" />


**10 Thành phố có số doanh thu mua hàng lớn nhất**
 New York City dẫn đầu với doanh thu trên 50K, cao hơn đáng kể so với Lafayette và các thành phố còn lại. Các thành phố trong nhóm Top 10 phía sau có doanh thu tương đối gần nhau hơn, chủ yếu nằm trong khoảng 5K–20K.
<img width="494" height="262" alt="image" src="https://github.com/user-attachments/assets/399d897f-eda0-49e5-86f0-5c4ab593ffce" />

**Mối quan hệ giữa doanh thu và lợi nhuận**
Technology dẫn đầu về cả doanh thu và lợi nhuận. Office Supplies và Furniture có doanh thu tương đương nhưng chênh lệch đáng kể về lợi nhuận, cho thấy hiệu quả sinh lời khác nhau giữa hai nhóm.

<img width="446" height="270" alt="image" src="https://github.com/user-attachments/assets/58248e84-cd49-4fc9-b04f-04506a603929" />

**Tỉ lệ doanh thu mua hàng theo phân khúc khách hàng**

Consumer là nhóm khách hàng đóng góp doanh thu lớn nhất, chiếm hơn một nửa tổng doanh thu (50,56%), trong khi Corporate và Home Office lần lượt chiếm 30,74% và 18,70%.
<img width="337" height="254" alt="image" src="https://github.com/user-attachments/assets/576e126e-ecdd-44ca-a522-57b6e6f12ffb" />


**customer id**

SM-20320 là khách hàng có doanh thu cao nhất trong Top 10, đạt khoảng 25K và vượt khá xa phần lớn các khách hàng còn lại.
<img width="496" height="267" alt="image" src="https://github.com/user-attachments/assets/e6abb1ff-eafd-48ea-b5ef-fe690bc03a60" />



## Một số phát hiện chính
- **20% số sản phẩm hàng đầu đóng góp 78% tổng doanh thu**, một quy luật điển hình của quy luật **patero**

- có đến **99,78%** người dùng quyết định **mua hàng lần 2**, doanh nghiệp cần **duy trì và giữ chân** nhóm khách hàng này, đồng thời ưu tiên **mở rộng tệp khách hàng mới**

- Doanh thu **tập trung nhiều hơn** ở các khu vực **West và East**, lần lượt chiếm **31,58% và 29,55%** tổng doanh thu. Trong khi đó, **South có tỷ trọng thấp nhất với 17,05%**. Cho thấy có sự **phân bố** doanh thu khá cao theo **khu vực địa lý**

## đề xuất kinh doanh
- Tập trung nguồn lực vào nhóm sản phẩm tạo doanh thu cao, đặc biệt là **20% sản phẩm đóng góp phần lớn doanh thu**; đồng thời **theo dõi và tối ưu** các sản phẩm có doanh thu thấp.
- Duy trì và chăm sóc khách hàng hiện tại thông qua chương trình **khách hàng thân thiết, ưu đãi và bán thêm sản phẩm; đồng thời mở rộng tệp khách hàng mới để tăng quy mô thị trường.**
- **Tiếp tục khai thác thị trường West và East**, đồng thời phân tích **nguyên nhân** doanh thu tại South thấp hơn để xác định cơ hội cải thiện và mở rộng thị trường.
