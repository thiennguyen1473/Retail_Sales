create database Retaild_Sales;

use Retaild_Sales;

create table Calendar(
`Date` date primary key not null,
`Year` bigint,
`Month` int,
`Day` int,
`Start of Quarter` datetime,
`Start of Month` datetime,
`end of month` datetime,
`day name` varchar(255),
`day of week` int
);

create table Category(
`category id` int primary key not null,
`category` varchar(255)
);

create table SubCate(
`sub-Cate id` int primary key not null,
`sub-Category` varchar(255),
`category id` int,

foreign key(`category id`) references Category(`category id`)
);

create table CusSegment(
`cusSegment id` int primary key not null,
`segment` varchar(255)
);

create table Customer(
`customer id` varchar(255) primary key not null,
`cusSegment id` int,
`customer Name` varchar(255),
foreign key(`cusSegment id`) references CusSegment(`cusSegment id`)
);

create table Location(
`postal Code` BigInt primary key not null, 
`country` varchar(255),
`region` varchar(255),

`city` varchar(255),
`longtitude` varchar(255),
`latitude` varchar(255)
);

ALTER TABLE Location
ADD COLUMN `state` VARCHAR(255);


create table Product(
`product id` varchar(255) primary key not null,
`product Name` varchar(255),
`sub-Cate id` int,
`Unit Cp` float,
`Unit Sp` float,
foreign key (`sub-Cate id`) references SubCate(`sub-Cate id`)
);

create table Product_test(
`product id` varchar(255) primary key not null,
`product Name` varchar(255),
`sub-Cate id` int,
`Unit Cp` float,
`Unit Sp` float
);


create table RetaildSalesPeople(
`retail Sales People id` int primary key not null,
`retaild Sales People` varchar(255)
);

create table ShipMode(
`ship Mode id` int primary key not null,
`ship Mode` varchar(255)
);

create table FactRetaild(
`retail Order id` bigint primary key not null,
`order id` varchar(255),
`order Date` date,
`ship Date` date,
`ship Mode id` int,
`customer id` varchar(255),
`postal Code` bigint,
`retail Sales People id` int,
`product id` varchar(255),

foreign key(`order Date`) references Calendar(`date`),
foreign key(`ship Mode id`) references ShipMode(`ship Mode id`),
foreign key(`customer id`) references Customer(`customer id`),
foreign key(`postal Code`) references Location(`postal Code`),
foreign key(`product id`) references Product(`product id`),
foreign key(`retail Sales People id`) references RetaildSalesPeople(`retail Sales People id`)

);



alter table factRetaild
add returned varchar(255),
add `ship status` varchar(255),
add sales double,
add quantity bigint,
add profit double,
add cost double,
add days bigint;


-- tổng doanh thu bán được
select sum(sales) as tong from factretaild;

-- tổng sản phẩm
select sum(quantity) as tong_quantity from factretaild;

-- số lượng đơn hàng
select count(distinct `order id`) from factretaild;

-- tổng chi phí
select sum(sales) - sum(cost) as loinhuan from factretaild;

-- doanh thu theo năm
select c.year, round(sum(f.sales), 2) as total_revenue from factretaild f join calendar c
on f.`order date` = c.`date`
group by c.year;

-- giá trung bình của tất cả hàng
select sum(sales)/sum(quantity) as avg_price from factretaild ;

-- doanh thu theo tháng
select c.month,c .year, round(sum(f.sales), 2) as total_revenue from factretaild f join calendar c
on f.`order date` = c.`date`
group by c.month,c.year
order by c.year, c.month;

# doanh thu và lợi nhuận cao nhất
select c.`category`, round(sum(f.sales), 2) as total_sales, round((sum(f.sales) - sum(f.cost)), 2) as total_profit from factretaild f join product p
on f.`product id` = p.`product id`
join subcate s on p.`sub-Cate id` = s.`sub-Cate id`
join category c on s.`category id` = c.`category id`
group by c.`category`
order by total_profit desc;



#sub-cate doanh thu cao nhất 
select s.`sub-cate id`, round(sum(f.sales)) from factretaild f join product p on f.`product id`
= p.`product id`
join subCate s on s.`sub-Cate id` = p.`sub-Cate id`
group by s.`sub-cate id`
order by sum(f.sales) desc
limit 1;

# top 10 mua nhieu tien nhat
select c.`customer name`, f.`customer id`, round(sum(f.sales)) as total_revenue from factretaild f 
join customer c on f.`customer id` = c.`customer id` 
group by c.`customer name`, f.`customer id`
order by total_revenue desc
limit 10;



# phương thức vận chuyển và đơn hàng tương ứng
select sh.`ship mode`, sh.`ship mode id` from factretaild f 
join shipmode sh  on f.`ship mode id` = sh.`ship mode id`
group by sh.`ship mode id`,sh.`ship mode`;


# khu vực doanh thu cao nhất
select l.city, l.region ,l.`postal code`, l.`country`, round(sum(f.sales), 2) as total_revenue from factretaild f 
join location l on f.`postal Code` = l.`postal code` 
where `ship status` = 'late'
group by l.`country`, l.`postal Code`, f.days
order by total_revenue desc
limit 20;


select count(*), c.`quarter` from factretaild f join calendar c on c.`date` = f.`order date`
group by c.month;



# doanh thu các năm so với năm trước đó
select c.year, sum(f.sales), sum(f.sales) - lag(sum(f.sales)) over (order by c.year) as distince from factretaild f join calendar c
on f.`order date` = c.`date`
group by c.year
order by distince desc;

# sản phẩm chưa từng bán
select c.`category id`,s.`sub-cate id`,p.`product id`, p.`product name`,f.`retail Order id` from product p 
left join factretaild f on p.`product id` = f.`product id`
join subcate s on s.`sub-cate id` = p.`sub-cate id` 
join category c on c.`category id` = s.`category id`
where f.`product id` is null;

#khách hàng chưa đặt đơn nào
select c.`customer id`,f.`retail order id` from factretaild f right join customer c on f.`customer id` = c.`customer id` where f.`retail Order id` is null;

#phân loại khách hàng theo doanh thu
select c.`customer id` , c.`customer name`, sum(f.sales) as total_sales, 
case
when sum(f.sales) >= 10000 then 'hight value'
when sum(f.sales) >= 5000 then 'medium value'
else 'low value'
    end as customer_segment 
from factretaild f join customer c 
on f.`customer id` = c.`customer id` 
group by c.`customer id`, c.`customer name`;

#top 3 san pham doanh thu cao nhat 
with cte as (select c.`category`, c.`category id`,p.`product id`, p.`product name`, sum(f.sales) as total_sales, 
rank() over(partition by c.`category` order by sum(f.sales) desc ) as sales_rank
from factretaild f join product p on f.`product id` = p.`product id`
join subcate s on p.`sub-cate id` = s.`sub-cate id` 
join category c on c.`category id` = s.`category id`
group by c.`category`, c.`category id`, p.`product name`, p.`product id` )
select * from cte where sales_rank <=3
order by `category`, sales_rank;


with cte as (
select cs.`cusSegment id`, c.`customer id`, c.`customer name`, sum(f.sales) as total_revenue, 
rank() over(partition by cs.`Segment` order by sum(f.sales) desc) as rank_revenue
from factretaild f join customer c on f.`customer id` = c.`customer id`
join cusSegment cs on cs.`cusSegment id` = c.`cusSegment id`
group by c.`customer id`, c.`customer name`
)
select ct.`customer id`,ct.`customer name`,ct.`cusSegment id`, ct.rank_revenue, round(ct.total_revenue, 2) as total_revenue from cte ct 
join (select `cussegment id`, max(rank_revenue) from cte group by `cusSegment id`)as t
on t.`cusSegment id` = ct.`cusSegment id` where rank_revenue <= 10;

#top 10 doanh thu khách hàng theo sub-cate
with cte as(select s.`sub-category`, c.`customer name`, c.`customer id`, sum(f.sales) as total_revenue, rank() over(partition by s.`sub-Category` order by sum(f.sales) desc) as sales_rank from factretaild f 
join customer c on f.`customer id` = c.`customer id`
join product p on p.`product id` = f.`product id` 
join subcate s on s.`sub-cate id` = p.`sub-cate id` 
group by s.`sub-category`,c.`customer name`, c.`customer id`) select `customer name`, `customer id`, `sub-category`, round(total_revenue, 2), sales_rank  from cte where sales_rank <= 10 ;

